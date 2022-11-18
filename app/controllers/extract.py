from ..includes import database as db
from ..services import extract as ExtractService

async def youtube_metadata(id: str):
    data = await ExtractService.youtube_metadata(id)
    return data


async def googleplay_metadata(package: str):
    return ""

    