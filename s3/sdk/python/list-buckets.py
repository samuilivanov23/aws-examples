import boto3
import json
from datetime import datetime
from botocore.exceptions import ClientError

class DateTimeEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime):
      return obj.isoformat()
    return json.JSONEncoder.default(self, obj)

s3 = boto3.client('s3')
response = s3.list_buckets()

print('Existing buckets JSON format:')
print(json.dumps(response, indent=2, cls=DateTimeEncoder))

print("\nExisting buckets. Short variant")
for bucket in response['Buckets']:
  print(f'  {bucket["Name"]} {bucket["CreationDate"]}')