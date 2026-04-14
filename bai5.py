import pandas as pd
import matplotlib.pyplot as plt

# Doc du lieu
df = pd.read_csv("data.csv")

# Ve scatter plot
df.plot(kind="scatter", x="X", y="Y", title="Moi quan he giua X va Y", figsize=(8,5))

plt.xlabel("X")
plt.ylabel("Y")
plt.show()