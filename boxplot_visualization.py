import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def boxplots_visualisation():
  df = pd.read_csv('adult11.csv')
  education = df['education']
  workclass = df['workclass']
  salary = df['salary']
  relationship = df['relationship']

  sns.set(style="whitegrid")

  plt.figure(figsize=(8, 6))
  sns.boxplot(x=workclass, y=salary, palette="pastel")
  plt.title("Distribution of salary by hours per week")
  plt.xlabel("Work class")
  plt.ylabel("Salary")
  plt.savefig("salary_by_hours_per_week.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  sns.boxplot(x=education, y=salary, palette="pastel")
  plt.title("Distribution of salary by education")
  plt.xlabel("Education")
  plt.ylabel("Salary")
  plt.savefig("salary_by_education.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  sns.boxplot(x=relationship, y=salary, palette="pastel")
  plt.title("Distribution of salary by race")
  plt.xlabel("Relationship")
  plt.ylabel("Salary")
  plt.savefig("salary_by_occupation.png", dpi=300)
  plt.show()

if __name__ == "__main__":
  boxplots_visualisation()