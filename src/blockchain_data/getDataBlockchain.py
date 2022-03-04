#!/usr/bin/env python3
from web3 import Web3
from serverMongoDB import serverMongoDB
import datetime
import time

class getDataBlockchain():
    ''' This function used connect information from infura.io
        Create dictionary last block nummber that has transaction
            INPUT - API key Infura.io
    '''
    # kao's project 
    projectId = '<token id>' # toten id : infula token's on project 

    def __getInformation():
        ''' This module call information blockchain from infura.io
            OUTPUT - Information of Blockchain
        '''
        projectId = getDataBlockchain.projectId
        web3 = Web3(Web3.HTTPProvider( 'https://mainnet.infura.io/v3/' + projectId  ) )

        return web3


    def informationByBlock( number ):
        '''This is function that is information of blockchain ethereum
            INPUT - get number block in API from web3.eth
            OUTPUT - Information of blockchain
                    {   
                        'gasLimit': int, 'gasUsed': int, 'miner': str, 
                        'number': int, 'size': int, 'transactions': list, 'date': str, 'time': str
                    }
        '''
        #   call infura.io
        web3 = getDataBlockchain.__getInformation()
        numBlock = web3.eth.get_block( number )

        #   Change AttibuteDict to be dictation
        informationBlock = vars(numBlock)
        listTransaction = list()

        #   Tranfer timestamp to date and time
        timestamp = informationBlock[ 'timestamp' ]
        dateTime = datetime.datetime.fromtimestamp( timestamp )
        #   Get form 2021-12-01 00:00:00
        time = dateTime.strftime('%Y-%m-%d %H:%M:%S')
        #   Split date and time
        timeSplit = time.split(' ')

        #   Get in dict to call informationBlock
        informationBlock[ 'date' ] = timeSplit[0]
        informationBlock[ 'times' ] = timeSplit[1]

        transactions = informationBlock[ 'transactions' ]
        #   Tranfer hexbyte to be 8-byte of transactions
        for strtransaction in transactions:
            hexTrasaction = strtransaction.hex()
            listTransaction.append( hexTrasaction )
        #   Keep to be list
        informationBlock['transactions'] = listTransaction
        informationBlock.pop('timestamp')
        informationBlock.pop('extraData')
        informationBlock.pop('hash')
        informationBlock.pop('logsBloom')
        informationBlock.pop('mixHash')
        informationBlock.pop('nonce')
        informationBlock.pop('parentHash')
        informationBlock.pop('receiptsRoot')
        informationBlock.pop('sha3Uncles')
        informationBlock.pop('stateRoot')
        informationBlock.pop('transactionsRoot')
        
        if 'baseFeePerGas' in informationBlock:
            informationBlock.pop('baseFeePerGas')
        informationBlock.pop('difficulty')
        informationBlock.pop('totalDifficulty')
        informationBlock.pop('uncles')

        return informationBlock

    def informationBlockByTime( number ):
        ''' This is function that Choose time to keep data
            INPUT - Information of blockchain from function informationByBlock
                    {   
                        'gasLimit': int, 'gasUsed': int, 'miner': str, 
                        'number': int, 'size': int, 'transactions': list, 'date': str, 'time': str
                    }
            OUTPUT - Information of blockchain that choose time
        '''
        #   Get information from informationByBlock for geting transaction
        informationBlock = getDataBlockchain.informationByBlock( number )
        informationBlockByTime = dict()
        #   Choose time to keep data
        if '20:00:00' <= informationBlock[ 'times' ] <= '22:00:59':
            informationBlockByTime = informationBlock
        return informationBlockByTime

    def informationByTransaction( number ):
        ''' This function is call web3 for get_transaction
            INPUT - information of block in function informationByBlock
            OUTPUT - information of transaction
                {   blockNumber:str,
                    from:str,
                    gas:str,
                    gasPrice:str,
                    hash:str,
                    to:str,
                    value:str
                }
        '''
        n = 1
        #   call infura.io
        web3 = getDataBlockchain.__getInformation()
        #   Get information from informationByBlock for geting transaction
        getDataByBlock = getDataBlockchain.informationByBlock( number )
        #   Get transactions
        getTransactions = getDataByBlock[ 'transactions' ]
        dictInformationTransaction = dict()
        listInformationTransaction  = list()
        #   Use web3 get_transaction by each transaction
        for getTransaction in getTransactions:

            informationByTransactions = web3.eth.get_transaction( getTransaction )
            informationTransactions = vars(informationByTransactions)

            informationTransactions[ 'blockNumber' ] = str( number )
            informationTransactions[ 'hash' ] = getTransaction
            informationTransactions[ 'gas' ] = str( informationTransactions[ 'gas' ] )
            informationTransactions[ 'gasPrice' ] = str( informationTransactions[ 'gasPrice' ] )
            informationTransactions[ 'value' ] = str( informationTransactions[ 'gas' ] )

            informationTransactions.pop('blockHash')
            if 'accessList' in informationTransactions:
                informationTransactions.pop( 'accessList' )
            if 'chainId' in informationTransactions:
                informationTransactions.pop( 'chainId' )
            informationTransactions.pop( 'input' )
            if 'maxFeePerGas' in informationTransactions:
                informationTransactions.pop( 'maxFeePerGas' )
            if 'maxPriorityFeePerGas' in informationTransactions:
                informationTransactions.pop( 'maxPriorityFeePerGas' )
            informationTransactions.pop( 'nonce' )
            informationTransactions.pop( 'r' )
            informationTransactions.pop( 's' )
            informationTransactions.pop( 'transactionIndex' )
            informationTransactions.pop( 'type' )
            informationTransactions.pop( 'v' )
            # print(informationTransactions)
            #   Count num transaction 
            print('+------------------------------------------------------------------------------------------------+-----------------+')
            print('|',n,'| Complete : Transaction ',getTransaction, '|','Block : ',number,'|')
            #   Keep information of transaction in list
            # listInformationTransaction.append( informationTransactions )
            #   Get in MongoDB of Transaction
            collectionTransaction = serverMongoDB.collectionTransaction()
            collectionTransaction.insert_one( informationTransactions )
            
            n = n + 1 
        print('+------------------------------------------------------------------------------------------------+-----------------+')
        #   Get list information of transaction in diction by number blockchain is key
        # dictInformationTransaction[ str( number ) ] = listInformationTransaction
        print( 'Count          : ',n )
        return 'Transaction Complete' 
