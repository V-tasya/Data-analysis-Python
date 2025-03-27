import pandas as pd

def calculate_numerical_features(df):
  num_data = df.select_dtypes(include=['number'])

  if num_data.empty:
    print("No numerical data found")
    return

  statistics = {
        'mean': num_data.mean(),
        'median': num_data.median(),
        'std': num_data.std(),
        'min': num_data.min(),
        'max': num_data.max(),
        '5th_percentile': num_data.quantile(0.05),
        '95th_percentile': num_data.quantile(0.95),
        'missing_values': num_data.isna().sum()
    }
  
  values = pd.DataFrame(statistics)
  values.to_csv('numerical_data.csv', index=True)

  print("Analysed numerical data: ")
  print(values)


def calculate_categorial_features(df):
  categor_data = df.select_dtypes(include=['object'])

  if categor_data.empty:
    print("No categorial data found.")
    return

  statistics = {
    'unique_klasses': categor_data.nunique(),
    'missing_values': categor_data.isna().sum()
  }

  values = pd.DataFrame(statistics)
  class_proportions_df = values.apply(lambda col: col.value_counts(normalize=True)).T.add_suffix("_proportion")
  values = values.join(class_proportions_df, how='left')
  values.to_csv('categorical_data.csv', index=True)

  print("Analyzed categorical data:")
  print(values)
