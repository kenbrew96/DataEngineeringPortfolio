import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Database connection
DB_CONNECTION = "postgresql://username:password@localhost:5432/maryland_transit"

def extract(csv_file):
    """Extract bus transit data from CSV file."""
    df = pd.read_csv(csv_file)
    print("✅ Data extracted successfully.")
    return df

def transform(df):
    """Transform data: Calculate average delay per route."""
    df['arrival_time'] = pd.to_datetime(df['arrival_time'])
    df['scheduled_time'] = pd.to_datetime(df['scheduled_time'])
    df['delay_minutes'] = (df['arrival_time'] - df['scheduled_time']).dt.total_seconds() / 60
    avg_delay = df.groupby('route')['delay_minutes'].mean().reset_index()
    print("✅ Data transformed successfully.")
    return avg_delay

def load(df, table_name):
    """Load data into PostgreSQL database."""
    engine = create_engine(DB_CONNECTION)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Data loaded successfully into {table_name}.")

if __name__ == "__main__":
    csv_file = "transit_data.csv"
    table_name = "bus_delays"

    # Run ETL process
    extracted_data = extract(csv_file)
    transformed_data = transform(extracted_data)
    load(transformed_data, table_name)

