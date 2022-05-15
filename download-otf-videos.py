import yt_dlp as youtube_dl


def download_videos(url):

    video_container = "mp4"
    ydl_opts = {
        "outtmpl": "otf-videos/%(title)s.%(ext)s",
        "merge_output_format": video_container,
        "format": "best[height<=720]",
        "quiet": False,
        "writeautomaticsub": True,
        "writesub": True,
        "nooverwrites": True,
        "subtitleslangs":['en']
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with ydl:
        result = ydl.extract_info(
            url,
            download=False
        )

    if 'entries' in result:
        for v in range(len(result['entries'])):
            try:
                ydl.download([result['entries'][v]['webpage_url']])
                print("Downloaded:", result['entries'][v]['title'])
            except:
                print("Error, quitting")
                exit
    else:
        exit

if __name__ == '__main__':
    result = download_videos('https://www.youtube.com/watch?v=MxkuqFyrSIc&list=PLeSKM0GTcnfE1c-yI8y-x5O2rdM3X9mZD')
    print("All done!")