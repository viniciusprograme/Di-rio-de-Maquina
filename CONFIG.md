# 🔧 Configurações do Projeto

Este documento explica como as configurações são automaticamente importadas para novos desenvolvedores.

## 📦 Como Funcionam as Configurações

### 1. **Arquivos Versionados (Git)**

Esses arquivos são automáticamente baixados quando você faz `git clone`:

```
.streamlit/config.toml          ✅ Tema e configuração Streamlit
requirements.txt                ✅ Dependências Python
.gitignore                       ✅ Arquivos ignorados
LICENSE                          ✅ Licença MIT
```

**Resultado:** Quando você faz clone, essas configurações já vêm prontas!

---

### 2. **Arquivos Gerados Automaticamente**

O script `setup.py` cria automaticamente:

```
.env                            ← Criado de .env.example
.streamlit/                      ← Diretório criado
.streamlit/config.toml           ← Config padrão do Streamlit (se não existir)
```

---

## ⚡ Fluxo de Setup Automático

```
git clone repositório
    ↓
python setup.py  (script cria configurações locais)
    ↓
pip install -r requirements.txt
    ↓
streamlit run app.py
    ↓
🚀 App rodando com todas as configs!
```

---

## 📋 O que Cada Configuração Faz

### `.streamlit/config.toml`
Define:
- 🎨 Cores do tema (azul #1565c0)
- 🌙 Fundo escuro (#111820)
- 📝 Fonte padrão
- ⚙️ Porta (8501)

### `.env`
Define:
- 📁 Nome do arquivo CSV
- 📊 Formato de exportação (xlsx)
- 📊 Log level

### `requirements.txt`
Especifica:
- 🌊 Streamlit 1.39.0
- 🐼 Pandas 2.2.0
- 📚 OpenPyXL 3.1.2

---

## ✅ Verificar se Está Tudo Configurado

```bash
# Verificar se .env existe
ls -la .env

# Verificar se .streamlit/config.toml existe
ls -la .streamlit/config.toml

# Testar importações
python -c "import streamlit, pandas, openpyxl; print('✅ Tudo OK!')"
```

---

## 🆘 Solução de Problemas

### Problema: "ModuleNotFoundError: No module named 'streamlit'"
**Solução:**
```bash
pip install -r requirements.txt
```

### Problema: ".env arquivo não existe"
**Solução:**
```bash
python setup.py
```

### Problema: "Caminho do .streamlit/config.toml inválido"
**Solução:**
```bash
mkdir -p .streamlit
python setup.py
```

---

## 📝 Customização de Configurações

Se você quiser mudar algo:

1. **Cores do Streamlit:**
   - Edite `.streamlit/config.toml`
   - Reinicie o app: `streamlit run app.py`

2. **Variáveis de Ambiente:**
   - Edite `.env`
   - Reinicie o app

3. **Dependências:**
   - Edite `requirements.txt`
   - Execute: `pip install -r requirements.txt`

**Nota:** Não faça commit de `.env` (está em `.gitignore`). Apenas `.env.example` deve ser versionado!

---

## 🚀 Para Novos Colaboradores

1. Clone o repositório
2. Execute `python setup.py`
3. Instale dependências: `pip install -r requirements.txt`
4. Pronto! Tudo configurado automaticamente ✨

