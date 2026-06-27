import pandas as pd

# Load the dataset
data = pd.read_csv("cars_dataset.csv")

# Show the first few rows
print("Car Dataset Preview:")
print(data.head())

# Calculate average price
avg_price = data["Price"].mean()
print(f"\nAverage Car Price: ${avg_price:.2f}")

# Filter cars newer than 2017
newer_cars = data[data["Year"] > 2017]
print("\nCars newer than 2017:")
print(newer_cars)
