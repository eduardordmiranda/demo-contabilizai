import streamlit as st
import pandas as pd
import datetime
import random
import plotly.express as px

# Configuração da página - tema moderno
st.set_page_config(
    page_title="Contabiliza AI - Dashboard",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS moderno e profissional (inspirado no seu exemplo)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .stSidebar {
        background-color: #1e293b;
    }
    .card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        text-align: center;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.5);
    }
    .metric-value {
        font-size: 2.6rem;
        font-weight: 700;
        color: #10b981;
    }
    .metric-label {
        font-size: 1rem;
        color: #94a3b8;
    }
    .stExpander {
        background-color: #1e293b !important;
        border-radius: 12px;
        border: none;
    }
    .stExpander > div > div {
        background-color: #1e293b !important;
    }
    </style>
""", unsafe_allow_html=True)

# Dados simulados (substitua por reais depois)
@st.cache_data
def load_data():
    clientes = pd.DataFrame({
        'Cliente': [f"Empresa {i:03d}" for i in range(1, 51)],
        'CNPJ': [f"12.345.678/000{i}-99" for i in range(1, 51)],
        'Regime Atual': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], k=50),
        'Regime Ideal': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], k=50),
        'Recuperação Potencial (R$)': [random.randint(5000, 45000) for _ in range(50)],
        'Produtos Errados': [random.randint(0, 15) for _ in range(50)],
        'Status': random.choices(['Ação Imediata', 'Médio', 'Baixo'], k=50),
        'Data Análise': [datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 90)) for _ in range(50)]
    })
    
    total_recuperacao = clientes['Recuperação Potencial (R$)'].sum()
    clientes_regime_errado = len(clientes[clientes['Regime Atual'] != clientes['Regime Ideal']])
    total_produtos_errados = clientes['Produtos Errados'].sum()
    
    # Dados para gráfico simples
    df_grafico = clientes[['Data Análise', 'Recuperação Potencial (R$)']].sort_values('Data Análise')
    df_grafico['Acumulado'] = df_grafico['Recuperação Potencial (R$)'].cumsum()
    
    return clientes, total_recuperacao, clientes_regime_errado, total_produtos_errados, df_grafico

clientes, total_recuperacao, clientes_regime_errado, total_produtos_errados, df_grafico = load_data()

# Sidebar
with st.sidebar:
    st.title("Contabiliza AI")
    st.markdown("**Dashboard Inteligente**")
    st.markdown("---")
    st.info("Versão Demonstração - 2026")
    selected = st.radio(
        "Navegação",
        ["Dashboard Principal", "Detalhes por Cliente", "Sobre a Solução"]
    )

# Header
st.title("Contabiliza AI - Dashboard Inteligente")
st.markdown(f"**Atualizado em:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
st.markdown("---")

if selected == "Dashboard Principal":
    # Cards principais - layout moderno e clicável
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Total Recuperável", f"R$ {total_recuperacao:,.2f}", "Projeção 12 meses")
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("Ver detalhes", key="btn_rec", use_container_width=True):
                st.session_state['expand_rec'] = True

    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Clientes Regime Errado", clientes_regime_errado, "Oportunidade imediata", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("Ver detalhes", key="btn_regime", use_container_width=True):
                st.session_state['expand_regime'] = True

    with col3:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Produtos/NCM Errados", total_produtos_errados, "Risco fiscal detectado", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("Ver detalhes", key="btn_prod", use_container_width=True):
                st.session_state['expand_prod'] = True

    st.markdown("---")

    # Gráfico de evolução (inspiração no seu exemplo)
    st.subheader("Evolução da Recuperação Potencial")
    fig = px.line(df_grafico, x='Data Análise', y='Acumulado',
                  title="Acumulado de Recuperação (R$)",
                  labels={'Acumulado': 'Valor Acumulado (R$)', 'Data Análise': 'Período'},
                  color_discrete_sequence=["#10b981"])
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="#e2e8f0"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Expansores condicionais
    if st.session_state.get('expand_rec', False):
        with st.expander("Detalhes - Recuperação de Créditos", expanded=True):
            st.dataframe(
                clientes[['Cliente', 'Recuperação Potencial (R$)', 'Status']]
                .sort_values('Recuperação Potencial (R$)', ascending=False)
                .head(10),
                use_container_width=True
            )

    if st.session_state.get('expand_regime', False):
        with st.expander("Detalhes - Clientes Regime Errado", expanded=True):
            st.dataframe(
                clientes[clientes['Regime Atual'] != clientes['Regime Ideal']]
                [['Cliente', 'Regime Atual', 'Regime Ideal']],
                use_container_width=True
            )

    if st.session_state.get('expand_prod', False):
        with st.expander("Detalhes - Produtos/NCM Errados", expanded=True):
            st.dataframe(
                clientes[clientes['Produtos Errados'] > 0]
                [['Cliente', 'Produtos Errados']]
                .sort_values('Produtos Errados', ascending=False),
                use_container_width=True
            )

elif selected == "Detalhes por Cliente":
    st.subheader("Busca e Detalhes por Cliente")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        cliente_selecionado = st.selectbox(
            "Selecione o cliente",
            clientes['Cliente'].tolist(),
            index=None,
            placeholder="Escolha um cliente..."
        )

    if cliente_selecionado:
        cliente_data = clientes[clientes['Cliente'] == cliente_selecionado].iloc[0]

        col_left, col_right = st.columns([2, 1])

        with col_left:
            st.markdown(f"### {cliente_selecionado}")
            st.markdown(f"**CNPJ:** {cliente_data['CNPJ']}")
            st.markdown(f"**Regime Atual:** {cliente_data['Regime Atual']}")
            st.markdown(f"**Regime Ideal:** {cliente_data['Regime Ideal']}")
            st.markdown(f"**Recuperação Potencial:** R$ {cliente_data['Recuperação Potencial (R$)']:,.2f}")
            st.markdown(f"**Produtos Errados:** {cliente_data['Produtos Errados']}")
            st.markdown(f"**Status:** {cliente_data['Status']}")

        with col_right:
            st.markdown("### Ações Rápidas")
            
            if st.button("Gerar Mensagem de Prospecção", type="primary", use_container_width=True):
                mensagem = f"""
Olá, {cliente_selecionado.split()[0]}!

Identificamos uma oportunidade real de **recuperar R$ {cliente_data['Recuperação Potencial (R$)']:,.2f}** em créditos previdenciários na sua folha de pagamento.

Além disso, seu regime tributário atual pode estar gerando custo extra.

Podemos agendar uma conversa rápida (15 minutos) para mostrar o valor exato e os próximos passos? Sem compromisso.

Abraços,  
[Seu Nome] - Contabiliza AI
                """
                st.text_area("Mensagem gerada (copie e envie via WhatsApp)", mensagem, height=180)
                st.success("Mensagem pronta! Copie e envie.")

elif selected == "Sobre a Solução":
    st.subheader("Sobre a Contabiliza AI")
    st.markdown("""
    **Objetivo principal**  
    Transformar escritórios contábeis em máquinas de recuperação de receita e redução de custo operacional.

    **Principais ganhos**
    - Recuperação média de R$ 5–30 mil por cliente (INSS patronal, tributos)
    - Redução de 30–50% do tempo em tarefas repetitivas
    - Menos 1–3 auxiliares/estagiários para cada 20–30 clientes
    - Aumento de fidelização e ticket médio (contador vira consultor estratégico)

    **Tecnologia**
    - IA para análise inteligente (Gemini/Claude)
    - Automação de fluxos (WhatsApp, relatórios, alertas)
    - Integração futura com sistemas contábeis (Omie, Domínio, etc.)

    **Preço sugerido**  
    R$ 497–997/mês por escritório (depende do volume de clientes)
    """)

# Rodapé
st.markdown("---")
st.caption("Contabiliza AI - Demonstração | Prototipo Streamlit | 2026")
