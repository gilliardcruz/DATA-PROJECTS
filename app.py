import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("../src"))

from predict import load_model, make_prediction

st.set_page_config(page_title="Previsão de Vendas", page_icon="📊")

st.title("📊 Previsão de Vendas E-commerce")
st.markdown("Preveja o valor total de vendas com base em características temporais")

try:
    # Load model
    model = load_model()

    # Create columns for better layout
    col1, col2, col3 = st.columns(3)

    with col1:
        day = st.slider("Dia do Mês", min_value=1, max_value=31, value=15)

    with col2:
        month = st.slider("Mês", min_value=1, max_value=12, value=1)

    with col3:
        day_of_week = st.slider("Dia da Semana", min_value=0, max_value=6, value=0,
                               help="0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4=Sexta, 5=Sábado, 6=Domingo")

    # Day of week mapping for display
    days_mapping = {0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo"}

    st.markdown("---")

    if st.button("🔮 Prever", type="primary", use_container_width=True):
        result = make_prediction(model, day, month, day_of_week)

        # Display result
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric("Vendas Previstas", f"R$ {result:,.2f}")
        with col2:
            st.info(f"📅 Data: {day}/{month:02d} ({days_mapping[day_of_week]})")

        st.success("✅ Previsão realizada com sucesso!")

except FileNotFoundError as e:
    st.error(f"❌ Erro: {str(e)}")
    st.info("Por favor, execute o arquivo `train.py` para treinar o modelo.")
except Exception as e:
    st.error(f"❌ Erro ao fazer a previsão: {str(e)}")

