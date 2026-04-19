"""
Configuration module for the project.
Centralized configuration for data paths, model parameters, and settings.
"""

import os
from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).parent.parent

# Data Configuration
DATA_PATH = PROJECT_ROOT / "data" / "ecommerce_dataset.csv"
MODEL_PATH = PROJECT_ROOT / "model.pkl"

# Model Parameters
MODEL_CONFIG = {
    'n_estimators': 100,
    'random_state': 42,
    'n_jobs': -1,
    'max_depth': None,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
}

# Train/Test Configuration
TRAIN_TEST_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
}

# Features
FEATURE_COLUMNS = ['day', 'month', 'day_of_week']
TARGET_COLUMN = 'sales'

# Date Columns - Try these columns in order
DATE_COLUMNS = ['Date', 'data_hora']

# Sales/Revenue Columns - Try these columns in order
SALES_COLUMNS = ['Total_Amount', 'valor_total']

