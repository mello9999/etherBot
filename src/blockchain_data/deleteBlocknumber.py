import pymongo
from serverMongoDB import serverMongoDB

#   Number:int
deleteBlockNumber = serverMongoDB.collectionBlockchain()
#   blockNumber:'str'
deleteTransactionNumber = serverMongoDB.collectionTransaction()
#   Input number to delete
numberOfDataBlockchain = 13894186

#   การลบข้อมูลที่อยู่ในตาราง dataBlockchain in MongoDB 
deleteDataBlockchain = deleteBlockNumber.delete_one({'number':numberOfDataBlockchain})
print('Delete DataBlockchain : Complete')


#   การลบข้อมูลที่อยู่ในตาราง dataTransaction in MongoDB
numberOfDataTransaction = str(numberOfDataBlockchain)
deleteDataTransaction = deleteTransactionNumber.delete_many({'blockNumber':numberOfDataTransaction})
print('Delete DataTransaction : Complete')