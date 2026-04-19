"""
Módulo de previsão usando modelo treinado.
Fornece funções para carregar o modelo e fazer previsões de vendas.
"""

import os
import joblib
import pandas as pd
from typing import Optional, Any


def load_model(path: Optional[str] = None) -> Any:
    """
    Carrega o modelo treinado do disco.

    Args:
        path: Caminho do arquivo do modelo. Se None, usa o local padrão.

    Returns:
        Modelo treinado carregado

    Raises:
        FileNotFoundError: Se o arquivo do modelo não existir
    """
    if path is None:
        # Default path relative to project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = os.path.join(project_root, "model.pkl")

    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at: {path}. Please train the model first.")

    return joblib.load(path)


def make_prediction(model: Any, day: int, month: int, day_of_week: int) -> float:
    """
    Faz uma previsão de vendas usando o modelo treinado.

    Args:
        model: Modelo sklearn treinado
        day: Dia do mês (1-31)
        month: Mês (1-12)
        day_of_week: Dia da semana (0-6, onde 0=Segunda, 6=Domingo)

    Returns:
        Valor previsto de vendas em R$
    """
    data = pd.DataFrame({
        'day': [day],
        'month': [month],
        'day_of_week': [day_of_week]
    })

    prediction = model.predict(data)
    return float(prediction[0])
