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

## 4) Pega funcional e base usados no calculo (Com IOPs se tiver) (retornar uma string)

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