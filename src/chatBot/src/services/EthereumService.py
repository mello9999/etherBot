from src.utils.configs.app_settings import get_settings
import requests

class EthereumService():
  def __init__(self) -> None:
    self.URL = '{}?module=stats&action=ethprice&apikey={}'.format(get_settings().URL_ETERSCAN, get_settings().API_KEY)

  def get_price_eth(self):
    """
    The function is a getter for the price of eth from Eterscan API. 
    
    :return: The price of ETH in USD.
    """

    try:
      resonponse = requests.get(self.URL)
      resonponse = resonponse.json().get("result")['ethusd']

      return None, resonponse
    except Exception as e:
      return str(e), str(e)