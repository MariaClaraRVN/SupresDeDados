# Armazenando o arquivo com o texto em modo leitura
arquivo = open("./THERING.txt", "r")
texto = arquivo.read()

# Criando dois arquivos para escrever a compressão e descompressão
texto_comprimido = open("./texto_comprimido.txt", "w")
texto_descomprimido = open("./texto_descomprimido.txt", "w")

# Definindo variáveis para contar os espaços e uma para armazenar a frase comprimida
espacos = 0
frase_comprimida = ""

# Percorrendo cada caracter do texto e realizando a compressão
for caracter in texto:
    # Se o caracter for um espaço em branco, incrementa a variável espacos
    if caracter == " ":
        espacos += 1
    else:
        # Se a variável espacos for maior que zero, adiciona uma barra e o número de espaços em branco encontrados
        if espacos > 0:
            frase_comprimida += "|" + str(espacos)
            espacos = 0
        # Adiciona o caracter atual na frase comprimida
        frase_comprimida += caracter

# Escreve a frase comprimida no arquivo de texto comprimido
texto_comprimido.write(frase_comprimida)

#Descomprimindo
lista2 = []
i = 0
#Lendo cada caracter da frase comprimida se o caracter atual for | o codigo faz a descompressão da sequencia de espaços
while i < len(frase_comprimida):
    caracter_atual = frase_comprimida[i]
    if caracter_atual == "|":
#espacos_str irá armazenr a quantidade de espaços consecutivos
        espacos_str = ""
#A variável j é inicializada com o próximo índice após o "|" encontrado
        j = i + 1
#nesse loop ele verifica se o j esta dentro dos limites da frase_comprimida e se o caracter for um digito, isso garante que os digitos são a quantidade de espaços comprimidos
        while j < len(frase_comprimida) and frase_comprimida[j].isdigit():
            espacos_str += frase_comprimida[j]
            j +=1
            # A variavel virando um numero inteiro representando a quantidade de espaços consecutivos que foram comprimidos.
            espacos = int(espacos_str)
            #Colocando os espaços comprimidos de volta no lugar como está no arquivo original
            lista2.extend([" "] * espacos) 
        # O índice i é atualizado para j - 1 para pular a parte comprimida do texto e continuar a leitura após a sequência de espaços descomprimida
        i = j - 1 
    else:
        lista2.append(caracter_atual)
    i +=1
    
#armazendo a lista2 em uma variavel e colocando suas informações no texto_descomprimido 
frase_descomprimida = "".join(lista2)
texto_descomprimido.write(frase_descomprimida)

#print(lista1)
print(lista2)


# Fecha os arquivos
arquivo.close()
texto_comprimido.close()
texto_descomprimido.close()
