# 📁 Estrutura Completa do Projeto

## Visão Geral
Este é um guia detalhado de todos os arquivos e pastas do projeto **Previsão de Vendas E-commerce**.

---

## 📂 Arquivos na Raiz

### **main.py** ⭐ (65 linhas)
**Tipo:** Ponto de Entrada Principal
**Descrição:** Interface CLI (Command-Line Interface) para executar o projeto
**Funções:** 
- Comando `train` - Treina o modelo
- Comando `app` - Executa aplicação Streamlit
- Comando `predict` - Faz previsões via terminal

**Como usar:**
```bash
python main.py train
python main.py app
python main.py predict --day 15 --month 3 --dow 2
```

---

### **verify_setup.py** ✅ (201 linhas)
**Tipo:** Script de Verificação
**Descrição:** Verifica se o projeto está configurado corretamente

**Testa:**
- ✅ Imports (pandas, sklearn, joblib, streamlit)
- ✅ Estrutura de arquivos
- ✅ Carregamento de dados
- ✅ Imports internos

**Como usar:**
```bash
python verify_setup.py
```

---

### **requirements.txt** 📦
**Tipo:** Arquivo de Dependências
**Descrição:** Lista todas as bibliotecas Python necessárias com versões

**Conteúdo:**
```
pandas>=2.0.0
scikit-learn>=1.3.0
joblib>=1.3.0
streamlit>=1.28.0
seaborn>=0.13.0
```

**Como usar:**
```bash
pip install -r requirements.txt
```

---

### **pyproject.toml** 🔧
**Tipo:** Configuração do Projeto
**Descrição:** Metadados do projeto e configuração de build

**Informações:**
- Nome: previsao-vendas
- Versão: 0.1.0
- Python requerido: >=3.9
- Dependências: pandas, scikit-learn, joblib, streamlit, seaborn

---

### **README.md** 📖
**Tipo:** Documentação Principal
**Descrição:** Guia completo de uso do projeto

**Seções:**
- Descrição do Projeto
- Início Rápido
- Instalação
- Uso (train, app, predict)
- Estrutura do Projeto
- Dataset
- Modelo
- Performance
- Troubleshooting
- Melhorias Sugeridas

---

### **PROJECT_REVIEW.md** 📝
**Tipo:** Relatório Técnico de Revisão
**Descrição:** Resumo completo das melhorias implementadas

**Contém:**
- Comparativo Antes/Depois
- Detalhes de cada arquivo alterado
- Tabelas de melhoria
- Checklist de conclusão
- Destaques das melhorias

---

### **REVISION_SUMMARY.md** 📊
**Tipo:** Sumário de Alterações
**Descrição:** Visão geral das mudanças técnicas

**Contém:**
- Arquivos modificados
- Arquivos criados
- Checklist de alterações
- Próximas melhorias

---

### **QUICK_START.md** ⚡
**Tipo:** Guia Rápido
**Descrição:** Setup em 5 minutos

**Contém:**
- Passos de instalação
- Comandos principais
- Troubleshooting rápido
- Checklist de verificação

---

### **.gitignore** 🚫
**Tipo:** Arquivo de Git
**Descrição:** Lista de arquivos/pastas a ignorar no versionamento

**Exclui:**
- `__pycache__/`
- `.venv/`, `venv/`
- `.env`
- `model.pkl`
- `.idea/`, `.vscode/`
- `*.pyc`
- E muito mais...

---

### **.env.example** ⚙️
**Tipo:** Template de Variáveis de Ambiente
**Descrição:** Exemplo de arquivo `.env` para configuração

**Variáveis:**
```
DATA_PATH=./data/vendas_ecommerce.csv
MODEL_PATH=./model.pkl
RANDOM_STATE=42
TEST_SIZE=0.2
N_ESTIMATORS=100
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
```

---

## 📁 Pasta: src/

### **__init__.py** 📦 (5 linhas)
**Tipo:** Iniciador de Pacote Python
**Descrição:** Torna `src` um pacote Python válido
**Contém:** Metadados (version, author)

---

### **config.py** 🎛️ (38 linhas)
**Tipo:** Configuração Centralizada
**Descrição:** Centraliza todas as configurações do projeto

**Define:**
- `PROJECT_ROOT` - Raiz do projeto (dinâmica)
- `DATA_PATH` - Caminho para dados
- `MODEL_PATH` - Caminho para modelo
- `MODEL_CONFIG` - Parâmetros do RandomForest
- `TRAIN_TEST_CONFIG` - Configuração train/test split
- `FEATURE_COLUMNS` - Nomes das features
- `TARGET_COLUMN` - Nome do target
- `DATE_COLUMNS` - Possíveis colunas de data

**Benefício:** Mudanças de configuração em um só lugar!

---

### **preprocess.py** 🔧 (38 linhas)
**Tipo:** Módulo de Preprocessamento
**Descrição:** Carrega e preprocessa os dados brutos

**Funções:**

#### `load_data(path)`
- **Descrição:** Carrega CSV do caminho especificado
- **Parâmetro:** path (str) - Caminho do arquivo
- **Retorno:** DataFrame do pandas
- **Trata:** FileNotFoundError, Exception genérica

#### `preprocess(df)`
- **Descrição:** Preprocessa dados extraindo features temporais
- **Parâmetro:** df (DataFrame) - Dados brutos
- **Retorno:** DataFrame preprocessado
- **O que faz:**
  - Renomeia 'valor_total' → 'sales'
  - Converte 'data_hora' em datetime
  - Extrai day, month, day_of_week
  - Remove NaNs em 'sales'

---

### **train.py** 🚀 (49 linhas)
**Tipo:** Script de Treinamento
**Descrição:** Treina o modelo RandomForest e o salva

**Processo:**
1. Define caminhos (dinâmicos)
2. Carrega dados
3. Preprocessa dados
4. Divide em train/test (80/20)
5. Treina RandomForest (100 estimadores)
6. Avalia (R² Score)
7. Salva modelo (model.pkl)

**Saída:**
```
Loading data...
Data loaded: XXXX rows, XX columns
Preprocessing data...
Data after preprocessing: XXXX rows
Splitting data into train/test sets...
Training RandomForest model...
Model R² Score - Train: 0.XXXX, Test: 0.XXXX
Model saved to: ...
```

**Como rodar:**
```bash
python main.py train
# ou
python src/train.py
```

---

### **predict.py** 📈 (41 linhas)
**Tipo:** Módulo de Previsão
**Descrição:** Carrega modelo e faz previsões

**Funções:**

#### `load_model(path=None)`
- **Descrição:** Carrega modelo treinado
- **Parâmetro:** path (str, opcional) - Caminho do modelo
- **Retorno:** Modelo joblib carregado
- **Trata:** FileNotFoundError se modelo não existe

#### `make_prediction(model, day, month, day_of_week)`
- **Descrição:** Faz previsão de vendas
- **Parâmetros:**
  - model - Modelo treinado
  - day (int) - Dia do mês (1-31)
  - month (int) - Mês (1-12)
  - day_of_week (int) - Dia da semana (0-6)
- **Retorno:** Valor de vendas (float)

---

## 📁 Pasta: app/

### **__init__.py** 📦 (1 linha)
**Tipo:** Iniciador de Pacote Python
**Descrição:** Torna `app` um pacote Python válido

---

### **app.py** 🎨 (46 linhas)
**Tipo:** Aplicação Streamlit
**Descrição:** Interface web para fazer previsões

**Interface:**
- Campo de entrada: Dia (1-31)
- Campo de entrada: Mês (1-12)
- Campo de entrada: Dia da semana (0-6)
- Botão: "Prever"

**Funcionalidades:**
- Configuração de página (título, ícone)
- Layout responsivo com colunas
- Tratamento robusto de erros
- Mensagens informativas com emojis
- Mapeamento legível de dias

**Como rodar:**
```bash
python main.py app
# ou
streamlit run app/app.py
```

**URL padrão:** `http://localhost:8501`

---

## 📁 Pasta: data/

### **vendas_ecommerce.csv** 📊
**Tipo:** Dataset
**Descrição:** Dados de transações de e-commerce

**Colunas (11):**
- `id_compra` - ID único da compra
- `data_hora` - Data e hora da transação (IMPORTANTE!)
- `produto` - Nome do produto
- `preco_unitario` - Preço unitário
- `quantidade` - Quantidade vendida
- `cliente` - Nome do cliente
- `cidade` - Cidade da transação
- `forma_pagamento` - Método de pagamento
- `frete` - Custo de frete
- `avaliacao` - Avaliação do cliente
- `valor_total` - **Valor total (TARGET)**

**Características:**
- Formato: CSV
- Linhas: ~5000
- Colunas: 11
- Target: valor_total
- Features utilizadas: day, month, day_of_week (extraídas de data_hora)

---

## 📁 Pasta: notebook/
**Tipo:** Diretório de Notebooks
**Descrição:** Para análise exploratória (opcional)
**Status:** Vazio (pode ser usado para Jupyter notebooks)

---

## 📁 Pasta: __pycache__/
**Tipo:** Cache Python
**Descrição:** Arquivos compilados Python
**Status:** Ignorado em .gitignore

---

## 📁 Pasta: .idea/
**Tipo:** Configuração PyCharm
**Descrição:** Settings do IDE PyCharm
**Status:** Ignorado em .gitignore

---

## 📁 Pasta: .venv/
**Tipo:** Virtual Environment
**Descrição:** Ambiente virtual Python isolado
**Status:** Ignorado em .gitignore

---

## 📄 Arquivo: uv.lock
**Tipo:** Lock file
**Descrição:** Arquivo de lock do gerenciador uv (opcional)
**Status:** Presente mas não essencial

---

## 📄 Arquivo: model.pkl
**Tipo:** Modelo Serializado
**Descrição:** Modelo Random Forest treinado
**Status:** Criado após executar `python main.py train`
**Tamanho:** ~2-5 MB (típico)

---

## 📊 Resumo de Arquivos

| Tipo | Arquivo | Status | Descrição |
|------|---------|--------|-----------|
| Python | main.py | ✅ | Entry point CLI |
| Python | verify_setup.py | ✅ | Verificação |
| Config | requirements.txt | ✅ | Dependências |
| Config | pyproject.toml | ✅ | Metadados |
| Config | .gitignore | ✅ | Git exclusões |
| Config | .env.example | ✅ | Template env |
| Docs | README.md | ✅ | Doc principal |
| Docs | PROJECT_REVIEW.md | ✅ | Revisão técnica |
| Docs | REVISION_SUMMARY.md | ✅ | Sumário |
| Docs | QUICK_START.md | ✅ | Quick start |
| Python | src/__init__.py | ✅ | Pacote src |
| Python | src/config.py | ✅ | Configuração |
| Python | src/preprocess.py | ✅ | Preprocessar |
| Python | src/train.py | ✅ | Treinar |
| Python | src/predict.py | ✅ | Prever |
| Python | app/__init__.py | ✅ | Pacote app |
| Python | app/app.py | ✅ | Interface web |
| Data | data/vendas_ecommerce.csv | ✅ | Dataset |
| Model | model.pkl | ⏳ | Gerado após train |

---

## 📈 Estatísticas

- **Total de Arquivos:** 20+ (sem cache)
- **Total de Linhas de Código:** 500+
- **Total de Linhas de Documentação:** 1000+
- **Total de Diretórios:** 5
- **Total de Pacotes Python:** 2 (src, app)

---

## 🎯 Fluxo de Uso

```
1. Instalar deps       → pip install -r requirements.txt
2. Verificar setup     → python verify_setup.py
3. Treinar modelo      → python main.py train (cria model.pkl)
4. Opção A: App Web    → python main.py app (acesso em localhost:8501)
5. Opção B: CLI        → python main.py predict --day 15 --month 3 --dow 2
```

---

**Último Atualização:** 15 de Abril de 2026
**Versão do Projeto:** 0.1.0

