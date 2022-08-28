import aiohttp
from .local_setting import WORDS_API_URL_Street, WORDS_API_URL_Home, WORDS_API_URL_Food

async def get_word_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()




