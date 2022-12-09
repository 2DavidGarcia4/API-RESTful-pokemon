import requests
from flask import Flask, request
import sys
import os

app = Flask(__name__)

def controller_poke(headers):
  try:
    endpoint_poke_api = headers['Endpoint_poke_api']
    exists_ability_name = headers['Ability_name']

    response = requests.get(endpoint_poke_api).json()
    abilities = response['abilities'][0]
    ability_name = abilities['ability']['name']
    print(abilities, ability_name)
    # return response

  except Exception as error:
    return {'error': error.args[0]}, 400
  else:
    if exists_ability_name in ability_name:
      return {'exists_ability_name': True}, 200
    return {'exists_ability_name': False}, 200

@app.route('/poke')
def poke():
  return controller_poke(request.headers)

@app.route('/status')
def status():  
  return {'sistem': sys.platform, 'ram': os.cpu_count()}, 200

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=4000, debug=True)