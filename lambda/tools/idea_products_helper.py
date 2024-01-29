import json
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal
import uuid

dynamodb = boto3.resource('dynamodb')
table_name = 'idea_products'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError

def json_dump(data):
    return json.dumps(data, default=decimal_default)

def add_new_product(product_data):
    table = dynamodb.Table(table_name)

    # Generate a unique ID for the new product
    product_id = str(uuid.uuid4())

    # Add the new product to DynamoDB
    try:
        table.put_item(
            Item={
                'id': product_id,
                'name': product_data['name'],
                'description': product_data['description'],
                'image_url': product_data['image_url'],
                'thumbnail_url': product_data['thumbnail_url'],
                'likes': product_data.get('likes', 0),  # Default likes to 0 if not provided
            }
        )
        return product_id
    except ClientError as e:
        print(f"Error adding new product: {e}")
        return None

def get_products():
    table = dynamodb.Table(table_name)
    try:
        response = table.scan()
        products = response.get('Items')
        print(products)
        return products
    except ClientError as e:
        print(f"Error getting all products: {e}")
        return None

def get_product_details(product_id):
    table = dynamodb.Table(table_name)
    try:
        response = table.get_item(
            Key={
                'id': product_id
            }
        )
        item = response.get('Item')
        return item
    except ClientError as e:
        print(f"Error getting product details: {e}")
        return None

def increment_likes(product_id):
    table = dynamodb.Table(table_name)

    try:
        # Get the current likes value
        response = table.get_item(
            Key={
                'id': product_id
            },
            ProjectionExpression='likes'
        )
        
        item = response.get('Item')
        
        if item:
            current_likes = decimal_default(item.get('likes', 0))
        else:
            return None  # Product not found

        # Increment likes
        updated_likes = current_likes + 1

        # Update the DynamoDB item with the new likes value
        table.update_item(
            Key={
                'id': product_id
            },
            UpdateExpression='SET likes = :new_likes',
            ExpressionAttributeValues={
                ':new_likes': updated_likes
            }
        )

        return updated_likes

    except ClientError as e:
        print(f"Error incrementing likes: {e}")
        return None
