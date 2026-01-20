import csv
from typing import List
from datetime import datetime
from models.reading import EnergyReading

class DataIngestionService:
    def load_file(self, filepath: str) -> List[EnergyReading]:
        readings = []
        try:
            with open(filepath, 'r') as f:
                # SKIP HEADER
                next(f)
                for line in f:
                    # BUG: Naive splitting will fail on quoted strings or varying formats
                    parts = line.strip().split(',')
                    if len(parts) != 5:
                        continue
                    
                    try:
                        readings.append(EnergyReading(
                            timestamp=datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S"),
                            device_id=parts[1],
                            voltage=float(parts[2]),
                            current=float(parts[3]),
                            power_factor=float(parts[4])
                        ))
                    except (ValueError, IndexError):
                        continue
        except FileNotFoundError:
            pass
        return readings
