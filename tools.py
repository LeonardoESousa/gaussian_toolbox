## Funcoes
import numpy as np

## 1) Pega ultima geometria do log (printa a ultima geometria)

## 2) Pega as frequencias (retorna lista de frequencias)

def pega_freqs(file):
    freq = []
    with open(file, 'r') as f:#abre o arquivo pra ler
        for line in f: #para cada elemento(no caso linha) do arquivo
            line = line.split() #separa cada elemento(da linha) por espaço
            if "Frequencies" in line: #se tiver "Frequencies" na linha
                for elem in line: #para cada elemento da linha
                    try: #tente pegar os numeros
                        numero = float(elem)
                        freq.append(numero) #se for numero colocar na lista
                    except:
                        pass
            else:
                pass
    return freq

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
    important_lines = []
    iop = []
    with open(file, 'r') as f: 
        for index, line in enumerate(f):
            if ('# ') in line:
                important_lines.append(line)        
    important_line = important_lines[0]
    important_line = important_line.split(' ')
    for word in important_line:
        if ('/' and '-') in word:
            func_basis = word
        elif ('iop') in word:
            iop.append(word)
    return func_basis,iop
    
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
                dip_vec = []
                for j in range(1,4):
                    dip_vec.append(float(line[j]))
                dip_sqrd.append(float(line[4]))
                n +=1
            elif n >= 3:
                n = -1
        mu=np.sqrt(float(dip_sqrd[-1])) 
    return mu,dip_vec 