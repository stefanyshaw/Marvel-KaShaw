from dotenv import load_dotenv
from time import time

import  os
import hashlib
import request

load_dotenv()
#os.getenv('API_kEY')

def get_hash():
    ts = int(time())
    pvt = os.getenv('PVT_KEY')
    apikey = os.getenv('API_KEY')

    cripto = str(ts) + pvt + apikey
    
    hash_marvel = hashlib.md5(cripto.encode()).hexdigest()
