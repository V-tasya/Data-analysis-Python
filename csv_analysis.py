import pandas as pd

def reading_file():
  try:
    df = pd.read_csv('adult11.csv')  
    if df.empty:
      print("The file is empty.")

    print("rows, columns:", df.shape) 
  except FileNotFoundError:
    print("The file wasn't found.")
  except Exception as exeption:
    print(f"Error: {exeption}")
  
  if df is not None:
    calculate_numerical_features(df)

def calculate_numerical_features(df):
  # numerical data for analysis
  num_data = ['age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']

  average_values = df[num_data].mean()
  median_values = df[num_data].median()
  min_values = df[num_data].min()
  max_values = df[num_data].max()
  standart_deviation = df[num_data].std()
  quantiles_5 = df[num_data].quantile(0.05)
  quantiles_95 = df[num_data].quantile(0.95)
  missing_values = df.isna().sum()

  statistics = {
        'mean': average_values,
        'median': median_values,
        'std': standart_deviation,
        'min': min_values,
        'max': max_values,
        '5th_percentile': quantiles_5,
        '95th_percentile': quantiles_95,
        'missing_values': missing_values
    }
  
  values = pd.DataFrame(statistics)
  cleaned_values = values.dropna(axis=1, how='all')

  cleaned_values.to_csv('numerical_data.csv', index=True)
  print("Analysed numerical data: ")
  print(cleaned_values)




if __name__ == "__main__":
  reading_file()