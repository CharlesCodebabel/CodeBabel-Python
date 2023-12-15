"""
First  : create virtual envoirement
Second : install by (Windows) pip -r requirements.txt
( linux/Mac ) pip3 -r requirements.txt
"""

from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field # Tinydb database
from tinydb import TinyDB, Query

# tools
from typing import Optional # typing
from itertools import count # intertools

#{ setup }
server = Flask(__name__)
spec = FlaskPydanticSpec('Flask RestAPI', title='🐍 Python Flask RestFull')
spec.register(server)
database = TinyDB('pessoas.json')
c = count()

#{ BaseModel }
class QueryPessoa(BaseModel):
    id: Optional[int]
    nome:Optional[str]
    idade:Optional[int]

class Pessoa(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
    #id: Optional[int]
    nome:str
    idade:int

class Pessoas(BaseModel):
    pessoas: list[Pessoa]
    count:int


#{ methods }
# GET
@server.get('/pessoas') # route '/pessoas'
@spec.validate(resp=Response(HTTP_200=Pessoas))
def pegar_pessoas():
    """🔎 Mostra pessoa no banco de dados.""" # docstring: change on swagger...
    return jsonify(
        Pessoas(
            pessoas=database.all(),
            count=len(database.all())
        ).dict()
    )

# POST
@server.post('/pessoas')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_201=Pessoa))
def inserir_pessoa():
    """ 👤 : Insere uma pessoa no banco de dados.""" # docstring: change on swagger...
    body = request.context.body.dict() # insert pessoa on BaseModel
    database.insert(body)
    return(body)

# PUT
@server.put('/pessoas/<int:id>')
@spec.validate(body=Request(Pessoa), resp=Response(HTTP_200=Pessoa))
def altera_pessoa(id):
    """ 🧽 : Alteração feita no banco de dados.""" # docstring: change on swagger...
    Pessoa = Query()
    body = request.context.body.dict() # insert pessoa on BaseModel
    database.update(body, Pessoa.id == id)
    return(body)

# DELETE
@server.delete('/pessoas/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def deleta_pessoa(id):
    """ 💥 : Deleta dado escolhido no banco atual.""" # docstring: deleta direto na swagger...
    database.remove(Query().id == id)
    return(jsonify({}))



if (__name__ == "__main__"):
    server.run()