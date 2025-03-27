import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def histograms_visualization(df):

  sns.set_style("whitegrid")

  plt.figure(figsize=(16, 15))
  plt.title("Destibution of education")
  sns.displot(df, x="education", bins=20)
  plt.xticks(rotation=45, ha="right")
  plt.xlabel("education")
  plt.ylabel("frequency")
  plt.savefig("education.png", dpi=300)

  plt.figure(figsize=(16, 6))
  plt.title("Distribution of relationships")
  sns.histplot(df, x="relationship", bins=20)
  plt.xlabel("relationship")
  plt.ylabel("frequency")
  plt.savefig("relationship.png", dpi=300)

