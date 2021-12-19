import json

from dkplus.dk import dkp

endpoint_path = "/Product"

class Product(dkp):

  valid = False
  quantity = 0
  reference = ''
  itemprice = 0

  def __init__(self, auth, prod='', qty=0, priz=0):
    super().__init__(auth)
    if prod!='':
      self.valid = super().gett("/"+str(prod))
      self.quantity = qty
      self.itemprice = priz

  def getProduct(self, prod, qty):
    self.valid = super().gett("/"+str(prod))
    self.quantity = qty
    return self.valid

  def getUnitPrice(self):
    if self.valid:
      return self.getdata('UnitPrice1WithTax')

  def getItemCode(self):
    if self.valid:
      return self.getdata('ItemCode')

  def getItemDescription(self):
    if self.valid:
      return self.getdata('Description')

  def getItemQuantity(self):
    if self.valid:
      return self.quantity      

  def setItemReference(self, ref):
    if self.valid:
      self.reference = ref

  def getItemReference(self):
    if self.valid:
      return self.reference

  def getItemPrice(self, VAT=False):
    if self.valid:
      if self.itemprice==0:
        if VAT:
          return self.getdata('UnitPrice1WithTax')
        else:
          return self.getdata('UnitPrice1')
      else:
        return self.itemprice

  def endpoint(self):
    return super().endpoint()+endpoint_path