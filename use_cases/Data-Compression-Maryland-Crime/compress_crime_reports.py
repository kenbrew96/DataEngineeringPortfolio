import pandas as pd
import gzip
import shutil

def compress_crime_data(input_file, output_file):
    """Compress the Maryland crime data file using gzip."""
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"✅ Crime data compressed and saved to {output_file}")

def load_crime_data(input_file):
    """Load the crime data from a CSV file."""
    return pd.read_csv(input_file)

if __name__ == "__main__":
    # Input and output file paths
    input_file = "maryland_crime_data.csv"
    output_file = "maryland_crime_data_compressed.csv.gz"
    
    # Compress the crime data file
    compress_crime_data(input_file, output_file)
    
    # Load and display the data
    crime_data = load_crime_data(input_file)
    print("Crime Data Loaded Successfully:")
    print(crime_data.head())

