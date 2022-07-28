from yt_dlp import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

def search(args):
    with YoutubeDL(params=YDL_OPTIONS) as ydl:
        video = ydl.extract_info(f"ytsearch10:{arg}", download=False)
        return video