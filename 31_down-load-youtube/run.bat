@echo off
chcp 65001 >nul
echo ========================================
echo YouTube Video Downloader
echo ========================================

if not exist venv (
    echo [ERROR] Ambiente virtual nao encontrado!
    echo [*] Execute setup.ps1 primeiro.
    echo.
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python youtube_downloader.py
pause
