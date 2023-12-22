#TinyDB CRUD
from datetime import datetime as dt
from tinydb import TinyDB, Query, where

#DATETIME
""" if you need to insert date, time or timestamp in json """
HOUR = str(dt.now().strftime('%H:%M:%S'))
DATE = str(dt.now().strftime('%d/%m/%Y'))
DATETIME = str(dt.now().strftime('%d/%m/%Y - %H:%M:%S'))
TIMESTAMP = str(dt.now().timestamp())

#CREATE DATADOC
"""
sort_keys=True, indent=4, separators=(',', ': ') ~> ascending alphabetical order... a to z
sort_keys=False, indent=4, separators=(',', ': ') ~> order by construction... {'name'...}
"""
db = TinyDB('db.json', sort_keys=False, indent=4, separators=(',', ': '))

#INSERT -> CREATE

'INSERT INLINE'
#db.insert({'name':'CodeBabel', 'age':100, 'language':'Python','date': DATE})

'INSERT BY VARIABLE'
data = {
    'name':'Elon',
    'age':44,
    'language':'Cash',
    'date': DATE,
}

#db.insert(data)

'INSERT MULTIPLE'
data_a = {'name':'Anna', 'age':22, 'language':'Jython','date': DATE}
data_b = {'name':'Mark', 'age':23, 'language':'Brython','date': DATE}
data_c = {'name':'John', 'age':32, 'language':'Cython','date': DATE}
#db.insert_multiple([data_a, data_b, data_c]) # execute 1x and change data
#print(db.all) # show created

'SEARCH -> READ'
s_anna = db.search(Query().name == 'Anna')
print(s_anna)
s_age = db.search(Query()['age'] == 100)
print(s_age)

#COMPARISION OPERATORS ( ==, !=, >= <= )
s_equals = db.search(Query().name == 'Mark')
s_diferent = db.search(Query().name != 'Elon')
s_major = db.search(Query().age > 90 'Elon')
print(s_major)

#LOGICAL OPERATORS
s_denial =  db.search(~ (Query().name == 'John'))
s_and = db.search(Query().name == 'John') & (Query().age == 32)
s_or = db.search(Query().name == 'John') | (Query().age == 32)

#FUNCTIONS
f_exist = db.search(Query().name.exist()) #~> prints the object that has the name attribute
f_matches = db.search(Query().name.matches('[a-z]')) #~> prints the object that has the name from a to z (regex)
f_fragments = db.search(Query().fragment({'date':TIMESTAMP})) #~> search for matches.
f_any = Query().name.any(['F'])
f_one_of = db.search(Query().age.one_of([32])) # ~> John age...
f_db_all = db.all() # ~> all data document...

#WHERE
db.search(where('nome')=='Anna')
db.search(where('language').Jogar == 'Jython')

#UPDATE
db.update(
    {'nome':'Marcela'},
    where('nome')=='Julia',
)

db.update_multiple([
    ({'nome':'Marcela'}, where('nome')=='Julia'),
    ({'nome':'Carla'}, where('nome')=='Carlos'),
])

db.update({'adm':False}) # ~> updates the 'adm' field to false on all "users"

#UPSERT
db.upsert(
    {'nome':'Paul', 'acess':True}, where('name')=='Julia', # ~> If the field exists, update it, if it doesn't exist, insert the data.
)

#OPERATIONS
def OPERATIONS():
    from tinydb.operations import delete, set, increment, decrement, subtract, add

    db.update(
        operations.delete('adm'),
        where('name') == 'Alice'
    )

    db.update(
        operations.set('routine', ['comer churrasco']),
        where('sku') == 1,
    )

    """
    delete : deleta
    set : atribui valor
    increment : adiciona mais um +1
    decrement : decrementa menos um -1
    subtract : subtrai N para o campo
    add : adiciona N para campo...

    delete : delete
    set : assigns value
    increment: adds another +1
    decrement: decreases by minus one -1
    subtract : subtracts N for the field
    add : adds N to field...
    """

#REMOVE
#db.remove(where('name') == 'Mill')

'TRUNCATE ~> ERASE ALL DOCBASE'
#db.truncate()
    
