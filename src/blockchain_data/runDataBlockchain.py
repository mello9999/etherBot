#!/usr/bin/env python3
import time
from getDataBlockchain import getDataBlockchain
from serverMongoDB import serverMongoDB

startAllTime = time.time()
print('>>>> Loading Process... <<<< ')

#   วันที่ 20/12/2564
# n0 = 13842730 # 13842156 > Block เเรกของ 20.00 
# n = 13842731 # 13842730 > Block สุดท้ายของ 22.00 

#   วันที่ 29/12/2564
# n0 = 13900809 # 13900354 > Block เเรกของ 20.00 
# n = 13900904 # 13900903 > Block สุดท้ายของ 22.00 

#   วันที่ 31/12/2564
n0 = 13913464 # 13913266 > Block เเรกของ 20.00 
n = 13913793 # 13913792 > Block สุดท้ายของ 22.00 

#   วันที่ 08/12/2564
# n0 = 13765452 # 13764939 > Block เเรกของ 20.00 
# n = 13765459 # 13765457 > Block สุดท้ายของ 22.00 

for number in range(n0,n):
    informationBlock = getDataBlockchain.informationBlockByTime( number )
    if informationBlock == {}:
        print('+--------------------------------------------------------------------------------------------------------------+')
        print('| Block :' ,number,'( Out of time )' )
        continue
    else:
        print('+--------------------------------------------------------------------------------------------------------------+')
        # informationTransaction = getDataBlockchain.informationByTransaction( number )
        print('>>> Loading Block Number... <<<<')
        time.sleep(3)
        print('>>> Start keep block number in MongoDB <<<')
        #   Get in MongoDB of BlockNumber
        collectionData = serverMongoDB.collectionBlockchain()
        collectionData.insert_one( informationBlock )
        print('+--------------------------------------------------------------------------------------------------------------+')
        print('| **** Complete Insert DataBlockchain in MongoDB ****')
        #   Get in MongoDB of Transaction
        print(getDataBlockchain.informationByTransaction( number ))
        print('Complete       :  Block ',number )
        
endAllTime = time.time()
print('+--------------------------------------------------------------------------------------------------------------+')
print('All Time       : ',( endAllTime - startAllTime ) /60,'min' )
print('+--------------------------------------------------------------------------------------------------------------+')
