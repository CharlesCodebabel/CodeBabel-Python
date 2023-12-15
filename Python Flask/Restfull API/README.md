<style>
    .crimson { color:crimson; }
    .ired { color:indianred;}
    .yellow { color:yellow; }
    .lyellow { color: #f7dc6f ;}
    .pgreen { color:palegreen;}
    .mint { color:#47b776;}
    .lblue { color:lightblue;}
    .purp { color: #d7bde2;}
</style>
# [![icon32-New.gif](https://i.postimg.cc/vBbqzZbp/icon32-New.gif)](https://postimg.cc/bGV9Y8GT)<span class="crimson"> CodeBabel-Python</span>
## CodeBabel PyFlask RestFull-API
___
## Os : <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
___
[![Banner-New-13-12-23.png](https://i.postimg.cc/L6CqTCBD/Banner-New-13-12-23.png)](https://postimg.cc/MvBKZYLf)<h3>Python</h3>
<img src="https://img.shields.io/badge/python-3.10%20|%203.11-blue">
___

## <b class="ired">* Flask RestFull API ( Flask Folder )</b> 
### <b class="lblue">1 : [[ Windows ]]</b>
#### <b class="lblue">create venv</b>
> python -m venv myrestapi

#### <b class="lblue">windows Activate</b>
> <b class="pgreen">(PowerShell)></b> .\myrestapi\Scripts\Activate.ps1<br>
> (CMD)> .\myrestapi\Scripts\activate.bat
___
### <b class="mint">1 : [[ Linux/Mac ]]</b>
#### <b class="mint">create venv</b>
> python3 -m venv myrestapi

#### <b class="mint">Linux/Mac activate</b>
> source myrestapi/bin/activate<br>

___

### 2 : [ pip ]
#### <b class="lblue">[[ Windows ]]</b>
> <b class="lblue">pip -r install requirements.txt</b>
#### <b class="mint">[[ Linux/Mac ]]</b>
> <b class="mint">pip3 -r install requirements.txt</b>

### 3 : [ rodar/run ]
> <b class="lyellow">flask</b> run

### 4 : [ json ]
> http://127.0.0.1:5000/pessoas
    
## 🧾 <b class="purp">documentation</b>
> http://127.0.0.1:5000/apidoc/swagger<br>
> http://127.0.0.1:5000/apidoc/redoc

## <b class="ired">* HTTP Client for test and CRUD data.</b>

### <b class="ired">💠 HTTPie : </b>
* client... not install on virtual env!<br>
* Instalar fora da venv!

>pip install httpie
### 🔹 usage/uso ()
```cmd
> http get http://127.0.0.1:5000/pessoas
> http post http://127.0.0.1:5000/pessoas/ id=66 idade=99 nome=Camilo
> http put http://127.0.0.1:5000/pessoas/ id=66 idade=99 nome=Chamilo
> http delete http://127.0.0.1:5000/pessoas/66
```

### <b class="ired">🐍 Python requests : </b>
* client... create a python file : client.py....<br>

```python
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
#client.py
```
