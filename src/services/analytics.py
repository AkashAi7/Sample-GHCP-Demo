import math
from typing import List
from models.reading import EnergyReading

class EnergyAnalytics:
    def __init__(self, base_rate: float = 0.15):
        self.base_rate = base_rate

    def calculate_complex_efficiency_score(self, readings: List[EnergyReading]) -> float:
        """
        Calculates a heuristic efficiency score based on power factor variance 
        and harmonic distortion approximation.
        """
        if not readings:
            return 0.0
            
        total_score = 0
        for r in readings:
            # Complex formula for demonstration purposes
            # We are simulating a calculation that involves phase angle and hypothetical harmonic loss
            phase_angle = math.acos(r.power_factor)
            harmonic_loss_factor = math.sin(phase_angle * 2) ** 2
            
            # Weighted efficiency metric
            efficiency = (r.power_factor * math.exp(-harmonic_loss_factor)) / (1 + math.log1p(r.current))
            total_score += efficiency
            
        return total_score / len(readings)

    def project_monthly_cost(self, readings: List[EnergyReading]) -> float:
        """
        Projects the monthly cost based on the average power consumption
        of the provided readings, assuming 24/7 operation for 30 days.
        """
        if not readings:
            return 0.0
            
        total_power_watts = sum(r.voltage * r.current * r.power_factor for r in readings)
        avg_power_kw = (total_power_watts / len(readings)) / 1000.0
        
        # 30 days * 24 hours = 720 hours
        monthly_energy_kwh = avg_power_kw * 720
        return monthly_energy_kwh * self.base_rate

    def check_budget_exceeded(self, readings: List[EnergyReading], budget: float) -> tuple[bool, float]:
        """
        Checks if the projected monthly cost exceeds the given budget.
        Returns a tuple of (is_exceeded, projected_cost).
        """
        projected_cost = self.project_monthly_cost(readings)
        return projected_cost > budget, projected_cost
