# Eu
 "Criei uma ferramenta CLI em Python para download de vídeos do YouTube usando yt-dlp."
 

# YouTube Video Downloader 🎬

Um app simples em Python para baixar vídeos do YouTube com escolha de qualidade.

## Instalação

### 1. Clone ou navegue para o diretório do projeto

```bash
cd 05_down-load-youtube
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Como usar

```bash
python youtube_downloader.py
```

### Passo a passo:

1. Execute o script
2. Cole a URL do vídeo do YouTube
3. Visualize as qualidades disponíveis
4. Digite o número da qualidade desejada
5. O vídeo será baixado na pasta `downloads/`

## Exemplo de uso

```
==================================================
YouTube Video Downloader
==================================================

Digite a URL do video do YouTube: https://www.youtube.com/watch?v=...

[*] Obtendo informacoes do video...
[*] Video: Titulo do Video

[VIDEO FORMATS AVAILABLE]

1. 1080p @ 60fps (mp4) (ID: 313)
2. 720p @ 60fps (mp4) (ID: 308)
3. 480p @ 60fps (mp4) (ID: 303)
4. 360p @ 60fps (mp4) (ID: 298)

Escolha o numero da qualidade desejada (1-4): 1

[DOWNLOAD] Iniciando download...
[SUCCESS] Download concluido com sucesso!
```

## Funcionalidades

✓ Lista todas as qualidades disponíveis  
✓ Permite escolher a qualidade desejada  
✓ Mostra informações do vídeo  
✓ Salva na pasta `downloads/`  
✓ Interface simples e funcional  
✓ Compatível com Windows, Linux e Mac  

## Requisitos

- Python 3.7+
- yt-dlp
- FFmpeg (opcional, mas recomendado para melhor compatibilidade)

## Troubleshooting

### "ModuleNotFoundError: No module named 'yt_dlp'"
Instale as dependências: `pip install -r requirements.txt`

### Erro de permissão ao baixar
Certifique-se de que tem permissão de escrita na pasta do projeto.

### Erro ao processar vídeo
Pode ser necessário instalar o FFmpeg (opcional, mas recomendado):
- **Windows**: Baixe em https://ffmpeg.org/download.html ou use `choco install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg`
- **Mac**: `brew install ffmpeg`

### Problema com caracteres especiais no Windows
O script foi otimizado para funcionar com o Windows. Se tiver problemas, tente executar em PowerShell em vez de CMD.

## Licença

MIT
