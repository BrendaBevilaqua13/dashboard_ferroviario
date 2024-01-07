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

def view_all_data():
    c.execute('select * from info_partida order by idpartida')
    data = c.fetchall()
    return data
