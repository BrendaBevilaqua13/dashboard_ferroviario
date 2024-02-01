import streamlit as st 
import pandas as pd
import query
from PIL import Image

result = query.view_all_data()
df = pd.DataFrame(result,columns=["idpartida","data","competicao","status_jogo","time_adversario","placar","resultado","cartoes_amarelos",
                                  "cartoes_vermelhos","gols_feitos","gols_sofridos","finalizacoes_gol","finalizacoes_totais",
                                  "faltas_cometidas","faltas_recebidas","esquema_tatico","decisao_penalti","finalizacoes_sofridas","esquema_tatico_adv"])

df_filtro = df[['data','competicao','time_adversario','resultado']]

st.dataframe(df_filtro)

# SIDEBAR

with st.sidebar:
    st.header('FERROVIÁRIO')
    logo = Image.open('image\Ferroviario.png')
    st.image(logo, use_column_width=True)
    st.subheader('SELEÇÃO DE FILTROS')
    fCompeticao = st.selectbox(
        'Selecione a competição:',
        options=df['competicao'].unique()
    )
    fAdversario = st.selectbox(
        'Selecione o adversário:',
        options=df['time_adversario'].unique()
    )