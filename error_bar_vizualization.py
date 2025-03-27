import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def error_bars_vizualization(df):

  sns.set(style="whitegrid")

  plt.figure(figsize=(12, 6))
  plt.title("Distribution of workclass by gender")
  sns.barplot(x="gender", y = "workclass", data = df, errorbar="sd", palette="pastel")
  plt.xlabel("gender")
  plt.ylabel("workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_gender.png", dpi=300)

  plt.figure(figsize=(12, 6))
  plt.title("Distribution of workclass by race")
  sns.pointplot(x="race", y = "workclass", data = df, errorbar="sd", palette="pastel")
  plt.xlabel("race")
  plt.ylabel("workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_race.png", dpi=300)

  plt.figure(figsize=(16, 8))
  plt.title("Distribution of workclass by education")
  sns.lineplot(x="education", y = "workclass", data = df, errorbar="se", palette="pastel")
  plt.xticks(rotation=45, ha="right")
  plt.xlabel("education")
  plt.ylabel("workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_education.png", dpi=300)

  plt.figure(figsize=(16, 8))
  plt.title("Distribution of workclass by relationship")
  sns.boxplot(x="education", y = "workclass", data = df, palette="pastel")
  plt.xticks(rotation=45, ha="right")
  plt.xlabel("relationship")
  plt.ylabel("workclass")
  plt.grid(axis="y", linestyle="--", alpha=0.7)
  plt.savefig("workclass_by_relationship.png", dpi=300)

