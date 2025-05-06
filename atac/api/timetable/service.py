import aiohttp
from atac.api.timetable.model import TimingsRequest
from atac.config.settings import atac
from atac.common.url import Url
from atac.config.logger import get_logger

logger = get_logger()


async def get_timings(request: TimingsRequest):
    url = Url(
        base_url=atac.atac_timings_url,
        params={
            "pathCode": request.path_code.value,
            "daysFromNow": request.days_from_now,
        },
    )

    logger.info(f"Fetching timings from {url}")

    # Make Request
    async with aiohttp.ClientSession() as session:
        # Define headers to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            # 'Referer': 'https://www.google.com/', # Uncomment and set if you want to simulate traffic coming from a specific page
        }

        try:
            async with session.get(url.get(), headers=headers) as response:
                response.raise_for_status()

                logger.info(
                    f"Fetched timings: {response.status}"
                )  # Log status instead of the whole response object
                # You can add further processing of the response here

                data = await response.json()
                logger.info(f"Fetched timings: {data}")

                return data

        except aiohttp.ClientResponseError as e:
            logger.error(f"HTTP error fetching timings: {e}")
            raise e
        except aiohttp.ClientConnectorError as e:
            logger.error(f"Connection error fetching timings: {e}")
            raise e
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise e
