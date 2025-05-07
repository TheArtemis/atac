from enum import Enum
from pydantic import BaseModel


class MetroLine(str, Enum):
    A = "A"
    B = "B"
    B1 = "B1"
    C = "C"


class MetroStation(BaseModel):
    name: str
    latitude: float
    longitude: float
    line: list[MetroLine]
