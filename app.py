import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA (FORÇAR TEMA CLARO PARA COMBINAR COM A IMAGEM) ---
st.set_page_config(page_title="Contabiliza AI | Pro", layout="wide")

# --- CSS DEFINITIVO (UI/UX INDUSTRIAL) ---
st.markdown("""
    <style>
    /* Reset de fundo para cinza claro industrial */
    .stApp { background-color: #f0f2f5; }
    
    /* Barra Superior Estilo Dashboard */
    .header-bar {
        background-color: #343a40; padding: 10px 20px;
        display: flex; justify-content: space-between; align-items: center;
        color: white; margin: -60px -100px 20px -100px;
    }

    /* Grid de Cards Coloridos */
    .card-row { display: flex; justify-content: space-between; gap: 10px; margin-bottom: 20px; }
    .card {
        flex: 1; padding: 15px; border-radius: 4px; color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: left;
    }
    .c-blue { background-color: #4da3ff; }
    .c-cyan { background-color: #4bc0c0; }
    .c-orange { background-color: #ff9f40; }
    .c-pink { background-color: #ff6384; }
    
    .card-title { font-size: 14px; opacity: 0.9; margin-bottom: 5px; }
    .card-value { font-size: 24px; font-weight: bold; }

    /* Layout Lateral (Filtros) */
    .filter-box {
        background-color: white; padding: 20px; border-radius: 5px;
        border: 1px solid #ddd; margin-bottom: 20px;
    }

    /* Grid Azul de Status (Lado Esquerdo Inferior) */
    .status-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; background-color: #4da3ff; border: 2px solid #4da3ff; }
    .status-item { background-color: #5dafff; color: white; padding: 15px; text-align: center; border: 1px solid #4da3ff; }
    .status-val { font-size: 28px; font-weight: bold; display: block; }
    .status-lab { font-size: 11px; text-transform: uppercase; }

    /* Esconder elementos chatos do streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SIMULADO ---
st.markdown("""
    <div class="header-bar">
        <span><b>Contabiliza AI</b> | Performance v3.0</span>
        <span>Olá, Dr. Otávio • Unidade São Paulo ⚙️</span>
    </div>
    """, unsafe_allow_html=True)

# --- LAYOUT EM COLUNAS ---
col_sidebar, col_main = st.columns([1, 3])

with col_sidebar:
    st.markdown('<div class="filter-box">', unsafe_allow_html=True)
    st.subheader("DashBoard Performance")
    st.date_input("Início", value=pd.to_datetime("2019-02-01"))
    st.date_input("Fim", value=pd.to_datetime("2020-03-09"))
    st.selectbox("Tipo de Atividade", ["Auditoria 5S", "PIS/COFINS", "Recuperação INSS"])
    st.button("🔄 Aplicar Filtros", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Grid Azul de Performance (Igual à imagem 1)
    st.markdown("""
        <div class="status-grid">
            <div class="status-item"><span class="status-lab">Concluídas</span><span class="status-val">9</span></div>
            <div class="status-item"><span class="status-lab">Menor Pontuação</span><span class="status-val">37</span></div>
            <div class="status-item"><span class="status-lab">Pendentes</span><span class="status-val">1</span></div>
            <div class="status-item"><span class="status-lab">Maior Pontuação</span><span class="status-val">91</span></div>
            <div class="status-item"><span class="status-lab">Canceladas</span><span class="status-val">0</span></div>
            <div class="status-item"><span class="status-lab">Tempo Médio</span><span class="status-val">12d</span></div>
        </div>
    """, unsafe_allow_html=True)

with col_main:
    # Cards Superiores Coloridos
    st.markdown("""
        <div class="card-row">
            <div class="card c-blue"><div class="card-title">Nota Média</div><div class="card-value">65,44</div></div>
            <div class="card c-cyan"><div class="card-title">Atividades Totais</div><div class="card-value">10</div></div>
            <div class="card c-orange"><div class="card-title">Comentários</div><div class="card-value">4</div></div>
            <div class="card c-pink"><div class="card-title">Total de Notas</div><div class="card-value">13</div></div>
        </div>
    """, unsafe_allow_html=True)

    # Gráfico de Linhas (Simulando a imagem)
    st.markdown("#### Indicadores Gerais no Período")
    fig = go.Figure()
    datas = ['01-02-19', '08-04-19', '14-06-19', '20-08-19', '26-10-19', '01-01-20', '09-03-20']
    
    fig.add_trace(go.Scatter(x=datas, y=[25, 25, 45, 45, 85, 85, 60], name='Potencial Crédito', line=dict(color='#4da3ff', width=3)))
    fig.add_trace(go.Scatter(x=datas, y=[40, 0, 15, 0, 10, 0, 15], name='Atividades', line=dict(color='#ff6384', width=2)))
    fig.add_trace(go.Scatter(x=datas, y=[10, 0, 10, 0, 10, 0, 5], name='Riscos', line=dict(color='#4bc0c0', width=2)))

    fig.update_layout(
        margin=dict(l=0, r=0, t=20, b=0),
        height=350,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tabela de Oportunidades (Agora renderizando CORRETAMENTE)
    st.markdown("#### 📂 Detalhamento de Oportunidades")
    df_show = pd.DataFrame({
        "Empresa": ["Farmácia Central", "Auto Peças Silva", "Supermercado Ideal", "Clínica de Olhos"],
        "Crédito Identificado": ["R$ 18.500", "R$ 42.300", "R$ 41.000", "R$ 31.900"],
        "Tipo": ["PIS/COFINS", "ICMS-ST", "INSS Patronal", "ISS"],
        "Status": ["Pendente", "Em Análise", "Pendente", "Concluído"]
    })
    st.table(df_show) # Usando a função nativa st.table para evitar erros de HTML
