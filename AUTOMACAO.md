# 🔄 Automação Git

## **Opção 1: GitHub Actions (Automático na Nuvem)**

✅ Já configurado! O arquivo `.github/workflows/auto-commit.yml` faz:
- Commit automático a cada 30 minutos
- Detecta mudanças no repositório
- Envia para o GitHub automaticamente

**Vantagens:**
- Funciona na nuvem (sem depender do seu PC)
- Seguro e confiável
- Sem necessidade de scripts locais

---

## **Opção 2: Script PowerShell (Local)**

Para rodar manualmente no seu computador:

### Passo 1: Permitir Scripts
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Passo 2: Executar o Script
```powershell
cd c:\Users\Vinicius\Desktop\PASTA
.\auto-push.ps1
```

### Passo 3: Rodar em Background (Opcional)
```powershell
Start-Process powershell -ArgumentList ".\auto-push.ps1" -WindowStyle Hidden
```

**Intervalo Customizável:**
```powershell
.\auto-push.ps1 -IntervalSeconds 600  # 10 minutos
.\auto-push.ps1 -IntervalSeconds 60   # 1 minuto
```

**Vantagens:**
- Sincronização em tempo real
- Controle total local
- Pode ajustar intervalo

---

## **Opção 3: Criar Tarefa Agendada (Windows)**

### Via PowerShell:
```powershell
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Users\Vinicius\Desktop\PASTA\auto-push.ps1"
$trigger = New-ScheduledTaskTrigger -AtStartup
Register-ScheduledTask -TaskName "GitAutoSync" -Action $action -Trigger $trigger -RunLevel Highest
```

Agora o script roda **automaticamente ao iniciar o Windows**!

---

## **Recomendação**

Para este projeto, recomendo usar **GitHub Actions** (Opção 1):
- ✅ Já está configurado
- ✅ Funciona 24/7
- ✅ Sem necessidade de seu PC ligado
- ✅ Rastreia mudanças automaticamente

Próximo passo: Faça um push para ativar o workflow!

```bash
git add .
git commit -m "feat: adicionar automação com GitHub Actions"
git push origin main
```

Depois acesse: https://github.com/viniciusprograme/Di-rio-de-Maquina/actions
