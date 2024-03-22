import pandas as pd
from dateutil import parser
from django.conf import settings

# Attempts to parse a string into a date. If successful, returns the date; otherwise, returns None.
def try_parse_date(string):
    try:
        return parser.parse(string, fuzzy=False)
    except (ValueError, TypeError):
        return None

# Determines if the majority of values in a column can be converted to numbers. Returns True if so.
def is_mostly_numeric(col):
    numeric_count = col.apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().sum()
    return numeric_count / len(col) > 0.5

# Main function to infer and convert data types within a DataFrame. It iterates through each column,
# converting them to appropriate data types based on the content of the column.
def infer_and_convert_data_types(df, categorization_threshold=0.5):
    for col in df.columns:
        if df[col].dtype != 'object':
            continue  # Skip columns that are not of 'object' type, as they are likely already properly typed.

        # Convert columns mostly containing numeric values to numeric dtype
        if is_mostly_numeric(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')
            continue

        # Convert columns that can be parsed into dates to datetime dtype
        if df[col].apply(try_parse_date).notna().any():
            df[col] = pd.to_datetime(df[col], errors='coerce')
            continue

        # Convert columns with a high ratio of unique values to categorical dtype if they meet a threshold
        unique_ratio = len(df[col].dropna().unique()) / len(df[col].dropna())
        if 0 < unique_ratio < categorization_threshold:
            df[col] = pd.Categorical(df[col])

    return df  # Returns the DataFrame with converted data types

# Processes a file by reading it into a DataFrame, then calling the function to infer and convert data types.
def process_file(file_path, categorization_threshold=0.5):
    try:
        df = pd.read_csv(file_path)  # Attempt to read the file into a DataFrame
    except Exception as e:
        print(f"Error processing the file: {e}")
        return None  # Return None if the file cannot be processed

    print("Data types before inference:")
    print(df.dtypes)  # Print the data types before inference for comparison

    df = infer_and_convert_data_types(df, categorization_threshold)  # Infer and convert data types

    print("\nData types after inference:")
    print(df.dtypes)  # Print the data types after inference to see the changes
    return df  # Return the processed DataFrame
