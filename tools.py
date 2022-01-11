## Funcoes

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