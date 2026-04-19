import pandas as pd
import numpy as np

df = pd.read_csv("data/current.csv")

df["MonthlyCharges"] = np.random.randint(100, 250, size=len(df))

df.to_csv("data/current.csv", index=False)