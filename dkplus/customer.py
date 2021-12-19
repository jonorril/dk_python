import json

from dkplus.dk import dkp

endpoint_path = "/customer"

class Customer(dkp):

  cust = ""

  def __init__(self, auth):
    super().__init__(auth)

  def loadCustomer(self, cust):
    return super().gett("/"+str(cust))

  def endpoint(self):
    return super().endpoint()+endpoint_path

  def getNumber(self):
    return self.getdata('Number')

  def getName(self):
    return self.getdata('Name')    

  def getAddress(self):
    return self.getdata('Address1')    

  def getCurrency(self):
    return self.getdata('CurrencyCode')        

  def getDiscount(self,disc=0):
    if disc!=0:
      return disc
    else:
      return self.getdata('Discount')