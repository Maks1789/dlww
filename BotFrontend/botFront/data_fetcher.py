import aiohttp
import random
async def get_word_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

