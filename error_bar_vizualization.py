import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def error_bars_vizualization():

  df = pd.read_csv("adult11.csv")

  sns.set(style="whitegrid")

  
  plt.figure(figsize=(8, 6))
  plt.title("Distribution of workclass by gender")
  sns.barplot(x="gender", y = "workclass", data = df, errorbar="sd", palette="pastel")
  plt.xlabel("Gender")
  plt.ylabel("Workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_gender.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  plt.title("Distribution of workclass by race")
  sns.pointplot(x="race", y = "workclass", data = df, errorbar="sd", palette="pastel")
  plt.xlabel("Race")
  plt.ylabel("Workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_race.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  plt.title("Distribution of workclass by education")
  sns.lineplot(x="education", y = "workclass", data = df, errorbar="se", palette="pastel")
  plt.xlabel("Education")
  plt.ylabel("Workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_education.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  plt.title("Distribution of workclass by relationship")
  sns.boxplot(x="education", y = "workclass", data = df, palette="pastel")
  plt.xlabel("Relationship")
  plt.ylabel("Workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_relationship.png", dpi=300)
  plt.show()

if __name__ == "__main__":
  error_bars_vizualization()