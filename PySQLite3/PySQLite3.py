import sqlite3

#create bank
bank = sqlite3.connect('db_first.db')

#cursor: cursor.
cursor = bank.cursor()

#cursor:create table.
def create_tb_people():
    cursor.execute("CREATE TABLE people(name text, phone integer, age integer, email text)")
#create_tb_people()

def insert_people_data():
#cursor:insert data on table
    cursor.execute("INSERT INTO people VALUES('Mary Jane',99999999999,40,'mjane@mail.com')")
#insert_people_data()

def insert_people_new_data():
    print('INSERT DATA : NAME, AGE, E-MAIL')
    nam = str(input('First name : '))
    pho = int(input('Phone : '))
    age = int(input('Age : '))
    eml = str(input('E-mail : '))

    #mount:INSERT_INTO string
    minc = ("INSERT INTO people VALUES('{}',{},{},'{}')".format(nam,pho,age,eml))

    #INSERT_INTO_MOUNT__
    if (nam != '' and pho!= '' and age != '' and eml != ''):
        cursor.execute(minc)
        print('Data registered successfully.')
        bank.commit()
    else:
        print('Fill in all data correctly!')
        exit()

#call__ insert_data__
#insert_people_new_data()

#comit__ command
#bank.commit()

def delete_data():
    try:
        reason = str(input('Reason for exclusion : '))
        print('DELETING...')
        sleep(2)
        cursor.execute("DELETE from people WHERE age = 31")
        bank.commit()
        bank.close()
        print(F'Data deleted successfully, reason : {reason}.')
    except sqlite3.error as err:
        print('Error deleting',err)
#delete_data()

def verify_data():
    cursor.execute("SELECT * FROM people")
    db_list = (cursor.fetchall())
    #dataview_mount
    dt_sz = (len(db_list)) # list size
    print(db_list[0])
    print(db_list[0][0])
    print(db_list[0][1])
    print(db_list[0][2])
    print(db_list[0][3])
    print('\n')
    print(db_list[1])
    print(db_list[1][0])
    print(db_list[1][1])
    print(db_list[1][2])
    print(db_list[1][3])
#delete_data()

def update_data():
    #Example...
    change_name = 'Steve'
    cursor.execute("UPDATE people SET nome='Steve' WHERE idade=41 ")
    bank.commit()
    print('Data updated successfully.')
#update_data()








