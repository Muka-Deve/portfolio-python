# Função para contar as palavras em um arquivo
def contar_palavras(arquivo):
    with open(arquivo, 'r') as f:
        texto = f.read()
    palavras = texto.split()
    return len(palavras)

# Especificar o arquivo de entrada
arquivo_entrada = 'entrada.txt'

# Criar um arquivo de exemplo (entrada.txt)
with open(arquivo_entrada, 'w') as f:
    f.write("Este é um exemplo de programa simples em Python.\nVamos contar as palavras.")

# Contar as palavras no arquivo
numero_palavras = contar_palavras(arquivo_entrada)

# Exibir o número de palavras
print(f"O número de palavras no arquivo é: {numero_palavras}")

# Salvar o resultado em outro arquivo
with open('resultado.txt', 'w') as f:
    f.write(f"Número de palavras: {numero_palavras}")
