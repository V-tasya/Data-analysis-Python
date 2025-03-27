import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def histograms_with_hue():

  df = pd.read_csv("adult11.csv")

  sns.set_style("whitegrid")

  plt.figure(figsize=(8, 6))
  plt.title("Destibution of marital status divided by gender")
  sns.displot(df, x="marital-status", bins=20, hue="gender")
  plt.xlabel("Marital status")
  plt.ylabel("Frequency")
  plt.savefig("maritalStatus.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  plt.title("Distribution of occupation gain divided by race")
  sns.histplot(df, x="occupation", bins=20, hue="race", kde=True)
  plt.xlabel("Occupation")
  plt.ylabel("Frequency")
  plt.savefig("occupation.png", dpi=300)
  plt.show()

if __name__ == "__main__":
  histograms_with_hue()