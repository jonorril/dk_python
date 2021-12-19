import dkplus
import logging
from requests.auth import HTTPBasicAuth

# Change from logging.INFO to logging.DEBUG
# to get more information.
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("logg.log"),
                              logging.StreamHandler()])

auth = HTTPBasicAuth('demo@dkplus.is', 'Demo123')

cust = dkplus.Customer(auth)
if (cust.loadCustomer("1710794709")):

  paym = dkplus.Payments(auth)
  if (paym.getpayment(8)):

    prodlist = []
    prodlist.append(
      dkplus.Product(auth, "0001",     2, 2323)
    )
    prodlist.append(
      dkplus.Product(auth, "29874443", 1, 1500)
    )

    inv = dkplus.Invoice(auth, cust, paym)
    if inv.createInvoice(prodlist, True):
      logging.info("Invoice no. "+inv.getInvoiceNo()+" created.")
    else:
      logging.info(inv.getMessage())

  else:
    logging.info(paym.getMessage())

else:
  logging.info(cust.getMessage())