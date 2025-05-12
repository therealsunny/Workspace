import pandas as pd

#pd.set_option('display.max.rows',235)
#pd.set_option('display.max.columns',50)

"""
df = pd.read_excel(
    r"/Users/snakkina/Workspace/Python/Datafiles/world_population_excel_workbook.xlsx", header=0, names=['X','Y','Z','W'], sheet_name='world_population')
"""
df = pd.read_csv(r"/Users/snakkina/Workspace/Python/Datafiles/countries of the world.csv")

print(df)
#print(df['Rank'].max())
"""
for row in df.iterrows():
    print(f"Row data:\n{row}")
"""
