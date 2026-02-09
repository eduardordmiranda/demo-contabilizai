import streamlit as st
import pandas as pd
import time

# --- CONFIGURAÇÃO VISUAL PREMIUM ---
st.set_page_config(page_title="Contabiliza AI | Portal do Contador", layout="wide", initial_sidebar_state="collapsed")

# CSS para injetar um design mais limpo e moderno
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #1E3A8A; font-weight: 700; }
    div[data-testid="stMetricDelta"] { font-size: 1rem; }
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 3em; 
        background-color: #1E3A8A; color: white; border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #3b82f6; border: none; color: white; transform: translateY(-2px); }
    .card {
        padding: 20px; border-radius: 12px; background-color: white;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADO DE NAVEGAÇÃO ---
if 'page' not in st.session_state: st.session_state.page = 'home'
if 'empresa' not in st.session_state: st.session_state.empresa = None

# --- BANCO DE DADOS DA DEMO ---
dados = pd.DataFrame([
    {"Empresa": "Farmácia Central Ltda", "Credito": 18500.00, "Origem": "PIS/COFINS Monofásico", "Risco": "Baixo"},
    {"Empresa": "Auto Peças Silva", "Credito": 42300.50, "Origem": "ICMS-ST", "Risco": "Baixo"},
    {"Empresa": "Restaurante Bom Gosto", "Credito": 12100.00, "Origem": "Simples Nacional", "Risco": "Médio"},
    {"Empresa": "Supermercado Ideal", "Credito": 156000.00, "Origem": "Multiverbas", "Risco": "Baixo"},
])

# --- LÓGICA DE TELAS ---

# TELA 1: DASHBOARD DE INDICADORES
if st.session_state.page == 'home':
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=60)
    st.title("Contabiliza AI")
    st.subheader("Hub de Inteligência e Auditoria Fiscal")
    
    st.markdown("---")
    
    # KPIs Superiores
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Identificado", f"R$ {dados['Credito'].sum():,.2f}", "+R$ 12k este mês")
    with c2:
        st.metric("Empresas na Carteira", "142", "8 novas")
    with c3:
        st.metric("Auditorias Pendentes", "14", "-3", delta_color="inverse")
    with c4:
        st.metric("Honorários Estimados (20%)", f"R$ {(dados['Credito'].sum()*0.2):,.2f}", "Cash-in")

    st.markdown("### 🎯 Oportunidades Prontas para Prospecção")
    
    # Criando os cards de clientes
    for idx, row in dados.iterrows():
        with st.container():
            col_a, col_b, col_c, col_d = st.columns([2, 1, 1, 1])
            with col_a:
                st.markdown(f"#### {row['Empresa']}")
                st.caption(f"Origem: {row['Origem']}")
            with col_b:
                st.markdown(f"**Crédito:** \n<span style='color:green; font-size:1.2rem'>R$ {row['Credito']:,.2f}</span>", unsafe_allow_html=True)
            with col_c:
                st.markdown(f"**Risco:** \n{row['Risco']}", unsafe_allow_html=True)
            with col_d:
                if st.button("Abrir Painel", key=f"btn_{idx}"):
                    st.session_state.empresa = row['Empresa']
                    st.session_state.page = 'detalhes'
                    st.rerun()
            st.markdown("---")

# TELA 2: DETALHES DO CLIENTE E PROSPECÇÃO
elif st.session_state.page == 'detalhes':
    emp = st.session_state.empresa
    info = dados[dados['Empresa'] == emp].iloc[0]

    if st.button("⬅️ Voltar para a Lista"):
        st.session_state.page = 'home'
        st.rerun()

    st.title(f"Detalhamento: {emp}")
    
    col_l, col_r = st.columns([2, 1])
    
    with col_l:
        st.markdown(f"""
        <div class="card">
            <h3>Relatório Técnico de Auditoria</h3>
            <p>A inteligência artificial analisou os arquivos <b>XML e e-CAC</b> dos últimos 60 meses.</p>
            <ul>
                <li><b>Inconsistência detectada:</b> Pagamento integral de PIS/COFINS em produtos monofásicos.</li>
                <li><b>Base Legal:</b> Lei 10.147/00 e Soluções de Consulta COSIT.</li>
                <li><b>Documentos analisados:</b> 4.280 notas fiscais de saída.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.warning("⚠️ **Nota:** A recuperação pode ser feita via compensação administrativa imediata no PGDAS-D.")

    with col_r:
        st.markdown(f"""
        <div style="background-color: #1E3A8A; color: white; padding: 25px; border-radius: 12px; text-align: center;">
            <p style="margin-bottom: 0;">VALOR RECUPERÁVEL</p>
            <h2 style="color: #4ade80; margin-top: 0;">R$ {info['Credito']:,.2f}</h2>
            <hr>
            <p>Seus Honorários (20%)</p>
            <h3>R$ {(info['Credito']*0.2):,.2f}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # Espaçador
        if st.button("🚀 INICIAR PROSPECÇÃO AUTOMÁTICA"):
            with st.spinner("IA Contabiliza está gerando a proposta..."):
                time.sleep(2)
                st.success("Proposta enviada para o WhatsApp do cliente!")
                st.balloons()
                st.chat_message("assistant").write(f"**Mensagem enviada:** 'Olá, notamos que a {emp} pagou impostos a maior em itens de {info['Origem']}. Temos R$ {info['Credito']:,.2f} para recuperar. Podemos falar?'")
