import logging

import azure.functions as func
from . import scrap_functions

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger scrap function processed a request.')

    ref = req.params.get('ref') # "/fr/properties/20665a-3027alb.htm"

    print(ref)

    if not ref:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ref = req_body.get('ref')

    if ref:
        bien_immo = scrap_functions.scrap(ref)
        return func.HttpResponse(str(bien_immo))
    else:
        return func.HttpResponse(
             "Please pass a web page reference on the query string or in the request body",
             status_code=400
        )
