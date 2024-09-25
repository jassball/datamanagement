import pandas as pd

file_path = "schemas/characters.csv"
data = pd.read_csv(file_path)




superpower_filter = 'flight|intangibility'
filtered_data = data[data['superpowers'].str.contains(superpower_filter, case=False, na=False)]


for index, row in filtered_data.iterrows():
    print(f"Character: {row['charname']}")
    print(f"Birth Name : {row['birthname']}")
    print(f"Superpower: {row['superpowers']}")
    print("-" * 40)


