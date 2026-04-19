# 🚀 GUIA DE MELHORIAS DO MODELO - IMPLEMENTAÇÃO PRÁTICA

## 📊 Situação Atual

O modelo Random Forest atual usa apenas **3 features** (dia, mês, dia da semana) e tem:
- **R² Train:** 0.12 (ruim)
- **R² Test:** -0.30 (péssimo - pior que predição constante!)

O dataset tem **18 colunas** e estamos usando menos de 20% delas!

---

## 🎯 Melhorias Sugeridas (Por Ordem de Impacto)

### **MELHOR #1: Adicionar Mais Features** ⭐⭐⭐⭐⭐
**Impacto Esperado:** 🔺 MUITO ALTO

**O que fazer:**
Incluir outras colunas que provavelmente correlacionam com vendas:
- `Quantity` - Quantidade vendida
- `Unit_Price` - Preço unitário  
- `Discount_Amount` - Desconto dado
- `Age` - Idade do cliente
- `Customer_Rating` - Avaliação do cliente

**Código sugerido para train.py:**
```python
# Feature columns - EXPANDIDO
FEATURE_COLUMNS = [
    'day', 'month', 'day_of_week',  # Temporal features
    'Quantity', 'Unit_Price',        # Product features
    'Discount_Amount', 'Age',        # Customer/Offer features
    'Customer_Rating'                 # Quality indicator
]
```

**Ganho esperado:** R² pode aumentar de 0.12 para 0.40-0.60

---

### **MELHORIZ #2: Adicionar Features Categóricas** ⭐⭐⭐⭐
**Impacto Esperado:** 🔺 ALTO

**O que fazer:**
Converter colunas categóricas em numéricas (one-hot encoding):
- `Product_Category` - Qual categoria de produto?
- `Payment_Method` - Como pagou?
- `Device_Type` - Que tipo de dispositivo?
- `Gender` - Gênero do cliente
- `Is_Returning_Customer` - É cliente recorrente?

**Código sugerido:**
```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Após carregar dados
categorical_columns = ['Product_Category', 'Payment_Method', 'Device_Type', 
                       'Gender', 'Is_Returning_Customer']

# Usar label encoding ou one-hot encoding
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
```

**Ganho esperado:** R² pode adicionar +0.10 a +0.20

---

### **MELHORIA #3: Feature Engineering Temporal** ⭐⭐⭐⭐
**Impacto Esperado:** 🔺 MÉDIO-ALTO

**O que fazer:**
Criar features mais sofisticadas a partir da data:
- `is_weekend` - É fim de semana?
- `is_holiday` - É feriado?
- `days_from_start` - Número de dias desde o início do período
- `week_of_year` - Semana do ano (sazonalidade)
- `quarter` - Trimestre (padrões trimestrais)

**Código sugerido:**
```python
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
df['week_of_year'] = df['date'].dt.isocalendar().week
df['quarter'] = df['date'].dt.quarter
df['days_from_start'] = (df['date'] - df['date'].min()).dt.days
```

**Ganho esperado:** R² pode adicionar +0.05 a +0.15

---

### **MELHORIA #4: Remover Outliers** ⭐⭐⭐
**Impacto Esperado:** 🔺 MÉDIO

**O que fazer:**
Identificar e remover valores anormais que prejudicam o treinamento:

```python
from scipy import stats

# Remover valores muito altos/baixos (outliers)
# Usar z-score: manter apenas valores com |z| < 3
df_clean = df[(np.abs(stats.zscore(df['sales'])) < 3)]

# Ou usar IQR (Interquartile Range)
Q1 = df['sales'].quantile(0.25)
Q3 = df['sales'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[(df['sales'] >= Q1 - 1.5*IQR) & (df['sales'] <= Q3 + 1.5*IQR)]
```

**Ganho esperado:** R² pode adicionar +0.05 a +0.10

---

### **MELHORIA #5: Tentar Modelos Melhores** ⭐⭐⭐⭐
**Impacto Esperado:** 🔺 MÉDIO

**O que fazer:**
Substituir RandomForest por XGBoost ou Gradient Boosting (geralmente melhores):

```bash
pip install xgboost
```

**Código sugerido:**
```python
from xgboost import XGBRegressor

# Em vez de RandomForestRegressor
model = XGBRegressor(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)
```

**Ganho esperado:** R² pode adicionar +0.05 a +0.20

---

### **MELHORIA #6: Normalização/Escalamento** ⭐⭐⭐
**Impacto Esperado:** 🔺 MÉDIO

**O que fazer:**
Normalizar features para mesma escala:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

**Quando ajuda:** Com modelos baseados em distância (KNN, SVM, Neural Networks)

---

### **MELHORIA #7: Validação Cruzada** ⭐⭐
**Impacto Esperado:** 🔺 MELHOR AVALIAÇÃO

**O que fazer:**
Usar k-fold cross-validation em vez de simples train/test:

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(f"CV Scores: {scores}")
print(f"Mean R²: {scores.mean():.4f} (+/- {scores.std():.4f})")
```

**Benefício:** Avaliação mais confiável

---

## 📋 PLANO DE AÇÃO RECOMENDADO

### **Fase 1: Investigação (1-2 horas)**
1. Analisar correlação entre features e vendas
2. Identificar outliers
3. Explorar distribuição de dados

**Código para exploração:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ecommerce_dataset.csv')

# Correlação
correlation = df.corr()['Total_Amount'].sort_values(ascending=False)
print(correlation)

# Visualizar
plt.figure(figsize=(12, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Distribuição
df['Total_Amount'].describe()
df['Total_Amount'].hist(bins=50)
plt.show()
```

### **Fase 2: Preparação de Dados (2-3 horas)**
1. Adicionar features sugeridas (#1, #2, #3)
2. Remover outliers (#4)
3. Normalizar dados (#6)

### **Fase 3: Modelo Melhorado (1-2 horas)**
1. Testar XGBoost (#5)
2. Implementar validação cruzada (#7)
3. Tuning de hiperparâmetros

### **Fase 4: Validação (1 hora)**
1. Comparar R² antes e depois
2. Testar em Streamlit
3. Documentar melhorias

---

## 💻 CÓDIGO EXEMPLO COMPLETO (train.py MELHORADO)

```python
"""
Script de treinamento MELHORADO - com mais features e XGBoost
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBRegressor
from sklearn.preprocessing import StandardScaler
from scipy import stats

# Carregar dados
df = pd.read_csv('data/ecommerce_dataset.csv')
print(f"Dados originais: {df.shape}")

# Remover outliers (z-score)
df = df[(np.abs(stats.zscore(df['Total_Amount'])) < 3)]
print(f"Após remover outliers: {df.shape}")

# Preparar data
df['Date'] = pd.to_datetime(df['Date'])
df['day'] = df['Date'].dt.day
df['month'] = df['Date'].dt.month
df['day_of_week'] = df['Date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
df['week_of_year'] = df['Date'].dt.isocalendar().week

# Renomear coluna alvo
df['sales'] = df['Total_Amount']

# Features numéricas
numeric_features = ['day', 'month', 'day_of_week', 'is_weekend', 'week_of_year',
                    'Age', 'Unit_Price', 'Quantity', 'Discount_Amount', 'Customer_Rating']

# Adicionar one-hot encoding para categóricas
categorical_features = ['Product_Category', 'Payment_Method', 'Device_Type', 'Gender']
df_encoded = pd.get_dummies(df, columns=categorical_features, drop_first=True)

# Preparar features e target
feature_cols = numeric_features + [col for col in df_encoded.columns 
                                    if col.startswith(tuple(categorical_features))]
X = df_encoded[feature_cols]
y = df_encoded['sales']

# Normalizar features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=feature_cols)

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Treinar XGBoost
print("Treinando XGBoost...")
model = XGBRegressor(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train, 
          eval_set=[(X_test, y_test)],
          verbose=50)

# Avaliação
train_r2 = model.score(X_train, y_train)
test_r2 = model.score(X_test, y_test)
print(f"R² Score - Train: {train_r2:.4f}, Test: {test_r2:.4f}")

# Validação cruzada
cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='r2')
print(f"CV R² Scores: {cv_scores}")
print(f"Mean R²: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")

# Salvar modelo e scaler
joblib.dump(model, 'model_improved.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Modelo salvo!")

# Importância de features
import matplotlib.pyplot as plt
feature_importance = model.feature_importances_
indices = np.argsort(feature_importance)[-10:]
plt.figure(figsize=(10, 6))
plt.barh([feature_cols[i] for i in indices], feature_importance[indices])
plt.xlabel('Feature Importance')
plt.title('Top 10 Features')
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Gráfico de importância salvo!")
```

---

## 📈 MÉTRICAS ESPERADAS

| Abordagem | R² Train | R² Test | Tipo |
|-----------|----------|---------|------|
| Atual (3 features) | 0.12 | -0.30 | 😞 Péssimo |
| + Mais features | 0.35 | 0.25 | 🙂 Bom |
| + Categóricas | 0.45 | 0.35 | 😊 Muito Bom |
| + Engenharia features | 0.55 | 0.40 | 😍 Excelente |
| + XGBoost | 0.65 | 0.50 | 🤩 Melhor Caso |

---

## 🎯 PRÓXIMAS ETAPAS

1. **Semana 1:** Implementar Fase 1 e 2 (investigação + preparação)
2. **Semana 2:** Implementar Fase 3 e 4 (modelo + validação)
3. **Semana 3:** Documentar e compartilhar resultados

---

## 📚 REFERÊNCIAS

- [Feature Engineering](https://scikit-learn.org/stable/modules/preprocessing.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Feature Importance](https://xgboost.readthedocs.io/en/latest/python/python_intro.html#feature-importance)

---

**Tempo estimado total:** 6-8 horas
**Ganho esperado em R²:** +0.40 a +0.50
**Dificuldade:** Média

Boa sorte! 🚀


