import azure.functions as func
import random

# Hardcoded minimum and maximum values
MIN_VALUE = 0
MAX_VALUE = 100

def generate_random_number():
    return random.randint(MIN_VALUE, MAX_VALUE)

def main(req: func.HttpRequest) -> func.HttpResponse:
    random_number = generate_random_number()

    return func.HttpResponse(
        f"Random number between {MIN_VALUE} and {MAX_VALUE}: {random_number}",
        status_code=200
    )
