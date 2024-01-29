import json
from tools.idea_products_helper import *

def lambda_handler(event, context):
    
    http_method = event["httpMethod"]
    try:
        
        if http_method == "GET":
            
            if event["pathParameters"]:
                product_id = event["pathParameters"].get("id")
                product_details = get_product_details(product_id)
    
                if product_details:
                    return {
                        'statusCode': 200,
                        'body': json_dump(product_details)
                    }
                else:
                    return {
                        'statusCode': 404,
                        'body': json.dumps({'error': 'Product not found'})
                    }
            else:
                products = get_products()
                if products:
                    return {
                        "statusCode": 200,
                        "body": json_dump(products)
                    }
                else:
                    return {
                        'statusCode': 500,
                        'body': json.dumps({'error': ' Get Products Internal Server Error'})
                    }
                    
        elif http_method == "POST":
            if body.get("name") and body.get("description") and body.get("image_url"):
                # Add the new product
                new_product_id = add_new_product(body)
                return {
                    'statusCode': 201,
                    'body': json.dumps({'message': 'Product added successfully', 'productId': new_product_id})
                }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Invalid request. Ensure name, description, and image are provided for adding a new product'})
                }
        elif http_method == "PUT":
            # Check if the request is for incrementing the likes of a product
            product_id = event["pathParameters"].get("id")

            if product_id:
                # Increment the likes for the specified product
                updated_likes = increment_likes(product_id)
                if updated_likes is not None:
                    return {
                        'statusCode': 200,
                        'body': json.dumps({'message': 'Likes incremented successfully', 'updatedLikes': updated_likes})
                    }
                else:
                    return {
                        'statusCode': 404,
                        'body': json.dumps({'error': updated_likes})
                    }
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Invalid request. Provide a valid product ID for updating likes'})
                }

        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Unsupported HTTP method:%s'%(http_method)})
            }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Exception:%s'%(e)})
        }
    
    
