import logging
from dkplus.dk import dkp
from datetime import datetime

endpoint_path = "/sales/invoice"

#===============================================================================

class Invoice(dkp):

  cust = None
  prod = None
  paym = None
  VATIncluded = False
  reference = ''

  def __init__(self, auth, Customer, Payments, ref=''):
    super().__init__(auth)
    self.data = {}
    self.cust = Customer
    self.paym = Payments    
    self.reference = ref

#===============================================================================

  def createInvoice(self, itemList, VAT=False):

    # Invoice header
    self.VATIncluded = VAT
    self.storedata('Date',
      datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-1]
    )
    self.storedata('Reference', self.reference)
    self.storedata('Currency',self.cust.getCurrency())

    # Custmer
    self.storedata('Customer', {
      "Number":self.cust.getNumber(),
      "Name":self.cust.getName(),
      "Address1": self.cust.getAddress()
    })

    # Invoice lines
    lines = []
    for prod in itemList:
      if prod.valid:
        prod.setItemReference('DCBA')
        lines.append(
          {
            "ItemCode":prod.getItemCode(),
            "Text": prod.getItemDescription(),
            "Quantity": prod.getItemQuantity(),
            "Reference": prod.getItemReference(),
            "IncludingVAT": self.VATIncluded,
            "Price": prod.getItemPrice(self.VATIncluded),
            "Discount": self.cust.getDiscount()
          }
        )

    self.storedata('Lines', lines)

    # Payments
    self.storedata('Payments', [
      {
        "ID": self.paym.getpaymentid(),
        "Name": self.paym.getpaymentname()
      }
    ])

    # Create the invoice
    logging.debug('Inoice->',self.data)
    return self.postt('?post=true')

  def getInvoiceNo(self):
    return self.getdata('Number')

  def endpoint(self):
    return super().endpoint()+endpoint_path

#===============================================================================
