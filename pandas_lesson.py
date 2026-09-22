import pandas as pd

df = pd.read_csv("students_messy.csv")

df.info()
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())

df["City"] = df["City"].str.strip().str.title()

df["Score"] = pd.to_numeric(df["Score"], errors="coerce")

df = df.drop_duplicates()

df.info()