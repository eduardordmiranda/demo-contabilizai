import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Contabiliza AI | Hub de Inteligência", layout="wide", initial_sidebar_state="collapsed")

# --- CSS AVANÇADO PARA VISUAL PROFISSIONAL (UI/UX) ---
st.markdown("""
    <style>
    /* Importando fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"]  { font-family: 'Inter', sans-serif; background-color: #F3F4F6; }
    
    /* Esconder elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Estilização dos Cards */
    .metric-card {
        background-color: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #E5E7EB;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #2563EB;
    }
    .metric-title { color: #6B7280; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.025em; }
    .metric-value { color: #111827; font-size: 1.875rem; font-weight: 700; margin-top: 8px; }
    .metric-delta { font-size: 0.875rem; margin-top: 4px; font-weight: 500; }
    .delta-positive { color: #10B981; }
    
    /* Botões Customizados */
    .stButton>button {
        background-color: #2563EB; color: white; border-radius: 8px;
        border: none; padding: 12px 24px; font-weight: 600; width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover { background-color: #1E40AF; color: white; box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO DO HUB ---
st.markdown("""
    <div style='display: flex; align-items: center; margin-bottom: 30px;'>
        <div style='background-color: #2563EB; padding: 10px; border-radius: 12px; margin-right: 15px;'>
            <img src='https://img.icons8.com/ios-filled/50/ffffff/artificial-intelligence.png' width='30'/>
        </div>
        <div>
            <h1 style='margin:0; color: #111827; font-size: 24px;'>Contabiliza AI - Hub</h1>
            <p style='margin:0; color: #6B7280;'>Sistema de Gestão Inteligente 360°</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- GRID DE INDICADORES PRINCIPAIS (BOXES) ---
st.markdown("### 🚀 Visão Geral de Oportunidades")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""<div class="metric-card">
        <div class="metric-title">Créditos Recuperáveis</div>
        <div class="metric-value">R$ 284.900</div>
        <div class="metric-delta delta-positive">↑ 12% em relação ao mês anterior</div>
    </div>""", unsafe_allow_html=True)
    if st.button("Ver Auditoria", key="aud"): st.toast("Carregando Auditoria...")

with c2:
    st.markdown("""<div class="metric-card">
        <div class="metric-title">Eficiência Operacional</div>
        <div class="metric-value">94.2%</div>
        <div class="metric-delta delta-positive">Aumento de +40h livres/mês</div>
    </div>""", unsafe_allow_html=True)
    if st.button("Ver Operação", key="ope"): st.toast("Abrindo Módulo de Automação...")

with c3:
    st.markdown("""<div class="metric-card">
        <div class="metric-title">Risco Fiscal Ativo</div>
        <div class="metric-value">4 Pendências</div>
        <div class="metric-delta" style='color:#EF4444'>Ação imediata recomendada</div>
    </div>""", unsafe_allow_html=True)
    if st.button("Ver Compliance", key="com"): st.toast("Acessando e-CAC...")

with c4:
    st.markdown("""<div class="metric-card">
        <div class="metric-title">Atendimento IA</div>
        <div class="metric-value">1.240</div>
        <div class="metric-delta delta-positive">Tickets resolvidos sem humanos</div>
    </div>""", unsafe_allow_html=True)
    if st.button("Ver Chatbot", key="cha"): st.toast("Abrindo Logs de Atendimento...")

st.markdown("<br>", unsafe_allow_html=True)

# --- SEÇÃO DE MÓDULOS 360° ---
st.markdown("### 🛠️ Módulos de Execução")
m1, m2 = st.columns(2)

with m1:
    with st.expander("📂 **AUDITORIA E RECUPERAÇÃO (Tributário)**", expanded=True):
        st.write("Análise profunda de XMLs e cruzamento com e-CAC.")
        st.checkbox("PIS/COFINS Monofásico (Segregação Automática)")
        st.checkbox("Verbas Indenizatórias (INSS Patronal)")
        st.checkbox("Exclusão do ICMS da base do PIS/COFINS")
        st.button("⚙️ Configurar Regras de Auditoria")

with m2:
    with st.expander("🤖 **OPERAÇÃO E BPO (Automação)**", expanded=True):
        st.write("Trabalho braçal executado pela Engine em Dallas.")
        st.checkbox("Captura Automática SEFAZ (Certificado A1)")
        st.checkbox("Fechamento de Folha via eSocial")
        st.checkbox("Conciliação Bancária via IA (NLP)")
        st.button("⚡ Executar Fechamento Massivo")

m3, m4 = st.columns(2)

with m3:
    with st.expander("📈 **CONSULTORIA E ESTRATÉGIA**", expanded=True):
        st.write("Transforme o contador em um conselheiro.")
        st.info("Simulador de Reforma Tributária disponível (Cálculo IBS/CBS)")
        st.write("Dashboards de rentabilidade por cliente.")
        st.button("📊 Gerar Relatório Consultivo")

with m4:
    with st.expander("💬 **HUB DE COMUNICAÇÃO (White Label)**", expanded=True):
        st.write("Seu escritório disponível 24/7.")
        st.write("WhatsApp Business API com IA integrada.")
        st.write("Envio automático de guias e notificações.")
        st.button("📱 Configurar WhatsApp")
