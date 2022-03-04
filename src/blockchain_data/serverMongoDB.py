from pymongo import MongoClient
import certifi

class serverMongoDB():

    #   New
    def __databaseMongoDB():
        ''' This module connect server MongoDB
                OUTPUT - Database that keep information
                'dataBlockchain' 
        '''
        # <password> : use 'password' on MongoDB database 
        ethereum = MongoClient("mongodb+srv://data:<password>@databaseblockchain4.lubse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

        db = ethereum[ 'dataBlockchain_test' ]
    
        return db

    #   Old
    def __databaseInformation():
        ''' This module connect server MongoDB
                OUTPUT - Database that keep information
                'databaseBlockchain'
        '''
        # <password> : use 'password' on MongoDB database 
        ethereum = MongoClient("mongodb+srv://data:<password>@databaseblockchain4.lubse.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=certifi.where())

        db = ethereum[ 'databaseBlockchain' ]
    
        return db

    #   New
    def collectionBlockchain():

        dataBlockChain = serverMongoDB.__databaseMongoDB()

        collationData = dataBlockChain[ 'dataBlockchain' ]

        return collationData

    def collectionTransaction():

        dataTransactionChain = serverMongoDB.__databaseMongoDB()

        collationData = dataTransactionChain[ 'dataTransaction' ]

        return collationData