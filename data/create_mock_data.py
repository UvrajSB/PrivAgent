# tools/mock_data.py

import random
import pandas as pd
from datetime import datetime, timedelta

def generate_mock_vitals(days=60):
    data = []
    for i in range(days):
        entry = {
            "date": (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'),
            "heart_rate": random.randint(70, 100),
            "blood_pressure_sys": random.randint(110, 130),
            "blood_pressure_dia": random.randint(70, 85),
            "spo2": random.randint(96, 100),
        }
        data.append(entry)
    return pd.DataFrame(data[::-1])

if __name__ == "__main__":
    df = generate_mock_vitals()
    print(df)
    df.to_csv("mock_vitals.csv", index=False)
