import pandas as pd
import sqlite3

# Extract: Load CSV data
def extract():
    data = pd.read_csv('input_data.csv')
    return data

# Transform: Process data (example: filter rows)
def transform(data):
    transformed_data = data[data['value'] > 10]
    return transformed_data

# Load: Save data to SQLite database
def load(data):
    conn = sqlite3.connect('output_data.db')
    data.to_sql('table_name', conn, if_exists='replace', index=False)

def etl_pipeline():
    data = extract()
    transformed_data = transform(data)
    load(transformed_data)

if __name__ == '__main__':
    etl_pipeline()

