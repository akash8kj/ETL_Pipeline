import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "data" / "processed" / "breweries_cleaned.csv"

if not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0:
    raise FileNotFoundError(
        f"Processed dataset is missing or empty at: {CSV_PATH}. "
        "Run 'python Scripts/transform.py' first."
    )

# Read cleaned data
try:
    df = pd.read_csv(CSV_PATH)
except pd.errors.EmptyDataError as exc:
    raise FileNotFoundError(
        f"The cleaned dataset at {CSV_PATH} could not be parsed."
    ) from exc


# PostgreSQL credentials from .env
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
PGHOST = os.getenv("PGHOST")
PGPORT = os.getenv("PGPORT")
PGDATABASE = os.getenv("PGDATABASE")

if not all([PGUSER, PGPASSWORD, PGHOST, PGPORT, PGDATABASE]):
    raise ValueError(
        "PostgreSQL credentials are missing. Check your .env file."
    )


ADMIN_URL = (
    f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/postgres"
)

TARGET_URL = (
    f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}"
)


# Create database if it does not exist
admin_engine = create_engine(ADMIN_URL)

with admin_engine.connect().execution_options(
    isolation_level="AUTOCOMMIT"
) as conn:
    database_exists = conn.execute(
        text("SELECT 1 FROM pg_database WHERE datname = :dbname"),
        {"dbname": PGDATABASE},
    ).scalar()

    if database_exists is None:
        conn.execute(text(f'CREATE DATABASE "{PGDATABASE}"'))
        print(f"Created PostgreSQL database: {PGDATABASE}")


# Load data into PostgreSQL
engine = create_engine(TARGET_URL)

df.to_sql(
    "breweries",
    engine,
    if_exists="replace",
    index=False,
    method="multi",
)

print(
    f"Data loaded successfully into PostgreSQL database '{PGDATABASE}'!"
)