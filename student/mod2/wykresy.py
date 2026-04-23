import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("energydata_complete.csv")
df['date'] = pd.to_datetime(df['date'])

sns.set(style="whitegrid")

# 1. Średnie zużycie energii wg dnia tygodnia

df['weekday_name'] = df['date'].dt.day_name()

order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

weekday_avg = df.groupby('weekday_name')['Appliances'].mean().reindex(order)

plt.figure(figsize=(10,5))
weekday_avg.plot(kind='bar')

plt.title("Średnie zużycie energii wg dnia tygodnia")
plt.xlabel("Dzień tygodnia")
plt.ylabel("Średnie Wh")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("wykres1.png")
plt.close()

# 2. Porównanie: czwartki vs weekend (średnie godzinowe)

df['weekday'] = df['date'].dt.dayofweek  # 0=pon, 6=niedz
df['hour'] = df['date'].dt.hour

# Czwartki (3)
thu = df[df['weekday'] == 3]

# Weekend (sobota=5, niedziela=6)
weekend = df[df['weekday'].isin([5,6])]

# Średnie godzinowe
thu_hourly = thu.groupby('hour')['Appliances'].mean()
weekend_hourly = weekend.groupby('hour')['Appliances'].mean()

plt.figure(figsize=(10,5))
plt.plot(thu_hourly.index, thu_hourly.values, marker='o', label='Czwartki')
plt.plot(weekend_hourly.index, weekend_hourly.values, marker='o', label='Weekend')

plt.title("Porównanie zużycia energii: czwartki vs weekend")
plt.xlabel("Godzina")
plt.ylabel("Średnie Wh")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig("wykres2.png")
plt.close()

# 3. Zużycie wg godziny
df['hour'] = df['date'].dt.hour
hourly = df.groupby('hour')['Appliances'].mean()

plt.figure(figsize=(10,5))
hourly.plot(kind='bar')
plt.title("Średnie zużycie energii wg godziny")
plt.tight_layout()
plt.savefig("wykres3.png")
plt.close()

print("Gotowe wykresy")