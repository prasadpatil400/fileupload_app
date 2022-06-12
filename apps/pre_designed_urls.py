import os

import boto3
import requests
#from boto3 import s3
s3 = boto3.resource('s3')
session = boto3.Session()
credentials = session.get_credentials()

def generate(filename,basepath):
    AWS_S3_FILE_NAME = filename
    AWS_ACCESS_KEY_ID = 'AKIAZFER2Z7IWKGUCLHC'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_S3_REGION = 'ap-south-1'
    AWS_S3_BUCKET_NAME = "fileupload2"
    s3.Bucket(AWS_S3_BUCKET_NAME).upload_file(basepath+AWS_S3_FILE_NAME, filename)
    #PRESIGNED_URL_EXPIRY = 100  # in seconds
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, region_name=AWS_S3_REGION, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    presigned_url = s3_client.generate_presigned_url('get_object',    Params={"Bucket": AWS_S3_BUCKET_NAME, "Key": AWS_S3_FILE_NAME}, ExpiresIn=386400)
    #print("suucessful",presigned_url)
    return presigned_url




