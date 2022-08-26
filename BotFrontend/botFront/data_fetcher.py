import aiohttp
from . local_setting import WORDS_API_URL_RANDOM

async def get_word_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

