from dotenv import load_dotenv
from time import time
from model.hero import hero

import  os
import hashlib
import request

load_dotenv()
#os.getenv('API_kEY')

#segurança
def get_hash():
    ts = int(time())
    pvt = os.getenv('PVT_KEY')
    apikey = os.getenv('API_KEY')

    cripto = str(ts) + pvt + apikey

    hash_marvel = hashlib.md5(cripto.encode()).hexdigest()

    return ts, apikey, hash_marvel

#api
def get_hero(name_starts_with = ''):
    info_hash = get_hash()

    params = {
        "NameStartWith": name_starts_with,
        "limit": 50,
        "ts": info_hash[0],
        "apikey": info_hash[1],
        "hash": info_hash[2]
    }

    resp = request.get('https://developer.marvel.com:443/v1/public/characters', params)
    return resp.json()['data']['result']