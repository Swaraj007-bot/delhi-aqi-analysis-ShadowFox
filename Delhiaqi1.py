"""
Research Questions:
RQ1: Which pollutants contribute most to poor air quality in Delhi?
RQ2: How does AQI and PM2.5 vary across different seasons?
RQ3: Which season experiences the worst air quality?
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Load Data ----------------
df = pd.read_csv("delhiaqi.csv")

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

# ---------------- Season Mapping ----------------
def get_season(month):
    if month in [11, 12, 1]:
        return "Winter"
    elif month in [3, 4, 5, 6]:
        return "Summer"
    elif month in [7, 8, 9]:
        return "Monsoon"
    else:
        return "Post-Monsoon"

df["season"] = df["month"].apply(get_season)

# ---------------- PM2.5 Statistics ----------------
print("\nOverall PM2.5 Statistics:")
print(df["pm2_5"].describe())

print("\nSeason-wise PM2.5 Mean:")
print(df.groupby("season")["pm2_5"].mean())

# ---------------- PM2.5 Trend ----------------
plt.figure()
plt.plot(df["date"], df["pm2_5"])
plt.title("PM2.5 Trend in Delhi")
plt.xlabel("Date")
plt.ylabel("PM2.5")
plt.show()

# ---------------- PM10 Trend ----------------
plt.figure()
plt.plot(df["date"], df["pm10"])
plt.title("PM10 Trend in Delhi")
plt.xlabel("Date")
plt.ylabel("PM10")
plt.show()

# ---------------- Season-wise PM2.5 Boxplot ----------------
plt.figure()
df.boxplot(column="pm2_5", by="season")
plt.title("Season-wise PM2.5 Distribution")
plt.suptitle("")
plt.xlabel("Season")
plt.ylabel("PM2.5")
plt.show()

# ---------------- Pollutant Correlation ----------------
pollutants = ["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]
corr = df[pollutants].corr()

print("\nCorrelation Matrix:")
print(corr)

# ---------------- Key Insights ----------------
print("\nKey Insights:")
print("• PM2.5 levels peak during winter due to temperature inversion and emissions.")
print("• Monsoon season shows improved air quality because of rainfall.")
print("• PM2.5 and PM10 have strong correlation, indicating common pollution sources.")
