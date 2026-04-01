# Diário de Bordo — Máquinas

Aplicativo Streamlit para registro e gestão de operação de equipamentos (KAL, RS, EP).

## 🚀 Instalação

1. **Clone ou copie o projeto**
   ```bash
   cd seu_projeto
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente (opcional)**
   ```bash
   cp .env.example .env
   # Edite o arquivo .env conforme necessário
   ```

## ▶️ Executar

```bash
streamlit run app.py
```

O app será aberto em `http://localhost:8501`

## 📋 Funcionalidades

- **📝 Novo Registro**: Preencher formulário com dados de operação
- **📋 Registros**: Visualizar, filtrar e exportar dados (CSV/Excel)
- **📊 Resumo**: Gráficos e estatísticas de operação por equipamento e operador

## 📁 Estrutura

```
.
├── app.py                    # Aplicação principal
├── requirements.txt          # Dependências Python
├── .env.example             # Exemplo de variáveis de ambiente
├── .gitignore               # Arquivos ignorados pelo Git
└── registros_maquinas.csv   # Base de dados (gerado automaticamente)
```

## 🛠️ Tecnologias

- **Streamlit** → Framework web
- **Pandas** → Manipulação de dados
- **OpenPyXL** → Geração de Excel

## 📝 Notas

- Os dados são salvos em `registros_maquinas.csv`
- Exportações em Excel são geradas dinamicamente
- O arquivo `.env` não é versionado (está em `.gitignore`)

---

**Desenvolvido com ❤️**
