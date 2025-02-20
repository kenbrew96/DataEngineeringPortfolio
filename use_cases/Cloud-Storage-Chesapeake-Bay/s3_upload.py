import boto3
import json

# AWS S3 Configuration
AWS_ACCESS_KEY = "your_access_key"
AWS_SECRET_KEY = "your_secret_key"
S3_BUCKET_NAME = "chesapeake-water-quality"
S3_OBJECT_NAME = "water_quality_data.json"

def upload_to_s3(file_name, bucket, object_name):
    """Uploads a file to an AWS S3 bucket."""
    s3_client = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"✅ Successfully uploaded {file_name} to {bucket}/{object_name}")
    except Exception as e:
        print(f"❌ Upload failed: {e}")

if __name__ == "__main__":
    # Upload the JSON data file to S3
    upload_to_s3("sample_water_quality.json", S3_BUCKET_NAME, S3_OBJECT_NAME)

