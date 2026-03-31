#Função para converter segundos para horas, minutos e segundos
def segundos_para_hms(segundos):
    horas = segundos // 3600  # 1 hora tem 3600 segundos
    minutos = (segundos % 3600) // 60  # 1 minuto tem 60 segundos
    segundos_restantes = segundos % 60  # Resto dos segundos
    return horas, minutos, segundos_restantes

# Função para converter horas, minutos e segundos para segundos
def hms_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Menu para o usuário escolher a conversão
def menu_conversao():
    print("Escolha uma opção de conversão:")
    print("1. Converter segundos para horas, minutos e segundos")
    print("2. Converter horas, minutos e segundos para segundos")
   
    # Solicita ao usuário a opção
    escolha = input("Digite 1 ou 2: ")

    if escolha == '1':
        # Solicita o número de segundos
        segundos = int(input("Digite o número de segundos: "))
        horas, minutos, segundos_restantes = segundos_para_hms(segundos)
        print(f"{segundos} segundos são {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
   
    elif escolha == '2':
        # Solicita horas, minutos e segundos
        horas = int(input("Digite o número de horas: "))
        minutos = int(input("Digite o número de minutos: "))
        segundos = int(input("Digite o número de segundos: "))
        total_segundos = hms_para_segundos(horas, minutos, segundos)
        print(f"{horas} horas, {minutos} minutos e {segundos} segundos são {total_segundos} segundos.")
   
    else:
        print("Opção inválida. Tente novamente.")

# Chama a função de menu
menu_conversao()
