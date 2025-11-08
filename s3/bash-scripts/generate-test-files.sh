#!/usr/bin/env bash
DIR="./test_files"

mkdir -p "$DIR"
for i in {1..10}; do
  dd if=/dev/urandom of=./test_files/file_$i.bin bs=1K count=1 iflag=fullblock
done