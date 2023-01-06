#((( API ))) : requests
#CodeBabelPayCep

"""
https://cep.awesomeapi.com.br/:format/:cep
( end point ) https://cep.awesomeapi.com.br/json/05424020

atualização : 30s
resp : 200 cep encontrado,
resp : 400 cep inválido
resp : 404 Cep não encontrado ((error))
"""

import requests
import json

#
print('\n<CodeBabelPyCEP : Somente números>\n')
get_cep = int(input('Digite o CEP : '))
ep = "https://cep.awesomeapi.com.br/json/{}".format(get_cep) #End Point
req = requests.get(ep)  #Obter resposta 220 : ok, 404 : erro.
# Requisição print(req)

consulta = req.json()

#colect data/coletando dados

cep_data = consulta['cep']
cep_address = consulta['address']
cep_state = consulta['state']
cep_district = consulta['district']
cep_city = consulta['city']
cep_city_ibge = consulta['city_ibge']
cep_lat = consulta['lat']
cep_lng = consulta['lng']
cep_ddd = consulta['ddd']

#exit__
print('CEP : {}\nEndereço : {}\nEstado : {}\nBairro : {}\nCidade : {}\nIBGE : {}\nLatitude : {}\nLongitude : {}\nDDD : {}'.format(cep_data,cep_address,cep_state,cep_district,cep_city,cep_city_ibge,cep_lat,cep_lng,cep_ddd))


