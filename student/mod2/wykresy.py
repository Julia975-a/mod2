import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("energydata_complete.csv")
df['date'] = pd.to_datetime(df['date'])

sns.set(style="whitegrid")

# 1. Zużycie energii – wybrany tydzień
week = df[(df['date'] >= '2016-01-10') & (df['date'] < '2016-01-17')]

plt.figure(figsize=(12,5))
plt.plot(week['date'], week['Appliances'])
plt.title("Zużycie energii – wybrany tydzień")
plt.xlabel("Data")
plt.ylabel("Wh")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("wykres1.png")
plt.close()

# 2. Korelacja (heatmapa)
corr = df[['Appliances','T1','T2','T_out','RH_1','RH_2']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Korelacja zmiennych")
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