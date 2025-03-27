import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def histograms_with_hue(df):

  sns.set_style("whitegrid")

  plt.figure(figsize=(16, 15))
  plt.title("Destibution of marital status divided by gender")
  sns.displot(df, x="marital-status", bins=20, hue="gender")
  plt.xticks(rotation=45, ha="right")
  plt.xlabel("marital status")
  plt.ylabel("frequency")
  plt.savefig("maritalStatus.png", dpi=300)

  plt.figure(figsize=(16, 10))
  plt.title("Distribution of occupation gain divided by race")
  sns.histplot(df, x="occupation", bins=20, hue="race", kde=True)
  plt.xlabel("occupation")
  plt.ylabel("frequency")
  plt.xticks(rotation=45, ha="right")
  plt.savefig("occupation.png", dpi=300)