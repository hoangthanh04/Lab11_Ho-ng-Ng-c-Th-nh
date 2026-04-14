import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Doc du lieu
df = pd.read_csv("data.csv")

# Chon bien
X = df[["X1", "X2"]]
y = df["Label"]

# Chia du lieu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tao mo hinh
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Du doan
y_pred = model.predict(X_test)

# Danh gia
print("Accuracy:", accuracy_score(y_test, y_pred))