import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = pd.read_csv("f1_race_sample.csv")

print("Top drivers by total points:")
print(df.groupby("driver")["points"].sum().sort_values(ascending=False).head(10))

print("\nAverage points by team:")
print(df.groupby("team")["points"].mean().sort_values(ascending=False))

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Total points by driver
points_by_driver = df.groupby("driver", as_index=False)["points"].sum().sort_values("points", ascending=False).head(10)
sns.barplot(data=points_by_driver, x="points", y="driver", palette="viridis", ax=axes[0, 0])
axes[0, 0].set_title("Total Points by Driver")
axes[0, 0].set_xlabel("Points")
axes[0, 0].set_ylabel("Driver")

# 2. Average pit stop time by team
pit_by_team = df.groupby("team", as_index=False)["pit_stop_time_sec"].mean().sort_values("pit_stop_time_sec")
sns.barplot(data=pit_by_team, x="pit_stop_time_sec", y="team", palette="coolwarm", ax=axes[0, 1])
axes[0, 1].set_title("Average Pit Stop Time by Team")
axes[0, 1].set_xlabel("Pit Stop Time (s)")
axes[0, 1].set_ylabel("Team")

# 3. Race pace vs average speed
sns.scatterplot(data=df, x="avg_speed_kmh", y="race_pace_index", hue="team", s=70, alpha=0.8, ax=axes[1, 0])
axes[1, 0].set_title("Race Pace Index vs Average Speed")
axes[1, 0].set_xlabel("Average Speed (km/h)")
axes[1, 0].set_ylabel("Race Pace Index")

# 4. Overtakes vs tyre wear
sns.scatterplot(data=df, x="tyre_wear_index", y="overtakes", hue="circuit", s=70, alpha=0.7, ax=axes[1, 1])
axes[1, 1].set_title("Tyre Wear vs Overtakes")
axes[1, 1].set_xlabel("Tyre Wear Index")
axes[1, 1].set_ylabel("Overtakes")

plt.tight_layout()
plt.show()

# Additional insight: podium rate by driver
podium_rates = (
    df.groupby("driver")["podium"].mean().sort_values(ascending=False).head(10) * 100
).round(1)
print("\nPodium rate (%) by driver:")
print(podium_rates)

# Additional chart: podium rate by driver
plt.figure(figsize=(10, 6))
series = podium_rates.reset_index().rename(columns={"driver": "Driver", "podium": "Podium Rate (%)"})
sns.barplot(data=series, x="Podium Rate (%)", y="Driver", palette="mako")
plt.title("Podium Rate by Driver")
plt.tight_layout()
plt.show()
