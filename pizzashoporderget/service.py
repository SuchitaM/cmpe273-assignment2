# -*- coding: utf-8 -*-
import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  keys = {'order_id'}
  #Make sure the API is correct
  if all(key in event for key in keys):
    try:
      order_table = boto3.resource('dynamodb', region_name='us-west-1').Table('Order')
    except Exception as e:
      return e.message

    item = order_table.get_item(Key={'order_id': event['order_id']}).get('Item')
    return item
  else:
    return "missing key: order_id"
