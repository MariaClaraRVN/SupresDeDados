import re
#biblioteca de padrão de expressão regular

def comprimir_arquivo(arquivo_entrada, arquivo_saida):
    #recebe os arquivos de entrada e saida
    with open(arquivo_entrada, 'r') as arquivo_origem:
        #abre o arquivo de entrada em modo leitura
        texto = arquivo_origem.read()
        #cria a variavel texto e le o arquivo original

    texto_comprimido = re.sub(r'(.)\1+', lambda match: match.group(1) + str(len(match.group(0))), texto)
# o re.sub encontra os caracteres repetidos
#o lambda é o argumento de substituição
#o match.group é o caracter encontrado
# o len(math.group é a quantidade que foi achada de repetições
# a função substitui a sequencia encontrada pelo caracter seguido do numero de repetições

    with open(arquivo_saida, 'w') as arquivo_destino:
        arquivo_destino.write(texto_comprimido)
        #abre o arquivo de modo de saida 
        #escreve o conteudo comprimido nele

    print('Arquivo comprimido com sucesso!')

def descomprimir_arquivo(arquivo_comprimido, arquivo_descomprimido):
    #recebe os arquivos comprimidos e descomprimidos
    with open(arquivo_comprimido, 'r') as arquivo_origem:
          #abre o arquivo comprimido em modo leitura
        texto_comprimido = arquivo_origem.read()
         #cria a variavel texto_comprimido e le o arquivo original

    texto_descomprimido = re.sub(r'(.)\d', lambda match: match.group(1) * int(match.group(0)[1:]), texto_comprimido)
# o re.sub encontra os digitos repetidos
#o lambda é o argumento de substituição
#o match.group é o digito encontrado
# o len(math.group é o caracter original
# o int (math.group é o numero de repetições dos digitos
# a função substitui a sequencia encontrada pelo caracter seguido do numero de repetições

    with open(arquivo_descomprimido, 'w') as arquivo_destino:
        arquivo_destino.write(texto_descomprimido)
        #abre o arquivo descomprimido em modo escrita
        #escreve o conteudo descomprimido nele

    print('Arquivo descomprimido com sucesso!')

# Exemplo de uso:
arquivo_entrada = 'arquivo_original.txt'
arquivo_comprimido = 'arquivo_comprimido.txt'
arquivo_descomprimido = 'arquivo_descomprimido.txt'

comprimir_arquivo(arquivo_entrada, arquivo_comprimido)
descomprimir_arquivo(arquivo_comprimido, arquivo_descomprimido)

#foi feita a descrição dos aqruivos de entrada e saida
#foi feita as funções