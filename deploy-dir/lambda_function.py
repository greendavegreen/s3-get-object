from __future__ import print_function
import urllib
import os
import l_utils
import json


def hello():
    print("hi")



def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    targetBucket = os.environ['S3_BUCKET']

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))

    l_utils.copy(bucket, key, targetBucket)


