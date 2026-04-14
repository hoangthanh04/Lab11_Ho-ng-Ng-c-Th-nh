import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu
df = pd.read_csv("data.csv")

# Xu ly va ve bieu do
group_data = df.groupby("Nhom")["GiaTri"].mean()

group_data.plot(kind="bar", title="Gia tri trung binh theo nhom", figsize=(8,5))
plt.xlabel("Nhom")
plt.ylabel("Gia tri trung binh")
plt.show()