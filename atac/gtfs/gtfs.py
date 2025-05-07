from google.transit import gtfs_realtime_pb2
import requests

ROME_TRANSIT_DATA_URL = "https://dati.comune.roma.it/catalog/dataset/a7dadb4a-66ae-4eff-8ded-a102064702ba/resource/d2b123d6-8d2d-4dee-9792-f535df3dc166/download/rome_vehicle_positions.pb"


def fetch_gtfs_feed(url, timeout=10):
    """
    Fetch GTFS realtime feed from the given URL.

    Args:
        url (str): URL of the GTFS realtime feed
        timeout (int): Request timeout in seconds

    Returns:
        bytes: Raw content of the feed

    Raises:
        requests.exceptions.RequestException: If there's an error fetching the feed
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.content


def parse_gtfs_feed(feed_content):
    """
    Parse GTFS realtime feed content using protobuf.

    Args:
        feed_content (bytes): Raw content of the feed

    Returns:
        gtfs_realtime_pb2.FeedMessage: Parsed feed

    Raises:
        Exception: If there's an error parsing the feed
    """
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(feed_content)
    return feed


def extract_vehicle_information(feed, filter_by_route_id=None):
    """
    Extract relevant vehicle information from GTFS feed.

    Args:
        feed (gtfs_realtime_pb2.FeedMessage): Parsed GTFS feed

    Returns:
        list: List of dictionaries containing vehicle information
    """
    vehicles = []

    for entity in feed.entity:
        if entity.HasField("vehicle"):
            vehicle_info = {"id": entity.id}
            vehicle_position = entity.vehicle

            # Extract position data
            if vehicle_position.HasField("position"):
                position = vehicle_position.position
                vehicle_info["latitude"] = position.latitude
                vehicle_info["longitude"] = position.longitude

                if position.HasField("bearing"):
                    vehicle_info["bearing"] = position.bearing

                if position.HasField("speed"):
                    vehicle_info["speed"] = position.speed

            # Extract trip data
            if vehicle_position.HasField("trip"):
                trip = vehicle_position.trip
                vehicle_info["trip_id"] = trip.trip_id

                if trip.HasField("route_id"):
                    vehicle_info["route_id"] = trip.route_id

            if (
                filter_by_route_id
                and vehicle_info.get("route_id") not in filter_by_route_id
            ):
                continue
            vehicles.append(vehicle_info)

    return vehicles


def print_vehicle_information(vehicles):
    """
    Print formatted vehicle information.

    Args:
        vehicles (list): List of dictionaries containing vehicle information
    """
    for vehicle in vehicles:
        print(f"Vehicle ID: {vehicle['id']}")

        if "latitude" in vehicle and "longitude" in vehicle:
            print(f"  Latitude: {vehicle['latitude']}")
            print(f"  Longitude: {vehicle['longitude']}")

            if "bearing" in vehicle:
                print(f"  Bearing: {vehicle['bearing']}")

            if "speed" in vehicle:
                print(f"  Speed: {vehicle['speed']}")

        if "trip_id" in vehicle:
            print(f"  Trip ID: {vehicle['trip_id']}")

            if "route_id" in vehicle:
                print(f"  Route ID: {vehicle['route_id']}")

        print("-" * 20)  # Separator for clarity


def get_rome_transit_data():
    """
    Main function to fetch, parse and display Rome transit data.
    """
    url = "https://dati.comune.roma.it/catalog/dataset/a7dadb4a-66ae-4eff-8ded-a102064702ba/resource/d2b123d6-8d2d-4dee-9792-f535df3dc166/download/rome_vehicle_positions.pb"

    try:
        # Fetch the GTFS feed
        feed_content = fetch_gtfs_feed(url)

        # Parse the feed
        feed = parse_gtfs_feed(feed_content)

        # Extract vehicle information
        vehicles = extract_vehicle_information(feed)

        # Print vehicle information
        print_vehicle_information(vehicles)

        # Return the vehicle data for potential further use
        return vehicles

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the GTFS Realtime feed: {e}")
        return None
    except Exception as e:
        print(f"Error parsing the GTFS Realtime feed: {e}")
        return None


# Example usage
if __name__ == "__main__":
    get_rome_transit_data()
