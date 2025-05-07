from atac.gtfs.metroA import get_metroA_data
from atac.models.veichle import VehiclePosition


async def test_get_metroA_data():
    """
    Test the get_metroA_data function.
    """
    data = await get_metroA_data()

    # Check if the data is a list
    assert isinstance(data, list)

    # Check if each item in the list is a VehiclePosition object
    for item in data:
        assert isinstance(item, VehiclePosition)
        print(item)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_get_metroA_data())
