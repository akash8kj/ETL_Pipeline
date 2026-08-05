from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_JSON_PATH = BASE_DIR / "data" / "raw" / "breweries.json"
PROCESSED_CSV_PATH = BASE_DIR / "data" / "processed" / "breweries_cleaned.csv"

# Read JSON file
df = pd.read_json(RAW_JSON_PATH)

# ----------------------------
# Data Cleaning
# ----------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove leading/trailing spaces from text columns
text_columns = df.select_dtypes(include=["object", "string"]).columns
for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# Replace missing values in text columns with "Unknown"
df[text_columns] = df[text_columns].fillna("Unknown")

# Save cleaned data
PROCESSED_CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCESSED_CSV_PATH, index=False)

# ----------------------------
# Summary
# ----------------------------

print("Data cleaned successfully!\n")

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())