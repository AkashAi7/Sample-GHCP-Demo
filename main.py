import sys
from services.data_ingestion import DataIngestionService
from services.analytics import EnergyAnalytics

def main():
    print("Starting Smart Home Energy Monitor...")
    
    # Initialize services
    ingestion = DataIngestionService()
    analytics = EnergyAnalytics()
    
    # 1. Load data from 'data/readings.csv'
    readings = ingestion.load_file('data/readings.csv')
    if not readings:
        print("No data found in data/readings.csv")
        return

    # 2. Calculate the efficiency score
    efficiency_score = analytics.calculate_complex_efficiency_score(readings)
    
    # 3. Project monthly cost and check budget
    budget = 50.0
    is_exceeded, projected_cost = analytics.check_budget_exceeded(readings, budget)

    # 4. Print a summary report
    print("\n--- Energy Summary Report ---")
    print(f"Total Readings: {len(readings)}")
    print(f"Efficiency Score: {efficiency_score:.4f}")
    print(f"Projected Monthly Cost: ${projected_cost:.2f}")
    print(f"Budget: ${budget:.2f}")
    
    if is_exceeded:
        print("ALERT: Projected cost exceeds budget!")
    else:
        print("Budget Status: Within limits.")
    
    print("-----------------------------\n")

if __name__ == "__main__":
    main()
