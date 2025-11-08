#!/usr/bin/env bash
echo "== sync objects"

#Check for a bucket name
if [ -z "$1" ]; then
  echo "There needs to be a bucket name eg. ./put-object bucket-name"
  exit 1
fi

#Check for a dir with files to sync
if [ -z "$2" ]; then
  echo "There needs to be a dirname eg. ./put-bucket bucket-name dirname"
  exit 1
fi

BUCKET_NAME=$1
DIR_NAME=$2

aws s3 sync $DIR_NAME s3://$BUCKET_NAME/files