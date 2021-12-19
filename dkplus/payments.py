from dkplus.dk import dkp

endpoint_path = "/sales/payment/type"


class Payments(dkp):
    paymentNo = ""

    def __init__(self, auth):
        super().__init__(auth)

    def endpoint(self):
        return super().endpoint() + endpoint_path

    def getpayment(self, paymentno):
        return super().gett("/" + str(paymentno))

    def getpaymentid(self):
        return self.getdata('PaymentId')

    def getpaymentname(self):
        return self.getdata('Name')
