import pandas as pd

# Read JSON data
df = pd.read_json("data/raw/state_population.json")

# First row contains the column names
df.columns = df.iloc[0]

# Remove the first row (headers)
df = df[1:].reset_index(drop=True)

# Rename columns
df.rename(columns={
    "NAME": "state",
    "POP_2021": "population",
    "state": "state_code"
}, inplace=True)

# Convert population to integer
df["population"] = df["population"].astype(int)

# Save cleaned data
df.to_csv("data/processed/state_population_cleaned.csv", index=False)

print("State population data cleaned successfully!")