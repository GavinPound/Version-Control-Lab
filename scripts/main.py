import pandas as pd


df = pd.read_csv("../data/sales_data.csv")

df["date"] = pd.to_datetime(df["date"])
print("Accuracy Check")
negative_prices = (df["price"]< 0).sum()
current_date = pd.Timestamp.now()
future_date_count = (df["date"]>current_date).sum()
print(f"Negative Prices: {negative_prices}")
print (f"Number of Future Dates: {future_date_count}")


print("Consistency Check")
unique_value = df["product"].unique()
unique_product_count = df["product"].nunique()
print(f"Unique products:{unique_value}")
print(f"Count of unique products: {unique_product_count}")


print("Completeness Check")
missing_value = df.isnull().sum()
completeness_rate = df.notnull().mean()*100
print(f"Missing Values: {missing_value}")
print(f"Overall completeness rate: {completeness_rate}%")

assert(df["price"]>=0).all(),"Negative price found!"