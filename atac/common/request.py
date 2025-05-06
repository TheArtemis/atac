import aiohttp
from atac.config.logger import get_logger

logger = get_logger()

ANTI_BOT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


async def get(
    url: str,
):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=ANTI_BOT_HEADERS) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        logger.error(f"HTTP error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise e
