import json
from sys import getsizeof

# Simple Fastapi server
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, ORJSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from yt_dlp import YoutubeDL


def format_selector(ctx):
    """ Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases """

    # formats are already sorted worst to best
    formats = ctx.get('formats')[::-1]

    # acodec='none' means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != 'none' and f['acodec'] == 'none')

    # find compatible audio extension
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    # vcodec='none' means there is no video
    best_audio = next(f for f in formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    # These are the minimum required fields for a merged format
    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        # Must be + separated list of protocols
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }


YDL_OPTIONS = {
    'quiet': True,
    'no_warnings': True,
    'forcejson': False,
    'dump_single_json': False,
    'writedescription': False,
    'writeinfojson': False,
    'noprogress': True,
    'format': "b",
    'allow_unplayable_formats': False,
    'allow_multiple_video_streams': False,
    'allow_multiple_audio_streams': False,
    'clean_infojson': True,
    'getcomments': False,
    'listsubtitles': False,
    'noplaylist':True,
    'check_formats':False,
}
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.post("/search/", response_class=JSONResponse)
async def search(search: str = Form()):
    print(search)
    with YoutubeDL(params=YDL_OPTIONS) as ydl:
        results = ydl.extract_info(f"ytsearch10:{search}", download=False)
        with open("test_results.json", "w") as f:
            json.dump(results, f, indent=4)
        return results

@app.get("/ping")
async def ping():
    return {"message": "pong"}
