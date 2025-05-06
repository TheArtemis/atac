from atac.api.timetable.model import PathCode, TimingsRequest
from atac.api.timetable.service import get_timings


async def test_get_timings():
    request = TimingsRequest(
        path_code=PathCode.metroA_anagnina_battistini, days_from_now=2
    )

    response = await get_timings(request)
    assert response is not None


async def main():
    await test_get_timings()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
