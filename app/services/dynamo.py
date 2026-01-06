import boto3
from app.core.config import settings


class DynamoDBService:
    def __init__(self):
        self.resource = boto3.resource(
            "dynamodb",
            region_name=settings.AWS_REGION
        )
        self.table = self.resource.Table(settings.DYNAMODB_TABLE)

    def put_item(self, item: dict):
        return self.table.put_item(Item=item)

    def get_item(self, key: dict):
        response = self.table.get_item(Key=key)
        return response.get("Item")

    def update_item(
        self,
        key: dict,
        update_expression: str,
        expression_values: dict
    ):
        return self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ReturnValues="ALL_NEW"
        )

    def delete_item(self, key: dict):
        return self.table.delete_item(Key=key)
