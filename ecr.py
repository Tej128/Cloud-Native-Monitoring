import boto3
from botocore.exceptions import ClientError

def create_ecr_repository(repository_name):
    """Creates an ECR repository and returns its URI."""
    ecr_client = boto3.client('ecr')
    try:
        response = ecr_client.create_repository(repositoryName=repository_name)
        repository_uri = response['repository']['repositoryUri']
        print(f"Repository created successfully: {repository_uri}")
        return repository_uri
    except ClientError as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    repository_name = "my_monitoring_app_image"
    repository_uri = create_ecr_repository(repository_name)
