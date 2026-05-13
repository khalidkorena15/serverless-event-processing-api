import json

def lambda_handler(event, context):

    try:
        body = event.get("body")

        # HTTP API sometimes sends body as string
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError:
                body = {"raw": body}

        # If body is None
        if body is None:
            body = {}

        response = {
            "message": "Event processed successfully by serverless pipeline",
            "data": body
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }