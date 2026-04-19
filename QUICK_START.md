# ⚡ QUICK START GUIDE - Previsão de Vendas

## 🚀 5 Minutos de Setup

### Passo 1: Instalar Dependências (1 minuto)
```bash
cd D:\PROJETOS\MEUS_PROJETOS\Previsao-vendas
pip install -r requirements.txt
```

### Passo 2: Verificar Setup (30 segundos)
```bash
python verify_setup.py
```

Você deve ver:
```
✅ PASS: Imports
✅ PASS: File Structure
✅ PASS: Data Loading
✅ PASS: Internal Imports
```

### Passo 3: Treinar Modelo (2 minutos)
```bash
python main.py train
```

Saída esperada:
```
Loading data...
Data loaded: XXXX rows, XX columns
Preprocessing data...
Data after preprocessing: XXXX rows
Training RandomForest model...
Model R² Score - Train: 0.XX, Test: 0.XX
Model saved to: ...\model.pkl
```

### Passo 4: Executar App Web (1 minuto)
```bash
python main.py app
```

Será aberto em: `http://localhost:8501`

---

## 🎯 Comandos Principais

### Treinar Modelo
```bash
python main.py train
```

### Executar Aplicação Web
```bash
python main.py app
```

### Fazer Previsão via CLI
```bash
# Formato: python main.py predict --day [1-31] --month [1-12] --dow [0-6]
# 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo

python main.py predict --day 15 --month 3 --dow 2
```

### Ver Ajuda
```bash
python main.py --help
python main.py predict --help
```

---

## 📊 Estrutura do Projeto

```
Previsao-vendas/
├── main.py                 ← Entrada principal
├── verify_setup.py         ← Verificação
├── requirements.txt        ← Dependências
├── README.md              ← Documentação
├── PROJECT_REVIEW.md      ← Relatório de revisão
├── QUICK_START.md         ← Este arquivo
│
├── src/
│   ├── config.py          ← Configurações
│   ├── preprocess.py      ← Preprocessar dados
│   ├── train.py           ← Treinar modelo
│   └── predict.py         ← Fazer previsões
│
├── app/
│   └── app.py             ← Interface Streamlit
│
├── data/
│   └── vendas_ecommerce.csv  ← Dataset
│
└── model.pkl              ← Modelo treinado (criado após train)
```

---

## 🎨 Interface Web (Streamlit)

Após executar `python main.py app`:

1. **Dia**: Escolha entre 1-31
2. **Mês**: Escolha entre 1-12
3. **Dia da Semana**: Escolha entre 0-6
4. **Botão "Prever"**: Clique para fazer a previsão

Resultado:
```
💰 Vendas Previstas: R$ 1.234,56
📅 Data: 15/03 (Quarta)
✅ Previsão realizada com sucesso!
```

---

## ✅ Checklist de Verificação

- [ ] Python 3.9+ instalado
- [ ] Dependências instaladas: `pip install -r requirements.txt`
- [ ] Verificação passou: `python verify_setup.py`
- [ ] Modelo treinado: `python main.py train`
- [ ] App roda sem erros: `python main.py app`
- [ ] Previsão funciona: `python main.py predict --day 15 --month 3 --dow 2`

---

## 🐛 Troubleshooting Rápido

### ❌ "pandas not found"
```bash
pip install pandas scikit-learn joblib streamlit
```

### ❌ "Model file not found"
```bash
python main.py train
```

### ❌ "Port 8501 already in use"
```bash
streamlit run app/app.py --server.port 8502
```

### ❌ "data_hora column not found"
Verifique se `data/vendas_ecommerce.csv` existe

---

## 📈 Próximos Passos

1. ✅ Explorar os arquivos em `src/`
2. ✅ Modificar parâmetros em `src/config.py`
3. ✅ Adicionar novas features em `src/preprocess.py`
4. ✅ Customizar interface em `app/app.py`
5. ✅ Ler documentação completa em `README.md`

---

## 📚 Documentação

- **README.md** - Documentação completa
- **PROJECT_REVIEW.md** - Relatório técnico de revisão
- **REVISION_SUMMARY.md** - Sumário das alterações
- **QUICK_START.md** - Este arquivo

---

## 🎉 Pronto para Começar!

```bash
python main.py train && python main.py app
```

Bom uso! 🚀

