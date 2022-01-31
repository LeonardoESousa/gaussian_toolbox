## Funcoes
import numpy as np

import matplotlib.pyplot as plt

from scipy import constants

import scipy.stats as stats
## 1) Pega ultima geometria do log (printa a ultima geometria)

def pega_geometria(file):
    atomos = []
    matriz = []
    arquivo = open(file, 'r')
    lista = arquivo.readlines()
    i=1
    for linha in lista:
        i += 1
        if 'Standard orientation:' in linha:
            j=i+3
        if "NAtoms=" in linha:
            aux=linha.split()
            num_a=int(aux[1])
    
    geom=lista[j:j+num_a]
    for linha in geom:
        aux=linha.split()
        atomos.append(int(aux[1]))
        matriz.append([float(aux[3]),float(aux[4]),float(aux[5])])
    atomos=np.array(atomos)
    matriz=np.array(matriz)
    return atomos, matriz


## 2) Pega as frequencias (retorna lista de frequencias)

def pega_freqs_redmas(file):
    freq = []
    redmas = []
    with open(file, 'r') as f:#abre o arquivo pra ler
        for line in f: #para cada elemento(no caso linha) do arquivo
            line = line.split() #separa cada elemento(da linha) por espaço
            if 'Frequencies' in line: #se tiver "Frequencies" na linha
                for elem in line: #para cada elemento da linha
                    try: #tente pegar os numeros
                        numero = float(elem)
                        freq.append(numero) #se for numero colocar na lista
                    except:
                        pass
            elif 'masses' in line:
                for elem in line: #para cada elemento da linha
                    try: #tente pegar os numeros
                        numero = float(elem)
                        redmas.append(numero) #se for numero colocar na lista
                    except:
                        pass
            else:
                pass
    freq = np.array(freq)
    freq = 29.979245800*freq*1E9 #Hz
    redmas = np.array(redmas)
    amu = constants.atomic_mass
    redmas = amu*redmas
    return freq, redmas

def dist_modos_nor(file, T):
    freq, redmas = pega_freqs_redmas(file)
    h = constants.hbar
    k = constants.Boltzmann
    R = np.linspace(-1, 1, 100)*1E-10
    for i in range(len(freq)):
        rho = ((redmas[i]*freq[i])/(2*np.pi*h*np.sinh(h*freq[i]/(k*T))))*np.exp((-redmas[i]*freq[i]/h)*(R**2)*np.tanh(h*freq[i]/(2*k*T)))
        plt.plot(R,rho)
    plt.show()
    return rho

## 3) Pega (ultimas) energias e forcas de oscilador (duas listas)
def energy_and_osc(file):
    exc_energies = []
    osc_str = []
    with open(file,'r') as f:
        i=0
        for line in f:
            if 'Excited State' in line:
                if 'Excited State   1:' in line:
                    i+=1
                    if i>1:
                        exc_energies.clear()
                        osc_str.clear()
                        i=0
                line=line.replace('=',' ').split()
                exc_energies.append(float(line[4]))
                osc_str.append(float(line[9]))
    return exc_energies,osc_str

## 4) Pega funcional e base usados no calculo (Com IOPs se tiver) (retornar uma string)
def func_basis_iop(file):
    linha = []
    functional = []
    basis = []
    iop = []
    var = []
    newvar = []
    with open(file, 'r') as f: 
        for line in f:
            if ('SCF Done: ') in line:
                functional = line.split('(R')
                functional = functional[1]
                functional = functional.split(')')
                functional = functional[0]
            if ('Standard basis: ') in line:
                basis = line.split(': ')
                basis = basis[1]
                basis = basis.split(' (')
                basis = basis[0]
            if ('(3/107=') in line:
                linha.append(line)
                iop = linha[0]
                iop = iop.split(' ')
                for word in iop:
                    if ('iop') in word:
                        var.append(word)
                for element in var:
                    if (element) not in newvar:
                        newvar.append(element)
                iop =' '.join([str(item) for item in newvar])
        return functional+'/'+basis+' '+iop
    
## 5) Pega o transition dipole moment do S1 (retorna um numero)
def get_moment(file):
    busca = "transition electric dipole moments" 
    n = -1
    with open(file ,'r') as f:
        for line in f:
            if busca in line:
                n = 0
                dip_sqrd = []
            elif n >= 0 and n < 1:
                n += 1
            elif n == 1 and "transition velocity" not in line:    
                line = line.split()
                dip_sqrd.append(float(line[4]))
                n +=1
            elif n >= 3:
                n = -1
        mu=np.sqrt(float(dip_sqrd[-1])) 
    return mu

    ###### BATCH 2

    #1) i)Ajustar a funcao 1 do batch 1 pra retornar um array com as geometrias e outro com os atomos.

    #2) i) Ajustar a funcao 2 do batch 1 pra retornar uma array de frequencias e um array de massas reduzidas. As freqs devem ser convertidas de cm^-1 para freq angular (Hz) e massas reduzidas de au para kg.
    ### ii) Fazer uma funcao nova que calcula a distribuicao de modos normais pra cada frequencia. Argumentos: nome do arquivo, temperatura. Retorna:

    #3) i) Ajustar a funcao 3 do batch 1 pra retornar um array com energias e outro array com forcas de oscilador
def energy_and_osc(file):
    exc_energies = []
    osc_str = []
    with open(file, 'r') as f:
        i = 0
        for line in f:
            if 'Excited State' in line:
                if 'Excited State   1:' in line:
                    i += 1
                    if i > 1:
                        exc_energies.clear()
                        osc_str.clear()
                        i = 0
                line = line.replace('=', ' ').split()
                exc_energies.append(float(line[4]))
                osc_str.append(float(line[9]))
    energy = np.array(exc_energies)
    f_osc = np.array(osc_str)
    return energy,f_osc
    
    #   ii) Fazer uma funcao que calcula o espectro de absorcao usando as energias e forcas de oscilador. Use a expressao que a gente usa no nuclear ensemble com só uma geometria. Cada excitacao deve contribuir com uma gaussiana centrada
    #na energia de transicao e com um desvio padrao sigma. Argumentos: nome do arquivo, sigma. Retorna: dois arrays: os valores para os eixos x e y do espectro. 
def abs_spectra(file,sigma):
    energy, f_osc = energy_and_osc(file)
    y_ax = 0
    x_ax=np.linspace(energy.min()-10*sigma, energy.max()+10*sigma, 100)
    cte=((constants.pi*(constants.e**2)*constants.hbar)/(2*constants.m_e*constants.c*constants.epsilon_0))
    
    for i in range(len(energy)):
        spec=cte*f_osc[i]*stats.norm.pdf(x_ax, energy[i], sigma)
        y_ax = y_ax + spec

    return cte,x_ax,y_ax

    #    iii) Plota espectro de absorcao
def plot_abs_spectra(file,sigma):
    energy, f_osc = energy_and_osc(file)
    cte,x_ax, y_ax = abs_spectra(file,sigma)
    
    ##### PLOT ####
    fig, ax = plt.subplots(figsize=(10,5))
    #plt.vlines(x=energy,ymin=0,ymax=30*cte*f_osc,color='red',ls=':',lw=2, label='Excited State Energy')    #Excited State Energy proportional to oscillator strength              
    plt.vlines(x=energy,ymin=0,ymax=20*cte,color='red',ls=':',lw=2, label='Excited State Energy')
    
    #### FONT #####
    plt.rcParams["font.family"] = 'Times New Roman'
    csfont = {'fontname':'Times New Roman'}

    #### STYLE ####
    ax.plot(x_ax,y_ax, lw=2, color='blue', label='Absorption Spectra') 
    ax.set_xlabel('Energy (eV)', size=18,**csfont)   
    ax.set_ylabel('Cross Section ($\AA$²)', size=18,**csfont)
    #ax.set_xlim([0,5])
    #ax.set_ylim([0,1.0e-40])
    #ax.set_xticks([0,1,2,3,4,5])
    #ax.set_yticks([0,1.0e-40]) 
    ax.tick_params(axis='both', which='major', labelsize=12)

    plt.legend(loc='upper center', fontsize=14)
    plt.tight_layout() 
    plt.show()

    #4) i) Fazer uma funcao que gera inputs para os calculos de energia de reorganizacao com mesmo nivel de calculo que o log que serve de input.
    ## Argumentos: nome do arquivo. Retorna: Nada, mas cria dois inputs de opt: um com carga positiva e outro negativa.  
def header(file):
    with open(file, 'r') as f: 
        for line in f:
            if ('%nproc') in line:
                nproc = line.split('\n')
                nproc = nproc[0]
            if ('%mem') in line:
                mem = line.split('\n')
                mem = mem[0]
    return nproc,mem
def reorg_energy(file):
    atomos, geometria = pega_geometria(file)
    _func_basis_iop =  func_basis_iop(file)
    nproc, mem = header(file)
    with open('opt_chargeplus.com', 'w') as plus:
        plus.write(nproc + '\n')
        plus.write(mem + '\n')
        plus.write(' #n ' + _func_basis_iop + ' ' + 'opt' + '\n')
        plus.write(' ' + '\n')
        plus.write('  Charged +' + '\n')
        plus.write(' ' + '\n')
        plus.write('1 2' + '\n')
        sp= '     '
        for i in range(len(atomos)):
            plus.write(str(atomos[i]) + sp + str(geometria[i,0]) + sp + str(geometria[i,1]) + sp + str(geometria[i,2]) + '\n')
    with open('opt_chargeminus.com', 'w') as minus:
        minus.write(nproc + '\n')
        minus.write(mem + '\n')
        minus.write(' #n ' +  _func_basis_iop + ' ' + 'opt' + '\n')
        minus.write(' ' + '\n')
        minus.write('  Charged -' + '\n')
        minus.write(' ' + '\n')
        minus.write('-1 2' + '\n')
        sp= '     '
        for i in range(len(atomos)):
            minus.write(str(atomos[i]) + sp + str(geometria[i,0]) + sp + str(geometria[i,1]) + sp + str(geometria[i,2]) + '\n')

    #5) i) Ajustar funcao 5 do batch 1 pra retornar apenas um array com as componentes do vetor.
def get_moment_vector(file):
    busca = "transition electric dipole moments" 
    n = -1
    with open(file ,'r') as f:
        for line in f:
            if busca in line:
                n = 0
                dip_sqrd = []
            elif n >= 0 and n < 1:
                n += 1
            elif n == 1 and "transition velocity" not in line:    
                line = line.split()
                dip_vec = []
                for j in range(1,4):
                    dip_vec.append(float(line[j]))
                dip_sqrd.append(float(line[4]))
                n +=1
            elif n >= 3:
                n = -1
        mu_components = np.array(dip_vec)
    return mu_components 

    ##  ii) Fazer um notebook jupyter com análise de KMC 
