#!/bin/bash
# helper for starting/stopping dev stack (just the backend stuff)
set -e
cd `dirname "$0"`

action=$@
if [ "$#" == "0" ]; then
  action='up -d'
fi

# source the .env file, thanks https://stackoverflow.com/a/20909045/1410035
echo "Performing action on stack='$action'"
export $(grep -v '^#' .env | xargs)

docker-compose -f docker-compose.yml -f docker-compose.dev.yml $action

dbUrl=postgres://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME
accessKey=$S3_ACCESS_KEY
secretKey=$S3_SECRET_KEY
s3Bucket=$S3_BUCKET_NAME
s3Url=http://localhost:9000

echo "
[INFO] You'll probably want to export some env vars for your local app:
# bash
export DATABASE_URL=$dbUrl
export AWS_ACCESS_KEY_ID=$accessKey
export AWS_SECRET_ACCESS_KEY=$secretKey
export AWS_S3_BUCKET=$s3Bucket
export AWS_S3_ENDPOINT_URL=$s3Url
# fish
set -x DATABASE_URL $dbUrl
set -x AWS_ACCESS_KEY_ID $accessKey
set -x AWS_SECRET_ACCESS_KEY $secretKey
set -x AWS_S3_BUCKET $s3Bucket
set -x AWS_S3_ENDPOINT_URL $s3Url
"
