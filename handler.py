import json

def endpoint(event, context):
body = {
"message": "Hello Serverless training team"
    }
    response = {
"statusCode": 200,
"body": json.dumps(body)
    }
    return response
