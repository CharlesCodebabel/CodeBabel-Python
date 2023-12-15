import requests, json

EP = 'http://127.0.0.1:5000/pessoas'
RQ = requests.get(EP)

def get():
    global EP, RQ
    DI = RQ.json()
    print(DI)
#get()

def post():
    global EP
    RQ = requests.post(EP, json={"id":111, "nome":"Gibrautar", "idade":1077})
    DI = RQ.json()
    print(RQ)
#post()

def put():
    global EP
    RQ = requests.put(EP+'/99', json={"id":99, "idade":77, "nome":"Leviathan"})
    print(RQ.content)
#put()

def delete():
    global EP
    ID:int = 111
    RQ = requests.delete(EP+f'/{ID}')
    print(RQ.content)
#delete()