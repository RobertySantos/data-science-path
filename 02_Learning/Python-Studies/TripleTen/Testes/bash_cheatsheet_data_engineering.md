# 🖥️ Bash Terminal — Cheat Sheet Avançada para Engenharia de Dados
> **Nível:** Intermediário–Avançado | **Contexto:** VS Code Terminal | **Foco:** Arquivos CSV & JSON

---

## 📁 MÓDULO 1 — Manipulação de Arquivos Grandes (CSV & JSON)

### 1.1 — Inspeção e Leitura

| Comando | O que faz | Exemplo Prático |
|---|---|---|
| `head -n 5 arquivo.csv` | Exibe as primeiras N linhas | `head -n 5 vendas.csv` → ver cabeçalho + 4 linhas |
| `tail -n 10 arquivo.csv` | Exibe as últimas N linhas | `tail -n 10 logs.csv` → checar os registros mais recentes |
| `wc -l arquivo.csv` | Conta linhas (total de registros) | `wc -l clientes.csv` → retorna `10001 clientes.csv` |
| `wc -c arquivo.json` | Conta bytes (tamanho do arquivo) | `wc -c dados.json` → útil para arquivos grandes |
| `cat arquivo.csv` | Despeja TODO o conteúdo no terminal | ⚠️ Evite em arquivos >10MB — congela o terminal |
| `less arquivo.csv` | Paginação interativa (navegável) | Use `q` para sair, `/termo` para buscar dentro |
| `file dados.json` | Detecta o tipo real do arquivo | Retorna: `JSON data` ou `ASCII text` |

### 1.2 — Filtragem e Busca

| Comando | O que faz | Exemplo Prático |
|---|---|---|
| `grep "SP" clientes.csv` | Busca linhas que contêm o padrão | Filtra todos clientes com "SP" |
| `grep -c "ERROR" app.log` | Conta quantas linhas batem | Quantos erros existem no log? |
| `grep -i "null" dados.csv` | Busca case-insensitive | Acha "NULL", "Null", "null" |
| `grep -v "header" arquivo.csv` | Exibe linhas que NÃO contêm o padrão | Remove a linha de cabeçalho da saída |
| `grep -n "timeout" app.log` | Mostra número da linha com a ocorrência | Localiza erros para depuração |
| `cut -d',' -f1,3 dados.csv` | Extrai colunas específicas (delimitador `,`) | Retorna só colunas 1 e 3 |
| `awk -F',' '{print $2}' dados.csv` | Extrai coluna 2 com separador customizado | Mais poderoso que `cut` para lógica |
| `sort -t',' -k2 dados.csv` | Ordena pelo campo 2 | Ordenar clientes por nome |
| `sort -t',' -k3 -rn dados.csv` | Ordena campo 3 numérico e reverso (maior→menor) | Ranking de vendas decrescente |
| `uniq -c` | Conta ocorrências de linhas consecutivas repetidas | Sempre use com `sort` antes |

### 1.3 — Manipulação de JSON com `jq`

> **Instalar:** `sudo apt install jq` (Linux) ou `brew install jq` (Mac)

| Comando | O que faz | Exemplo Prático |
|---|---|---|
| `jq '.' dados.json` | Pretty-print formatado e colorido | Leitura humana de JSON compactado |
| `jq '.nome' dados.json` | Extrai campo específico | Retorna o valor da chave `nome` |
| `jq '.[0]' array.json` | Acessa o primeiro elemento de um array | Inspeciona o 1º registro |
| `jq '.[] \| .email' usuarios.json` | Extrai campo de todos os elementos | Lista todos os e-mails |
| `jq 'length' array.json` | Conta elementos do array | Equivalente ao `wc -l` para JSON |
| `jq 'select(.status == "ativo")' dados.json` | Filtra por condição | Registros onde status = "ativo" |
| `jq '[.[] \| {nome, email}]' usuarios.json` | Projeta apenas campos escolhidos | Reduz o payload do JSON |

---

## ⚖️ MÓDULO 2 — Comandos que Parecem Iguais mas Não São

### 2.1 — `echo` vs `cat`

| Critério | `echo` | `cat` |
|---|---|---|
| **O que recebe** | Um texto/string literal | Um arquivo existente |
| **Origem do conteúdo** | Você digita o texto na hora | Lê bytes de um arquivo do disco |
| **Uso principal** | Criar conteúdo, debug de variáveis | Exibir ou concatenar arquivos |
| **Exemplo** | `echo "id,nome,valor"` | `cat cabeçalho.csv dados.csv` |
| **Com variáveis** | `echo $HOME` → exibe `/home/user` | `cat` não expande variáveis |
| **Risco** | Nenhum | ⚠️ `cat arquivo_gigante.csv` trava o terminal |

**Regra prática:** use `echo` para *gerar texto*, use `cat` para *ler arquivo*.

---

### 2.2 — `rm` vs `rmdir`

| Critério | `rm` | `rmdir` |
|---|---|---|
| **Remove** | Arquivos (e diretórios com `-r`) | Apenas diretórios **vazios** |
| **Segurança** | ⚠️ Sem lixeira — IRREVERSÍVEL | Mais seguro (falha se não estiver vazio) |
| **Recursivo** | `rm -r pasta/` remove tudo dentro | Não existe modo recursivo |
| **Forçado** | `rm -rf pasta/` — sem confirmação | Nunca força |
| **Uso ideal** | Limpeza de arquivos temporários e CSVs processados | Remover estrutura de diretório vazia após ETL |
| **⚠️ Nunca faça** | `rm -rf /` ou `rm -rf *` sem revisão | — |

---

### 2.3 — `mv` vs `cp`

| Critério | `mv` | `cp` |
|---|---|---|
| **Operação** | Move/renomeia (origem some) | Copia (origem permanece) |
| **Arquivo original** | ❌ Removido do local de origem | ✅ Preservado |
| **Uso em dados** | Mover CSV processado para `/output` | Backup antes de transformações |
| **Recursivo** | `mv pasta/ destino/` (funciona direto) | `cp -r pasta/ destino/` (precisa de `-r`) |
| **Renomear** | `mv dados.csv dados_v2.csv` | Não renomeia — só copia |

---

### 2.4 — `>` vs `>>`

| Critério | `>` (sobrescreve) | `>>` (acrescenta) |
|---|---|---|
| **Comportamento** | Cria ou **substitui** o arquivo inteiro | Cria ou **adiciona** ao final |
| **Risco** | ⚠️ Apaga conteúdo existente silenciosamente | Seguro para logs e acumulação |
| **Exemplo** | `echo "id,nome" > novo.csv` | `cat lote2.csv >> resultado.csv` |
| **Uso típico** | Gerar arquivo de resultado limpo | Agregar múltiplos arquivos CSV por lote |

---

### 2.5 — `find` vs `locate`

| Critério | `find` | `locate` |
|---|---|---|
| **Busca em** | Disco em tempo real | Banco de dados de índice (cache) |
| **Velocidade** | Lento em árvores grandes | Muito rápido |
| **Atualização** | Sempre atual | Pode estar desatualizado (`updatedb` para atualizar) |
| **Filtros** | Muito poderoso (por data, tamanho, tipo) | Apenas por nome |
| **Exemplo** | `find . -name "*.csv" -size +10M` | `locate vendas_2024.csv` |

---

## 🔗 MÓDULO 3 — Pipe (`|`) e Redirecionadores (`>`, `>>`) na Prática

> **Conceito-chave:** o `pipe` conecta a **saída** de um comando à **entrada** do próximo.  
> Pense como um pipeline ETL: cada etapa transforma os dados antes de passar adiante.

### 3.1 — Anatomia do Pipe

```bash
comando_A | comando_B | comando_C
#   ↑ gera dados    ↑ transforma   ↑ apresenta/salva
```

### 3.2 — Exemplos Práticos de Análise de Dados

| Objetivo | Comando | Explicação passo a passo |
|---|---|---|
| **Contar registros únicos de uma coluna** | `cut -d',' -f2 vendas.csv \| sort \| uniq -c \| sort -rn` | Extrai col.2 → ordena → conta repetições → ordena por frequência |
| **Top 5 valores mais frequentes** | `cut -d',' -f3 dados.csv \| sort \| uniq -c \| sort -rn \| head -5` | Pipeline completo de frequência |
| **Buscar e contar erros em log** | `grep "ERROR" app.log \| wc -l` | Filtra linhas de erro → conta |
| **Verificar duplicatas por ID** | `cut -d',' -f1 clientes.csv \| sort \| uniq -d` | `-d` mostra só as linhas duplicadas |
| **Filtrar JSON e salvar resultado** | `jq '.[] \| select(.ativo == true)' users.json > ativos.json` | Filtra e redireciona para novo arquivo |
| **Ver distribuição de status** | `cut -d',' -f5 pedidos.csv \| sort \| uniq -c` | Quantos pedidos por status |
| **Checar se tem valores nulos** | `grep -c ",," dados.csv` | Conta campos vazios consecutivos (,,) |
| **Criar CSV filtrado sem cabeçalho** | `grep -v "^id" dados.csv \| grep "2024" > dados_2024.csv` | Remove cabeçalho e filtra por ano |
| **Acumular resultados diários** | `echo "$(date): $(wc -l < novos.csv) registros" >> auditoria.log` | Registra log de auditoria com data |
| **Inspecionar encoding do arquivo** | `file -i dados.csv \| grep charset` | Detecta se é UTF-8, ISO-8859, etc. |

### 3.3 — Padrão de Pipeline ETL no Terminal

```bash
# Exemplo: extrair clientes ativos de SP com alto valor, salvar e auditar
cat clientes_raw.csv \
  | grep ",SP," \
  | grep ",ativo," \
  | awk -F',' '$6 > 1000' \
  | sort -t',' -k6 -rn \
  > clientes_sp_alto_valor.csv

# Registrar auditoria
echo "$(date '+%Y-%m-%d %H:%M'): $(wc -l < clientes_sp_alto_valor.csv) registros exportados" >> pipeline_audit.log
```

### 3.4 — Redirecionamento de Erros

| Símbolo | Significado | Exemplo |
|---|---|---|
| `>` | Redireciona stdout (saída padrão) | `ls > lista.txt` |
| `>>` | Acrescenta ao stdout | `ls >> lista.txt` |
| `2>` | Redireciona stderr (erros) | `comando 2> erros.log` |
| `2>>` | Acrescenta stderr | `comando 2>> erros.log` |
| `&>` | Redireciona stdout **e** stderr | `script.sh &> tudo.log` |
| `2>/dev/null` | Descarta erros silenciosamente | `find / -name "*.csv" 2>/dev/null` |

---

## 🧪 EXERCÍCIOS PRÁTICOS

> Prepare um ambiente: crie um arquivo `clientes.csv` com o conteúdo abaixo para todos os exercícios.

```bash
# Execute no terminal para criar o arquivo de teste:
cat > clientes.csv << 'EOF'
id,nome,estado,status,valor
1,Ana Lima,SP,ativo,1500
2,Bruno Costa,RJ,inativo,800
3,Carla Dias,SP,ativo,3200
4,Daniel Souza,MG,ativo,950
5,Elena Matos,SP,inativo,4100
6,Felipe Nunes,RJ,ativo,2750
7,Gabi Rocha,SP,ativo,620
8,Hugo Alves,MG,inativo,1100
9,Iris Pinto,SP,ativo,3800
10,João Vaz,RJ,ativo,2200
EOF
```

---

### 🔵 Exercício 1 — Inspeção Básica
**Objetivo:** Verificar a estrutura do arquivo sem carregá-lo inteiro.

**Tarefa:** Execute os comandos para:
- a) Ver apenas o cabeçalho e as 3 primeiras linhas de dados
- b) Descobrir quantos registros existem (excluindo o cabeçalho)
- c) Exibir apenas as 3 últimas linhas

<details>
<summary>💡 Solução</summary>

```bash
# a)
head -n 4 clientes.csv

# b)
tail -n +2 clientes.csv | wc -l

# c)
tail -n 3 clientes.csv
```
</details>

---

### 🔵 Exercício 2 — Filtragem com `grep`
**Objetivo:** Extrair subconjuntos de dados por padrão.

**Tarefa:**
- a) Liste apenas os clientes do estado SP
- b) Conte quantos clientes estão com status "inativo"
- c) Mostre as linhas que NÃO pertencem ao estado SP

<details>
<summary>💡 Solução</summary>

```bash
# a)
grep ",SP," clientes.csv

# b)
grep -c "inativo" clientes.csv

# c)
grep -v ",SP," clientes.csv
```
</details>

---

### 🔵 Exercício 3 — Extração de Colunas com `cut`
**Objetivo:** Trabalhar com colunas específicas do CSV.

**Tarefa:**
- a) Extraia apenas os nomes (coluna 2) de todos os clientes
- b) Extraia o ID e o estado (colunas 1 e 3)
- c) Liste apenas os estados presentes no arquivo (sem repetição), em ordem alfabética

<details>
<summary>💡 Solução</summary>

```bash
# a)
cut -d',' -f2 clientes.csv

# b)
cut -d',' -f1,3 clientes.csv

# c)
cut -d',' -f3 clientes.csv | sort | uniq
```
</details>

---

### 🟡 Exercício 4 — Pipeline de Análise
**Objetivo:** Encadear comandos para responder perguntas de negócio.

**Tarefa:**
- a) Qual estado aparece com mais frequência? (ranking de estados)
- b) Quantos clientes únicos existem por status?
- c) Liste os nomes de clientes ativos do estado SP

<details>
<summary>💡 Solução</summary>

```bash
# a)
cut -d',' -f3 clientes.csv | grep -v "estado" | sort | uniq -c | sort -rn

# b)
cut -d',' -f4 clientes.csv | grep -v "status" | sort | uniq -c

# c)
grep ",SP," clientes.csv | grep ",ativo," | cut -d',' -f2
```
</details>

---

### 🟡 Exercício 5 — Redirecionamento e Criação de Arquivos
**Objetivo:** Salvar resultados de análises em novos arquivos.

**Tarefa:**
- a) Crie um arquivo `clientes_sp.csv` contendo apenas clientes de SP (com cabeçalho)
- b) Crie um arquivo `relatorio.txt` com o texto `"Total de clientes SP: X"` onde X é o número real
- c) Adicione ao `relatorio.txt` (sem sobrescrever) o texto `"Gerado em: <data atual>"`

<details>
<summary>💡 Solução</summary>

```bash
# a)
head -n 1 clientes.csv > clientes_sp.csv
grep ",SP," clientes.csv >> clientes_sp.csv

# b)
echo "Total de clientes SP: $(grep -c ',SP,' clientes.csv)" > relatorio.txt

# c)
echo "Gerado em: $(date '+%Y-%m-%d %H:%M')" >> relatorio.txt
```
</details>

---

### 🔴 Exercício 6 — Desafio: Pipeline ETL Completo
**Objetivo:** Simular um mini-pipeline de engenharia de dados.

**Tarefa:**  
Crie um único pipeline (pode usar `\` para quebrar as linhas) que:
1. Leia o `clientes.csv`
2. Filtre apenas clientes **ativos**
3. Filtre apenas os do estado **SP**
4. Extraia somente as colunas **nome** e **valor**
5. Ordene pelo **valor** de forma **decrescente**
6. Salve o resultado em `top_clientes_sp.csv`
7. Em seguida, em **uma linha separada**, registre no arquivo `audit.log` a mensagem: `"[DATA HORA] ETL concluído: X registros"` (X = número de linhas do arquivo gerado)

<details>
<summary>💡 Solução</summary>

```bash
# Passo 1–6: Pipeline ETL
grep ",ativo," clientes.csv \
  | grep ",SP," \
  | cut -d',' -f2,5 \
  | sort -t',' -k2 -rn \
  > top_clientes_sp.csv

# Passo 7: Auditoria
echo "[$(date '+%Y-%m-%d %H:%M')] ETL concluído: $(wc -l < top_clientes_sp.csv) registros" >> audit.log
```
</details>

---

### 🔴 Exercício 7 — Detetive de Dados (Qualidade)
**Objetivo:** Identificar problemas de qualidade de dados com comandos Bash.

**Tarefa:**  
Sem editar o arquivo original, use comandos para responder:
- a) Existe algum campo completamente vazio (vírgulas consecutivas `,,`) no arquivo?
- b) Algum nome de cliente está duplicado?
- c) Qual é o valor máximo na coluna `valor`? (dica: `sort -t',' -k5 -rn` + `head`)

<details>
<summary>💡 Solução</summary>

```bash
# a) Verificar campos vazios
grep -c ",," clientes.csv
# 0 = sem campos vazios

# b) Verificar nomes duplicados
cut -d',' -f2 clientes.csv | sort | uniq -d
# saída vazia = sem duplicatas

# c) Valor máximo
tail -n +2 clientes.csv | sort -t',' -k5 -rn | head -1 | cut -d',' -f5
```
</details>

---

*"O terminal não é um atalho — é a linguagem nativa dos dados."*  
**Próximos passos sugeridos:** `awk` avançado, `sed` para transformações, `xargs` para operações em lote, e `bash scripting` para automatizar esses pipelines.
