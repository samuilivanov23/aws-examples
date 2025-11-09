import boto3
import logging
import pprint
from botocore.exceptions import ClientError

logging.basicConfig(
  level=logging.INFO,
  format='%(levelname)s: %(message)s'
)

def delete_bucket(bucket_name, region='us-east-1'):
  try:
    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket(Bucket=bucket_name)

    if response['ResponseMetadata']['HTTPStatusCode'] == 204:
      logging.info(f"🗑️ S3 Bucket '{bucket_name}' deleted successfully.")
      return True
    
    return True
  except ClientError as e:
    error_code = e.response['Error']['Code']

    if error_code == 'NoSuchBucket':
      logging.warning(f"⚠️ Bucket '{bucket_name}' does not exist.")
      return True
    elif error_code == 'BucketNotEmpty':
      logging.error(f"❌ Failed to delete bucket '{bucket_name}': The bucket must be empty first.")
    else:
      logging.error(f"❌ Failed to delete S3 Bucket '{bucket_name}':")
      logging.error(e)
    return False

bucket_to_delete = 'my-new-bucket-svi'

if delete_bucket(bucket_to_delete):
  print(f"\nScript finished operation on '{bucket_to_delete}'.")
else:
  print(f"\nScript failed operation on '{bucket_to_delete}'.")