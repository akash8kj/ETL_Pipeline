# Multi-Source ETL Pipeline with PostgreSQL & SQL Analytics

## 📌 Project Overview

This project demonstrates an end-to-end **ETL (Extract, Transform, Load) pipeline** built using Python, multiple public APIs, and PostgreSQL.

The pipeline extracts data from external sources, performs data cleaning and transformation, loads the processed datasets into PostgreSQL, and performs SQL-based analysis to generate meaningful insights.

The project integrates two different data sources:

- **Open Brewery DB API** → Brewery information across the United States
- **US Census Population API** → State-level population statistics

By combining these datasets, the project enables analytical queries such as brewery distribution and brewery density analysis by state.

---

# 🏗️ Project Architecture

```
External APIs
      |
      |
      ↓
Extract Layer (Python Requests)
      |
      |
      ↓
Raw JSON Data
(data/raw)
      |
      |
      ↓
Transform Layer (Python + Pandas)
      |
      |
      ↓
Cleaned CSV Data
(data/processed)
      |
      |
      ↓
Load Layer (SQLAlchemy)
      |
      |
      ↓
PostgreSQL Database
      |
      |
      ↓
SQL Analytics Queries
```

---

# 🛠️ Tech Stack

## Programming Language
- Python

## Data Processing
- Pandas
- Requests

## Database
- PostgreSQL

## Database Connectivity
- SQLAlchemy
- Psycopg2

## APIs Used
- Open Brewery DB API
- US Census Population API

## Tools
- VS Code
- pgAdmin
- Git
- GitHub

---

# 📂 Project Structure

```
ETL_Pipeline/

│
├── Scripts/
│   ├── extract.py
│   ├── extract_population.py
│   ├── transform.py
│   ├── transform_population.py
│   ├── load.py
│   └── load_population.py
│
├── data/
│   ├── raw/
│   │   ├── breweries.json
│   │   └── state_population.json
│   │
│   └── processed/
│       ├── breweries_cleaned.csv
│       └── state_population_cleaned.csv
│
├── sql/
│   └── analysis_queries.sql
│
├── docs/
│   └── ETL_Project_Documentation.docx
│
├── reports/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# 🔄 ETL Workflow

## 1. Extract

Data is extracted from external APIs using Python.

Sources:

### Open Brewery DB API
Provides brewery information including:
- Brewery name
- Type
- Location
- State
- City
- Coordinates

### US Census Population API
Provides:
- State name
- State code
- Population data

Raw API responses are stored in:

```
data/raw/
```

---

## 2. Transform

Data cleaning and transformation is performed using Pandas.

Operations performed:

- Removed duplicate records
- Standardized column names
- Cleaned text fields
- Handled missing values
- Converted population values into numeric format
- Prepared datasets for database loading

Processed files are stored in:

```
data/processed/
```

---

## 3. Load

Cleaned datasets are loaded into PostgreSQL using SQLAlchemy.

Database:

```
ETL
```

Tables created:

```
breweries
state_population
```

---

# 📊 SQL Analytics

The project contains SQL queries for business-oriented analysis.

Examples:

- Total breweries by state
- Top states with highest brewery count
- Brewery distribution across regions
- State population comparison
- Brewery density per 100,000 population
- JOIN analysis between brewery and population datasets

SQL scripts are available:

```
sql/analysis_queries.sql
```

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/akash8kj/ETL_Pipeline.git

cd ETL_Pipeline
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ETL
```

---

## 5. Run ETL Pipeline

### Extract Data

```bash
python Scripts/extract.py

python Scripts/extract_population.py
```

### Transform Data

```bash
python Scripts/transform.py

python Scripts/transform_population.py
```

### Load Data

```bash
python Scripts/load.py

python Scripts/load_population.py
```

---

# 📈 Future Improvements

- Add automated ETL scheduling using Apache Airflow
- Add Docker containerization
- Add database indexing and query optimization
- Add automated data quality checks
- Build an interactive dashboard using Power BI or Streamlit

---

# 📄 Documentation

Detailed project documentation including:

- ETL explanation
- Database design
- SQL query outputs
- Analysis results

is available in:

```
docs/ETL_Project_Documentation.pdf
```

---

# 👤 Author

**Ankan Mondal**

BCA Student | Aspiring Data Analyst

Skills:
Python • SQL • PostgreSQL • Power BI • Data Analytics
