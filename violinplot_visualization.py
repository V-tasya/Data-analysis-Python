import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def violinplots_visualizations(df):

  race = df["race"]
  marital_status = df["marital-status"]
  gender = df["gender"]
  salary = df["salary"]

  sns.set(style="whitegrid")

  plt.figure(figsize=(12, 6))
  plt.title("Distribution of salary by race")
  sns.violinplot(x=race, y=salary, data=df, palette="pastel", bw=0.2, cut=1, linewidth=1.5)
  plt.xlabel("race")
  plt.ylabel("salary")
  plt.savefig("salary_by_race.png", dpi=300)

  plt.figure(figsize=(12, 6))
  plt.title("Distribution of salary by gender")
  sns.violinplot(x=gender, y=salary, data=df, palette="pastel", bw=0.2, cut=1, linewidth=1.5)
  plt.xlabel("gender")
  plt.ylabel("salary")
  plt.savefig("salary_by_gender.png", dpi=300)

  plt.figure(figsize=(14, 6))
  plt.title("Distribution of salary by marital status")
  sns.violinplot(x=marital_status, y=salary, data=df, palette="pastel", bw=0.2, cut=1, linewidth=1.5)
  plt.xlabel("marital status")
  plt.ylabel("salary")
  plt.savefig("salary_by_marital_status.png", dpi=300)



