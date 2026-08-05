import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Read cleaned population data
df = pd.read_csv("data/processed/state_population_cleaned.csv")

# PostgreSQL connection
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Load data into PostgreSQL
df.to_sql(
    "state_population",
    engine,
    if_exists="replace",
    index=False
)

print("State population data loaded successfully!")