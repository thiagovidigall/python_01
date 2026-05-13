#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
import yt_dlp


def get_video_formats(url):
    """Obtém os formatos disponíveis do vídeo."""
    try:
        with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
            info = ydl.extract_info(url, download=False)
            return info['formats'], info['title']
    except Exception as e:
        print(f"[ERROR] Erro ao obter informacoes do video: {e}")
        return None, None


def list_formats(formats):
    """Lista os formatos disponíveis de forma legível."""
    video_formats = {}

    for fmt in formats:
        if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none':
            res = fmt.get('height', 'unknown')
            fps = fmt.get('fps', 'unknown')
            ext = fmt.get('ext', 'unknown')
            format_id = fmt.get('format_id')

            quality_str = f"{res}p @ {fps}fps ({ext})"
            video_formats[format_id] = quality_str

    print("\n[VIDEO FORMATS AVAILABLE]\n")
    for i, (fmt_id, quality) in enumerate(video_formats.items(), 1):
        print(f"{i}. {quality} (ID: {fmt_id})")

    return video_formats


def download_video(url, format_id, output_path):
    """Baixa o vídeo com o formato escolhido."""
    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }

    try:
        print(f"\n[DOWNLOAD] Iniciando download...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("[SUCCESS] Download concluido com sucesso!")
    except Exception as e:
        print(f"[ERROR] Erro ao baixar video: {e}")


def main():
    output_dir = Path("downloads")
    output_dir.mkdir(exist_ok=True)

    print("=" * 50)
    print("YouTube Video Downloader")
    print("=" * 50)

    url = input("\nDigite a URL do video do YouTube: ").strip()

    if not url:
        print("[ERROR] URL invalida!")
        sys.exit(1)

    print("\n[*] Obtendo informacoes do video...")
    formats, title = get_video_formats(url)

    if not formats:
        sys.exit(1)

    print(f"[*] Video: {title}")

    video_formats = list_formats(formats)

    if not video_formats:
        print("[ERROR] Nenhum formato de video + audio encontrado!")
        sys.exit(1)

    choice = input(f"\nEscolha o numero da qualidade desejada (1-{len(video_formats)}): ").strip()

    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(video_formats):
            format_id = list(video_formats.keys())[choice_idx]
            download_video(url, format_id, str(output_dir))
        else:
            print("[ERROR] Opcao invalida!")
            sys.exit(1)
    except ValueError:
        print("[ERROR] Digite um numero valido!")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Download cancelado pelo usuario!")
        sys.exit(0)
