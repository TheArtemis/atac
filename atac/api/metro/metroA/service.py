from atac.models.metro_station import MetroStation
from atac.models.metro_station import MetroLine
from atac.constants.metro_line import METRO_LINE_A


async def get_closest_station(
    latitude: float, longitude: float, metro_line: MetroLine
) -> MetroStation:
    if metro_line == MetroLine.A:
        line = METRO_LINE_A  # TODO fix this
        closest = None
        min_distance = float("inf")
        for station in line:
            distance = (  # TODO is this the best way to calculate distance?
                (station.latitude - latitude) ** 2
                + (station.longitude - longitude) ** 2
            ) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest = station
        return closest
    else:
        raise ValueError("Unsupported metro line")


if __name__ == "__main__":
    # Example usage
    closest_station = get_closest_station(41.8916, 12.4833, MetroLine.A)
    print(closest_station)
