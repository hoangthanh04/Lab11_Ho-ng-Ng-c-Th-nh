import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu
df = pd.read_csv("data.csv")

# Ve boxplot
df.boxplot(column="GiaTri", figsize=(6,5))

plt.title("Boxplot phat hien ngoai le")
plt.ylabel("GiaTri")
plt.show()