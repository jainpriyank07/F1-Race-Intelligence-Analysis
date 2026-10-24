import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

constructors = {
    "Red Bull": {"team_color": "#1E41FF", "power_unit": "Honda"},
    "Ferrari": {"team_color": "#DC0000", "power_unit": "Ferrari"},
    "Mercedes": {"team_color": "#00D2BE", "power_unit": "Mercedes"},
    "McLaren": {"team_color": "#FF8700", "power_unit": "Mercedes"},
    "Aston Martin": {"team_color": "#006F62", "power_unit": "Mercedes"},
    "Alpine": {"team_color": "#0090FF", "power_unit": "Renault"},
    "AlphaTauri": {"team_color": "#2B4562", "power_unit": "Honda"},
    "Williams": {"team_color": "#005AFF", "power_unit": "Mercedes"},
}

circuits = [
    "Monaco", "Silverstone", "Spa", "Monza", "Bahrain", "Suzuka",
    "Abu Dhabi", "Hungaroring", "Imola", "Miami"
]

rows = []
for round_num in range(1, 21):
    for driver in [
        "Max Verstappen", "Charles Leclerc", "Lewis Hamilton", "Carlos Sainz",
        "Lando Norris", "Fernando Alonso", "George Russell", "Esteban Ocon",
        "Oscar Piastri", "Pierre Gasly"
    ]:
        team = list(constructors.keys())[(hash(driver) + round_num) % len(constructors)]
        circuit = circuits[(round_num - 1) % len(circuits)]

        pace = 90 + rng.normal(0, 4)
        qualifying = 1 + rng.integers(1, 18)
        tyre_wear = round(rng.uniform(8, 30), 2)
        pit_stop_time = round(rng.uniform(19.0, 28.5), 2)
        overtakes = rng.integers(0, 18)
        sector_1 = round(24 + rng.normal(0, 0.7), 3)
        sector_2 = round(28 + rng.normal(0, 0.8), 3)
        sector_3 = round(21 + rng.normal(0, 0.7), 3)
        avg_speed = round(210 + rng.normal(0, 8), 2)
        laps_led = rng.integers(0, 25)
        grid = rng.integers(1, 11)
        finish_position = rng.integers(1, 11)

        rows.append({
            "race_round": round_num,
            "circuit": circuit,
            "driver": driver,
            "team": team,
            "race_finish_position": finish_position,
            "grid_position": grid,
            "qualifying_position": qualifying,
            "laps_led": laps_led,
            "pit_stop_time_sec": pit_stop_time,
            "overtakes": overtakes,
            "tyre_wear_index": tyre_wear,
            "sector_1_time_sec": sector_1,
            "sector_2_time_sec": sector_2,
            "sector_3_time_sec": sector_3,
            "avg_speed_kmh": avg_speed,
            "race_pace_index": round(pace, 2),
            "podium": 1 if finish_position <= 3 else 0,
            "points": 25 if finish_position == 1 else 18 if finish_position == 2 else 15 if finish_position == 3 else 12 if finish_position == 4 else 10 if finish_position == 5 else 8 if finish_position == 6 else 6 if finish_position == 7 else 4 if finish_position == 8 else 2 if finish_position == 9 else 1 if finish_position == 10 else 0
        })

# Force a few realistic winners to make the dataset credible
for round_num in range(1, 21, 2):
    winner = "Max Verstappen" if round_num % 4 else "Charles Leclerc"
    for row in rows:
        if row["race_round"] == round_num and row["driver"] == winner:
            row["race_finish_position"] = 1
            row["points"] = 25
            row["podium"] = 1
            row["laps_led"] = rng.integers(10, 40)

# Build data frame and save CSV
f1_df = pd.DataFrame(rows)
f1_df.to_csv("f1_race_sample.csv", index=False)

print(f1_df.head())
print(f"Saved {len(f1_df)} rows to f1_race_sample.csv")
