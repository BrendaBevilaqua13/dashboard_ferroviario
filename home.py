import streamlit as st 
import pandas as pd
import query as query
import plotly.figure_factory as ff
import plotly.graph_objects as go
from PIL import Image
from streamlit_option_menu import option_menu


#Query
result = query.view_all_data()
df = pd.DataFrame(result,columns=["idpartida","data","competicao","status_jogo","time_adversario","placar","resultado","cartoes_amarelos",
                                  "cartoes_vermelhos","gols_feitos","gols_sofridos","finalizacoes_gol","finalizacoes_totais",
                                  "faltas_cometidas","faltas_recebidas","esquema_tatico","decisao_penalti","finalizacoes_sofridas","esquema_tatico_adv"])



def team():
    
    selected = option_menu(
        menu_title='Estatísticas do Time',
        options=['Desempenho','Gráficos'],
        orientation='horizontal'                
        )

    if selected == 'Desempenho':
        utils_columns = ['competicao','time_adversario', 'resultado', 'placar']
        df_filtered = df[utils_columns]
        fCompeticao = st.selectbox('Selecione a competição:',
            options=df['competicao'].unique(), 
            index=None,
            placeholder="Sua escolha...",
            )
        fAdversario = st.selectbox('Selecione o adversário:',
            options=df['time_adversario'].unique(),
            index=None,
            placeholder="Sua escolha...",
            ) 
        
        if fCompeticao and fAdversario:
            df_filtered = df_filtered.query(
                'competicao == @fCompeticao & time_adversario == @fAdversario' 
            )
        elif fCompeticao and not fAdversario:
            df_filtered = df_filtered.query(
                'competicao == @fCompeticao' 
            )
        elif not fCompeticao and fAdversario:
            df_filtered = df_filtered.query(
                'time_adversario == @fAdversario' 
            ) 
        

        st.header('Tabela')
        df_sample = [[],[],[],[]]

        for i in df_filtered.values:
            df_sample[0].append(i[0])
            df_sample[1].append(i[1])
            df_sample[2].append(i[2])
            df_sample[3].append(i[3])

        if not df_filtered.empty:
            fig = go.Figure(data=go.Table(
            header=dict(values=['COMPETIÇÃO','ADVERSÁRIO', 'RESULTADO', 'PLACAR'],
                        line_color='#000000',
                        fill_color='#ff4B4B',
                        font=dict(color='white', size=16),
                        ),
       
            cells=dict(values=[df_sample[0],df_sample[1],df_sample[2],df_sample[3]],
                        line_color='#000000',
                        fill_color=['#FFFAFA'],
                        font=dict(color='#000000', size=14),
                        align=['left', 'center'],
                        height=30)
            ))

            fig.update_layout(margin=dict(l=5,r=5,b=5,t=10))
            st.write(fig)
        else:
            st.write('0 Resultados')
        


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
    team()
else:
    st.title(f'{selected}')
    

