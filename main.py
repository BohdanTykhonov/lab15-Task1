import pandas as pd

teams = {
    "Динамо": 42,
    "Шахтар": 48,
    "Металіст": 36,
    "Зоря": 44,
    "Десна": 39,
    "Львів": 35,
    "Олександрія": 33,
    "Ворскла": 30,
    "Колос": 37,
    "Маріуполь": 31
}

df = pd.DataFrame(list(teams.items()), columns=["Team", "Points"])

print("Original DataFrame:")
print(df)

df['Region'] = ['Київ', 'Донецьк', 'Харків', 'Луганськ', 'Чернігів', 'Львів', 'Кіровоград', 'Полтава', 'Київ', 'Донецьк']

grouped_df = df.groupby('Region').agg({'Points': 'sum'})

print("\nGrouped DataFrame by Region (Sum of Points):")
print(grouped_df)
