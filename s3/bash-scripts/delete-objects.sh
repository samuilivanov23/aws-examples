#!/usr/bin/env bash
echo "== delete objects"

# Exit immediately if any command returns a non-zero status
set -e

# Check for a bucket name
if [ -z "$1" ]; then
    echo "There needs to be a bucket name eg. ./delete-objects my-bucket-name"
    exit 1
fi

BUCKET_NAME=$1

# constructs the JSON file dynamically
aws s3api list-objects-v2 \
  --bucket "$BUCKET_NAME" \
  --output json | \
  jq '{Objects: [.Contents[]? | {Key: .Key}]}' \
  > /tmp/s3-objects-to-delete.json

aws s3api delete-objects \
  --bucket "$BUCKET_NAME" \
  --delete file:///tmp/s3-objects-to-delete.json