from dataclasses import dataclass
from datetime import datetime

@dataclass
class EnergyReading:
    timestamp: datetime
    device_id: str
    voltage: float
    current: float
    power_factor: float
