# Script para commit automático a cada mudança
# Salve como: auto-push.ps1

param(
    [int]$IntervalSeconds = 300  # 5 minutos
)

Write-Host "🚀 Sincronizador Automático iniciado..."
Write-Host "Intervalo: $IntervalSeconds segundos"
Write-Host "Pressione CTRL+C para parar`n"

$repoPath = Split-Path -Parent $MyInvocation.MyCommandPath

while ($true) {
    Set-Location $repoPath
    
    $status = git status -s
    
    if ($status) {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Mudanças detectadas!" -ForegroundColor Green
        
        git add -A
        $message = "docs: atualização automática - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git commit -m $message
        
        $pushResult = git push origin main 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✅ Push realizado com sucesso`n" -ForegroundColor Green
        } else {
            Write-Host "❌ Erro no push: $pushResult`n" -ForegroundColor Red
        }
    } else {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Sem mudanças detectadas" -ForegroundColor Gray
    }
    
    Start-Sleep -Seconds $IntervalSeconds
}
