import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Contabiliza AI | Performance", layout="wide", initial_sidebar_state="expanded")

# --- CSS PARA DESIGN INDUSTRIAL (IGUAL À IMAGEM) ---
st.markdown("""
    <style>
    /* Estilo do Fundo e Barra Lateral */
    .main { background-color: #f4f6f9; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #dee2e6; }
    
    /* Títulos e Textos */
    h1, h2, h3 { color: #343a40; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }

    /* Estilização dos Cards Coloridos */
    .card-container { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
    .card {
        flex: 1; min-width: 200px; padding: 20px; border-radius: 4px;
        color: white; position: relative; overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .card h4 { margin: 0; font-size: 0.9rem; opacity: 0.9; font-weight: 400; }
    .card h2 { margin: 10px 0; font-size: 1.8rem; color: white; font-weight: 700; }
    .card .icon { position: absolute; right: 10px; bottom: 10px; opacity: 0.2; font-size: 3rem; }

    /* Cores dos Cards */
    .bg-blue { background-color: #007bff; }
    .bg-orange { background-color: #fd7e14; }
    .bg-green { background-color: #28a745; }
    .bg-cyan { background-color: #17a2b8; }
    .bg-red { background-color: #dc3545; }

    /* Tabela Customizada */
    .styled-table { width: 100%; border-collapse: collapse; background: white; border-radius: 8px; overflow: hidden; }
    .styled-table thead tr { background-color: #e9ecef; color: #495057; text-align: left; }
    .styled-table th, .styled-table td { padding: 12px 15px; border-bottom: 1px solid #dee2e6; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (FILTROS) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/48/artificial-intelligence.png", width=50)
    st.title("Filtros")
    st.date_input("Período", value=pd.to_datetime("2026-01-01"))
    st.selectbox("Tipo de Atividade", ["Consultivo", "Operacional", "Auditoria"])
    st.multiselect("Status", ["Pendente", "Em Análise", "Concluído"], default=["Pendente", "Em Análise"])
    st.button("🚀 Aplicar Filtros")
    st.markdown("---")
    st.caption("Logado como: Dr. Otávio (Sócio)")

# --- ÁREA PRINCIPAL ---
st.markdown("## Dashboard Gerencial")
st.caption("Qualidade Aplicada Ltda.")

# --- LINHA DE CARDS COLORIDOS ---
st.markdown(f"""
    <div class="card-container">
        <div class="card bg-blue">
            <h4>Potential de Crédito</h4>
            <h2>R$ 325.800</h2>
            <div class="icon">💰</div>
        </div>
        <div class="card bg-orange">
            <h4>Conversão</h4>
            <h2>91.5%</h2>
            <div class="icon">📈</div>
        </div>
        <div class="card bg-green">
            <h4>Eficiência Automação</h4>
            <h2>91.5%</h2>
            <div class="icon">🤖</div>
        </div>
        <div class="card bg-cyan">
            <h4>Alertas de Risco</h4>
            <h2>7</h2>
            <div class="icon">⚠️</div>
        </div>
        <div class="card bg-red">
            <h4>Alertas Ativos</h4>
            <h2>1844</h2>
            <div class="icon">🔔</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SEÇÃO DE TABELA (OPORTUNIDADES DETALHADAS) ---
st.markdown("### 📊 Oportunidades de Recuperação (Detalhado)")

# Dados simulados
dados_tabela = [
    ["Farmácia Central", "18.500", "PIS/COFINS", "Pendente", "10", "Pendente"],
    ["Auto Peças Silva", "42.300", "ICMS-ST", "Em Análise", "26", "Aguardando"],
    ["Supermercado Ideal", "41.000", "INSS Patronal", "Pendente", "18", "Pendente"],
    ["Clínica de Olhos", "31.900", "ISS/Verbas", "Concluído", "20", "Concluído"],
]

# Construção da tabela em HTML para controle total do design
tabela_html = """
<table class="styled-table">
    <thead>
        <tr>
            <th>Empresa</th>
            <th>Crédito (R$)</th>
            <th>Origem</th>
            <th>Status Auditoria</th>
            <th>Notas</th>
            <th>Status Mensal</th>
        </tr>
    </thead>
    <tbody>
"""

for linha in dados_tabela:
    tabela_html += f"""
        <tr>
            <td><b>{linha[0]}</b></td>
            <td style="color: #28a745; font-weight: bold;">R$ {linha[1]}</td>
            <td>{linha[2]}</td>
            <td><span style="background: #fff3cd; padding: 4px 8px; border-radius: 4px;">{linha[3]}</span></td>
            <td>{linha[4]}</td>
            <td>{linha[5]}</td>
        </tr>
    """

tabela_html += "</tbody></table>"

st.markdown(tabela_html, unsafe_allow_html=True)

# --- BOTÃO DE AÇÃO ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button("📥 Exportar Relatórios de Prospecção (PDF)"):
    st.success("Gerando relatórios detalhados para os 4 clientes...")
