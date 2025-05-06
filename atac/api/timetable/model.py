from enum import Enum
from pydantic import BaseModel


class PathCode(str, Enum):
    metroA_anagnina_battistini = "METROAA"  # Metro A (Anagnina -> Battistini)
    metroA_battistini_anagnina = "METROAR"  # Metro A (Battistini -> Anagnina)


class TimingElement(BaseModel):
    minute: str
    time: str


class Timings(BaseModel):
    timinglist: list[TimingElement]


class TimingsRequest(BaseModel):
    path_code: PathCode
    days_from_now: int
