import boto3
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    table = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
    table.update_item(
      Key={'menu_id': event['menu_id']},
      UpdateExpression="SET selection = :a",
      ExpressionAttributeValues={':a': event['selection']})
    return 200,"OK"
  except Exception as e:
    return e.message
