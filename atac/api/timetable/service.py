from atac.api.timetable.model import TimingsRequest
from atac.config.settings import atac
from atac.common.url import Url
from atac.config.logger import get_logger
from atac.common.request import get
from .model import Timings

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
    data = await get(url.get())

    timings = Timings(**data)
    logger.info(f"Fetched timings: {timings}")
    return timings
