import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu
df = pd.read_csv("data.csv")

# Ve histogram
df["GiaTri"].plot(kind="hist", bins=10, title="Phan phoi du lieu", figsize=(8,5))

plt.xlabel("GiaTri")
plt.ylabel("Tan so")
plt.show()