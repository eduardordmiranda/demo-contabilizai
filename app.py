import streamlit as st
import pandas as pd
import datetime
import random
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(
    page_title="Contabiliza AI - Dashboard Inteligente",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema moderno e profissional (escuro, clean, empresarial)
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
        font-family: 'Segoe UI', sans-serif;
    }
    .stSidebar {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    .card {
        background: linear-gradient(135deg, #1e293b 0%, #111827 100%);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        transition: all 0.3s ease;
        cursor: pointer;
        border: 1px solid #334155;
    }
    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        border-color: #10b981;
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 700;
        color: #10b981;
        margin: 0;
    }
    .metric-label {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-top: 8px;
    }
    .metric-delta {
        font-size: 1rem;
        color: #10b981;
    }
    .stExpander {
        background-color: #1e293b !important;
        border-radius: 12px;
        border: 1px solid #334155;
    }
    .stExpander > div > div {
        background-color: #1e293b !important;
    }
    hr {
        border-color: #334155;
        margin: 32px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Dados simulados (baseados em tudo que discutimos)
@st.cache_data
def load_data():
    clientes = pd.DataFrame({
        'Cliente': [f"Empresa {i:03d} Ltda" for i in range(1, 51)],
        'CNPJ': [f"12.345.678/000{i}-99" for i in range(1, 51)],
        'Regime Atual': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], weights=[60, 30, 10], k=50),
        'Regime Ideal': random.choices(['Simples Nacional', 'Lucro Presumido', 'Lucro Real'], k=50),
        'Recuperação Potencial (R$)': [random.randint(4800, 52000) for _ in range(50)],
        'Créditos INSS Recuperáveis (R$)': [random.randint(3000, 35000) for _ in range(50)],
        'Créditos Tributários Recuperáveis (R$)': [random.randint(1800, 25000) for _ in range(50)],
        'Produtos/NCM Errados': [random.randint(0, 18) for _ in range(50)],
        'Status': random.choices(['Ação Imediata', 'Alta Prioridade', 'Médio', 'Baixo'], weights=[15, 25, 40, 20], k=50),
        'Data Última Análise': [datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 120)) for _ in range(50)]
    })
    
    # Métricas agregadas
    total_recuperacao = clientes['Recuperação Potencial (R$)'].sum()
    total_clientes_regime_errado = len(clientes[clientes['Regime Atual'] != clientes['Regime Ideal']])
    total_produtos_errados = clientes['Produtos/NCM Errados'].sum()
    total_clientes_acao_imediata = len(clientes[clientes['Status'] == 'Ação Imediata'])
    
    # Dados para gráficos
    df_grafico = clientes[['Data Última Análise', 'Recuperação Potencial (R$)']].sort_values('Data Última Análise')
    df_grafico['Acumulado'] = df_grafico['Recuperação Potencial (R$)'].cumsum()
    
    return clientes, total_recuperacao, total_clientes_regime_errado, total_produtos_errados, total_clientes_acao_imediata, df_grafico

clientes, total_recuperacao, clientes_regime_errado, total_produtos_errados, total_clientes_acao_imediata, df_grafico = load_data()

# Sidebar
with st.sidebar:
    st.title("Contabiliza AI")
    st.markdown("**Dashboard Inteligente**")
    st.markdown("---")
    st.info("Versão Demonstração – 2026")
    st.markdown("### Navegação Rápida")
    selected = st.radio(
        "Ir para",
        ["Dashboard Principal", "Detalhes por Cliente", "Sobre a Solução"]
    )

# Header
st.title("Contabiliza AI - Dashboard Inteligente")
st.markdown(f"**Atualizado em:** {datetime.datetime.now().strftime('%d/%m/%Y às %H:%M')}")
st.markdown("---")

if selected == "Dashboard Principal":
    # Cards principais (layout inspirado no seu exemplo, com hover e modernidade)
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Total Recuperável", f"R$ {total_recuperacao:,.2f}", "Projeção 12 meses", delta_color="normal")
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Clientes Regime Errado", clientes_regime_errado, "Oportunidade imediata", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Produtos/NCM Errados", total_produtos_errados, "Risco fiscal detectado", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.metric("Ação Imediata", total_clientes_acao_imediata, "Prioridade alta", delta_color="inverse")
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Gráfico principal - evolução acumulada
    st.subheader("Evolução da Recuperação Potencial (últimos 90 dias)")
    fig = px.line(
        df_grafico,
        x='Data Última Análise',
        y='Acumulado',
        title="Acumulado de Recuperação (R$)",
        labels={'Acumulado': 'Valor Acumulado (R$)', 'Data Última Análise': 'Período'},
        color_discrete_sequence=["#10b981"]
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="#e2e8f0",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Expansores rápidos para drill-down
    col_left, col_right = st.columns(2)

    with col_left:
        with st.expander("Top 10 - Recuperação Potencial", expanded=False):
            st.dataframe(
                clientes[['Cliente', 'Recuperação Potencial (R$)', 'Status']]
                .sort_values('Recuperação Potencial (R$)', ascending=False)
                .head(10)
                .style.format({'Recuperação Potencial (R$)': 'R$ {:,.2f}'}),
                use_container_width=True
            )

    with col_right:
        with st.expander("Clientes com Regime Errado", expanded=False):
            st.dataframe(
                clientes[clientes['Regime Atual'] != clientes['Regime Ideal']]
                [['Cliente', 'Regime Atual', 'Regime Ideal', 'Recuperação Potencial (R$)']]
                .sort_values('Recuperação Potencial (R$)', ascending=False)
                .head(10)
                .style.format({'Recuperação Potencial (R$)': 'R$ {:,.2f}'}),
                use_container_width=True
            )

elif selected == "Detalhes por Cliente":
    st.subheader("Análise Detalhada por Cliente")
    
    cliente_selecionado = st.selectbox(
        "Selecione o cliente para ver detalhes completos",
        clientes['Cliente'].tolist(),
        index=None,
        placeholder="Digite ou selecione um cliente..."
    )

    if cliente_selecionado:
        cliente_data = clientes[clientes['Cliente'] == cliente_selecionado].iloc[0]

        col_left, col_right = st.columns([3, 1])

        with col_left:
            st.markdown(f"### {cliente_selecionado}")
            st.markdown(f"**CNPJ:** {cliente_data['CNPJ']}")
            st.markdown(f"**Regime Atual:** {cliente_data['Regime Atual']}")
            st.markdown(f"**Regime Ideal:** {cliente_data['Regime Ideal']}")
            st.markdown(f"**Recuperação Potencial:** <span style='color:#10b981; font-size:1.6rem; font-weight:bold;'>R$ {cliente_data['Recuperação Potencial (R$)']:,.2f}</span>", unsafe_allow_html=True)
            st.markdown(f"**Produtos/NCM Errados:** {cliente_data['Produtos Errados']}")
            st.markdown(f"**Status Prioridade:** {cliente_data['Status']}")

        with col_right:
            st.markdown("### Ações Imediatas")
            
            if st.button("Gerar Mensagem de Prospecção", type="primary", use_container_width=True):
                valor = cliente_data['Recuperação Potencial (R$)']
                mensagem = f"""
Olá, {cliente_selecionado.split()[0]}!

Fizemos uma análise rápida da sua situação fiscal e identificamos uma oportunidade real de **recuperar R$ {valor:,.2f}** em créditos previdenciários (INSS patronal) que estão sendo pagos indevidamente.

Além disso, seu regime tributário atual pode estar gerando custo extra de aproximadamente R$ {valor//4:,.2f} ao ano.

Posso te mostrar o relatório completo e os próximos passos em uma conversa rápida de 15 minutos? Sem custo nem compromisso.

Basta responder com "Quero ver" ou me chamar no WhatsApp.

Abraços,  
[Seu Nome] - Contabiliza AI
                """
                st.text_area("Mensagem gerada (pronta para WhatsApp)", mensagem, height=220)
                st.success("Mensagem pronta! Copie e envie.")

elif selected == "Sobre a Solução":
    st.subheader("Sobre a Contabiliza AI")
    st.markdown("""
    **Objetivo principal**  
    Transformar escritórios contábeis em máquinas de recuperação de receita e redução de custo operacional, usando IA para identificar oportunidades que o contador transforma em faturamento.

    **Principais ganhos**
    - Recuperação média de R$ 5–30 mil por cliente (INSS patronal, tributos, créditos não aproveitados)
    - Redução de 30–50% do tempo gasto em tarefas repetitivas
    - Menos 1–3 auxiliares/estagiários para cada 20–30 clientes atendidos
    - Aumento de fidelização e ticket médio (contador passa a ser visto como consultor estratégico)

    **Tecnologia**
    - IA para análise inteligente (Gemini/Claude)
    - Automação de fluxos (WhatsApp, relatórios, alertas)
    - Integração futura com sistemas contábeis populares (Omie, Domínio, Alterdata, etc.)

    **Preço sugerido**  
    R$ 497–997/mês por escritório (depende do volume de clientes atendidos)

    **Próximo passo sugerido**  
    Teste grátis de 14–30 dias com 3–5 clientes seus para ver o valor real no seu escritório.
    """)

# Rodapé
st.markdown("---")
st.caption("Contabiliza AI - Demonstração Profissional | Prototipo Streamlit | 2026")
