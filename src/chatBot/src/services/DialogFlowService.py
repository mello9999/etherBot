from src.services.EthereumService import EthereumService
from src.utils.constants.log_dialog import LOG_ERROR

class DialogFlowService():

  def __init__(self) -> None:
    self.es = EthereumService()

  def get_price(self, raw_data):
    """
    The function is called when the user asks for the price of ETH
    
    :param raw_data: The data that is sent to the server
    :return: a log and a result. The log is None if there is no error, and is a string if there is an
    error. The result is a dictionary that contains the data that is to be returned to the user.
    """

    value = raw_data["queryResult"]["intent"]["displayName"]

    if value != 'price':
      return LOG_ERROR['BAG_REQUEST'] , None


    log, result = self.es.get_price_eth()
    if log is not None:
      return log, result

    return None, { "fulfillmentText": 'Now, the price of ETH is {} USD'.format(result)}