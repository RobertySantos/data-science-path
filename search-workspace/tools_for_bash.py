import argparse

def main():
    # 1. Criamos o "estacionamento" de argumentos
    parser = argparse.ArgumentParser(description="Meu Lab de Testes")

    # 2. Definimos as opções curtas e longas (action="store_true" cria o interruptor)
    parser.add_argument("-a", "--analise", action="store_true", help="Rodar análise")
    parser.add_argument("-b", "--backup",  action="store_true", help="Fazer backup")
    parser.add_argument("-c", "--clean",   action="store_true", help="Limpar temporários")

    args = parser.parse_args()

    # 3. O código checa quais chaves você "ligou" no terminal
    if args.analise:
        print("-> Executando Análise de Dados...")
    
    if args.backup:
        print("-> Fazendo Backup dos arquivos...")
        
    if args.clean:
        print("-> Limpando a pasta de testes...")

if __name__ == "__main__":
    main()