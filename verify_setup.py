"""
Quick verification script to test the project structure and imports.
Run this to verify everything is set up correctly.
"""

import sys
import os
from pathlib import Path

def check_imports():
    """Verify that all required modules can be imported."""
    print("🔍 Checking imports...")

    try:
        import pandas
        print("  ✅ pandas")
    except ImportError:
        print("  ❌ pandas - NOT INSTALLED")
        return False

    try:
        import sklearn
        print("  ✅ scikit-learn")
    except ImportError:
        print("  ❌ scikit-learn - NOT INSTALLED")
        return False

    try:
        import joblib
        print("  ✅ joblib")
    except ImportError:
        print("  ❌ joblib - NOT INSTALLED")
        return False

    try:
        import streamlit
        print("  ✅ streamlit")
    except ImportError:
        print("  ❌ streamlit - NOT INSTALLED (optional)")

    print()
    return True


def check_files():
    """Verify that all required files exist."""
    print("📁 Checking file structure...")

    project_root = Path(__file__).parent

    required_files = [
        "main.py",
        "requirements.txt",
        "pyproject.toml",
        "README.md",
        "src/train.py",
        "src/preprocess.py",
        "src/predict.py",
        "src/config.py",
        "src/__init__.py",
        "app/app.py",
        "app/__init__.py",
        "data/ecommerce_dataset.csv",
    ]

    all_exist = True
    for file in required_files:
        file_path = project_root / file
        if file_path.exists():
            print(f"  ✅ {file}")
        else:
            print(f"  ❌ {file} - NOT FOUND")
            all_exist = False

    print()
    return all_exist


def check_data():
    """Verify that the data file is readable."""
    print("📊 Checking data...")

    try:
        import pandas as pd
        from pathlib import Path

        data_path = Path(__file__).parent / "data" / "ecommerce_dataset.csv"
        df = pd.read_csv(data_path)

        print(f"  ✅ Data loaded successfully")
        print(f"     - Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"     - Columns: {', '.join(df.columns.tolist())}")
        print(f"     - Memory: {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")

        # Check for required columns
        required_cols = ['Date', 'Total_Amount']
        missing_cols = [col for col in required_cols if col not in df.columns]

        # Also accept alternative column names
        if 'data_hora' in df.columns or 'Date' in df.columns:
            date_col_ok = True
        else:
            date_col_ok = False
            missing_cols.append("No date column (Date or data_hora)")

        if 'valor_total' in df.columns or 'Total_Amount' in df.columns:
            sales_col_ok = True
        else:
            sales_col_ok = False
            missing_cols.append("No sales column (Total_Amount or valor_total)")

        if not (date_col_ok and sales_col_ok):
            print(f"  ⚠️  Data format issue: {', '.join(missing_cols)}")
            return False

        print()
        return True

    except Exception as e:
        print(f"  ❌ Error reading data: {str(e)}")
        print()
        return False


def check_imports_internal():
    """Verify that internal modules can be imported."""
    print("🔗 Checking internal imports...")

    try:
        # Add src to path
        sys.path.insert(0, str(Path(__file__).parent / "src"))

        from preprocess import load_data, preprocess
        print("  ✅ preprocess module")
    except ImportError as e:
        print(f"  ❌ preprocess module - {str(e)}")
        return False

    try:
        from predict import load_model, make_prediction
        print("  ✅ predict module")
    except ImportError as e:
        print(f"  ❌ predict module - {str(e)}")
        return False

    try:
        from config import PROJECT_ROOT, DATA_PATH, MODEL_PATH
        print("  ✅ config module")
    except ImportError as e:
        print(f"  ❌ config module - {str(e)}")
        return False

    print()
    return True


def main():
    """Run all checks."""
    print("\n" + "="*60)
    print("🚀 PREVISÃO DE VENDAS - VERIFICATION SCRIPT")
    print("="*60 + "\n")

    checks = [
        ("Imports", check_imports),
        ("File Structure", check_files),
        ("Data Loading", check_data),
        ("Internal Imports", check_imports_internal),
    ]

    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"⚠️  {name} check failed: {str(e)}\n")
            results.append((name, False))

    # Summary
    print("="*60)
    print("✅ VERIFICATION SUMMARY")
    print("="*60)

    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
        if not result:
            all_passed = False

    print("="*60)

    if all_passed:
        print("\n🎉 All checks passed! Project is ready to use.\n")
        print("Next steps:")
        print("  1. Train the model:     python main.py train")
        print("  2. Run the app:         python main.py app")
        print("  3. Make a prediction:   python main.py predict --day 15 --month 3 --dow 2")
        print()
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.\n")
        print("Common solutions:")
        print("  - Install dependencies: pip install -r requirements.txt")
        print("  - Check file permissions")
        print("  - Verify data file exists: data/ecommerce_dataset.csv")
        print()

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())

