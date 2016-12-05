from __future__ import print_function
import boto3

s3 = boto3.client('s3')


def copy(bucket, key, targetBucket):
    try:
        src = bucket + '/' + key
        s3.copy_object(Bucket=targetBucket, CopySource=src, Key=key)
        print('copied {} to {}'.format(src, targetBucket + '/' + key))
    except Exception as e:
        print(e)
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e
