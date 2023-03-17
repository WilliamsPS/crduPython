import psycopg2

def conectar():
    connetion = psycopg2.connect(
        host = '192.168.1.37', # reemplazar con la dirección IP de tu máquina host
        user = 'root',
        password = 'root',
        database = 'data'
    )
    return connetion

