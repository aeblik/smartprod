import boto3
import os
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename

MINIO_BUCKET = "uploads"

# Create S3 client
s3 = boto3.client(
    's3',
    endpoint_url="http://minio:9000",
    aws_access_key_id=os.getenv('MINIO_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('MINIO_SECRET_KEY'),
    region_name='us-east-1'
)

# ✅ Ensure bucket exists
def ensure_bucket_exists():
    try:
        s3.head_bucket(Bucket=MINIO_BUCKET)
        print(f"Bucket '{MINIO_BUCKET}' already exists.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Bucket '{MINIO_BUCKET}' not found. Creating...")
            s3.create_bucket(Bucket=MINIO_BUCKET)
        else:
            raise

ensure_bucket_exists()  # Call on import

# Upload function
def upload_to_minio(file):
    filename = secure_filename(file.filename)
    s3.upload_fileobj(file, MINIO_BUCKET, filename)
    return f"{os.getenv('MINIO_PUBLIC_URL')}/{MINIO_BUCKET}/{filename}"
