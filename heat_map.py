import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def heat_maps():
  df = pd.read_csv("adult11.csv")

  sns.set_style("whitegrid")

  numeric_df = df.select_dtypes(include=["number"])

  plt.figure(figsize=(10, 8))
  sns.heatmap(numeric_df.corr(), cmap="Pastel2", annot=True, fmt=".2f")
  plt.title("Heatmap for numerical Values")
  plt.savefig("heat_map_num_values.png", dpi=300)
  #plt.xlabel("Numerical values")
  #plt.ylabel("Numerical values")
  plt.show()

if __name__ == "__main__":
    heat_maps()
