from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return 'Hello World'

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if restaurante is None:

            return {'Dados': data}

        else:

            restaurantes = []
            for item in data:
                if item['Company'] == restaurante:

                    restaurantes.append( {
                            'item':item['Item'],
                            'price':item['price'],
                            'description':item['description']
                        }
                    )

            return {'restaurante': restaurante, 'cardapio':restaurantes}

            
    else:
        return {'status':'erro', 'code':response.status_code, 'desc':response.text}