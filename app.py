import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import time

# --- CONFIGURAÇÃO DE ELITE ---
st.set_page_config(page_title="Contabiliza AI | Enterprise", layout="wide", initial_sidebar_state="collapsed")

# --- DATABASE DE ALTA PERFORMANCE ---
if 'db' not in st.session_state:
    st.session_state.db = pd.DataFrame([
        {"id": 1, "empresa": "Indústrias Delta S.A", "credito": 854200.00, "origem": "Exclusão ICMS/PIS/COFINS", "status": "Oportunidade Crítica", "risco": "Mínimo", "cor": "#3b82f6"},
        {"id": 2, "empresa": "Varejo Global Ltda", "credito": 312500.00, "origem": "PIS/COFINS Monofásico", "status": "Auditoria Concluída", "risco": "Baixo", "cor": "#10b981"},
        {"id": 3, "empresa": "Tech Solutions SP", "credito": 125800.00, "origem": "INSS Verbas Indenizatórias", "status": "Pendente", "risco": "Mínimo", "cor": "#f59e0b"}
    ])

# --- CONTROLE DE ESTADOS ---
if 'screen' not in st.session_state: st.session_state.screen = 'dash'
if 'active_id' not in st.session_state: st.session_state.active_id = None

# --- CSS: O DESIGN DO UNICÓRNIO ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #0B0E14; color: #E2E8F0; }
    
    /* Remover Topo do Streamlit */
    header {visibility: hidden;}
    .block-container {padding-top: 2rem;}

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        transition: all 0.4s ease;
    }
    .glass-card:hover { border: 1px solid #3b82f6; box-shadow: 0 0 30px rgba(59, 130, 246, 0.2); transform: translateY(-5px); }

    /* Indicadores Estilizados */
    .metric-val { font-size: 32px; font-weight: 800; color: #fff; letter-spacing: -1px; }
    .metric-label { font-size: 14px; color: #94A3B8; text-transform: uppercase; font-weight: 600; }

    /* Botão Unicórnio */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white; border: none; border-radius: 12px;
        padding: 15px 30px; font-weight: 700; width: 100%;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover { box-shadow: 0 10px 20px rgba(37, 99, 235, 0.4); transform: scale(1.02); }

    /* Tabela de Luxo */
    .luxury-row {
        display: flex; justify-content: space-between; align-items: center;
        padding: 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
def go_details(id):
    st.session_state.active_id = id
    st.session_state.screen = 'details'

def go_dash(): st.session_state.screen = 'dash'

# --- TELA 01: DASHBOARD EXECUTIVO ---
if st.session_state.screen == 'dash':
    # Top Bar
    c_logo, c_user = st.columns([1, 1])
    with c_logo: st.markdown("### 💠 CONTABILIZA AI <span style='color:#3b82f6; font-size:12px'>ENTERPRISE</span>", unsafe_allow_html=True)
    with c_user: st.markdown("<div style='text-align:right; color:#94A3B8'>Sócio: Dr. Otávio Silveira • <b>Status: Ultra Scalable</b></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Big Numbers
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""<div class='glass-card'><p class='metric-label'>Potencial de Crédito</p><p class='metric-val'>R$ 1.292.500</p></div>""", unsafe_allow_html=True)
        if st.button("Explorar Carteira"): pass
    with col2: st.markdown(f"""<div class='glass-card'><p class='metric-label'>Economia Operacional</p><p class='metric-val'>82%</p></div>""", unsafe_allow_html=True)
    with col3: st.markdown(f"""<div class='glass-card'><p class='metric-label'>Riscos Auditados</p><p class='metric-val'>1.4M</p></div>""", unsafe_allow_html=True)
    with col4: st.markdown(f"""<div class='glass-card'><p class='metric-label'>Faturamento Extra (Fees)</p><p class='metric-val'>R$ 258k</p></div>""", unsafe_allow_html=True)

    st.markdown("<br><h4>💎 Oportunidades Identificadas pela IA</h4>", unsafe_allow_html=True)

    # Tabela Customizada
    for index, row in st.session_state.db.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom:15px; padding: 15px 25px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin:0;">{row['empresa']}</h4>
                        <span style="color:#94A3B8; font-size:12px;">{row['origem']}</span>
                    </div>
                    <div style="text-align:center;">
                        <span style="color:{row['cor']}; font-weight:800; font-size:18px;">R$ {row['credito']:,.2f}</span><br>
                        <span style="color:#94A3B8; font-size:10px;">Crédito Líquido</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Analisar Impacto: {row['empresa']}", key=f"btn_{row['id']}"):
                go_details(row['id'])
                st.rerun()

# --- TELA 02: DEEP DIVE & PROSPECÇÃO ---
elif st.session_state.screen == 'details':
    client = st.session_state.db[st.session_state.db['id'] == st.session_state.active_id].iloc[0]
    
    st.markdown(f"#### ← <span style='cursor:pointer' onclick='window.location.reload()'>Voltar</span>", unsafe_allow_html=True)
    if st.button("Voltar ao Dashboard Geral"): go_dash(); st.rerun()

    st.title(f"Estratégia: {client['empresa']}")
    
    c_left, c_right = st.columns([1.5, 1])
    
    with c_left:
        st.markdown(f"""
        <div class="glass-card">
            <h3>Diagnóstico da Inteligência</h3>
            <p style="color:#94A3B8">Nossa IA cruzou 60 meses de DCTFWeb com notas fiscais de entrada/saída.</p>
            <div style="background:rgba(59, 130, 246, 0.1); padding:20px; border-radius:12px;">
                <h4 style="color:#3b82f6; margin-top:0;">Possibilidade de Oferta</h4>
                <p>Identificamos que a empresa não segregou corretamente o PIS/COFINS Monofásico. 
                Isso gerou um pagamento a maior de <b>R$ {client['credito']:,.2f}</b>.</p>
                <p><b>Estratégia:</b> Compensação Administrativa via PER/DCOMP. Dinheiro no caixa em até 30 dias.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Gráfico de Projeção
        st.markdown("<br>", unsafe_allow_html=True)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = client['credito'],
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Impacto no Fluxo de Caixa (R$)", 'font': {'size': 20, 'color': '#fff'}},
            gauge = {'axis': {'range': [None, 1000000]}, 'bar': {'color': "#3b82f6"}}
        ))
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "#fff"})
        st.plotly_chart(fig, use_container_width=True)

    with c_right:
        st.markdown("### 🚀 Ativar Prospecção IA")
        st.write("A IA irá gerar uma proposta executiva visual e abordar o cliente via canal oficial.")
        
        if st.button("GERAR PROPOSTA E ENVIAR"):
            with st.status("IA modelando proposta financeira...", expanded=True) as status:
                time.sleep(1.5)
                st.write("Gerando imagem realista de impacto econômico...")
                time.sleep(1.5)
                st.write("Finalizando texto humanizado (Tom Executivo)...")
                status.update(label="Proposta Enviada com Sucesso!", state="complete", expanded=False)
            
            st.balloons()
            
            st.markdown(f"""
            <div style="background:white; color:#000; padding:30px; border-radius:15px; border-left: 10px solid #3b82f6;">
                <p style="font-size:12px; color:#666;">MENSAGEM ENVIADA VIA WHATSAPP BUSINESS</p>
                <p><b>Olá, Diretor da {client['empresa']}.</b></p>
                <p>Analisamos sua conta aqui na contabilidade e identificamos um 'fôlego' de <b>R$ {client['credito']:,.2f}</b> parado nos seus impostos dos últimos anos.</p>
                <p>Não é empréstimo, é dinheiro seu que foi pago a maior e que podemos recuperar agora para investir na sua operação. Veja a projeção que nossa IA fez para você:</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Imagem Realista da IA (Simulada)
            st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80", 
                     caption="Estudo de Viabilidade Econômica gerado pela Contabiliza AI")
