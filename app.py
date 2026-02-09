import streamlit as st
import datetime
import random  # só para simular variação nos valores

# Configuração da página
st.set_page_config(
    page_title="Contabiliza AI - Demonstração",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função simulada de IA (substitua por chamada real ao Gemini/Claude depois)
def simulate_ia_report(func_key):
    today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    valor_base = random.randint(5000, 30000)  # Simula variação realista
    
    reports = {
        "recupera_inss": f"""
        **Relatório de Recuperação INSS Patronal**  
        Data: {today}  

        **Valor estimado recuperável:** R$ {valor_base:,.2f}  
        **Atualização SELIC aproximada:** +R$ {valor_base * 0.08:,.2f}  

        **Itens encontrados:**  
        - Verbas indenizatórias mal classificadas: R$ {valor_base//3:,.2f}  
        - Horas extras sem reflexos corretos: R$ {valor_base//4:,.2f}  
        - Adicional noturno/insalubridade indevido: R$ {valor_base//5:,.2f}  

        **Risco de questionamento:** Médio  
        **Próximos passos:** Gerar PER/DCOMP + anexar eSocial/GFIP  
        """,

        "conciliacao": f"""
        **Conciliação Bancária Inteligente**  
        Data: {today}  

        **Divergências detectadas:** 7 itens  
        **Lançamentos sugeridos:** 12  

        Exemplos:  
        - Taxa bancária não lançada: R$ 47,50  
        - Depósito duplicado: R$ 1.200,00  
        - Juros de mora não contabilizado  

        **Tempo economizado estimado:** 8–12 horas/semana
        """,

        "alertas_fiscais": f"""
        **Alertas Fiscais Proativos**  
        Data: {today}  

        **Pendências críticas:** DCTFWeb vencida há 3 dias  
        **Pendências médias:** EFD-Contribuições em 5 dias  

        **Ações sugeridas:**  
        - Retificar DCTFWeb imediatamente  
        - Compensar crédito acumulado
        """,

        "reforma": f"""
        **Simulação Reforma Tributária**  
        Data: {today}  

        **Carga tributária atual:** 18,5%  
        **Carga projetada (IBS/CBS):** 16,2%  
        **Economia anual estimada:** R$ {valor_base // 2:,.2f}  

        **Recomendação:** Manter regime atual por 12 meses
        """,

        "classifica_despesas": f"""
        **Classificação Automática de Despesas**  
        Data: {today}  

        **Itens classificados:** 120  
        **Exemplos:**  
        - Aluguel → Despesa Operacional  
        - Taxa bancária → Despesa Financeira (sugerido ajuste)  

        **Tempo economizado:** 60–90%
        """,

        "pre_lancamentos": f"""
        **Pré-lançamentos de Fechamento Mensal**  
        Data: {today}  

        **Lançamentos gerados:** 28  
        **Provisões sugeridas:** Férias + 13º salário  

        **Tempo economizado:** 40–70%
        """,

        "regua_cobranca": f"""
        **Régua de Cobrança Inteligente**  
        Data: {today}  

        **Clientes inadimplentes detectados:** 4  
        **Mensagens geradas:** Prontas para envio via WhatsApp
        """,

        "assistente": f"""
        **Assistente de Dúvidas Contábeis**  
        Data: {today}  

        **Resposta IA:** Para esse CFOP, o CST correto é 00 (tributada integralmente) conforme legislação vigente.
        """,

        "planejamento": f"""
        **Planejamento Tributário Simples**  
        Data: {today}  

        **Sugestões principais:**  
        - Distribuição de lucros vs pró-labore: economia R$ {valor_base // 3:,.2f}/ano  
        - Compensação de créditos acumulados: R$ {valor_base // 4:,.2f}
        """,

        "incentivos": f"""
        **Incentivos Fiscais Setoriais**  
        Data: {today}  

        **Elegibilidade encontrada:** Redução de base ICMS para TI (SC)  
        **Economia estimada:** R$ {valor_base // 2:,.2f}/ano
        """
    }
    
    return reports.get(func_key, "<p>Relatório gerado com sucesso (simulação).</p>")

# Título da página
st.title("Contabiliza AI - Demonstração")
st.markdown("### Ferramenta de IA para escritórios contábeis | Teste todas as funcionalidades")

# Menu lateral com as funções
st.sidebar.title("Funcionalidades")
func_choice = st.sidebar.radio(
    "Escolha a função para testar:",
    [
        "1. Recuperar créditos INSS patronal",
        "2. Conciliação bancária inteligente",
        "3. Alertas fiscais proativos",
        "4. Simulação Reforma Tributária",
        "5. Classificar despesas automaticamente",
        "6. Pré-lançamentos de fechamento",
        "7. Régua de cobrança de clientes",
        "8. Assistente de dúvidas contábeis",
        "9. Planejamento tributário simples",
        "10. Incentivos fiscais setoriais"
    ]
)

# Mapeamento para chave interna
func_map = {
    "1. Recuperar créditos INSS patronal": "recupera_inss",
    "2. Conciliação bancária inteligente": "conciliacao",
    "3. Alertas fiscais proativos": "alertas_fiscais",
    "4. Simulação Reforma Tributária": "reforma",
    "5. Classificar despesas automaticamente": "classifica_despesas",
    "6. Pré-lançamentos de fechamento": "pre_lancamentos",
    "7. Régua de cobrança de clientes": "regua_cobranca",
    "8. Assistente de dúvidas contábeis": "assistente",
    "9. Planejamento tributário simples": "planejamento",
    "10. Incentivos fiscais setoriais": "incentivos"
}

selected_func = func_map[func_choice]

# Formulário genérico para entrada de dados
with st.expander(f"Preencha os dados para {func_choice}", expanded=True):
    dados = st.text_area(
        "Cole aqui os dados (planilha, exportação, descrição do caso, etc.)",
        height=150,
        placeholder="Exemplo:\nCNPJ: 12.345.678/0001-99\nRegime: Simples Nacional\nFaturamento mensal: R$ 120.000\n..."
    )

    if st.button("Gerar Relatório", type="primary"):
        with st.spinner("Analisando com IA..."):
            # Simula delay de IA
            import time
            time.sleep(1.5)
            
            report = simulate_ia_report(selected_func)
            st.markdown("### Relatório Gerado")
            st.markdown(report, unsafe_allow_html=True)
            
            # Botão de "download" simulado
            st.download_button(
                label="Baixar relatório como PDF (simulado)",
                data=report,
                file_name=f"relatorio_{selected_func}.txt",
                mime="text/plain"
            )

# Rodapé
st.markdown("---")
st.caption("Contabiliza AI - Demonstração | Versão protótipo | 2026")
