from pymongo import MongoClient
import certifi

class serverMongoDB():

    #   New
    def __databaseMongoDB():
        ''' This module connect server MongoDB
                OUTPUT - Database that keep information
                'dataBlockchain' 
        '''
        ethereum = MongoClient("mongodb+srv://data:data@databaseblockchain3.3fs8z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

        db = ethereum[ 'dataBlockchain_test' ]
    
        return db

    #   Old
    def __databaseInformation():
        ''' This module connect server MongoDB
                OUTPUT - Database that keep information
                'databaseBlockchain'
        '''
        ethereum = MongoClient("mongodb+srv://data:data@databaseblockchain3.3fs8z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

        db = ethereum[ 'databaseBlockchain' ]
    
        return db
    
    # def collectionDataBlockchainOld():

    #     dataBlockChain = serverMongoDB.__databaseMongoDB()

    #     collationData = dataBlockChain[ 'dataBlockchain' ]

    #     return collationData

    def collectionDataBlockchain():

        dataBlockChain = serverMongoDB.__databaseInformation()

        collationData = dataBlockChain[ 'dataBlockchain' ]

        return collationData

    # def collectionDataTransactionOld():

    #     dataTransactionChain = serverMongoDB.__databaseMongoDB()

    #     collationData = dataTransactionChain[ 'dataTransaction' ]

    #     return collationData

    def collectionDataTransaction():

        dataTransactionChain = serverMongoDB.__databaseInformation()

        collationData = dataTransactionChain[ 'dataTransaction' ]

        return collationData

    ############################

    #   New
    def collectionBlockchain():

        dataBlockChain = serverMongoDB.__databaseMongoDB()

        collationData = dataBlockChain[ 'dataBlockchain' ]

        return collationData

    def collectionTransaction():

        dataTransactionChain = serverMongoDB.__databaseMongoDB()

        collationData = dataTransactionChain[ 'dataTransaction' ]

        return collationData