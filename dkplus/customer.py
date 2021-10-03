import requests

from dkplus.dk import dkEntity

endpoint_path = "/customer"

class Customer(dkEntity):
  def __init__(self, CustNo):
    print(CustNo)

  def endpoint(self):
    return super().endpoint()+endpoint_path