import streamlit as st 
import pandas as pd
import query
from PIL import Image
from streamlit_option_menu import option_menu


result = query.view_all_data()
df = pd.DataFrame(result,columns=["idpartida","data","competicao","status_jogo","time_adversario","placar","resultado","cartoes_amarelos",
                                  "cartoes_vermelhos","gols_feitos","gols_sofridos","finalizacoes_gol","finalizacoes_totais",
                                  "faltas_cometidas","faltas_recebidas","esquema_tatico","decisao_penalti","finalizacoes_sofridas","esquema_tatico_adv"])



colunasUteis = ['data','competicao','time_adversario', 'status_jogo', 'resultado', 'placar']
df = df[colunasUteis]


def time():
    st.title('DESEMPENHO DO TIME')
    default = 'Escolha'
    fCompeticao = st.selectbox(
        'Selecione a competição:',
        options=df['competicao'].unique(), 
        index=None,
        placeholder="Sua escolha...",
       
    )
    fAdversario = st.selectbox(
        'Selecione o adversário:',
        options=df['time_adversario'].unique(),
        index=None,
        placeholder="Sua escolha...",
    )
    dadosUsuario = None
    if fCompeticao and fAdversario:
        dadosUsuario = df.query(
            'competicao == @fCompeticao & time_adversario == @fAdversario' 
        )
    elif fCompeticao and not fAdversario:
        dadosUsuario = df.query(
            'competicao == @fCompeticao' 
        )
    elif not fCompeticao and fAdversario:
        dadosUsuario = df.query(
            'time_adversario == @fAdversario' 
        ) 
    else:
        dadosUsuario = df    

    st.header('Resultados')
    if fCompeticao:
        st.markdown(f'**Competição selecionada:** {fCompeticao}')
    if fAdversario:
        st.markdown(f'**Time Adversário selecionado:** {fAdversario}')

    st.dataframe(dadosUsuario)



# SIDEBAR
with st. sidebar:
    st.header('FERROVIÁRIO')
    logo = Image.open('image\Ferroviario.png')
    st.image(logo, use_column_width=True)
    selected = option_menu(
        menu_title='Menu',
        options=['Time','Jogador'],           
        )

if selected == 'Time':
    time()
else:
    st.title(f'{selected}')
    
