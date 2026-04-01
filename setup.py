#!/usr/bin/env python3
"""
Script de Setup para o Diário de Bordo — Máquinas

Este script configura o ambiente automaticamente:
1. Copia .env.example para .env (se não existir)
2. Cria diretório .streamlit (se não existir)
3. Verifica dependências
4. Exibe instruções finais
"""

import os
import shutil
import sys
from pathlib import Path

def setup():
    print("\n" + "="*50)
    print("🚀 Setup do Diário de Bordo — Máquinas")
    print("="*50 + "\n")
    
    project_root = Path(__file__).parent
    
    # 1. Copiar .env.example para .env
    env_example = project_root / ".env.example"
    env_file = project_root / ".env"
    
    if env_example.exists() and not env_file.exists():
        print("📋 Copiando .env.example → .env...")
        shutil.copy(env_example, env_file)
        print("✅ Arquivo .env criado\n")
    elif env_file.exists():
        print("✅ Arquivo .env já existe\n")
    
    # 2. Criar diretório .streamlit
    streamlit_dir = project_root / ".streamlit"
    if not streamlit_dir.exists():
        print("📁 Criando diretório .streamlit...")
        streamlit_dir.mkdir(exist_ok=True)
        print("✅ Diretório criado\n")
    else:
        print("✅ Diretório .streamlit já existe\n")
    
    # 3. Copiar config.toml se não existir
    config_example = streamlit_dir / "config.toml"
    if not config_example.exists():
        print("⚙️ Criando configuração padrão do Streamlit...")
        config_content = """[theme]
primaryColor = "#1565c0"
backgroundColor = "#111820"
secondaryBackgroundColor = "#1b2533"
textColor = "#dde6f0"
font = "sans serif"

[client]
showErrorDetails = true
toolbarMode = "auto"

[logger]
level = "info"

[server]
port = 8501
headless = true
"""
        config_example.write_text(config_content)
        print("✅ config.toml criado\n")
    else:
        print("✅ config.toml já existe\n")
    
    # 4. Verificar se requirements.txt existe
    requirements_file = project_root / "requirements.txt"
    if requirements_file.exists():
        print("📦 Para instalar dependências, execute:")
        print("   pip install -r requirements.txt\n")
    
    print("="*50)
    print("✨ Setup concluído com sucesso!")
    print("="*50)
    print("\n🚀 Para iniciar a aplicação:")
    print("   streamlit run app.py\n")

if __name__ == "__main__":
    try:
        setup()
    except Exception as e:
        print(f"\n❌ Erro durante o setup: {e}")
        sys.exit(1)
