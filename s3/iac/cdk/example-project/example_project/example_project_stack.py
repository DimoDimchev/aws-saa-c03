from constructs import Construct
from aws_cdk import (
    Stack,
    aws_s3 as s3
)


class ExampleProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(self, "cdk-eb1-dd")
