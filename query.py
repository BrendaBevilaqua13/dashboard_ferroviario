import mysql.connector
import streamlit as lt

# connection

conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="12345",
    db="db_ferroviario"
)

c=conn.cursor()

#fetch

def view_all_data_game():
    c.execute('select * from info_partida order by idpartida')
    data = c.fetchall()
    return data

'''def view_all_data_player():
    c.execute('select * from info_jogador order by idjogador')
    data = c.fetchall()
    return data'''

def view_info(search):
    if search == 'idpartida':
        c.execute(f'select count({search}) from info_partida')
    else:
        c.execute(f'select count(resultado) from info_partida where resultado = "{search}"')
    data = c.fetchall()
    data = data[0][0]
    return data

def view_res():
    c.execute('select resultado from info_partida')
    data = c.fetchall()
    return data

def view_cards(color):
    c.execute(f'select sum(cartoes_{color}_recebidos) from info_partida')
    data = c.fetchall()
    return data

def view_goals(search):
    c.execute(f'select sum(gols_{search}) from info_partida')
    data = c.fetchall()
    return data

def view_fouls(search):
    c.execute(f'select sum(faltas_{search}) from info_partida')
    data = c.fetchall()
    return data