import hashlib
import pandas as pd

def generate_hash(text: str, salt: str = "EDTECH_LGPD_2026") -> str:
    """Gera hash SHA-256 para anonimizar nomes de alunos e responsáveis."""
    if pd.isna(text) or not str(text).strip():
        return "N/A"
    clean_text = str(text).strip().lower()
    return f"ID_{hashlib.sha256(f'{clean_text}_{salt}'.encode('utf-8')).hexdigest()[:8].upper()}"

def sanitize_orientacao_data(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica regras de LGPD ao DataFrame de orientação educacional."""
    df_clean = df.copy()
    if "nome" in df_clean.columns:
        df_clean["aluno_hash"] = df_clean["nome"].apply(generate_hash)
    if "responsavel_nome" in df_clean.columns:
        df_clean["responsavel_hash"] = df_clean["responsavel_nome"].apply(generate_hash)
        df_clean.drop(columns=["responsavel_nome"], inplace=True)
    return df_clean
