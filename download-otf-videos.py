import youtube_dl
import os
from pathlib import Path

def download_videos(url):
    
    video_container = 'mp4'
    ydl_opts = {
        'outtmpl': 'otf-videos/%(title)s.%(ext)s',
        'merge_output_format': video_container,
        'format': 'best',
        'quiet': True
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )

    if 'entries' in result:
        for v in range(len(result['entries'])):
            if os.path.exists(Path(Path('otf-videos') / str.join('', ([result['entries'][v]['title']][0], '.', video_container)))) is False:
                try:
                    ydl.download([result['entries'][v]['webpage_url']])
                    print("Downloaded:", result['entries'][v]['title'])
                except:
                    print("Error, quitting")
                    exit
            else:
                print("Already have video:", result['entries'][v]['title'])
    else:
        exit

if __name__ == '__main__':
    result = download_videos('https://www.youtube.com/watch?v=MxkuqFyrSIc&list=PLeSKM0GTcnfE1c-yI8y-x5O2rdM3X9mZD')
    print("All done!")