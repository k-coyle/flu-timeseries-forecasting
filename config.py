# config.py

from pathlib import Path

# Root directory of the project
ROOT_DIR = Path(__file__).resolve().parent

# Subdirectories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
SCRIPTS_DIR = ROOT_DIR / "scripts"

# Output directories (optional)
OUTPUT_DIR = ROOT_DIR / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"

# Example usage in scripts:
# df = pd.read_csv(RAW_DATA_DIR / "ILINet.csv")
