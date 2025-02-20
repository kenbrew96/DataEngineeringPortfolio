import boto3

def upload_file_to_s3(file_name, bucket_name):
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, file_name)

if __name__ == '__main__':
    upload_file_to_s3('data/sample.csv', 'my-new-bucket')

