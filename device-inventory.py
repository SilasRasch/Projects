import pandas as pd
import os

def get_csv():
    print('Input CSV filename (must be in excel folder)')
    try:
        df = pd.read_csv(f'excel/{input()}.csv', sep=",", on_bad_lines="skip")
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
        save_file(dataframe)


print(f'- Device Inventory Weekly - \nby Silas')

if not os.path.exists("excel/"):
    os.makedirs("excel/")
    print('Created excel-folder')

if not os.path.exists("excel/output"):
    os.makedirs("excel/output")
    print('Created excel/output-folder')

if not os.path.exists("excel/temp"):
    os.makedirs("excel/temp")
    print('Created excel/temp-folder')

df = get_csv()

# Print out and save Windows EOL data.
eol_filter = ["1511", "1607", "1703", "1709", "1803", "1809", "1903", "1909", "2004", "20H2", "21H1", "21H2"] # All the versions to be included in the report
eol = df
#eol['Last device update'] = pd.to_datetime(eol['Last device update'], format='%d%b%Y:%H:%M:%S.%f') # NOT DONE!!!!! CONVERT TO DATE TIME AND REMOVE ALL INACTIVE MORE THAN 1 MONTH??
eol = eol[eol['Onboarding Status'] == "Onboarded"]
eol = eol[eol['OS Platform'] == "Windows10"]
eol = eol[eol['OS Version'].isin(eol_filter)] # Check if the OS Version is in the filter
eol = eol['OS Version'].value_counts().sort_index() # Group by and sort by index

save_file(eol)

# Print out and save all MS Defender "Can be onboarded" devices

os_filter = ["Windows11", "Windows10", "WindowsServer2022", "WindowsServer2019", "WindowsServer2016", "WindowsServer2012R2", "WindowsServer2008R2", "Linux", "macOS", "iOS"]

df = df[df['Onboarding Status'] == "Can be onboarded"]
df = df[df['OS Platform'].isin(os_filter)]

save_file(df)