import subprocess
import yt_dlp
import os

YDL_OPTS = {
    'format': 'bestvideo+bestaudio/best',  
    'outtmpl': '%(title)s.%(ext)s',        
}

def webm_to_mp4(file: str) -> None:
    if os.path.exists(file):
        title = file.replace('.webm', '')
        subprocess.run(
            f'ffmpeg -i "{file}" -c:v copy -c:a aac "{title}.mp4"',
            shell=True,
            check=True
        )
        print('Conversão concluída!')
    else:
        print(f'Arquivo {file} não encontrado para conversão.')

def download_video(url: str, format: str = 'webm') -> str:
    try:
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            dwl_info = ydl.extract_info(url, download=True)
            video_title = dwl_info['title']
            return f'{video_title}.{format}'
    except Exception as e:
        print(f'Ocorreu um erro - {e}')

if __name__ == '__main__':
    url = input("Digite a URL do YouTube: ")
    output_format = input("Escolha o formato de saída (webm ou mp4): ").strip().lower()
    video_file = download_video(url, output_format)
    
    if output_format == 'mp4':
        webm_to_mp4(video_file)
    print("Download completo!")
