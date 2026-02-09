import streamlit as st
import pandas as pd
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Contabiliza AI | Hub", layout="wide", initial_sidebar_state="collapsed")

# --- CONTROLE DE NAVEGAÇÃO (Session State) ---
if 'view' not in st.session_state: st.session_state.view = 'dashboard'
if 'selected_client' not in st.session_state: st.session_state.selected_client = None

# --- DATABASE SIMULADO ---
clients_db = [
    {"nome": "Farmácia Santo Antônio", "credito": 24500, "detalhes": "Recuperação de PIS/COFINS Monofásico em medicamentos.", "oportunidade": "Redução de 12% no DAS mensal."},
    {"nome": "Mecânica Diesel Pro", "credito": 42100, "detalhes": "Créditos de ICMS-ST sobre autopeças.", "oportunidade": "Recuperação retroativa de 60 meses."},
    {"nome": "Supermercado Real", "credito": 156900, "detalhes": "Exclusão do ICMS da base do PIS/COFINS.", "oportunidade": "Geração de caixa imediata via compensação."},
]

# --- CSS CUSTOMIZADO ---
st.markdown("""
    <style>
    .stat-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        padding: 20px; border-radius: 12px; color: white; cursor: pointer;
        transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stat-card:hover { transform: translateY(-5px); background: #2563EB; }
    .client-card {
        background: white; padding: 15px; border-radius: 8px;
        margin-bottom: 10px; border-left: 5px solid #2563EB;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE TELAS ---

# 1. TELA DE DASHBOARD PRINCIPAL
if st.session_state.view == 'dashboard':
    st.title("🤖 Contabiliza AI | Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stat-card"><h4>Crédito Total</h4><h2>R$ 223.500</h2><p>Ver Clientes →</p></div>', unsafe_allow_html=True)
        if st.button("Abrir Lista de Créditos", use_container_width=True):
            st.session_state.view = 'client_list'
            st.rerun()
            
    # Outros indicadores (apenas visuais)
    with col2: st.markdown('<div class="stat-card"><h4>Empresas</h4><h2>3</h2><p>Ativas</p></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="stat-card"><h4>Riscos</h4><h2>Baixo</h2><p>Auditado</p></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="stat-card"><h4>Eficiência IA</h4><h2>94%</h2><p>Automação</p></div>', unsafe_allow_html=True)

# 2. TELA DE LISTA DE CLIENTES
elif st.session_state.view == 'client_list':
    if st.button("← Voltar ao Dashboard"):
        st.session_state.view = 'dashboard'
        st.rerun()
        
    st.subheader("🏦 Clientes com Créditos Identificados")
    st.write("Selecione um cliente para ver a oferta e prospectar.")
    
    for client in clients_db:
        with st.container():
            c1, c2, c3 = st.columns([2, 1, 1])
            c1.markdown(f"### {client['nome']}")
            c2.markdown(f"**Crédito:** R$ {client['credito']:,}")
            if c3.button(f"Analisar Oportunidade", key=client['nome']):
                st.session_state.selected_client = client
                st.session_state.view = 'prospect'
                st.rerun()
            st.markdown("---")

# 3. TELA DE DETALHES E PROSPECÇÃO IA
elif st.session_state.view == 'prospect':
    client = st.session_state.selected_client
    
    if st.button("← Voltar para Lista"):
        st.session_state.view = 'client_list'
        st.rerun()
        
    st.title(f"💼 Estratégia: {client['nome']}")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.info(f"**O que a IA identificou:**\n\n{client['detalhes']}")
        st.success(f"**Oferta Sugerida:**\n\n{client['oportunidade']}")
        
    with col_right:
        st.markdown("### 🚀 Prospecção Inteligente")
        st.write("A IA irá criar uma abordagem realista e humanizada para o WhatsApp do cliente.")
        
        if st.button("Gerar Prospecção e Enviar"):
            with st.status("IA criando imagem realista da oportunidade...", expanded=True) as status:
                time.sleep(2)
                st.write("Simulando impacto financeiro no fluxo de caixa...")
                time.sleep(2)
                st.write("Redigindo texto humanizado (Sem cara de bot)...")
                status.update(label="Prospecção Enviada!", state="complete", expanded=False)
            
            st.balloons()
            
            # SIMULAÇÃO DA MENSAGEM DA IA
            st.chat_message("assistant").write(f"""
                **Mensagem enviada para o cliente (via Contabilidade):**
                
                "Olá, Diretor da {client['nome']}. Tudo bem? 
                
                Estávamos revisando sua operação aqui na contabilidade com nossa nova ferramenta de auditoria e encontramos uma oportunidade real de recuperação de impostos (PIS/COFINS). 
                
                O valor identificado é de **R$ {client['credito']:,}**. Conseguimos usar isso para abater seus próximos impostos sem burocracia. 
                
                Fizemos um estudo rápido (veja o gráfico anexo) de como seu caixa ficaria com esse fôlego extra. Podemos agendar 5 min amanhã?"
            """)
            st.image("https://img.freepik.com/fotos-gratis/homem-negocios-analisando-graficos-financeiros-em-escritorio-moderno_23-2148835920.jpg", caption="Imagem gerada pela IA para ilustrar o ganho de capital ao cliente.")
