# Setup script for YouTube Downloader

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "YouTube Video Downloader - Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Check if Python is installed
Write-Host "`n[*] Verificando se Python esta instalado..." -ForegroundColor Yellow
$pythonCheck = python --version 2>&1
if ($?) {
    Write-Host "[OK] Python encontrado: $pythonCheck" -ForegroundColor Green
} else {
    Write-Host "[ERROR] Python nao encontrado! Instale o Python 3.7+" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "`n[*] Criando ambiente virtual..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "[!] Ambiente virtual ja existe" -ForegroundColor Yellow
} else {
    python -m venv venv
    Write-Host "[OK] Ambiente virtual criado" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`n[*] Ativando ambiente virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Install dependencies
Write-Host "`n[*] Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "[OK] Dependencias instaladas" -ForegroundColor Green

# Create downloads folder
Write-Host "`n[*] Criando pasta de downloads..." -ForegroundColor Yellow
if (-not (Test-Path "downloads")) {
    New-Item -ItemType Directory -Path "downloads" | Out-Null
    Write-Host "[OK] Pasta 'downloads' criada" -ForegroundColor Green
} else {
    Write-Host "[!] Pasta 'downloads' ja existe" -ForegroundColor Yellow
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "[OK] Setup concluido!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nPara usar o app, execute:" -ForegroundColor Cyan
Write-Host "  python youtube_downloader.py" -ForegroundColor Yellow
Write-Host "`nOu clique em 'run.bat' para iniciar!" -ForegroundColor Yellow
