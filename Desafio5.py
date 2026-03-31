# Passo 1: Solicitar os dados ao usuário
# Usamos float() para permitir números decimais (ex: 5.5)
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

# Passo 2: Realizar o cálculo da área
# Seguindo a fórmula (Base * Altura) / 2
area = (base * altura) / 2

# Passo 3: Exibir o resultado
# Usamos uma f-string (o 'f' antes das aspas) para incluir a variável dentro do texto
print(f"A área do triângulo com base {base} e altura {altura} é: {area}")
