import pandas as pd

ip_location = input("Input desired IP-location: ")

df = pd.read_excel('excel/shares.xlsx')
df = df[df['IPLocation'] == ip_location]

def merge_rows(group):
    return pd.Series({'ShareName': ', '.join(group['ShareName']), 'Path': ' | '.join(group['Path'])})

grouped = df.groupby(['AssetName', 'IPAddress']).apply(merge_rows).reset_index()

print(grouped)
grouped.to_excel(f'excel/output/{input("Choose the name of the output file: ")}.xlsx', sheet_name='Data')