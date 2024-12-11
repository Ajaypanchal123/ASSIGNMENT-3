import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger1")
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP function processed request.')

    return func.HttpResponse(
        "Hello, Professor Assignment3 Completed 8934575!",
        status_code=200
    )