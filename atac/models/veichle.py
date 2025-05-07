from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class VehiclePosition(BaseModel):
    id: str
    latitude: float
    longitude: float
    bearing: Optional[float] = None
    speed: Optional[float] = None
    trip_id: str = None
    route_id: str = None
    timestamp: str = datetime.now().isoformat()
