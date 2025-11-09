import boto3
import logging
import pprint
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region='us-east-1'):
  try:
    bucket_config = {}
    s3_client = boto3.client('s3', region_name=region)
    
    if region != 'us-east-1':
      bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}

    response = s3_client.create_bucket(Bucket=bucket_name, **bucket_config)
  
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
      logging.info(f"✅ S3 Bucket '{bucket_name}' created successfully in region '{region}'.")
      logging.info("--- AWS Response ---")
      logging.info(pprint.pformat(response))
      return True
    
    return True

  except ClientError as e:
    logging.error(f"❌ Failed to create S3 Bucket '{bucket_name}':")
    logging.error(e)
    return False

create_bucket('my-new-bucket-svi', region='eu-west-3')