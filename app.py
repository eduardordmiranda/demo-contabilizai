import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Contabiliza AI | Hub Performance",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS DE ALTA PERFORMANCE (UI/UX) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #F8FAFC;
    }

    /* Removendo padding padrão do Streamlit */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Header Estilizado */
    .main-header {
        background: linear-gradient(90deg, #1E293B 0%, #334155 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Grid de Filtros Lateral */
    .filter-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    /* Cards de Indicadores (Estilo Moderno) */
    .st-emotion-cache-12w0qpk { gap: 1rem; } /* Ajuste de espaçamento de colunas */
    
    .stat-card {
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        transition: transform 0.3s ease;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    .stat-card:hover { transform: translateY(-5px); }
    
    .bg-gradient-blue { background: linear-gradient(135deg, #3B82F6 0%, #1D4ED8 100%); }
    .bg-gradient-cyan { background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%); }
    .bg-gradient-orange { background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%); }
    .bg-gradient-rose { background: linear-gradient(135deg, #F43F5E 0%, #E11D48 100%); }

    /* Painel Azul de Operações (Igual à imagem) */
    .op-panel {
        background-color: #2563EB;
        border-radius: 12px;
        overflow: hidden;
        margin-top: 1rem;
    }
    .op-row { display: flex; border-bottom: 1px solid #3B82F6; }
    .op-col {
        flex: 1;
        padding: 1rem;
        text-align: center;
        color: white;
        border-right: 1px solid #3B82F6;
    }
    .op-col:last-child { border-right: none; }
    .op-val { font-size: 1.5rem; font-weight: 700; display: block; }
    .op-lab { font-size: 0.65rem; text-transform: uppercase; font-weight: 600; opacity: 0.8; }

    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="main-header">
        <div>
            <span style="font-size: 1.2rem; font-weight: 700; letter-spacing: 1px;">CONTABILIZA AI</span>
            <span style="margin-left: 10px; opacity: 0.6; font-size: 0.9rem;">| Performance Dashboard v3.0</span>
        </div>
        <div style="text-align: right;">
            <span style="font-size: 0.8rem; opacity: 0.8;">Qualidade Aplicada Ltda.</span><br>
            <span style="font-weight: 600;">Dr. Otávio Silveira</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CORPO PRINCIPAL ---
col_side, col_main = st.columns([1, 3.5])

with col_side:
    st.markdown('<div class="filter-card">', unsafe_allow_html=True)
    st.markdown("### 🛠️ Configurações")
    periodo = st.date_input("Período de Análise", [datetime(2024, 1, 1), datetime(2026, 2, 9)])
    atividade = st.selectbox("Módulo de IA", ["Auditoria Fiscal", "Recuperação Previdenciária", "Automação de Folha"])
    st.button("Aplicar Filtros Inteligentes", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Painel de Status Operacional
    st.markdown("""
        <div class="op-panel">
            <div class="op-row">
                <div class="op-col"><span class="op-lab">Concluídas</span><span class="op-val">124</span></div>
                <div class="op-col"><span class="op-lab">Pendentes</span><span class="op-val">12</span></div>
            </div>
            <div class="op-row">
                <div class="op-col"><span class="op-lab">Menor Pont.</span><span class="op-val">42</span></div>
                <div class="op-col"><span class="op-lab">Maior Pont.</span><span class="op-val">98</span></div>
            </div>
            <div class="op-row" style="border-bottom: none;">
                <div class="op-col"><span class="op-lab">Eficiência</span><span class="op-val">94%</span></div>
                <div class="op-col"><span class="op-lab">Tempo Médio</span><span class="op-val">3d</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_main:
    # Cards Superiores Coloridos
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="stat-card bg-gradient-blue"><h4>Nota Média</h4><h2>84,2</h2></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card bg-gradient-cyan"><h4>Crédito Total</h4><h2>R$ 420k</h2></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card bg-gradient-orange"><h4>Empresas</h4><h2>42</h2></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="stat-card bg-gradient-rose"><h4>Riscos</h4><h2>3</h2></div>', unsafe_allow_html=True)

    # Gráfico Principal
    st.markdown("<br>#### 📈 Tendência de Recuperação vs. Auditoria", unsafe_allow_html=True)
    
    # Criando gráfico Plotly profissional
    fig = go.Figure()
    datas = ['Jan/25', 'Fev/25', 'Mar/25', 'Abr/25', 'Mai/25', 'Jun/25']
    fig.add_trace(go.Scatter(x=datas, y=[10, 25, 40, 35, 60, 90], mode='lines+markers', name='Créditos (R$)', 
                             line=dict(color='#3B82F6', width=4), marker=dict(size=8)))
    fig.add_trace(go.Bar(x=datas, y=[5, 15, 10, 20, 15, 25], name='Riscos Detectados', marker_color='#F43F5E', opacity=0.3))

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0),
        height=320,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#E2E8F0')
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # Tabela de Dados Estilizada
    st.markdown("#### 📂 Oportunidades por Cliente")
    df = pd.DataFrame({
        "Cliente": ["Farmácia Santo Antônio", "Mecânica Diesel Pro", "Supermercado Real", "Clínica Bem Estar"],
        "Crédito Identificado": ["R$ 24.500,00", "R$ 42.100,00", "R$ 156.900,00", "R$ 12.400,00"],
        "Status": ["Auditado ✅", "Aguardando e-CAC ⏳", "Pendente ❌", "Concluído ✅"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Contabiliza AI © 2026 - Tecnologia Propriatária de Inteligência Fiscal em Nuvem.")
