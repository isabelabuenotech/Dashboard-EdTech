# Dashboard EdTech

# 🎓 EdTech Analytics Dashboard: Central de Performance & Sucesso do Aluno

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.15%2B-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

Uma solução completa de **Business Intelligence & Data Analytics para EdTechs**, desenvolvida para monitorar o desempenho de alunos do ensino médio/pré-vestibular, estratégias de aprovação universitária, fatores de risco socioemocionais e planos de intervenção pedagógica.

---

## 📌 O que é o projeto?

Em ambientes acadêmicos competitivos, o acompanhamento do progresso dos alunos por meio de planilhas descentralizadas gera fragmentação de dados e atraso nas tomadas de decisão. 

Este projeto transforma dados educacionais multivariados em um **Produto de Dados** interativo. Ele oferece uma estrutura de análise em dois níveis:

**Visão Geral da Turma (Cohort Analytics):**
- Painel de Indicadores Gerais (KPIs): Apresenta métricas agregadas instantâneas, como o total de alunos monitorados, médias de notas no ENEM e simulados, além do volume de atendimentos pendentes.

- Mapeamento de Demanda por Cursos: Gráficos interativos para visualizar quais carreiras e áreas têm maior procura pelos alunos.

- Monitoramento Socioemocional e Fatores de Risco: Painel dedicado à identificação de alunos com alertas de saúde mental ou vulnerabilidades, integrando esses fatores à gestão de risco acadêmico.

- Gestão de Intervenções e Atendimentos: Controle de fila de prioridades (alta, média, baixa) e status de agendamento de reuniões pedagógicas mês a mês.

- Filtros Dinâmicos: Segmentação de dados por unidade/escola, maturidade da escolha de curso e nível de risco.

**Painel Estratégico por Aluno (Student Deep-Dive):**
- Tabela de Decisão e Estratégia de Opções (Planos A a F): Mapeamento detalhado dos vestibulares desejados pelo aluno, calculando automaticamente a margem entre a nota atual e a nota de corte para classificar a viabilidade (Atingimento, Dentro da Nota ou Reconsiderar).

- Evolução Histórica por Área do Conhecimento: Gráficos comparativos de desempenho entre edições do ENEM e simulados, destacando automaticamente pontos de evolução, estabilidade ou regressão.

- Acompanhamento de Treineiros e Processos Seletivos: Registro e análise de desempenho em exames específicos (FUVEST, UNICAMP, VUNESP, etc.) e aprovação de fases.

- Histórico e Parecer de Orientação: Área dedicada para anotações do orientador pedagógico, histórico comportamental e plano de ação individualizado.

- Controle de Isenções e Bolsas de Estudo: Mapeamento de prazos, critérios de bolsas e status das inscrições do estudante.

---

## 🚀 Diferenciais: Funcionalidades e Impacto de Negócio
  
* **Motor de Probabilidade de Aprovação:** Cálculo automático da diferença entre a nota do aluno e a nota de corte das universidades, classificando dinamicamente a viabilidade das estratégias (*Reconsiderar*, *Plano de Atingimento*, *Dentro da Nota*).
  
* **Monitoramento Socioemocional e de Risco:** Integração de indicadores qualitativos (contexto familiar, saúde mental) com métricas quantitativas para priorizar intervenções da equipe de orientação.
  
* **Filtros Multidimensionais:** Segmentação simples por unidade escolar, nível de maturidade da escolha profissional e prioridade de atendimento.

---

## 🛠️ Arquitetura e Tecnologias

* **[Streamlit](https://streamlit.io/):** Framework para construção da interface Web, gerenciamento de estado (`session_state`), navegação modular em abas e colunas.

* **HTML5 & CSS3 Customizado:** Injeção de estilos para *design system* próprio (fontes *Google Fonts*, botões interativos, badges de status, alertas e componentes acessíveis).

* **Processamento e Tratamento de Dados (ETL):** [Pandas](https://pandas.pydata.org/)

* **Formatos de Dados:** Estruturas CSV e JSON para manipulação do estado da aplicação e estruturas de dados.
  
---
## 💡 Como Navegar na Dashboard

- **Visão Geral:** Utilize os filtros na barra lateral para isolar unidades escolares específicas ou níveis de maturidade da turma. Identifique os alunos que demandam suporte prioritário através das métricas de intervenção.

- **Visão Individual:** Analise a trajetória do aluno ao longo das edições do ENEM, acompanhe o atingimento em relação aos cursos desejados e consulte o parecer técnico do orientador.

---
## 🧪 Validação e Qualidade da Aplicação (QA)

Para garantir a estabilidade, precisão dos cálculos acadêmicos e fluidez da aplicação, foram aplicadas boas práticas de Garantia de Qualidade (QA) durante o desenvolvimento:

- **Validação de Cálculos e Regras de Negócio:** Testes de consistência na geração dinâmica de métricas — como cálculo de margem em relação à nota de corte (diferencial de pontos), classificação automática do status dos planos (*Atingimento*, *Dentro da Nota*, *Reconsiderar*) e evolução percentual no ENEM.

- **Tratamento de Exceções e Resiliência (Fallback Data):** Implementação de estratégias de manipulação de erros com para assegurar o carregamento gracioso da dashboard caso o arquivo de dados apresente valores nulos ou formatação inconsistente.

---

# 👩‍💻 Autora e Contato
> **Isabela Bueno**
> Psicóloga Escolar | Analista Educacional Sênior | Data & Tech Enabler (QA & Python)

📧 **E-mail:** isabelabueno.tech@gmail.com

💼 **LinkedIn:** isabela-bueno-silva

🐱 **GitHub:** @isabelabuenotech
