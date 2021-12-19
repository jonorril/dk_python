import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Base service endpoints
api_hostname = "https://api.dkplus.is"
api_version = "/v1"
api_base_url = "/api"


# ===============================================================================

# This is the base class.
class dkp:
    session = None

    # data = dict

    def __init__(self, auth):
        self.session = requests.Session()
        # auth = HTTPBasicAuth(self.username(), self.password())
        self.session.auth = auth
        # self.session.auth = (self.username(), self.password())

    # ===============================================================================

    # Here we try to connect to the server to fetch some data.
    # We try for 3 times if error occurs before we give up and return false.

    def gett(self, endp):
        try:
            response = retry(s=self.session).get(self.endpoint() + str(endp))
        finally:
            if response.text:
                self.data = json.loads(response.text)
            else:
                self.data = json.loads('{"Message":"' + str(response.status_code) + ' ' + type(self).__name__ + '"}')
            if response.status_code == 200:
                return True
            else:
                return False

    # ===============================================================================

    # This function sends request to the server to create records.

    def postt(self, endp):
        try:
            response = retry(s=self.session).post(self.endpoint() + str(endp),
                                                  headers={'Content-type': 'application/json; charset=utf8'},
                                                  data=json.dumps(self.data, indent=3, sort_keys=True)
                                                  )
        finally:
            if response.text:
                self.data = json.loads(response.text)
            else:
                self.data = json.loads('{"Message":"' + str(response.status_code) + ' ' + type(self).__name__ + '"}')
            if response.status_code == 200:
                return True
            else:
                return False

    # ===============================================================================

    def endpoint(self):
        return api_hostname + api_base_url + api_version

    # ===============================================================================

    def getMessage(self):
        try:
            return self.getdata('Message')
        except:
            return ""

    # ===============================================================================

    # Get data from the JSON string in data variable.

    def getdata(self, key):
        if key in self.data: return self.data[key]
        for k, v in self.data.items():
            if isinstance(v, dict):
                item = self.getvalue(v, key)
                if item is not None:
                    return item

    # ===============================================================================

    # Store the data in data variable to be sent to the server.

    def storedata(self, kkey, vvalue):
        self.data[kkey] = vvalue


# ===============================================================================

# This func is outside of the base class.

def retry(s=None):
    s = s or requests.Session()
    retry = Retry(
        total=3,
        read=3,
        connect=3,
        backoff_factor=0.3,
        status_forcelist=[500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    s.mount('http://', adapter)
    s.mount('https://', adapter)
    return s
