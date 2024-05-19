import azure.functions as func
import json

def process_data(data):
    # Process the incoming data (example: calculate the sum of two numbers)
    result = data['number1'] + data['number2']
    return result

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON payload",
            status_code=400
        )

    if 'number1' not in req_body or 'number2' not in req_body:
        return func.HttpResponse(
            "Please provide 'number1' and 'number2' in the JSON payload",
            status_code=400
        )

    result = process_data(req_body)

    response_data = {
        "result": result
    }

    return func.HttpResponse(
        json.dumps(response_data),
        status_code=200,
        mimetype="application/json"
    )
