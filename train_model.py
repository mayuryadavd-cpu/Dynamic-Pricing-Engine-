import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Create data
print("Creating data...")
data = []
for i in range(5000):
    base_price = random.choice([500, 700, 400, 150, 250])
    demand = random.randint(20, 90)
    inventory = random.randint(0, 500)
    
    price = base_price
    if demand > 70: price *= 1.15
    elif demand < 30: price *= 0.90
    if inventory < 20: price *= 1.10
    elif inventory > 400: price *= 0.92
    
    data.append([base_price, demand, inventory, round(price, 2)])

df = pd.DataFrame(data, columns=['base_price', 'demand', 'inventory', 'price'])

# Train model
X = df[['base_price', 'demand', 'inventory']]
y = df['price']
model = RandomForestRegressor()
model.fit(X, y)

# Save model
import joblib
joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved!")
print("\nTest prediction:")
test = model.predict([[500, 80, 20]])[0]
print(f"Product: $500, 80% demand, 20 inventory → AI Price: ${test:.2f}")