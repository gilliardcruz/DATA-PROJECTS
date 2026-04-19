"""
Previsão de Vendas E-commerce - Entry Point

Este script é o ponto de entrada principal do projeto.
Use este arquivo para treinar o modelo ou executar a aplicação Streamlit.

Uso:
    - Para treinar o modelo: python main.py train
    - Para executar a app Streamlit: python main.py app
    - Para fazer uma previsão: python main.py predict --day 15 --month 3 --dow 2
"""

import sys
import os
import argparse

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from predict import load_model, make_prediction


def main():
    parser = argparse.ArgumentParser(description='Previsão de Vendas E-commerce')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Train command
    train_parser = subparsers.add_parser('train', help='Train the model')

    # App command
    app_parser = subparsers.add_parser('app', help='Run Streamlit app')

    # Predict command
    predict_parser = subparsers.add_parser('predict', help='Make a prediction')
    predict_parser.add_argument('--day', type=int, required=True, help='Day of month (1-31)')
    predict_parser.add_argument('--month', type=int, required=True, help='Month (1-12)')
    predict_parser.add_argument('--dow', type=int, required=True, help='Day of week (0-6)')

    args = parser.parse_args()

    if args.command == 'train':
        print("Training model...")
        os.system(f"python {os.path.join(os.path.dirname(__file__), 'src', 'train.py')}")

    elif args.command == 'app':
        print("Starting Streamlit app...")
        os.system(f"streamlit run {os.path.join(os.path.dirname(__file__), 'app', 'app.py')}")

    elif args.command == 'predict':
        print(f"Making prediction for: Day={args.day}, Month={args.month}, DayOfWeek={args.dow}")
        try:
            model = load_model()
            result = make_prediction(model, args.day, args.month, args.dow)
            print(f"💰 Predicted sales: R$ {result:,.2f}")
        except Exception as e:
            print(f"Error: {str(e)}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
