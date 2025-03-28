import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def regression(df):

  sns.set_style("whitegrid")

  plt.figure(figsize=(12, 6))
  numeric_df = df.select_dtypes(include=["number"])
  sns.regplot(x="hours-per-week", y = "age", data=numeric_df, scatter_kws={"s": 10})
  plt.title("Linear regression")
  plt.xlabel("age")
  plt.ylabel("hours per week")
  plt.savefig("linear_regression_1.png", dpi = 300)

  plt.figure(figsize=(12, 6))
  numeric_df = df.select_dtypes(include=["number"])
  sns.lmplot(x="age", y = "capital-gain", data=numeric_df, scatter_kws={"s": 10})
  plt.title("Linear regression")
  plt.xlabel("age")
  plt.ylabel("capital-gain")
  plt.savefig("linear_regression_2.png", dpi = 300)

