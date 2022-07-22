if not __name__ == "__main__":
    # mensagem para os utilizadores saberem o que se passa quando o que eles
    # querem fazer não funciona
    exit("ERROR: The MaltaLang compiler should not be run as a library!")

import os

numero_da_linha = 1
lista_output = [] # lista com o bytecode final

while True:
    # sai do loop se a linha não existir
    if not os.path.exists("malta/line" + str(numero_da_linha)):
        break

    lista_de_bits = [] # lista para colocar os bits

    for numero_do_bit in range(8): # repete 8 vezes (uma para cada bit)
        line = os.path.exists("malta/line" + str(numero_da_linha) + "/" + str(numero_do_bit + 1) + "/raul.png")

        # adiciona o valor do bit na lista
        if line == False:
            lista_de_bits.append('0')
        else:
            lista_de_bits.append('1')
    
    # reverte a lista dos bits
    lista_de_bits.reverse()

    # adiciona a lista de bits revertida na lista output
    lista_output.append(lista_de_bits)

    numero_da_linha += 1

f = open('code.malta', 'w')
f.write(str(lista_output))
