import streamlit as st
import pandas as pd
import datetime
import random
from streamlit_extras.stylable_container import stylable_container

# Configuração da página - tema moderno
st.set_page_config(
    page_title="Contabiliza AI - Dashboard",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema escuro + cores modernas
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    .stSidebar {
        background-color: #161b22;
    }
    .card {
        background-color: #1f2937;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #10b981;
    }
    .metric-label {
        font-size: 1rem;
        color: #9ca3af;
    }
    </style>
""", unsafe_allow_html=True)

# Dados simulados (substitua por reais depois)
@st.cache_data
def load_data():
    clientes = pd.DataFrame({
        'Cliente': [f"Empresa {i}" for i in range(1, 51)],
        'CNPJ': [f"12.345.678/000{i}-99" for i in range(1, 51)],
        'Regime Atual': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], k=50),
        'Regime Ideal': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], k=50),
        'Recuperação Potencial (R$)': [random.randint(5000, 45000) for _ in range(50)],
        'Produtos Errados': random.randint(0, 15) for _ in range(50),
        'Status': random.choices(['Ação Imediata', 'Médio', 'Baixo'], k=50)
    })
    
    total_recuperacao = clientes['Recuperação Potencial (R$)'].sum()
    clientes_regime_errado = len(clientes[clientes['Regime Atual'] != clientes['Regime Ideal']])
    total_produtos_errados = clientes['Produtos Errados'].sum()
    
    return clientes, total_recuperacao, clientes_regime_errado, total_produtos_errados

clientes, total_recuperacao, clientes_regime_errado, total_produtos_errados = load_data()

# Sidebar - Navegação
with st.sidebar:
    st.title("Contabiliza AI")
    st.markdown("**Dashboard de Inteligência Contábil**")
    st.markdown("---")
    st.info("Versão Demonstração - 2026")
    st.markdown("### Menu Rápido")
    selected = st.radio(
        "Navegar",
        ["Dashboard Principal", "Detalhes por Cliente", "Sobre a Solução"]
    )

# Header
st.title("Contabiliza AI - Dashboard Inteligente")
st.markdown(f"**Atualizado em:** {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
st.markdown("---")

if selected == "Dashboard Principal":
    # Cards principais - layout moderno
    col1, col2, col3 = st.columns(3)

    with col1:
        with stylable_container(
            key="card1",
            css_styles="""
                background-color: #1f2937;
                border-radius: 12px;
                padding: 24px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            """
        ):
            st.metric(
                label="Total Recuperável",
                value=f"R$ {total_recuperacao:,.2f}",
                delta="Projeção 12 meses",
                delta_color="normal"
            )

    with col2:
        with stylable_container(
            key="card2",
            css_styles="""
                background-color: #1f2937;
                border-radius: 12px;
                padding: 24px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            """
        ):
            st.metric(
                label="Clientes Regime Errado",
                value=clientes_regime_errado,
                delta="Oportunidade imediata",
                delta_color="inverse"
            )

    with col3:
        with stylable_container(
            key="card3",
            css_styles="""
                background-color: #1f2937;
                border-radius: 12px;
                padding: 24px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            """
        ):
            st.metric(
                label="Produtos/NCM Errados",
                value=total_produtos_errados,
                delta="Risco fiscal detectado",
                delta_color="inverse"
            )

    st.markdown("---")

    # Expansores para detalhes rápidos
    with st.expander("Detalhes - Recuperação de Créditos", expanded=False):
        st.dataframe(
            clientes[['Cliente', 'Recuperação Potencial (R$)', 'Status']]
            .sort_values('Recuperação Potencial (R$)', ascending=False)
            .head(10)
        )

    with st.expander("Detalhes - Clientes Regime Errado", expanded=False):
        st.dataframe(
            clientes[clientes['Regime Atual'] != clientes['Regime Ideal']]
            [['Cliente', 'Regime Atual', 'Regime Ideal']]
        )

    with st.expander("Detalhes - Produtos/NCM Errados", expanded=False):
        st.dataframe(
            clientes[clientes['Produtos Errados'] > 0]
            [['Cliente', 'Produtos Errados']]
            .sort_values('Produtos Errados', ascending=False)
        )

elif selected == "Detalhes por Cliente":
    st.subheader("Busca e Detalhes por Cliente")
    cliente_selecionado = st.selectbox("Selecione o cliente", clientes['Cliente'].tolist())

    if cliente_selecionado:
        cliente_data = clientes[clientes['Cliente'] == cliente_selecionado].iloc[0]

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### {cliente_selecionado}")
            st.markdown(f"**CNPJ:** {cliente_data['CNPJ']}")
            st.markdown(f"**Regime Atual:** {cliente_data['Regime Atual']}")
            st.markdown(f"**Regime Ideal:** {cliente_data['Regime Ideal']}")
            st.markdown(f"**Recuperação Potencial:** R$ {cliente_data['Recuperação Potencial (R$)']:,.2f}")
            st.markdown(f"**Produtos Errados:** {cliente_data['Produtos Errados']}")

        with col2:
            st.markdown("### Ações Rápidas")
            if st.button("Gerar Mensagem de Prospecção", type="primary"):
                mensagem = f"""
                Olá, {cliente_selecionado.split()[0]}!

                Identificamos uma oportunidade de recuperação de R$ {cliente_data['Recuperação Potencial (R$)']:,.2f} em créditos previdenciários na sua folha de pagamento.

                Além disso, seu enquadramento tributário atual pode estar gerando custo extra.

                Podemos agendar uma conversa rápida (15 min) para mostrar o valor exato e os próximos passos?

                Abraços,
                [Seu Nome] - Contabiliza AI
                """
                st.text_area("Mensagem gerada (copie e envie via WhatsApp)", mensagem, height=150)
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
    - Aumento de fidelização e ticket médio (contador vira consultor)

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
