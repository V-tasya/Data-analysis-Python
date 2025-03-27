import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def histograms_visualization():

  df = pd.read_csv("adult11.csv")

  sns.set_style("whitegrid")

  plt.figure(figsize=(8, 6))
  plt.title("Destibution of education")
  sns.displot(df, x="education", bins=20)
  plt.xlabel("Education")
  plt.ylabel("Frequency")
  plt.savefig("education.png", dpi=300)
  plt.show()

  plt.figure(figsize=(8, 6))
  plt.title("Distribution of relationships")
  sns.histplot(df, x="relationship", bins=20)
  plt.xlabel("Relationship")
  plt.ylabel("Frequency")
  plt.savefig("relationship.png", dpi=300)
  plt.show()

if __name__ == "__main__":
    histograms_visualization()