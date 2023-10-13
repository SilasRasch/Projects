import pandas as pd
import os

new_strings = ['Min K?bmand', 'SPAR', 'Letk?b', 'Meny', 'K?bmanden']

word_filter = pd.read_csv('excel/filters/word_filter.csv', sep=",")

for index, row in word_filter.iterrows():
    new_strings.append(row[0])

def get_csv():
    print('Input CSV filename (must be in excel folder)')
    try:
        df = pd.read_csv(f'excel/{input()}.csv', sep=";")
        print('Loading file...')
        return df
    except: 
        print('Error occured, please try again')
        get_csv()

def save_file(dataframe):
    try:
        dataframe.to_excel(f'excel/output/{input("Choose the name of the output file: ")}.xlsx', sheet_name='Data')
        print('File saved succesfully')
    except:
        print("An error occured, maybe the name was already in use. Try again")
        save_file()

if not os.path.exists("excel/"):
    os.makedirs("excel/")
    print('Created excel-folder')

if not os.path.exists("excel/output"):
    os.makedirs("excel/output")
    print('Created excel/output-folder')

df1 = get_csv() # Get 1st file (DGFS / Dagrofa)
df2 = get_csv()

df1 = df1[df1['MFAEnabled'] == False] # Remove all entries where MFA is enabled
df2 = df2[df2['MFAEnabled'] == False] # Remove all entries where MFA is enabled
df1 = df1[df1['MFAEnforced'] != 'TRUE'] # Remove all entries where MFAEnforced is true. MFA should be enabled on next logon.
df2 = df2[df2['MFAEnforced'] != 'TRUE'] # 'TRUE' is a string because the PowerShell script is weird like that.

print(new_strings)

for s in new_strings: # Remove all entries containing specific string values -> see top of document
    df1 = df1[~df1['DisplayName'].str.contains(s, case=False)]
    df2 = df2[~df2['DisplayName'].str.contains(s, case=False)]
    df1 = df1[~df1['DisplayName'].str.lower().str.startswith(s.lower())]
    df2 = df2[~df2['DisplayName'].str.lower().str.startswith(s.lower())]

excluded = pd.read_excel(f'excel/filters/MFAFilter.xlsx')  # Filter out excluded members
df1 = df1[~df1['DisplayName'].isin(excluded['DisplayName'])]
df2 = df2[~df2['DisplayName'].isin(excluded['DisplayName'])]

big_df = pd.concat([df1, df2], ignore_index=True) # Merge the dataframes
print(big_df)
save_file(big_df)