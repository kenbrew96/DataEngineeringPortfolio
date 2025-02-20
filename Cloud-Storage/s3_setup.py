import boto3

def setup_s3_bucket():
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket='my-new-bucket')

if __name__ == '__main__':
    setup_s3_bucket()

