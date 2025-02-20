import pandas as pd
import sqlite3

# Extract: Load CSV data
def extract():
    data = pd.read_csv('input_data.csv')
    return data

# Load: Save data to SQLite database (ELT approach)
def load(data):
    conn = sqlite3.connect('output_data.db')
    data.to_sql('table_name', conn, if_exists='replace', index=False)

# Transform: Process data after loading
def transform():
    conn = sqlite3.connect('output_data.db')
    data = pd.read_sql('SELECT * FROM table_name', conn)
    transformed_data = data[data['value'] > 10]
    return transformed_data

def elt_pipeline():
    data = extract()
    load(data)
    transformed_data = transform()
    print(transformed_data)

if __name__ == '__main__':
    elt_pipeline()

