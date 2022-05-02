import mysql.connector
from mysql.connector import Error
from database import *
from data import *
from queries import *

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def execute_query(connection, query):
    if query != ';':
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

def read_query(connection, query,param):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query,param)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

menu_options = {
    1: 'A quantidade e valor de produtos com disconto que foram vendidos em cada categoria',
    2: 'Para todas as empresas, listar aquelas que venderam mais que N em produtos',
    3: 'Vendedores com produtos com avaliação acima da média',
    4: 'Produto com maior acesso',
    5: 'Devolve o nome dos usuários que compraram todos os produtos que um outro usuário comprou(e possivelmente outros)',
    6: 'Fornece dados dos produtos no carrinho de um cliente específico',
    7: 'Fornece os dados dos compradores de um determinado produto de um determinado vendedor',
    8: 'Fornece o nome de quem comprou o produto de uma marca especifica',
    9: 'Dá informações sobre os produtos de uma categoria',
    10: 'Dá as informações de entrega para uma compra',
    11: 'Exit'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

if __name__=='__main__':

    pw = "YOURPASSWORD"
    db = "amazon"

    connection = create_server_connection("localhost", "root", pw)
    create_database_query = f"CREATE DATABASE {db}"
    create_database(connection, create_database_query)

    connection = create_db_connection("localhost", "root", pw, db)

    drop_everything_ifexist = filter(None, drop_everything_ifexist.split(';'))
    create_tables = filter(None, create_tables.split(';'))
    alter_tables = filter(None, alter_tables.split(';'))
    insert_everything = filter(None, insert_everything.split(';'))

    for i in drop_everything_ifexist:
        execute_query(connection,i.strip()+';')

    for i in create_tables:
        execute_query(connection,i.strip()+';')

    for i in alter_tables:
        execute_query(connection,i.strip()+';')

    for i in insert_everything:
        execute_query(connection,i.strip()+';')
    
    #execute_query(connection,create_tables)
    #execute_query(connection,alter_tables)
    #execute_query(connection,insert_everything)
    execute_query(connection,create_view_ComprasUsuario)
    results = []
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Digite sua escolha: '))
        except:
            print('Por favor, digite um número ...')
        
        params = []
        #Check what choice was entered and act accordingly
        if option == 1:
            n = float(input('Insira a quantidade de disconto: '))
            params.append(n)
            results = read_query(connection,search_discount_category,params)
        elif option == 2:
            n = int(input('Insira a quantidade de produtos: '))
            params.append(n)
            results = read_query(connection,search_company_sold,params)
        elif option == 3:
            results = read_query(connection,search_product_rating,params)
        elif option == 4:
            results = read_query(connection,search_most_access,params)
        elif option == 5:         
            n = int(input('Digite o id do usuário: '))
            params.append(n)
            params.append(n)
            results = read_query(connection,search_buyer_profile,params)
        elif option == 6:
            n = int(input('Digite o id do usuário: '))
            params.append(n)
            results = read_query(connection,search_cart,params)
        elif option == 7:
            s = input('Digite o id do vendedor: ')
            n = int(input('Digite o nome do produto: '))
            params.append(n)
            params.append(s)
            results = read_query(connection,search_product_seller,params)
        elif option == 8:
            s = input('Digite o nome da marca: ')
            params.append(s)
            results = read_query(connection,search_product_brand,params)
        elif option == 9:
            s = input('Digite o nome da categoria: ')
            params.append(s)
            results = read_query(connection,search_category,params)
        elif option == 10:
            n = int(input('Digite o id da compra: '))
            params.append(n)
            results = read_query(connection,search_delivery,params)
        elif option == 11:
            print('Saindo...')
            exit()
        else:
            print('Opção inválida.Por favor, digite um número entre 1 e 11.')

        for result in results:
            print(result)

        input('Pressione enter...')