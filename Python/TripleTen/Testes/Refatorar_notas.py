import os
from google import genai
import time

# 1. Configuração do Cliente
# Use a sua chave aqui
client = genai.Client(api_key="AIzaSyBb94emSIJ3e1HxajogEHrwOQcdmN8we0U")

# Alterado para 2.0 para evitar o erro 404 da v1.5
MODEL_ID = "gemini-2.0-flash" 

# 2. Caminhos
PASTA_NOTAS = r'C:\Users\fa-he\OneDrive\Desktop\Coração Forjado'
CAMINHO_MODELO = r'C:\Users\fa-he\OneDrive\Desktop\Coração Forjado\# 📑 [Título do Assunto].md'

with open(CAMINHO_MODELO, 'r', encoding='utf-8') as f:
    meu_modelo_exemplo = f.read()

def processar_notas():
    pastas_ignoradas = ['.obsidian', '.trash', 'attachments', 'Workspace', 'venv', 'Scripts']

    for raiz, pastas, arquivos in os.walk(PASTA_NOTAS):
        if any(ignorada in raiz for ignorada in pastas_ignoradas):
            continue

        for nome_arquivo in arquivos:
            if nome_arquivo.endswith(".md") and nome_arquivo != os.path.basename(CAMINHO_MODELO):
                caminho_completo = os.path.join(raiz, nome_arquivo)
                
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo_original = f.read()

                print(f"Refatorando com Gemini 2.0: {nome_arquivo}...")
                
                prompt_especifico = f"""
                Aja como um Engenheiro de Documentação. Transforme a nota abaixo seguindo EXATAMENTE este MODELO:
                
                --- MODELO DE REFERÊNCIA ---
                {meu_modelo_exemplo}
                --- FIM DO MODELO ---

                REGRAS:
                1. Mantenha TODA a densidade técnica e códigos.
                2. Não altere links de imagens ![[...]].
                3. Use a mesma hierarquia de títulos e Callouts do modelo.
                """

                try:
                    # Chamada direta
                    response = client.models.generate_content(
                        model=MODEL_ID,
                        contents=f"{prompt_especifico}\n\nNOTA ORIGINAL:\n{conteudo_original}"
                    )
                    
                    with open(caminho_completo, 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    
                    print(f"✅ {nome_arquivo} padronizado.")
                    time.sleep(5) # Rate limit um pouco mais conservador

                except Exception as e:
                    print(f"❌ Erro em {nome_arquivo}: {e}")
                    if "429" in str(e):
                        print("Limite atingido. Aguardando 60s...")
                        time.sleep(60)

if __name__ == "__main__":
    processar_notas()