import boto3
from botocore.exceptions import ClientError
# Initialize the DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='region')
table = dynamodb.Table('your-table-name')


def read_device(id):
    response = table.get_item(Key={'id': id})
    item = response['Item']
    return item


def write_device(id, model, name, note, serial):
    table.put_item(
        Item={
            'id': id,
            'deviceModel': model,
            'name': name,
            'node': note,
            'serial': serial
        }
    )
