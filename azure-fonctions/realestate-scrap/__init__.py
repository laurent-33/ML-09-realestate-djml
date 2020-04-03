import logging
import json
import datetime

import azure.functions as func
from __app__.shared_code import scrap_functions


def datetime_convert(date):
    if isinstance(date, datetime.date):
        return str(date)

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
        json_output = json.dumps(bien_immo, default = datetime_convert)

        return func.HttpResponse(
            status_code = 200,
            body = json_output,
            mimetype = "application/json",
            charset = 'utf-8'
            )

    else:
        return func.HttpResponse(
             "Please pass a web page reference on the query string or in the request body",
             status_code=400
        )
