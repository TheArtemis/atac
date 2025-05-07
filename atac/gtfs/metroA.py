from atac.gtfs.gtfs import (
    fetch_gtfs_feed,
    parse_gtfs_feed,
    extract_vehicle_information,
    ROME_TRANSIT_DATA_URL,
)
from atac.models.veichle import VehiclePosition


async def get_metroA_data() -> list[VehiclePosition]:
    feed = fetch_gtfs_feed(ROME_TRANSIT_DATA_URL)

    parsed = parse_gtfs_feed(feed)

    info = extract_vehicle_information(parsed, filter_by_route_id=["nMA"])

    vehicles = [
        VehiclePosition(
            id=vehicle["id"],
            latitude=vehicle["latitude"],
            longitude=vehicle["longitude"],
            bearing=vehicle.get("bearing"),
            speed=vehicle.get("speed"),
            trip_id=vehicle.get("trip_id"),
            route_id=vehicle.get("route_id"),
        )
        for vehicle in info
    ]

    return vehicles
