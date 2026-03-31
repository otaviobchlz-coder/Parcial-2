# Este programa solicita ao usuário dois números e calcula a soma
# Inclui tratamento de erros para evitar que o programa quebre se o usuário digitar algo inválido

while True:
    try:
        # Solicita o primeiro número ao usuário
        numero1 = float(input("Digite o primeiro número: "))
        # Solicita o segundo número ao usuário
        numero2 = float(input("Digite o segundo número: "))
        break  # Sai do loop se ambos os números forem válidos
    except ValueError:
        # Se o usuário digitar algo que não seja número, exibe uma mensagem de erro
        print("Entrada inválida! Por favor, digite apenas números.")

# Calcula a soma dos dois números
soma = numero1 + numero2

# Exibe o resultado na tela
print(f"A soma de {numero1} e {numero2} é: {soma}")
