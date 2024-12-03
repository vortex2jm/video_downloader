import yt_dlp
import time
import os

# Audio setup
YDL_OPTS_AUDIO = {
    'format': 'bestaudio/best',             
    'outtmpl': '%(title)s.%(ext)s',         
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',        
        'preferredcodec': 'mp3',            
        'preferredquality': '192',          
    }],
    'noplaylist': True                    
}

# Video setup
YDL_OPTS_VIDEO_MP4 = {
    'format': 'bestvideo+bestaudio/best',   
    'outtmpl': '%(title)s.%(ext)s',         
    'merge_output_format': 'mp4',           
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',      
        'preferedformat': 'mp4',            
    }],
    'noplaylist': True         
}

# Video setup without convertion
YDL_OPTS_VIDEO_WEBM = {
  'format': 'bestvideo+bestaudio/best',  
  'outtmpl': '%(title)s.%(ext)s',        
  'noplaylist': True
}

# Download function=============================
def download_media(url: str, opts: dict) -> str:
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            dwl_info = ydl.extract_info(url, download=True)
            return dwl_info['title']
    except Exception as e:
        print(f'Something went wrong - {e}')
        return None

# Menu====
def main():
    while True:
        print("===YouTube Downloader===")
        print("1 - Download Music")
        print("2 - Download Video")
        print("0 - Exit")


        #  Setup options
        dwl_option = input("\n-> ")
        pll_opt = input("\nActivate playlist mode? (y/n): ")
        if pll_opt == "y":
            YDL_OPTS_AUDIO["noplaylist"]=False
            YDL_OPTS_VIDEO_MP4['noplaylist']=False
            YDL_OPTS_VIDEO_WEBM['noplaylist']=False
        elif pll_opt == "n":
            YDL_OPTS_AUDIO["noplaylist"]=True
            YDL_OPTS_VIDEO_MP4['noplaylist']=True
            YDL_OPTS_VIDEO_WEBM['noplaylist']=True
        else:
            print("\nInvalid option\n")
            continue


        #  Music download
        if dwl_option == "1":
            media_url = input("URL: ")
            download_media(media_url, YDL_OPTS_AUDIO)
            exit(0)


        # Video download
        elif dwl_option == "2":
            format = input("\nFormat (1 - webm / 2 - mp4): ")

            if format == "1":  # webm
                media_url = input("URL: ")
                download_media(media_url, YDL_OPTS_VIDEO_WEBM)
                exit(0)

            elif format == "2": # mp4
                media_url = input("URL: ")
                download_media(media_url, YDL_OPTS_VIDEO_MP4)
                exit(0)

            else: # Invalid
                print("\nInvalid option\n")
                continue
        
        # Exit mode
        elif dwl_option == "0":
            print("Bye bye...")
            time.sleep(1)
            os.system("clear")
            exit(0)

        # Invalid
        else:
            print("Invalid option\n")   

# ========================
if __name__ == '__main__':
    main()
