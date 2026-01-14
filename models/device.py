from dataclasses import dataclass
from typing import Optional

@dataclass
class Device:
    device_id: str
    name: str
    location: str
    power_rating_watts: float
    is_active: bool = False
