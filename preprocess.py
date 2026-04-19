"""
Módulo de preprocessamento de dados.
Responsável por carregar e processar dados de vendas.
"""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Carrega dados CSV do caminho especificado.

    Args:
        path: Caminho do arquivo CSV

    Returns:
        DataFrame do pandas com os dados carregados

    Raises:
        FileNotFoundError: Se o arquivo não existir
        Exception: Se houver erro ao carregar o arquivo
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found at: {path}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocessa os dados extraindo features temporais.

    Trata diferentes formatos de nomes de coluna:
    - 'Total_Amount', 'valor_total' → 'sales'
    - 'Date', 'data_hora' → coluna de data

    Extrai features (dia, mês, dia da semana) da coluna de data.
    Remove linhas com valores de vendas faltantes.

    Args:
        df: DataFrame com dados brutos

    Returns:
        DataFrame preprocessado com features temporais

    Raises:
        ValueError: Se nenhuma coluna de data ou vendas for encontrada
    """
    # Rename sales/revenue columns to 'sales' for consistency
    if 'Total_Amount' in df.columns:
        df = df.rename(columns={'Total_Amount': 'sales'})
    elif 'valor_total' in df.columns:
        df = df.rename(columns={'valor_total': 'sales'})

    if 'sales' not in df.columns:
        raise ValueError("No sales column found. Expected 'Total_Amount' or 'valor_total'")

    # Handle date columns
    date_column = None
    if 'Date' in df.columns:
        date_column = 'Date'
    elif 'data_hora' in df.columns:
        date_column = 'data_hora'

    if date_column is None:
        raise ValueError("No date column found. Expected 'Date' or 'data_hora'")

    df['date'] = pd.to_datetime(df[date_column])

    # Extract temporal features
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek

    # Remove rows with missing sales values
    df = df.dropna(subset=['sales'])

    return df