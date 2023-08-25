import pandas as pd
import os
import uuid
from numpy import array

filter_strings = ["adstec", "Truck", "Crosspad", "Test", "SRV", "SVC", "Service", "Sam Win", "vmware", "ax monitor", "axmonitor", "sharepoint",
                  "drift", "Kursus", "Lager", "IBM", "Kødgrossisten", "Navinasa", "Navision", "Ringsted", "rs.", "Mailbox", "Stoppet"] # Should be loaded from a file in the future

new_strings = []

def get_excel():
    print('Input XLSX filename (must be in excel folder)')
    try:
        df = pd.read_excel(f'excel/{input()}.xlsx')
        print('Loading file...')
        return df
    except: 
        print('Error occured, please try again')
        get_excel()

def save_file():
    try:
        df.to_excel(f'excel/output/{input("Choose the name of the output file: ")}.xlsx', sheet_name='Data')
        print('File saved succesfully')
    except:
        print("An error occured, maybe the name was already in use. Try again")
        save_file()

word_filter = pd.read_csv('excel/filters/word_filter.csv', sep=",")

for index, row in word_filter.iterrows():
    new_strings.append(row[0])

# Program starts here
print(f'- Password expired-kontrol auto-filter v1.0 - \nby Silas')

if not os.path.exists("excel/"):
    os.makedirs("excel/")
    print('Created excel-folder')

if not os.path.exists("excel/output"):
    os.makedirs("excel/output")
    print('Created excel/output-folder')

if not os.path.exists("excel/temp"):
    os.makedirs("excel/temp")
    print('Created excel/temp-folder')

df = get_excel() # Get file
id = uuid.uuid4()
df.to_csv(f'excel/temp/temp-{id}.csv') # Convert to csv for clean-up
df = pd.read_csv(f'excel/temp/temp-{id}.csv') # Save that

# Renaming columns
print('Renaming columns')
df = df.rename(columns={'Unnamed: 12': 'Days since password last set', 
                        'Unnamed: 4': 'Display Name', 
                        'Unnamed: 6': 'Common Name', 
                        'Unnamed: 9': 'SAM Account Name', 
                        'Unnamed: 10': 'Domain Name',
                        'Unnamed: 11': 'Account Status'})

print('Converting column from string to numeric value...')
df['Days since password last set'] = pd.to_numeric(df['Days since password last set'], errors='coerce') # Convert to float

# # # # # # # # # # # # # # # # # # # # # # # # # 
# Filtering all users with following parameters #
# # # # # # # # # # # # # # # # # # # # # # # # # 

print('Filtering data...')
df = df[df['Days since password last set'] >= 90] # Remove all entries below or equal to 90
df = df[df['Account Status'] == "Enabled"] # Remove all entries without enabled account


print(f'Removing entries containing \n{new_strings}')
for s in new_strings: # Remove all entries containing specific string values -> see top of document
    df = df[~df['Display Name'].str.contains(s, case=False)]

for s in new_strings: # Remove all entries containing specific string values -> see top of document
    df = df[~df['Common Name'].str.contains(s, case=False)]

for s in new_strings: # Remove all entries containing specific string values -> see top of document
    df = df[~df['SAM Account Name'].str.contains(s, case=False)]

df = df[~df['SAM Account Name'].str.lower().str.startswith("ex")] # str.startswith is case-sensitive
df = df[~df['Display Name'].str.startswith("-")]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Remove all users present in following CSV/XLSX files  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

manhattan = pd.read_csv(f'excel/filters/manhattan.csv', sep=";") # Filter out everyone in Manhattan
ext1 = pd.read_csv(f'excel/filters/ext1.csv', sep=";")  # Filter out all external members
ext2 = pd.read_csv(f'excel/filters/ext2.csv', sep=";")  # Filter out all external members
excluded = pd.read_excel(f'excel/filters/excluded.xlsx')  # Filter out all external members
ext = pd.read_excel(f'excel/filters/externe.xlsx')  # Filter out all external members
df = df[~df['Display Name'].isin(manhattan['Displayname'])]
df = df[~df['Display Name'].isin(ext1['Displayname'])]
df = df[~df['Display Name'].isin(ext2['Displayname'])]
df = df[~df['Display Name'].isin(excluded['Display Name'])]
df = df[~df['Display Name'].isin(ext['Display Name'])]

print('Filtering is done')

# Remove excess / Drop empty unwanted columns
print('Trimming excess')
df = df.dropna(how='all', axis=1)
df = df.drop(df.columns[[0, 1]], axis=1)

save_file()

# Removing temp files

os.remove(f"excel/temp/temp-{id}.csv")