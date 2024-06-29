import os
import azure.functions as func
import logging
import json
from azure.cosmos import CosmosClient, exceptions

# Initialize Cosmos client using environment variables
cosmos_url = os.getenv("CosmosDB_URL")
cosmos_key = os.getenv("CosmosDB_Key")
database_name = os.getenv("CosmosDB_Database")
container_name = os.getenv("CosmosDB_Container")

cosmos_client = CosmosClient(cosmos_url, credential=cosmos_key)
database = cosmos_client.get_database_client(database_name)
container = database.get_container_client(container_name)

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="resumeapi")
def resumeapi(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        item_id = req.params.get('id')
        if not item_id:
            return func.HttpResponse("Please pass an id in the query string", status_code=400)

        item_response = container.read_item(item=item_id, partition_key=item_id)
        basics_section = item_response.get('basics', {})
        
        return func.HttpResponse(json.dumps(basics_section, indent=2), status_code=200)
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Error reading item from Cosmos DB: {e.message}")
        return func.HttpResponse("Error reading item from Cosmos DB", status_code=500)


