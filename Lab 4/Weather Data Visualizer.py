
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_path = "weather_data.csv"

df = pd.read_csv(file_path)

print("FIRST 5 ROWS:")
print(df.head())

print("\nDATA INFO:")
print(df.info())

print("\nSTATISTICS:")
print(df.describe())


df["Date"] = pd.to_datetime(df["Date"], errors="coerce")


df = df.dropna(subset=["Date"])


df = df.fillna(df.mean(numeric_only=True))


df = df[["Date", "Temperature", "Rainfall", "Humidity"]]


df = df.sort_values("Date")



temps = df["Temperature"].values

daily_mean = np.mean(temps)
daily_min = np.min(temps)
daily_max = np.max(temps)
daily_std = np.std(temps)

print("\n===== NUMPY TEMPERATURE STATISTICS =====")
print("Mean Temperature:", daily_mean)
print("Minimum Temperature:", daily_min)
print("Maximum Temperature:", daily_max)
print("Std Deviation:", daily_std)




plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Temperature"])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("daily_temperature.png")
plt.close()


df["Month"] = df["Date"].dt.month
monthly_rain = df.groupby("Month")["Rainfall"].sum()

plt.figure(figsize=(10, 5))
plt.bar(monthly_rain.index, monthly_rain.values)
plt.title("Monthly Rainfall Total")
plt.xlabel("Month")
plt.ylabel("Rainfall")
plt.savefig("monthly_rainfall.png")
plt.close()


plt.figure(figsize=(10, 5))
plt.scatter(df["Temperature"], df["Humidity"])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temperature.png")
plt.close()


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.plot(df["Date"], df["Temperature"])
plt.title("Temperature Trend")


plt.subplot(1, 2, 2)
plt.scatter(df["Temperature"], df["Humidity"])
plt.title("Humidity vs Temperature")

plt.savefig("combined_plot.png")
plt.close()



monthly_stats = df.groupby("Month").agg({
    "Temperature": ["mean", "min", "max"],
    "Rainfall": "sum",
    "Humidity": "mean"
})

print("\n===== MONTHLY AGGREGATE STATISTICS =====")
print(monthly_stats)


df.to_csv("cleaned_weather_data.csv", index=False)

report = """
# Climate Data Analysis Report

## 1. Introduction
This report analyzes local weather data to understand climate patterns
using Python, Pandas, NumPy, and Matplotlib.

## 2. Key Statistical Findings
- **Average Temperature:** {:.2f}
- **Minimum Temperature:** {:.2f}
- **Maximum Temperature:** {:.2f}
- **Temperature Std Dev:** {:.2f}

## 3. Visualizations Generated
The following PNG files were created:
- daily_temperature.png
- monthly_rainfall.png
- humidity_vs_temperature.png
- combined_plot.png

## 4. Monthly Insights
Below are monthly aggregated statistics for temperature, rainfall, and humidity.

## 5. Conclusion
The analysis provides insights into temperature trends, rainfall distribution,
and humidity patterns that can support climate awareness initiatives.
""".format(daily_mean, daily_min, daily_max, daily_std)

with open("climate_report.md", "w") as file:
    file.write(report)

print("\nReport and cleaned data exported successfully!")
