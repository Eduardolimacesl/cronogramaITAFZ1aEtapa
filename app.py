import pandas as pd
import plotly.express as px
from datetime import datetime, date
import streamlit as st

# Dados fornecidos
data = {
    "idProject": [
        "ITAFZ-01", "ITAFZ-02", "ITAFZ-09", "ITAFZ-09", "ITAFZ-09", "ITAFZ-10", "ITAFZ-10",
        "ITAFZ-10", "ITAFZ-11", "ITAFZ-11", "ITAFZ-11", "ITAFZ-12", "ITAFZ-12", "ITAFZ-12",
        "ITAFZ-05", "ITAFZ-05", "ITAFZ-04", "ITAFZ-04", "ITAFZ-06", "ITAFZ-06", "ITAFZ-07",
        "ITAFZ-07", "ITAFZ-08", "ITAFZ-08", "ITAFZ-03", "ITAFZ-03"
    ],
    "Projeto": [
        "Prédio das Engenharias (Módulo 1)", "Alojamento 1", "Rede de Esgoto", "Rede de Esgoto", "Rede de Esgoto",
        "Rede de Água", "Rede de Água", "Rede de Água", "Rede Elétrica/Dados/Iluminação (Etapa 1)",
        "Rede Elétrica/Dados/Iluminação (Etapa 1)", "Rede Elétrica/Dados/Iluminação (Etapa 1)",
        "Pavimentação e Drenagem (Etapa 1)", "Pavimentação e Drenagem (Etapa 1)", "Pavimentação e Drenagem (Etapa 1)",
        "E-002 (Prédio Administrativo/Acadêmico)", "E-002 (Prédio Administrativo/Acadêmico)",
        "E-065 (Apoio SOP-CE e CO-ITACE)", "E-065 (Apoio SOP-CE e CO-ITACE)", "E-023 (Hotel de Trânsito Nível Superior)",
        "E-023 (Hotel de Trânsito Nível Superior)", "E-018 (Rancho)", "E-018 (Rancho)", "E-008, 009 e 010 (Grupo de Saúde)",
        "E-008, 009 e 010 (Grupo de Saúde)", "Recuperação de Coberturas do Plano de Transição",
        "Recuperação de Coberturas do Plano de Transição"
    ],
    "Prioridade": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
    ],
    "CustoPrevisto": [
        "R$ 59.951.740,53", "R$ 10.948.259,47", None, "R$ 11.529.165,48", None, None, "R$ 10.360.837,11", None,
        None, "R$ 12.280.435,29", None, None, "R$ 20.559.225,62", None, None, "R$ 5.675.987,37", None,
        "R$ 1.170.789,47", None, None, "R$ 6.842.093,68", None, "R$ 6.110.467,34", None, "R$ 6.673.500,00",
        None, "R$ 23.004.946,09", None
    ],
    "Etapa": [
        "Obra", "Obra", "Licitação", "Obra ITA-FZ", "Obra BAFZ", "Licitação", "Obra ITA-FZ", "Obra BAFZ",
        "Licitação", "Obra ITA-FZ", "Obra BAFZ", "Licitação", "Obra ITA-FZ", "Obra BAFZ", "Licitação",
        "Obra ITA-FZ", "Licitação", "Obra ITA-FZ", "Licitação", "Obra", "Licitação", "Obra",
        "Licitação", "Obra", "Licitação", "Obra"
    ],
    "Prazo": [
        540, 540, 150, 180, 270, 150, 180, 270, 150, 180, 270, 150, 324, 216, 150, 360,
        150, 90, 150, 360, 150, 360, 150, 360, 150, 360
    ],
    "Data Início": [
        "01/11/2024", "01/11/2024", "10/01/2025", "12/06/2025", "09/12/2025", "10/01/2025",
        "12/06/2025", "09/12/2025", "10/01/2025", "12/06/2025", "09/12/2025", "10/01/2025",
        "12/06/2025", "02/05/2026", "10/01/2025", "12/06/2025", "10/01/2025", "12/06/2025",
        "10/01/2025", "10/09/2025", "10/01/2025", "07/02/2026", "10/01/2025", "07/02/2026",
        "10/01/2025", "07/02/2026"
    ],
    "Data Término": [
        "25/04/2026", "25/04/2026", "12/06/2025", "09/12/2025", "05/09/2026", "12/06/2025",
        "09/12/2025", "05/09/2026", "12/06/2025", "09/12/2025", "05/09/2026", "12/06/2025",
        "02/05/2026", "04/12/2026", "12/06/2025", "07/06/2026", "12/06/2025", "10/09/2025",
        "12/06/2025", "05/09/2026", "12/06/2025", "02/02/2027", "12/06/2025", "02/02/2027",
        "12/06/2025", "02/02/2027"
    ],
    "Status": [
        "Em Obras", "Em Obras", "Em andamento", "Fase ITA", "Fase BAFZ", "Em andamento", "Fase ITA",
        "Fase BAFZ", "Em andamento", "Fase ITA", "Fase BAFZ", "Em andamento", "Fase ITA",
        "Fase BAFZ", "Em andamento", "Fase ITA", "Em andamento", "Fase ITA", "Em andamento",
        "Aguardando Licitação", "Em andamento", "Aguardando Licitação", "Em andamento",
        "Aguardando Licitação", "Em andamento", "Aguardando Licitação"
    ]
}

# Replace empty strings with None to represent missing values
for key in data:
    data[key] = [None if value == '' else value for value in data[key]]

# Padronizar o comprimento das colunas antes de criar o DataFrame
max_len = max(len(value) for value in data.values())  # Encontrar o comprimento máximo
for key in data:
    if len(data[key]) < max_len:
        data[key] += [None] * (max_len - len(data[key]))  # Preencher com None para igualar o comprimento

df = pd.DataFrame(data)

df['Data Início'] = pd.to_datetime(df['Data Início'], format='%d/%m/%Y')
df['Data Término'] = pd.to_datetime(df['Data Término'], format='%d/%m/%Y', errors='coerce')  # Lida com valores inválidos
df = df.sort_values(by="Prioridade", ascending=True) # Ordenação decrescente de prioridade

# Ordenar os projetos no gráfico pela prioridade decrescente
ordered_projects = df.drop_duplicates(subset=['Projeto'], keep='first').sort_values(by="Prioridade", ascending=False)['Projeto']

# Configurações do eixo x para mostrar todos os meses
x_axis_config = dict(
    tickmode='linear',
    dtick='M1',
    tickformat="%b %Y"
)

# Adicionar a linha vermelha para o dia atual
hoje = date.today() # Get today's date as a datetime.date object
hoje_datetime = datetime.combine(hoje, datetime.min.time()).timestamp() * 1000
inicio_aulas = datetime(2027, 3, 3).timestamp() * 1000
credenciamento = datetime(2026, 5, 3).timestamp() * 1000

fig = px.timeline(df, x_start="Data Início", x_end="Data Término", y="Projeto", color="Etapa", text="Etapa", title="ITA-FZ 1a FASE")

fig.add_vline(x=hoje_datetime, line_width=2, line_dash="longdashdot", line_color="red", annotation_text="Hoje", annotation_position="top")
fig.add_vline(x=inicio_aulas, line_width=2, line_dash="longdashdot", line_color="red", annotation_text="Aulas", annotation_position="top")
fig.add_vline(x=credenciamento, line_width=2, line_dash="longdashdot", line_color="red", annotation_text="Credenciamento", annotation_position="top")

fig.update_yaxes(categoryorder="array", categoryarray=ordered_projects)
#Para alinhar o texto da faixa à esquerda
fig.update_traces(textposition='inside', insidetextanchor='start')

fig.update_layout(
    title={
        'text': "ITA-FZ 1ª FASE",
        'y':0.95,
        'yanchor': 'top',
        'font': dict( size=24, color="Black", family="Arial", weight="bold")
    },
    xaxis=x_axis_config,
    yaxis_title="Projetos",
    showlegend=False,
)

fig.show()

st.plotly_chart(fig)