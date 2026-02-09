import streamlit as st
import pandas as pd
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Contabiliza AI - Hub", layout="wide")

# Inicialização de estado de navegação (para simular cliques)
if 'tela' not in st.session_state:
    st.session_state.tela = 'dashboard'
if 'cliente_selecionado' not in st.session_state:
    st.session_state.cliente_selecionado = None

# --- BANCO DE DADOS DA DEMO ---
dados_clientes = pd.DataFrame([
    {"Empresa": "Farmácia Central Ltda", "Credito": 18500.00, "Origem": "PIS/COFINS Monofásico", "Itens": 142, "Status": "Pendente"},
    {"Empresa": "Auto Peças Silva", "Credito": 42300.50, "Origem": "ICMS-ST e Monofásico", "Itens": 890, "Status": "Pendente"},
    {"Empresa": "Restaurante Bom Gosto", "Credito": 12100.00, "Origem": "Segregação Simples", "Itens": 56, "Status": "Abordado"},
    {"Empresa": "Supermercado Ideal", "Credito": 156000.00, "Origem": "PIS/COFINS + INSS", "Itens": 4500, "Status": "Pendente"},
])

total_credito = dados_clientes['Credito'].sum()

# --- FUNÇÕES DE NAVEGAÇÃO ---
def ir_para_lista(): st.session_state.tela = 'lista'
def ir_para_dashboard(): st.session_state.tela = 'dashboard'
def ver_detalhes(empresa):
    st.session_state.cliente_selecionado = empresa
    st.session_state.tela = 'detalhes'

# --- 1. TELA INICIAL: INDICADORES ---
if st.session_state.tela == 'dashboard':
    st.title("📊 Contabiliza AI - Torre de Controle")
    st.subheader("Visão Geral da Carteira")
    
    col1, col2, col3 = st.columns(3)
    
    # CARD CLICÁVEL (Simulado com botão abaixo do indicador)
    with col1:
        st.metric("Potencial de Crédito Total", f"R$ {total_credito:,.2f}", "Oportunidade")
        if st.button("🔍 Abrir Detalhes do Crédito"):
            ir_para_lista()
            st.rerun()
            
    with col2:
        st.metric("Clientes Auditados", len(dados_clientes), "Últimos 30 dias")
    with col3:
        st.metric("Taxa de Sucesso (Fee)", f"R$ {(total_credito * 0.2):,.2f}", "Estimado 20%")

# --- 2. TELA: LISTA DE CLIENTES ---
elif st.session_state.tela == 'lista':
    st.button("⬅️ Voltar ao Dashboard", on_click=ir_para_dashboard)
    st.title("📑 Clientes com Créditos Identificados")
    st.write("Clique no nome da empresa para abrir o painel estratégico.")

    for index, row in dados_clientes.iterrows():
        col_emp, col_val, col_acao = st.columns([2, 1, 1])
        with col_emp:
            st.markdown(f"**{row['Empresa']}**")
        with col_val:
            st.markdown(f"R$ {row['Credito']:,.2f}")
        with col_acao:
            if st.button("Ver Painel", key=f"btn_{index}"):
                ver_detalhes(row['Empresa'])
                st.rerun()
        st.divider()

# --- 3. TELA: DETALHES E PROSPECÇÃO ---
elif st.session_state.tela == 'detalhes':
    empresa = st.session_state.cliente_selecionado
    dados = dados_clientes[dados_clientes['Empresa'] == empresa].iloc[0]
    
    st.button("⬅️ Voltar para Lista", on_click=ir_para_lista)
    st.title(f"🏢 Painel Estratégico: {empresa}")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"""
        **Análise Técnica da IA:**
        * **Origem:** {dados['Origem']}
        * **Volume de Dados:** {dados['Itens']} itens processados
        * **Base Legal:** Solução de Consulta COSIT nº 123/2026
        """)
    with c2:
        st.success(f"### Valor Recuperável: R$ {dados['Credito']:,.2f}")
    
    st.markdown("---")
    st.subheader("🚀 Ação Imediata")
    
    if st.button(f"PROSPECTAR: Enviar Oportunidade para {empresa}"):
        with st.status("IA redigindo mensagem personalizada...", expanded=True) as status:
            time.sleep(1.5)
            st.write("Conectando ao WhatsApp Business API...")
            time.sleep(1.5)
            st.write("Mensagem enviada com sucesso!")
            status.update(label="Prospecção Concluída!", state="complete", expanded=False)
        
        st.balloons()
        st.chat_message("assistant").write(f"""
        **Mensagem enviada para o cliente:**
        'Olá, Diretor da {empresa}. Nossa auditoria inteligente identificou que sua empresa possui **R$ {dados['Credito']:,.2f}** em créditos tributários de {dados['Origem']} não aproveitados nos últimos meses. 
        Gostaria de agendar uma breve reunião para explicarmos como compensar esse valor no seu próximo imposto?'
        """)
