import csv
from typing import List, Optional
from datetime import datetime
from models.reading import EnergyReading

class DataIngestionService:
    def parse_csv_line(self, line: str) -> Optional[EnergyReading]:
        try:
            # Use csv.reader to correctly handle quoted values and extra spaces
            reader = csv.reader([line.strip()], skipinitialspace=True)
            parts = next(reader)
            
            if len(parts) != 5:
                return None
                
            return EnergyReading(
                timestamp=datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S"),
                device_id=parts[1],
                voltage=float(parts[2]),
                current=float(parts[3]),
                power_factor=float(parts[4])
            )
        except (ValueError, StopIteration):
            return None

    def load_file(self, filepath: str) -> List[EnergyReading]:
        readings = []
        with open(filepath, 'r') as f:
            for line in f:
                reading = self.parse_csv_line(line)
                if reading:
                    readings.append(reading)
        return readings
