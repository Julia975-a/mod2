import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("energydata_complete.csv")
df['date'] = pd.to_datetime(df['date'])

sns.set(style="whitegrid")

# 1. Średnie dzienne zużycie energii (czytelne)
df_daily = df.resample('D', on='date').mean()

plt.figure(figsize=(12,5))
plt.plot(df_daily.index, df_daily['Appliances'])
plt.title("Średnie dzienne zużycie energii")
plt.xlabel("Data")
plt.ylabel("Wh")
plt.tight_layout()
plt.savefig("wykres1.png")
plt.close()

# 2. Zużycie energii – tylko czwartki
df['weekday'] = df['date'].dt.day_name()
df['hour'] = df['date'].dt.hour

thursday = df[df['weekday'] == 'Thursday']

hourly_thu = thursday.groupby('hour')['Appliances'].mean()

plt.figure(figsize=(10,5))
hourly_thu.plot(kind='line', marker='o')
plt.title("Średnie zużycie energii w czwartki (wg godziny)")
plt.xlabel("Godzina")
plt.ylabel("Wh")
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