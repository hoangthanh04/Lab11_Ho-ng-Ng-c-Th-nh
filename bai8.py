# 1. Import thu vien
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 2. Doc du lieu
df = pd.read_csv("data.csv")

# 3. Kham pha du lieu
print(df.head())
print(df.info())
print(df.describe())

# 4. Ve bieu do cot
group_data = df.groupby("Nhom")["GiaTri"].mean()
group_data.plot(kind="bar", title="Gia tri trung binh theo nhom", figsize=(8,5))
plt.show()

# 5. Ve histogram
df["GiaTri"].plot(kind="hist", bins=10, title="Histogram GiaTri", figsize=(8,5))
plt.show()

# 6. Ve scatter plot
df.plot(kind="scatter", x="X", y="Y", title="Scatter plot X va Y", figsize=(8,5))
plt.show()

# 7. Xay dung mo hinh hoi quy
X = df[["X"]]
y = df["Y"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("He so:", model.coef_)
print("Intercept:", model.intercept_)