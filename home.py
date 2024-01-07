import streamlit as st 
import pandas as pd
import query

st.header('Minha dashboard!!')

# sidebar

st.sidebar.image("image/Ferroviario (1).png",use_column_width=True,)
st.sidebar.header('Home')
st.sidebar.header('Jogadores')
st.sidebar.header('Partidas')

result = query.view_all_data()
df = pd.DataFrame(result,columns=["idpartida","data","competicao","status_jogo","time_adversario","placar","resultado","cartoes_amarelos",
                                  "cartoes_vermelhos","gols_feitos","gols_sofridos","finalizacoes_gol","finalizacoes_totais",
                                  "faltas_cometidas","faltas_recebidas","esquema_tatico","decisao_penalti","finalizacoes_sofridas","esquema_tatico_adv"])

st.dataframe(df)