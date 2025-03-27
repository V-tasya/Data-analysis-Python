import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def boxplots_visualisation(df):
  education = df['education']
  workclass = df['workclass']
  salary = df['salary']
  relationship = df['relationship']

  sns.set(style="whitegrid")

  plt.figure(figsize=(12, 6))
  sns.boxplot(x=workclass, y=salary, palette="pastel")
  plt.title("Distribution of salary by hours per week")
  plt.xlabel("work class")
  plt.ylabel("salary")
  plt.savefig("salary_by_working_class.png", dpi=300)

  plt.figure(figsize=(14, 12))
  sns.boxplot(x=education, y=salary, palette="pastel")
  plt.title("Distribution of salary by education")
  plt.xlabel("education")
  plt.ylabel("salary")
  plt.xticks(rotation=45, ha="right")
  plt.savefig("salary_by_education.png", dpi=300)

  plt.figure(figsize=(12, 6))
  sns.boxplot(x=relationship, y=salary, palette="pastel")
  plt.title("Distribution of salary by race")
  plt.xlabel("relationship")
  plt.ylabel("salary")
  plt.savefig("salary_by_relationship.png", dpi=300)
