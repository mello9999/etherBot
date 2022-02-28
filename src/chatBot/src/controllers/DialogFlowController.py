from src.utils.helpers.general.logging import return_format
from src.services.DialogFlowService import DialogFlowService
from src.models.DialogFlowModel import DialogFlowModel
from src.utils.constants.log_dialog import LOG_ERROR
from fastapi import APIRouter, Response, Request
import logging

dialogFlowController = APIRouter()

dfs = DialogFlowService()

"""
This function is called when a POST request is sent to the / endpoint

:param data: The data that was sent to the endpoint
:type data: DialogFlowModel
:param response: Response
:type response: Response
:return: A JSON object with the price of Ether.
"""
@dialogFlowController.post('/', status_code=201)
async def get_ether(request: Request, response: Response):
    data = await request.json()
    logging.info(data)
    log, result = dfs.get_price(data)
    if log is not None :
        logging.error(log)
        if log == LOG_ERROR['BAG_REQUEST']:
            response.status_code = 400
            return return_format(False, log)

        logging.error(log)
        response.status_code = 500
        return return_format(False, log)

    response.status_code = 200
    return return_format(True, result)