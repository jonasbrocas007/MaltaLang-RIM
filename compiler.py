if not __name__ == "__main__":
    exit()
import os

numero_da_linha = 1
numero_do_bit = 0
lista_dos_numeros = []


length = len(lista_dos_numeros)

while True:
    numero_do_bit += 1
    line = os.path.exists("malta/line" + str(numero_da_linha) + "/" + str(numero_do_bit) + "/raul.png")

    if numero_do_bit == 9:
        numero_da_linha += 1
        numero_do_bit = 1
           
    if line == False:
        lista_dos_numeros.append('0')
    else:
        lista_dos_numeros.append('1')

    #debug
    #print(numero_do_bit, 'bit')
    #print(numero_da_linha, 'linha')
    if not os.path.exists("malta/line" + str(numero_da_linha) + "/" + str(numero_do_bit)):
        break
lista_dos_numeros.reverse()
output = [lista_dos_numeros[i:i+8] for i in range(0,len(lista_dos_numeros),8)]
f = open('code.malta', 'w')
f.write(str(output))