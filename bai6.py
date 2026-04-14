import pandas as pd
import matplotlib.pyplot as plt

try:
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
except ModuleNotFoundError as e:
    missing = e.name
    raise ModuleNotFoundError(
        f"Phải cài 'scikit-learn' để chạy file này.\n"
        f"Chạy: python -m pip install scikit-learn\n"
        f"Thiếu module: {missing}"
    ) from e

# Doc du lieu
df = pd.read_csv("data.csv")

# Chon bien
X = df[["X"]]
y = df["Y"]

# Chia du lieu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tao mo hinh
model = LinearRegression()
model.fit(X_train, y_train)

# Du doan
y_pred = model.predict(X_test)

# Danh gia
print("MSE:", mean_squared_error(y_test, y_pred))
print("He so:", model.coef_)
print("Intercept:", model.intercept_)