from pathlib import Path

# 1. Pegamos o caminho da PASTA onde este arquivo .py está
BASE_DIR = Path(__file__).resolve().parent

# 2. Definimos o nome do arquivo que queremos criar
caminho_arquivo = BASE_DIR / "lines.txt"
lines = ['um', 'dois', 'três']

def writelines():
    with open(caminho_arquivo, 'w') as f:
        f.writelines('\n'.join(lines))

def readlines():
    with open(caminho_arquivo, 'r') as f:
        for line in f.readlines():
            print(line.strip())
writelines()
readlines()