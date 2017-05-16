import boto3
import json
from botocore.exceptions import ClientError

def handler(event, context):
  try:
    order_table = boto3.resource('dynamodb', region_name='us-west-1').Table('Order')
    keys = {'menu_id', 'order_id', 'customer_name', 'customer_email'}
    if all(key in event for key in keys):
      event['order_status'] = 'processing'

      order = {}
      order['selection'] = 'empty'
      order['size'] = 'empty'
      order['cost'] = 'empty'
      order['order_time'] = 'empty'
      event['order'] = order

      order_table.put_item(Item=event)
      menu_table = boto3.resource('dynamodb', region_name='us-west-1').Table('Menu')
      selection = menu_table.get_item(Key={'menu_id': event['menu_id']}).get('Item').get('selection')
      for i in range(0, len(selection)):
        selection[i] = str(i+1) + ". " + selection[i]
      selection_str = ", ".join(selection)
      response = {}
      response['Message'] = 'Hi ' + event.get('customer_name') + ', please choose one of these selection:  ' + selection_str
      return response
    else:
      return "missing keys"
  except Exception as e:
    return e.message
