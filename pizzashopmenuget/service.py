from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError



def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    print("event: ")
    print(event['menu_id'])

    try:
       table = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
       item = table.get_item(Key={'menu_id': event['menu_id']}).get('Item')

    except Exception, e:
        return 400, e
    else:
        print(item)
        return 200, item
