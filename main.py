import pandas as pd

import csv_analysis
import violinplot_visualization
import linear_regression
import histograms
import histograms_with_conditions
import heat_map
import error_bar_vizualization
import boxplot_visualization

def reading_file():
  try:
    df = pd.read_csv('adult11.csv')  
    if df.empty:
      print("The file is empty.")
      return

    print("rows, columns:", df.shape) 
  except FileNotFoundError:
    print("The file wasn't found.")
    return
  except Exception as exeption:
    print(f"Error: {exeption}")
    return
  
  if df is not None:
    csv_analysis.calculate_numerical_features(df)
    csv_analysis.calculate_categorial_features(df)
    boxplot_visualization.boxplots_visualisation(df)
    violinplot_visualization.violinplots_visualizations(df)
    error_bar_vizualization.error_bars_vizualization(df)
    histograms.histograms_visualization(df)
    histograms_with_conditions.histograms_with_hue(df)
    heat_map.heat_maps(df)
    linear_regression.regression(df)

def main():
  reading_file()

if __name__ == "__main__":
  main()

