import streamlit as st 
import pandas as pd
import query as query
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from PIL import Image

#css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


#Query
result = query.view_all_data_game()
df = pd.DataFrame(result,columns=["idpartida","data","competicao","status_jogo","time_adversario","placar","resultado","cartoes_amarelos",
                                  "cartoes_vermelhos","gols_feitos","gols_sofridos","finalizacoes_gol","finalizacoes_totais",
                                  "faltas_cometidas","faltas_recebidas","esquema_tatico","decisao_penalti","finalizacoes_sofridas","esquema_tatico_adv"])



def team_func():
    selected = option_menu(
        menu_title='Informações do Time - Temporada 2024',
        options=['Desempenho','Estatísticas','Gráficos'],
        orientation='horizontal',
        icons=['graph-up','bar-chart-fill','pie-chart-fill']         
        )

    if selected == 'Desempenho':
        #Tabela
        compCol, advCol = st.columns(2, gap='large')
        utils_columns = ['competicao','time_adversario', 'resultado', 'placar']
        df_filtered = df[utils_columns]

        with compCol:
            fCompeticao = st.selectbox('Selecione a competição:',
                options=df['competicao'].unique(), 
                index=None,
                placeholder="Sua escolha...",
                )
        with advCol:
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
        st.header('Tabela de Resultados',divider='red')
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
    
        
    elif selected == 'Estatísticas':
        col1,col2,col3 = st.columns(3)
        with col1:
            st.header('Cartões', divider='red')
            res = query.view_cards('amarelos')
            st.info(f'{res[0][0]} AMARELOS', icon="🟨")
            res = query.view_cards('vermelhos')
            st.info(f'{res[0][0]} VERMELHOS', icon="🟥")
        with col2:
            st.header('Gols', divider='red')
            res = query.view_goals('feitos')
            st.info(f'{res[0][0]} GOLS FEITOS', icon="⚽")
            res = query.view_goals('sofridos')
            st.info(f'{res[0][0]} GOLS SOFRIDOS', icon="❌")
        with col3:
            st.header('Média de Faltas por Jogo', divider='red')
            res = query.view_fouls('cometidas')
            res = round(res[0][0] / (query.view_info('idpartida')))
            st.info(f'{res} FALTAS COMETIDAS', icon="📌")
            res = query.view_fouls('rebidas')
            res = round(res[0][0] / (query.view_info('idpartida')))
            st.info(f'{52} FALTAS SOFRIDAS', icon="📌")

    else:
        st.markdown('### Temporada 2024')
        res = query.view_res()
        list_values = []
        win=0
        loss=0
        draw=0
        for i in range(len(res)):
            if res[i][0].lower() == 'vitoria':
                win+=1
            elif res[i][0].lower() == 'derrota':
                loss+=1
            else:
                draw+=1

        list_values.append(win)
        list_values.append(loss)
        list_values.append(draw)

        labels = ['Vitórias', 'Derrotas', 'Empates']
        colors = ['MediumSeaGreen','FireBrick','LightGray']
        fig = go.Figure(data=go.Pie(
            labels=labels,
            values=list_values,
            marker_colors=colors,
            hole=0.5,
            showlegend=False
        ))
        fig.update_traces(textposition="outside", textinfo="value+label")
        fig.update_layout(annotations=[dict(text="Partidas",
                                            x=0.5,
                                            y=0.5,
                                            font_size=18,
                                            showarrow=False)])

        st.write(fig)   

# SIDEBAR
with st. sidebar:
    st.header('FERROVIÁRIO')
    logo = Image.open('image\Ferroviario.png')
    st.image(logo, use_column_width=True)
    selected = option_menu(
        menu_title='Menu',
        options=['Home','Time','Jogador'],  
        icons=['house-fill','people-fill','person-fill']       
        )

if selected == 'Home':
    st.title(f'{selected}')
elif selected == 'Time':
    team_func()
else:
    st.title(f'{selected}')
    
 
