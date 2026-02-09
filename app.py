import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# --- CONFIGURAÇÃO DE ALTA PERFORMANCE ---
st.set_page_config(page_title="Contabiliza AI | Performance Real", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: DESIGN DE ELITE COM FOCO NOS DADOS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #F1F3F6; color: #333; }
    header {visibility: hidden;}
    
    /* Grid de Cards Superiores (Cores da Imagem) */
    .card-row { display: flex; gap: 8px; margin-bottom: 15px; }
    .card { flex: 1; padding: 20px; color: white; border-radius: 4px; position: relative; min-height: 120px; }
    .c-blue { background-color: #4A90E2; }
    .c-cyan { background-color: #48C0C0; }
    .c-orange { background-color: #F7943D; }
    .c-pink { background-color: #F26685; }
    
    .card-label { font-size: 14px; opacity: 0.9; font-weight: 600; }
    .card-value { font-size: 38px; font-weight: 800; display: block; margin-top: 5px; }

    /* Painel Lateral Azul (Performance) */
    .perf-panel { background-color: #4A90E2; color: white; border-radius: 4px; overflow: hidden; }
    .perf-table { width: 100%; border-collapse: collapse; }
    .perf-table td { border: 1px solid rgba(255,255,255,0.2); padding: 15px; text-align: center; width: 50%; }
    .perf-label { font-size: 10px; text-transform: uppercase; display: block; opacity: 0.8; margin-bottom: 5px; }
    .perf-val { font-size: 24px; font-weight: 700; }

    /* Estilo Filtros */
    .filter-card { background: white; padding: 20px; border-radius: 4px; border: 1px solid #DFE3E8; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
if 'view' not in st.session_state: st.session_state.view = 'main'

# --- LAYOUT ---
col_side, col_main = st.columns([1, 3.2])

with col_side:
    # Quadrado de Filtros
    st.markdown('<div class="filter-card">', unsafe_allow_html=True)
    st.markdown("#### DashBoard Performance")
    st.caption("Período:")
    st.code("01/02/2019\n09/03/2020")
    st.selectbox("Tipo de Atividade:", ["5s Auditorias", "Recuperação Tributária"])
    st.button("🔍 Aplicar Filtros", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Painel de Status Azul (Fiel à Imagem)
    st.markdown("""
        <div class="perf-panel">
            <table class="perf-table">
                <tr>
                    <td><span class="perf-label">Atividades Concluídas</span><span class="perf-val">9</span></td>
                    <td><span class="perf-label">Menor Pontuação</span><span class="perf-val">37</span></td>
                </tr>
                <tr>
                    <td><span class="perf-label">Atividades Pendentes</span><span class="perf-val">1</span></td>
                    <td><span class="perf-label">Maior Pontuação</span><span class="perf-val">91</span></td>
                </tr>
                <tr>
                    <td><span class="perf-label">Atividades Canceladas</span><span class="perf-val">0</span></td>
                    <td><span class="perf-label">Tempo Médio (Dias)</span><span class="perf-val">12</span></td>
                </tr>
                <tr>
                    <td><span class="perf-label">Na Média</span><span class="perf-val">5</span></td>
                    <td><span class="perf-label">Desvio Padrão</span><span class="perf-val">19,36</span></td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)

with col_main:
    # Top Cards com Indicadores EXATOS da sua imagem
    st.markdown("""
        <div class="card-row">
            <div class="card c-blue"><span class="card-label">Nota Média</span><span class="card-value">65,44</span></div>
            <div class="card c-cyan"><span class="card-label">Atividades Totais</span><span class="card-value">10</span></div>
            <div class="card c-orange"><span class="card-label">Comentários</span><span class="card-value">4</span></div>
            <div class="card c-pink"><span class="card-label">Total de Notas/Fotos</span><span class="card-value">13</span></div>
        </div>
    """, unsafe_allow_html=True)

    # Gráfico de Linhas Profissional
    st.markdown("<p style='text-align:center; color:#666; font-size:12px;'>Indicadores Gerais no Período: 01/02/2019 - 09/03/2020</p>", unsafe_allow_html=True)
    
    fig = go.Figure()
    dates = ['01-02-19', '08-04-19', '14-06-19', '20-08-19', '26-10-19', '01-01-20', '09-03-20']
    
    # Linha Azul (Principal)
    fig.add_trace(go.Scatter(x=dates, y=[30, 28, 48, 48, 85, 85, 62], mode='lines+markers', name='Performance', line=dict(color='#4A90E2', width=3)))
    # Linha Rosa
    fig.add_trace(go.Scatter(x=dates, y=[42, 0, 18, 0, 10, 0, 18], mode='lines+markers', name='Atividades', line=dict(color='#F26685', width=2)))
    # Linha Laranja
    fig.add_trace(go.Scatter(x=dates, y=[10, 0, 12, 0, 12, 0, 8], mode='lines+markers', name='Créditos', line=dict(color='#F7943D', width=2)))

    fig.update_layout(
        margin=dict(l=0, r=0, t=10, b=0), height=350,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tabela de Oportunidades
    st.markdown("#### 🚀 Oportunidades de Recuperação (Análise IA)")
    df = pd.DataFrame({
        "Empresa": ["Farmácia Santo Antônio", "Mecânica Diesel Pro", "Supermercado Real"],
        "Crédito Identificado": ["R$ 24.500", "R$ 42.100", "R$ 156.900"],
        "Status": ["Pendente", "Em Análise", "Pendente"]
    })
    
    # Renderizando a tabela e o botão de prospecção
    for i, row in df.iterrows():
        c1, c2, c3, c4 = st.columns([2, 1, 1, 1.5])
        c1.write(f"**{row['Empresa']}**")
        c2.write(row['Crédito Identificado'])
        c3.write(row['Status'])
        if c4.button(f"Prospectar {row['Empresa']}", key=f"p_{i}"):
            with st.spinner("IA gerando abordagem humanizada..."):
                time.sleep(2)
                st.toast(f"Proposta enviada para {row['Empresa']}!")
                st.success(f"A IA enviou uma imagem de impacto real para o cliente via WhatsApp.")
        st.divider()
