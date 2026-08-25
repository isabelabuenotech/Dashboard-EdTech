import streamlit as st

# Adiciona o diretório raiz ao path para importação dos módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.lgpd_sanitizer import load_and_sanitize
from src.analytics.metrics import calculate_kpis

st.set_page_config(
    page_title="Dash Orientador | Painel Pedagógico",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Dash Orientador — Gestão Pedagógica & Estratégias")
st.caption("🛡️ Painel em conformidade com a LGPD (Lei nº 13.709/2018). Dados pseudonimizados.")

# Ingestão e Sanitização
data_path = "data/raw/ISABELA BUENO _ Dash Orientador _ Planos & Estratégias - ℹ️Painel por aluno.csv"
df = load_and_sanitize(data_path)

# Métricas
kpis = calculate_kpis(df)

m1, m2, m3 = st.columns(3)
m1.metric("Total de Alunos (Pseudonimizados)", kpis["total_alunos"])
m2.metric("Planos e Metas Ativas", kpis["total_registros"])
m3.metric("Status do Pipeline", "Protegido por LGPD ✅")

st.markdown("---")

# Filtro
col_id = [c for c in df.columns if 'aluno' in c or 'id' in c][0]
aluno_sel = st.sidebar.selectbox("Filtrar por ID Pseudônimo:", ["Todos"] + list(df[col_id].unique()))

df_display = df if aluno_sel == "Todos" else df[df[col_id] == aluno_sel]

st.subheader("📋 Tabela Integrada de Orientação")
st.dataframe(df_display, use_container_width=True)
