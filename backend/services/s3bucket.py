import boto3
import os

from dotenv import load_dotenv

load_dotenv(override=True)

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_Access_key"),
    aws_secret_access_key=os.getenv("AWS_secret_Access_key"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("S3_BUCKET_NAME")

def upload_docs_to_s3(job_id, docs_dict):

    uploaded_files = []

    for file_name, content in docs_dict.items():

        s3_key = f"{job_id}/{file_name}"

        content_type = "text/markdown"

        if file_name.endswith(".html"):
            content_type = "text/html"

        s3_client.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=content.encode("utf-8"),
            ContentType=content_type
        )

        url = f"https://codebase-documenter.s3.us-east-2.amazonaws.com/{s3_key}"

        uploaded_files.append({
            "file_name": file_name,
            "url": url
        })

    return uploaded_files