# Programa para criar uma lista de 5 nomes fornecidos pelo usuário e imprimir cada um

# Criamos uma lista vazia chamada 'nomes'
nomes = []

# Usamos um loop for para solicitar 5 nomes ao usuário
for i in range(5):
    # Solicita que o usuário digite um nome
    nome = input(f"Digite o nome {i+1}: ")
    # Adiciona o nome digitado à lista 'nomes'
    nomes.append(nome)

# Exibe uma mensagem indicando que os nomes serão listados
print("\nLista de nomes digitados:")

# Percorre cada nome na lista 'nomes' usando um loop for
for nome in nomes:
    # Imprime cada nome da lista
    print(nome)
