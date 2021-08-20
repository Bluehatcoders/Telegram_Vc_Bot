# Credits On ReadMe.md

from os import path

from youtube_dl import YoutubeDL

from config import BOT_USERNAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError
ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"❌{DURATION_LIMIT} minute(s) se jayada ka song diya to mai nhi bajaunga, abhi jo tune diya hai wo {duration} minute(s) ki hai :("
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"❌{DURATION_LIMIT} minute(s) se jayada ka song diya to mai nhi bajaunga, abhi jo tune diya hai wo {duration} minute(s) ki hai :("
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
