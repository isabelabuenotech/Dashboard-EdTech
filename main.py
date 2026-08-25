from fastapi import FastAPI
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.api.schemas import PlanoEstrategiaDTO
from src.utils.lgpd_sanitizer import load_and_sanitize

app = FastAPI(
    title="Dash Orientador API",
    description="API para disponibilização de dados pedagógicos sanitizados e integração com LMS.",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "ok", "lgpd_compliant": True}

@app.get("/api/v1/planos", response_model=list[PlanoEstrategiaDTO])
def get_planos():
    df = load_and_sanitize("data/raw/ISABELA BUENO _ Dash Orientador _ Planos & Estratégias - ℹ️Painel por aluno.csv")
    
    # Mapeamento dinâmico para DTO
    results = []
    for _, row in df.iterrows():
        results.append({
            "hash_aluno": str(row.iloc[0]),
            "plano_acao": "Plano Estratégico Registrado",
            "status": "Ativo"
        })
    return results
