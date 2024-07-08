#!/usr/bin/env python3

# Simple boilerplate code to use Boto3
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create Boto3 session with the default profile
aws_console = boto3.session.Session(profile_name="default")

# Define the AWS service you want to use
# Example: For S3, use 's3'; for IAM, use 'iam', etc.
service_name = "s3"  # Replace with the desired AWS service


# add code here to manipulate the service or session