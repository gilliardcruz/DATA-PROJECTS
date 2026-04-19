# 📊 Previsão de Vendas E-commerce

Uma aplicação de aprendizado de máquina para prever o valor total de vendas em um e-commerce com base em características temporais.

## 📋 Descrição do Projeto

Este projeto implementa um modelo de regressão usando Random Forest para prever vendas futuras em um e-commerce. O modelo utiliza características temporais (dia, mês e dia da semana) como entrada para prever o valor total de vendas.

### Características

- ✅ Pipeline de preprocessamento de dados
- ✅ Treinamento de modelo com Random Forest
- ✅ Validação cruzada e avaliação de desempenho
- ✅ Interface web interativa com Streamlit
- ✅ Modularização do código
- ✅ Documentação completa

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.9 ou superior
- pip ou uv (gerenciador de pacotes)

### Instalação

1. Clone o repositório:
```bash
cd Previsao-vendas
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou com uv:
```bash
uv pip install -r requirements.txt
```

### Uso

#### 1. Treinar o Modelo

```bash
python main.py train
```

Ou diretamente:
```bash
python src/train.py
```

#### 2. Executar a Aplicação Web

```bash
python main.py app
```

Ou diretamente:
```bash
streamlit run app/app.py
```

A aplicação será aberta em `http://localhost:8501`

#### 3. Fazer uma Previsão via CLI

```bash
python main.py predict --day 15 --month 3 --dow 2
```

Parâmetros:
- `--day`: Dia do mês (1-31)
- `--month`: Mês (1-12)
- `--dow`: Dia da semana (0=Segunda, 1=Terça, ..., 6=Domingo)

## 📁 Estrutura do Projeto

```
Previsao-vendas/
├── main.py                      # Entry point principal
├── requirements.txt             # Dependências do projeto
├── pyproject.toml              # Configuração do projeto
├── README.md                   # Este arquivo
├── data/
│   └── vendas_ecommerce.csv   # Dataset com dados de vendas
├── src/
│   ├── preprocess.py          # Functions para preprocessamento
│   ├── train.py               # Script de treinamento do modelo
│   └── predict.py             # Functions para fazer previsões
├── app/
│   └── app.py                 # Aplicação Streamlit
└── model.pkl                  # Modelo treinado (gerado após train.py)
```

## 📊 Dataset

O dataset contém dados de transações de e-commerce com as seguintes colunas principais:

- **data_hora**: Data e hora da transação
- **valor_total**: Valor total da venda (TARGET)
- Outras features: produto, preço, quantidade, cliente, cidade, forma_pagamento, frete, avaliação

## 🤖 Modelo

### Algoritmo
- **Random Forest Regressor** (100 estimadores)

### Features (Entradas)
1. `day` - Dia do mês (1-31)
2. `month` - Mês (1-12)
3. `day_of_week` - Dia da semana (0-6)

### Target (Saída)
- `sales` - Valor total previsto em R$

## 🔧 Estrutura do Código

### Funcionalidades principais:

1. **preprocess.py** - Carregamento e preprocessamento de dados
2. **train.py** - Treinamento do modelo
3. **predict.py** - Realizar previsões
4. **app/app.py** - Interface web com Streamlit
5. **main.py** - Entry point com CLI

## 💡 Melhorias Implementadas

✅ Tratamento robusto de erros
✅ Documentação com docstrings
✅ Caminhos relativos em vez de hardcoded
✅ Validação de entradas
✅ Interface Streamlit melhorada
✅ CLI intuitiva com argparse
✅ Compatibilidade com Python 3.9+
✅ Dependências versionadas

## 🚀 Próximas Etapas Sugeridas

1. Tentar modelos mais avançados (XGBoost, Gradient Boosting)
2. Otimização de hiperparâmetros
3. Adicionar mais features (sazonalidade, tendências)
4. Implementar validação cruzada
5. Criar testes unitários
6. API REST com FastAPI
7. Containerização com Docker

## 📝 Licença

Projeto de demonstração de Machine Learning em Python
