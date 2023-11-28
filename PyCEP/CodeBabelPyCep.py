# ((( API ))) : requests > CodeBabelPyCep

"""
( end point ) https://cep.awesomeapi.com.br/json/05424020 --> atualização : 30s
resp : 200 cep encontrado,
resp : 400 cep inválido
resp : 404 Cep não encontrado ((erro))
"""

import requests, json

print('\n<CodeBabelPyCEP : Somente números>\n')
get_cep = int(input('Digite o CEP : '))
ep = "https://cep.awesomeapi.com.br/json/{}".format(get_cep) # End Point
req = requests.get(ep)  # [ 200 : ok, 404 : error ] --> verify requisition ... print(req)
consulta = req.json()

# collect data/coletando dados
cep_data = consulta['cep']; cep_address = consulta['address']
cep_state = consulta['state']; cep_district = consulta['district']
cep_city = consulta['city']; cep_city_ibge = consulta['city_ibge']
cep_lat = consulta['lat']; cep_lng = consulta['lng']; cep_ddd = consulta['ddd']

# exit__
print('CEP : {}\nEndereço : {}\nEstado : {}\nBairro : {}\nCidade : {}',
      '\nIBGE : {}\nLatitude : {}\nLongitude : {}\nDDD : {}'.format(cep_data,
                                                                    cep_address,cep_state,
                                                                    cep_district,cep_city,
                                                                    cep_city_ibge,cep_lat,
                                                                    cep_lng,cep_ddd)
)

# colect state/district__
IBGES = cep_state; IBGEC = cep_district
INF = ('https://www.ibge.gov.br/cidades-e-estados/{}/{}.html'.format(IBGES,IBGEC))
PAN = ('https://cidades.ibge.gov.br/brasil/{}/{}/panorama'.format(IBGES,IBGES))

# general infos__
print('[INFORMAÇÕES GERAIS]: \n{}\n[PANORAMA]: \n{}'.format(INF, PAN))
