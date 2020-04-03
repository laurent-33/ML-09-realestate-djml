import logging
import requests
import json

import azure.functions as func
from __app__.shared_code import scrap_functions

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    page = req.params.get('page')

    if not page:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            page = req_body.get('page')

    if page:
        refs = scrap_functions.get_refs(page)

        biens =  []
        for ref in refs:
            r = requests.get(
            f"https://realestatescrap.azurewebsites.net/api/realestate-scrap",
            headers={'Accept-Language' : "fr-FR"},
            params={
                'code': "/7KfhTY2uDDOl0HjdzwgpAoQr/ETPMtLBKjPfH26eh58vEakBqjXYA==",
                'ref' : ref
                }
            )

            biens += [r.json()]

        return func.HttpResponse(
            status_code = 200,
            body = json.dumps(biens),
            mimetype = "application/json",
            charset = 'utf-8'
            )

    else:
        return func.HttpResponse(
             "Please pass a page with links on the query string or in the request body",
             status_code=400
        )
