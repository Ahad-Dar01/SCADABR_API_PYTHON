import datetime
import time
from suds.client import Client
dateStart = datetime.datetime.now() 
client = Client('http://127.0.0.1:8080/ScadaBR/services/API?wsdl')
#print ('######################################')
#print ('describing the service:')
#print (client)
#print ('######################################')
#types are created as follows:
#browseTagsOptions = client.factory.create('ns3:BrowseTagsOptions')
#note the type 
#print ('BronseTagsOptions')
#print (browseTagsOptions)
#set BrowseTagsParams
#browseTagsOptions.maxReturn = 2
#itemsPath = 'type'
#calling browseTags(xs:string itemsPath, ns3:BrowseTagsOptions options, )
#BrowseTagsResponse = client.service.browseTags(itemsPath,browseTagsOptions)
#rint ('browse tag counterProduct')
#print (BrowseTagsResponse)
#all tags
#print ('ALL TAGS')
#print (client.service.browseTags())
#print ('######################################')
############### FOR READING THE DATA SOURCE ######################
################################################################
while(1):
    itemPathList = ['type']
    readDataOptions = client.factory.create('ns3:ReadDataOptions')
    readDataOptions.maxReturn = 3
    readDataResponse = client.service.readData(itemPathList , readDataOptions )
    print ('reading tags: Type1')
    print (readDataResponse.itemsList[0]["value"])
    print ('reading the tag: counterProduct')
    time.sleep(5)
  ########################################################################### 
  #####################  Write DATA  ######################################
##############################################################################
#while(1):
    #writeDataOptions = client.factory.create('ns3:WriteDataOptions')
    #writeDataOptions.returnItemValues = True
    #itemStringList= client.factory.create('ns5:ItemStringValue')
    #dataType = client.factory.create('ns2:DataType')
    #quality = client.factory.create('ns2:QualityCode')
    #itemStringList.itemName = 'type'
    #itemStringList.dataType = dataType.FLOAT
    #itemStringList.value = 23.5
    #itemStringList.quality =quality.GOOD
    #itemStringList.timestamp = datetime.datetime.now()
    #writeStringDataResponse=client.service.writeStringData(itemStringList,writeDataOptions )
    #print ('writing on the tag counterProduct')
    #print  (writeStringDataResponse)
    #print ('######################################')
    #time.sleep(4)
