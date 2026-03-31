# Programa para verificar se um número é par ou ímpar
# Inclui tratamento de erro caso o usuário digite algo que não seja um número inteiro

while True:
    try:
        # Solicita que o usuário digite um número
        numero = int(input("Digite um número inteiro: "))
        break  # Sai do loop se a entrada for válida
    except ValueError:
        # Executado se o usuário digitar algo que não possa ser convertido em inteiro
        print("Entrada inválida! Por favor, digite um número inteiro.")

# Verifica se o número é par usando o operador módulo (%)
# O operador % retorna o resto da divisão do número por 2
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # Executado se o resto for 0
else:
    print(f"O número {numero} é ímpar.")  # Executado se o resto for diferente de 0
