import os

def calcular_juros_simples():
    # Limpa o console para ficar organizado (opcional)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*35)
    print("   CALCULADORA DE JUROS SIMPLES   ")
    print("="*35)
    
    try:
        # Entrada de dados
        capital = float(input("Digite o capital inicial (R$): "))
        taxa_percentual = float(input("Digite a taxa de juros (em %): "))
        tempo = float(input("Digite o tempo (período): "))
        
        # Processamento
        # i = taxa em decimal
        taxa_decimal = taxa_percentual / 100
        
        # J = C * i * t
        juros = capital * taxa_decimal * tempo
        
        # M = C + J
        montante = capital + juros
        
        # Saída de resultados
        print("\n" + "-"*35)
        print(f"RESUMO DO INVESTIMENTO:")
        print(f"-> Capital Inicial: R$ {capital:,.2f}")
        print(f"-> Juros Totais:    R$ {juros:,.2f}")
        print(f"-> Montante Final:  R$ {montante:,.2f}")
        print("-"*35)
        
    except ValueError:
        print("\n[ERRO]: Digite apenas números. Use ponto para decimais.")

if __name__ == "__main__":
    calcular_juros_simples()
