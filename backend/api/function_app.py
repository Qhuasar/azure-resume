import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.cosmos_db_input(arg_name="documents", 
                     database_name="azure-resume",
                     container_name="counter",
                     connection="AzureResumeConnectionString")
@app.cosmos_db_output(arg_name="outputDocument", 
                      database_name="azure-resume",
                      container_name="counter",
                      connection="AzureResumeConnectionString")
@app.route(route="GetCounter")
def GetCounter(req: func.HttpRequest, documents: func.DocumentList, outputDocument: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    updated_doc = documents.data[0]
    updated_doc.data["count"] += 1
    outputDocument.set(updated_doc)
    json_return = json.dumps(updated_doc.data)
    return func.HttpResponse(
         body=json_return,
         status_code=200,
         mimetype="application/json"
    )