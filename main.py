import subprocess
import yt_dlp
import os

YDL_OPTS = {
  'format': 'bestvideo+bestaudio/best',  # Best video and audio quality
  'outtmpl': '%(title)s.%(ext)s',        # Output file name
}

def webm_to_mp4(file: str) -> None:
  if os.path.exists(file):
    title = file.replace('.webm', '')
    subprocess.run(
      f'ffmpeg -i "{file}" -c:v copy -c:a aac "{title}.mp4"',
      shell=True,
      check=True
    )
    print('Conversion done!')
    return
  print(f'Failed to find the downloaded file {file}')

def download_video(url: str) -> str:
  try:
    with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
      dwl_info = ydl.extract_info(url, download= True)
      video_title = dwl_info['title']
      return f'{video_title}.webm'
      # ydl.download([url])
    print("Download complete!")
  except Exception as e:
    print(f'Something went wrong - {e}')

if __name__ == '__main__':
  url = input("Type the YouTube URL: ")
  video_file = download_video(url)
  webm_to_mp4(video_file)
