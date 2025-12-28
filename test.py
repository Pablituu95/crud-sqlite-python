import requests
from models import *
from db import *
def verificar_id(id):
    with criar_db() as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        return cur.fetchone()
def verificar_email(email):
    chave_api = '0fb1267373f206c20046ab01ad2db3efd5d8b970'
    url = 'https://api.hunter.io/v2/email-verifier'
    params = {'email': email,
              'api_key': chave_api}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        if response.json()['data']['status'] == 'valid':
            return True
    else:
        return False