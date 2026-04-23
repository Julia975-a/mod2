import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("energydata_complete.csv")
df['date'] = pd.to_datetime(df['date'])

sns.set(style="whitegrid")

# 1. Zużycie energii w czasie (średnia dzienna → czytelny wykres)
df_daily = df.resample('D', on='date').mean()

plt.figure(figsize=(12,5))
plt.plot(df_daily.index, df_daily['Appliances'])
plt.title("Dzienne zużycie energii")
plt.xlabel("Data")
plt.ylabel("Wh")
plt.tight_layout()
plt.savefig("wykres1.png")
plt.close()

# 2. Temperatura vs energia
plt.figure(figsize=(8,5))
sns.scatterplot(x='T1', y='Appliances', data=df.sample(2000), alpha=0.4)
plt.title("Temperatura vs Zużycie energii")
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