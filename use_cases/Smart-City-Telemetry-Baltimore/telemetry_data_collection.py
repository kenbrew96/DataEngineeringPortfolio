import pandas as pd
import boto3  # For AWS S3 or use azure-storage-blob for Azure
from io import StringIO
import os
from datetime import datetime

# Configuring AWS S3 connection
AWS_ACCESS_KEY = 'your_aws_access_key'
AWS_SECRET_KEY = 'your_aws_secret_key'
S3_BUCKET = 'your_s3_bucket_name'
S3_PATH = 'baltimore_energy_usage/processed_data.csv'

# Function to extract data from CSV file
def extract(csv_file):
    """Extract energy usage data from CSV file."""
    df = pd.read_csv(csv_file)
    print("✅ Data extracted successfully.")
    return df

# Function to transform data (e.g., clean, aggregate)
def transform(df):
    """Transform energy usage data."""
    # Convert timestamp to datetime format
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Aggregating energy usage by location and hour
    df['hour'] = df['timestamp'].dt.hour
    df_aggregated = df.groupby(['location', 'hour'], as_index=False)['energy_usage'].sum()
    
    print("✅ Data transformed successfully.")
    return df_aggregated

# Function to load data into AWS S3 (you can use Azure Blob Storage if needed)
def load(df, s3_bucket, s3_path):
    """Load transformed data into AWS S3."""
    # Create a connection to AWS S3
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    
    # Convert dataframe to CSV string and upload to S3
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    # Upload to S3
    s3_client.put_object(Bucket=s3_bucket, Key=s3_path, Body=csv_buffer.getvalue())
    print(f"✅ Data loaded successfully to S3: {s3_bucket}/{s3_path}")

if __name__ == "__main__":
    csv_file = 'baltimore_energy_usage.csv'  # Path to your local CSV file
    df = extract(csv_file)
    df_transformed = transform(df)
    load(df_transformed, S3_BUCKET, S3_PATH)

