import pandas as pd

def clean_data(df):
    df['BrandName'] = df['BrandName'].str.strip()
    df['Price'] = df['Price'].str.replace('₱', '').str.replace(',', '').astype(float)
    df['SalesPrice'] = df['SalesPrice'].str.replace('₱', '').str.replace(',', '').astype(float)
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def add_features(df):
    df['Discount'] = df['Price'] - df['SalesPrice']
    return df

def transform_data(input_file="products_raw.csv", output_file="dproducts_clean.csv"):
    df = pd.read_csv(input_file)
    df = clean_data(df)
    df = remove_duplicates(df)
    df = add_features(df)
    df.to_csv(output_file, index=False)
    print(f"Transformed data has been written to {output_file}")
    return df

if __name__ == "__main__":
    clean_data = transform_data()
    print(clean_data)
