#!/usr/bin/env bash
echo "== list buckets"

aws s3api list-buckets | grep 'BUCKETS' | awk '{print $3}' | sort