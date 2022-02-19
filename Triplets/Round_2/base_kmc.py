import kmc.morphology as morphology
from kmc.rates import *
from kmc.particles import *
import sys

###BASIC PARAMETERS######################################################################
identifier         = 'NPB_'+sys.argv[2]+'_D_'+sys.argv[3]+'_' # output identifier
time_limit         = np.inf            # in ps
animation_mode     = False 
#animation_mode     = True
save_animation     = False             # if you want to save the animation
animation_exten    = 'gif'             # possible options ('gif' and 'mp4')
rotate             = False             # True = animation rotates, False = remains fixed
marker_type        = 1                 # marker type used at the animation processs ( 0 = balls, 1 = symbols) 
pause              = False             # if you want that the annimation stops in the first frame (debug purposes)
rounds             = 250000           # Number of rounds
n_proc             = 15                 # Number of cores to be used
frozen             = True
#########################################################################################

###SINGLET EXCITONS######################################################################
#0: NPB, 1: DCJTB
##FORSTER RADII (Å)
r00   = 41.9  #Forster radius material 0 --> material 0 (Angstrom)    
r01   = 66.5   #material 0 --> material 1      
r10   = 35.3   
r11   = 66.8 
radii = {(0,0):r00, (0,1):r01, (1,0):r10, (1,1):r11}

##FLUORESCENCE LIFETIMES (ps)
f0 = 11340 #lifetime of material 0
f1 = 754    #lifetime of material 1
lifetimes = {0:f0,1:f1}

##TANSITION DIPOLE MOMENTS (a.u.)
mu0 = 1.10
mu1 = 5.10
mus = {0:mu0,1:mu1}

##EXCITON TRANSFER RATES
forster   = Forster(Rf=radii,life=lifetimes,mu=mus)

##FLUORESCENCE RATES
fluor     = Fluor(life=lifetimes)

#ISC section
isc_rates = {0:2.8E+08*1E-12,1:0.0*1E-12} #Será a soma das taxas S1-T2, Celula B27+B28 do NPB
#A taxa de isc do S1 pro T2 do DC é baixa comparada com a de fluor, então estamos desprezando.
isc = ISC(rate=isc_rates)

#Non-radiative processes:
nonrad1 ={0:5.0E+08*1E-12,1:0}  #Será a taxa de isc S1-T1 celula B26 da tab NPB
#Não teremos tripletos sendo gerados no DC
#Phosph do NPB é baixa, nonrad vai contar como isc e a simulação acaba para esse cara.
#Non-rad vai ser transferencia pro T1 no NPB que resultam em perdas.
nonrad_singlet = Nonrad(rate=nonrad1)

###TRIPLET EXCITONS######################################################################
##PHOSPHORESCENCE LIFETIMES (PS)
phlife = {0:648800000000,1:253164556962}

##PHOSPHORESCENCE RATE
phosph = Phosph(life=phlife)

##FORSTERT RADII (Å) #Raios são phosph T2 para abs_qualquer.lx
r00   = 37.7   #Forster radius material 0 --> material 0 (Angstrom)    
r01   = 69.0   #material 0 --> material 1      
r10   = 0.0
r11   = 0.0
radii = {(0,0):r00, (0,1):r01, (1,0):r10, (1,1):r11}

##TANSITION DIPOLE MOMENTS (a.u.)
mu0 = 0.0
mu1 = 1.0
mus = {0:mu0,1:mu1}

##EXCITON TRANSFER RATES
forsterT   = ForsterT(Rf=radii,life=phlife,mu=mus)

#rISC section
isc_rates2 = {0:5.1E+05*1E-12,1:0} #Celula B42 do NPB, T2-S1
#todas as taxas de tripleto do DCJTB são irrelevantes.
isc_triplet = ISC(rate=isc_rates2)

###PROCESSES#############################################################################

processes = {'singlet':[forster], 'triplet':[forsterT]}
monomolecular = {'singlet':[fluor,isc,nonrad_singlet],'triplet':[phosph,isc_triplet]}
#########################################################################################

###MORPHOLOGY############################################################################

##Morphology functions

#Reading a file name that contains your lattice
#file = 'lattice.example'
#lattice_func = morphology.ReadLattice(file)
conc_NPB=float(sys.argv[2])
distance=float(sys.argv[3])

# Creating a new lattice at each new round
num_sites         = 50*50*50             #number of sites of the lattice
displacement      = [distance,distance,distance] #vector of the unit cell
disorder          = [0, 0, 0]       #std deviation from avg position
composition       = [conc_NPB,1-conc_NPB]       #popuation probility Ex.: distribu_vect[0] is the prob of mat 0 appear in the lattice
lattice_func      = morphology.Lattice(num_sites,displacement,disorder,composition)

##ENERGIES
#Gaussian distribuitions
t1s   = {0:(2.85,0.17), 1:(1.47,0.28), 'level':'t1'}   #Energia do T1 será a do T2
s1s   = {0:(2.89,0.27), 1:(2.77,0.19), 'level':'s1'}   #mean energy (eV), standard deviation (eV)

s1   = morphology.Gaussian_energy(s1s)
t1   = morphology.Gaussian_energy(t1s)
#########################################################################################

##GENERATE PARTICLES#####################################################################
method    = morphology.randomized
exciton   = morphology.Create_Particles('singlet', 1, method, mat=[0])

#########################################################################################

##BIMOLECULAR OPTIONS###################################################################
bimolec               = False # Turn on annihilation
##list of all annihi funcs that will be used
#########################################################################################

