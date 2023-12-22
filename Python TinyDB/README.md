# <b style="color:crimson"> CodeBabel-Python</b>
## TinyDB
___
[![Banner-New-13-12-23.png](https://i.postimg.cc/L6CqTCBD/Banner-New-13-12-23.png)](https://postimg.cc/MvBKZYLf)<h3>TinyDB</h3>
<img src="https://img.shields.io/badge/python-3.10%20|%203.11-blue">
___

## <b style="color:indianred;">* TinyDB (TinyDB Folder)</b> 
#### tinydb version : 4.8.0
___
### TinyDB Database Document JSON ( TinyDB Folder )
📂 [TinyDB](https://github.com/CharlesCodebabel/CodeBabel-Python/tree/main/Python%20Flask/Restfull%20API)
___
### 1 : [ pip ]
#### <b style="color:lightblue;">[[ Windows ]]</b>
> <b style="lblue">pip install tinydb</b>
#### <b style="color:#47b776;">[[ Linux/Mac ]]</b>
> <b style="mint">pip3 install tinydb</b>

### <b style="color:indianred;">🐍 Python TinyDB : </b>
```python
from tinydb import TinyDB, Query, where
#CREATE DOCUMENT DATABASE/CRIAR DATABASE DOCUMENTO
db = TinyDB('db.json')

# INSERT DATA/INSERE DADO
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})

# SEARCH/READ/WHERE/ALL ~ PESQUISA/LÊ/ONDE/TUDO
db.search(Query().type == 'apple')
db.search(where('type') == 'peach')
db.all() #{ SHOW ALL DATABASE/ MOSTRA DATABASE COMPLETO}

# SEE MORE ON PROJECT...
#delete all data document, remove data
#deletar todos os dados, remover dado
```
### 🧾 <b style="color: indianred;">TinyDB ReadTheDocs : </b>
[https://tinydb.readthedocs.io/en/latest/getting-started.html](https://tinydb.readthedocs.io/en/latest/getting-started.html)

