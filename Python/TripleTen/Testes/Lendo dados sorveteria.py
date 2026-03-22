import pandas as pd
import matplotlib as mp

file_path = "https://raw.githubusercontent.com/dunmacleod/datasets/main/ice_cream_sales.csv"

df = pd.read_csv(file_path)

plt = df.plot(kind="bar", x="date", y="# Ice-cream cones sold")
plt.set_title = "Casquinhas vendidas por dia"

