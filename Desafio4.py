# Calculadora simples em Python
# Permite ao usuário realizar operações de soma, subtração, multiplicação e divisão

# Exibe uma mensagem de boas-vindas
print("=== Calculadora Simples ===")

# Solicita que o usuário digite o primeiro número
# A função float() permite aceitar números decimais
num1 = float(input("Digite o primeiro número: "))

# Solicita que o usuário digite o segundo número
num2 = float(input("Digite o segundo número: "))

# Exibe as opções de operações disponíveis
print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Solicita que o usuário escolha a operação desejada
operacao = input("Digite o número da operação (1/2/3/4): ")

# Verifica qual operação o usuário escolheu e realiza o cálculo
if operacao == "1":
    resultado = num1 + num2  # Soma
    print(f"O resultado da soma é: {resultado}")
elif operacao == "2":
    resultado = num1 - num2  # Subtração
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "3":
    resultado = num1 * num2  # Multiplicação
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "4":
    # Antes de dividir, verifica se o segundo número não é zero para evitar erro
    if num2 != 0:
        resultado = num1 / num2  # Divisão
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    # Se o usuário digitou uma opção inválida
    print("Operação inválida! Escolha entre 1, 2, 3 ou 4.")
