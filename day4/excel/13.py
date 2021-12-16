import pandas as pd

dfa = pd.read_excel("data1.xlsx")

# filter dfa['val_one'] > 100
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(dfa[dfa['val_three'] > 100])
