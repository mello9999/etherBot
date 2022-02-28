import json
import os
import requests
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def MainFunction():
    ''' This is function that connect Flask and Dailogflow
    '''

    #   Get intent from dailogflowJay
    questionFromDailogflow = request.get_json(silent=True, force=True)

    #   Call function generateAnswer for split question
    answerFromBot = generatingAnswer(questionFromDailogflow)
    
    #   Answers to dailogflow
    r = make_response(answerFromBot)

    #   Set type data that reply
    r.headers['Content-Type'] = 'application/json'

    return r

def generatingAnswer(questioFromDailogflowDict):
    ''' This is function that user ask bot
        INPUT : Message of user
        OUTPUT : Answers from bot
    '''

    #   Keep data of intent that get dailogflow
    intentQuestionStr = questioFromDailogflowDict["queryResult"]["intent"]["displayName"] 

    #   Loop option of function that reply
    if intentQuestionStr == 'price':
        answerStr = price()

    else: answerStr = "Error"

    #   Create dictation 
    answerFrom_Bot = {"fulfillmentText": answerStr}
    
    #   Trans dict to JSON
    answerFrom_Bot = json.dumps(answerFrom_Bot, indent=4) 
    
    return answerFrom_Bot


def price():
    ''' This is data price of ethereum
        INPUT : API of price ETH from Etherscan.io
        OUTPUT : Price of ETH ( USD )
    '''
    #   Call API
    responceBalanceEth = requests.get( 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken' )

    #   Trans to be json
    balanceEth = responceBalanceEth.json()

    #   Choose result of API
    resultBalanceEth = balanceEth.get( "result" )

    #   Clean data
    priceUSD = 'Price of ETH : ' + resultBalanceEth['ethusd'] + ' USD'

    return priceUSD

@app.route('/web', methods=['GET'])
def Hello():
    print('Hello')


#   Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)

