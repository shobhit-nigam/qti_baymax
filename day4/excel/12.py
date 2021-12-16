import pandas as pd

dfa = pd.read_excel("data1.xlsx")

print(list(dfa.columns))
print(dfa.describe())
