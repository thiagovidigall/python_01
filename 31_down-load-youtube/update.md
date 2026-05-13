# Opcoes para disponibilizar a ferramenta globalmente

## 1. Alias no PowerShell Profile (mais simples)

Adiciona uma funcao no perfil do PowerShell que roda o script de qualquer lugar.

```powershell
# Abre o profile
notepad $PROFILE

# Adiciona isso dentro:
function ytdl { python "C:\_dev_work\code-dev\05_down-load-youtube\youtube_downloader.py" @args }
```

Depois e so digitar `ytdl` em qualquer terminal PowerShell.

- Pro: Simples, facil de remover
- Contra: So funciona no PowerShell

---

## 2. Criar um .bat em uma pasta do PATH

Cria um `ytdl.bat` em `C:\Windows\System32` ou em qualquer pasta que ja esta no PATH.

```bat
@echo off
python "C:\_dev_work\code-dev\05_down-load-youtube\youtube_downloader.py" %*
```

Funciona em CMD e PowerShell.

- Pro: Universal, funciona em qualquer terminal
- Contra: Coloca arquivo em pasta do sistema

---

## 3. Pasta pessoal de scripts no PATH

Cria uma pasta `C:\scripts\`, coloca o `.bat` la, e adiciona essa pasta ao PATH do sistema
nas variaveis de ambiente do Windows.

- Pro: Organizado, sem mexer no sistema
- Contra: Precisa configurar o PATH uma vez

---

## 4. Instalar como pacote Python (pip install -e .)

Cria um `pyproject.toml` com entry point e instala com `pip install -e .`
O comando `ytdl` vira um executavel nativo do Python.

- Pro: Profissional, isolado, como qualquer ferramenta pip
- Contra: Um pouco mais de configuracao inicial

---

## 5. Empacotar com PyInstaller (.exe)

Gera um `.exe` standalone que nao depende do Python instalado.

```bash
pyinstaller --onefile youtube_downloader.py
```

- Pro: Portavel, funciona sem Python instalado, pode distribuir
- Contra: Arquivo grande (~10MB), rebuild a cada mudanca

---

## Resumo

| Objetivo                      | Opcao                       |
|-------------------------------|-----------------------------|
| Uso pessoal rapido            | 1 - Alias no PowerShell     |
| Uso no CMD tambem             | 2 ou 3 - .bat no PATH       |
| Projeto profissional          | 4 - pip install -e .        |
| Distribuir para outras pessoas| 5 - PyInstaller .exe        |
