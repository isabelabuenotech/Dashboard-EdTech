import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Painel do Orientador Educacional",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. GERAÇÃO DE DADOS FICTÍCIOS (MOCK DATA)
# ==========================================
@st.cache_data
def load_mock_data():
    """Gera dados simulados estruturados para o painel de orientação educacional."""
    np.random.seed(42)
    
    escolas = ["Colégio Dom Pedro", "Instituto de Educação Moderna", "Escola Santa Maria"]
    series = ["1ª Série EM", "2ª Série EM", "3ª Série EM"]
    situacoes_psi = ["Sem queixas", "Ansiedade leve", "Acompanhamento por estresse", "TDAH em acompanhamento", "Sintomas depressivos"]
    interesses_prof = ["Engenharia de Software", "Medicina", "Direito", "Psicologia", "Arquitetura", "Administração"]
    faculdades = ["USP", "UNICAMP", "UNESP", "FGV", "PUC"]
    
    nomes = [
        "Ana Silva", "Bruno Santos", "Carla Oliveira", "Daniel Souza", "Eduarda Lima",
        "Felipe Costa", "Gabriela Rocha", "Henrique Alves", "Isabela Ferreira", "João Pereira",
        "Larissa Barbosa", "Mateus Ribeiro", "Nathalia Gomes", "Otávio Martins", "Paula Araujo"
    ]
    
    data_list = []
    base_date = datetime.now() - timedelta(days=180)
    
    for i, nome in enumerate(nomes):
        escola = escolas[i % len(escolas)]
        serie = series[i % len(series)]
        psicoterapia = np.random.choice(["Sim", "Não"], p=[0.4, 0.6])
        psiquiatra = np.random.choice(["Sim", "Não"], p=[0.2, 0.8])
        situacao_psi = np.random.choice(situacoes_psi)
        
        # Simulando histórico de 4 bimestres/simulados por aluno
        for b in range(1, 5):
            data_registro = base_date + timedelta(days=b * 40)
            media_acad = round(np.random.uniform(5.5, 9.8), 1)
            nota_simulado = round(np.random.uniform(500, 920), 0)
            
            data_list.append({
                "id_aluno": i + 1,
                "nome": nome,
                "escola": escola,
                "serie": serie,
                "data_registro": data_registro,
                "bimestre": f"{b}º Bimestre",
                "media_academica": media_acad,
                "resultado_simulado": nota_simulado,
                "situacao_psicologica": situacao_psi,
                "faz_psicoterapia": psicoterapia,
                "acompanhamento_psiquiatra": psiquiatra,
                "registro_intervencoes": f"Atendimento realizado no {b}º bimestre. Foco em gestão de tempo e apoio emocional.",
                "planejamento_pedagógico": f"Plano de estudos ajustado para foco nas matérias com desempenho < 7.0.",
                "interesse_profissional": interesses_prof[i % len(interesses_prof)],
                "faculdade_interesse": faculdades[i % len(faculdades)],
                "responsavel_nome": f"Responsável de {nome.split()[0]}",
                "responsavel_contato": f"(11) 9{np.random.randint(1000, 9999)}-{np.random.randint(1000, 9999)}"
            })
            
    df = pd.DataFrame(data_list)
    df["data_registro"] = pd.to_datetime(df["data_registro"])
    return df

df_raw = load_mock_data()

# ==========================================
# 3. BARRA LATERAL E FILTROS GLOBAIS
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3429/3429149.png", width=80)
st.sidebar.title("Filtros do Painel")

# Filtro por Escola
escolas_disponiveis = sorted(df_raw["escola"].unique().tolist())
escolas_selecionadas = st.sidebar.multiselect("Filtrar por Colégio:", escolas_disponiveis, default=escolas_disponiveis)

# Filtro por Série
series_disponiveis = sorted(df_raw["serie"].unique().tolist())
series_selecionadas = st.sidebar.multiselect("Filtrar por Série:", series_disponiveis, default=series_disponiveis)

# Filtro por Aluno Especifico (Opcional)
alunos_disponiveis = sorted(df_raw["nome"].unique().tolist())
alunos_selecionados = st.sidebar.multiselect("Buscar Aluno(s) Específico(s):", alunos_disponiveis, default=[])

# Filtro por Período de Data
min_date = df_raw["data_registro"].min().date()
max_date = df_raw["data_registro"].max().date()
data_inicio, data_fim = st.sidebar.date_input(
    "Período do Registro:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Application dos Filtros
df_filtered = df_raw.copy()

if escolas_selecionadas:
    df_filtered = df_filtered[df_filtered["escola"].isin(escolas_selecionadas)]

if series_selecionadas:
    df_filtered = df_filtered[df_filtered["serie"].isin(series_selecionadas)]

if alunos_selecionados:
    df_filtered = df_filtered[df_filtered["nome"].isin(alunos_selecionados)]

df_filtered = df_filtered[
    (df_filtered["data_registro"].dt.date >= data_inicio) & 
    (df_filtered["data_registro"].dt.date <= data_fim)
]

# ==========================================
# 4. PAINEL PRINCIPAL & KPIS
# ==========================================
st.title("🎓 Dashboard de Acompanhamento Pedagógico e De Saúde Mental")
st.markdown("Visão consolidada para Orientadores Educacionais.")

if df_filtered.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados. Por favor, ajuste as opções na barra lateral.")
else:
    # Cálculo das métricas principais (KPIs)
    total_alunos = df_filtered["nome"].nunique()
    media_geral_notas = df_filtered["media_academica"].mean()
    media_simulados = df_filtered["resultado_simulado"].mean()
    
    # Subconjunto com o registro mais recente por aluno para contagens únicas
    df_ultimos_registros = df_filtered.sort_values("data_registro").groupby("nome").last().reset_index()
    em_psicoterapia = df_ultimos_registros[df_ultimos_registros["faz_psicoterapia"] == "Sim"].shape[0]
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Alunos", total_alunos)
    col2.metric("Média Acadêmica Geral", f"{media_geral_notas:.2f}", delta=f"{media_geral_notas - 7.0:.2f} vs Meta (7.0)")
    col3.metric("Média nos Simulados", f"{media_simulados:.0f} pts", delta=f"{media_simulados - 600:.0f} vs Meta (600)")
    col4.metric("Em Psicoterapia", f"{em_psicoterapia} alunos", delta=f"{(em_psicoterapia/total_alunos)*100:.1f}% do total", delta_color="off")

    st.markdown("---")

    # ==========================================
    # 5. GRÁFICOS INTERATIVOS
    # ==========================================
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("📈 Evolução Média Acadêmica ao Longo do Tempo")
        df_evolucao = df_filtered.groupby(["data_registro", "serie"])["media_academica"].mean().reset_index()
        fig_linha = px.line(
            df_evolucao, 
            x="data_registro", 
            y="media_academica", 
            color="serie",
            markers=True,
            labels={"data_registro": "Data de Avaliação", "media_academica": "Média Acadêmica", "serie": "Série"},
            title="Média por Série ao Longo dos Registros"
        )
        fig_linha.update_layout(yaxis_range=[0, 10])
        st.plotly_chart(fig_linha, use_container_width=True)

    with c2:
        st.subheader("🧠 Condição / Queixa de Saúde Mental")
        df_saude = df_ultimos_registros["situacao_psicologica"].value_counts().reset_index()
        df_saude.columns = ["Queixa / Situação", "Quantidade"]
        fig_barras = px.bar(
            df_saude,
            x="Quantidade",
            y="Queixa / Situação",
            orientation="h",
            color="Quantidade",
            color_continuous_scale="Reds",
            title="Distribuição das Condições Psicológicas Identificadas"
        )
        st.plotly_chart(fig_barras, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        st.subheader("🎯 Cursos de Interesse Profissional")
        df_cursos = df_ultimos_registros["interesse_profissional"].value_counts().reset_index()
        df_cursos.columns = ["Curso", "Quantidade"]
        fig_donut_cursos = px.pie(
            df_cursos, 
            names="Curso", 
            values="Quantidade", 
            hole=0.4,
            title="Distribuição de Interesse por Carreira"
        )
        st.plotly_chart(fig_donut_cursos, use_container_width=True)

    with c4:
        st.subheader("🏛️ Faculdades de Interesse (Estratégia Vestibular)")
        df_facul = df_ultimos_registros["faculdade_interesse"].value_counts().reset_index()
        df_facul.columns = ["Faculdade", "Quantidade"]
        fig_donut_facul = px.pie(
            df_facul, 
            names="Faculdade", 
            values="Quantidade", 
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            title="Instituições Alvo dos Estudantes"
        )
        st.plotly_chart(fig_donut_facul, use_container_width=True)

    st.markdown("---")

    # ==========================================
    # 6. TABELA DETALHADA E INTERVENÇÕES
    # ==========================================
    st.subheader("📋 Detalhamento dos Alunos, Planejamento e Responsáveis")
    
    # Seleção das colunas para apresentação limpa
    cols_exibicao = [
        "nome", "escola", "serie", "media_academica", "resultado_simulado",
        "situacao_psicologica", "faz_psicoterapia", "acompanhamento_psiquiatra",
        "interesse_profissional", "faculdade_interesse", 
        "registro_intervencoes", "planejamento_pedagógico", 
        "responsavel_nome", "responsavel_contato"
    ]
    
    st.dataframe(
        df_filtered[cols_exibicao],
        column_config={
            "nome": "Nome do Aluno",
            "escola": "Escola",
            "serie": "Série",
            "media_academica": st.column_config.NumberColumn("Média Geral", format="%.1f"),
            "resultado_simulado": st.column_config.NumberColumn("Simulado", format="%d pts"),
            "situacao_psicologica": "Saúde Mental",
            "faz_psicoterapia": "Psicoterapia?",
            "acompanhamento_psiquiatra": "Psiquiatra?",
            "interesse_profissional": "Carreira Alvo",
            "faculdade_interesse": "Faculdade Alvo",
            "registro_intervencoes": "Última Intervenção",
            "planejamento_pedagógico": "Plano Pedagógico",
            "responsavel_nome": "Responsável",
            "responsavel_contato": "Contato do Resp."
        },
        use_container_width=True,
        hide_index=True
    )
