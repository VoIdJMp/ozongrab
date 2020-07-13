# import pandas as pd

# tables = pd.read_html("http://apps.sandiego.gov/sdfiredispatch/")

# print(tables[0])

# import requests

# API_KEY = '0296d4f2-70a1-4c09-b507-904fd05567b9'
# Client_Id = 836

# res = requests.get('http://www.ozon.ru')


# print(res.read_html)

import json
import requests


api_token = '04c1d-a754-4c7f-aa2c-8d14e256'
client_id = '812'
api_url_base = 'http://api-seller.ozon.ru'
headers = {
          'Content-Type': 'application/json',
            'Host': api_url_base,
             'Client-Id': client_id,
          'Authorization': 'Bearer {0}'.format(api_token)
          }

api_url = 'http://api-seller.ozon.ru/v1/category/tree'.format(api_url_base)

response = requests.get(api_url, headers=headers)

print(response.status_code)
