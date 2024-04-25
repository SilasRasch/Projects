import pandas as pd
import os

def save_file(dataframe):
    try:
        dataframe.to_excel(f'excel/output/{input("Choose the name of the output file: ")}.xlsx', sheet_name='Data')
        print('File saved succesfully')
    except:
        print("An error occured, maybe the name was already in use. Try again")
        save_file(dataframe)

files = os.listdir("excel/temp/eol")

df_columns = ["1511", "1607", "1703", "1709", "1803", "1809", "1903", "1909", "2004", "20H2", "21H1", "21H2"]
final = pd.DataFrame({"date":"date", "version":df_columns, "count":0})
final = final.pivot(index="date", columns="version")

for file in files:
    date = file[8:18].replace('-', '/')

    df = pd.read_csv(f'excel/temp/eol/{file}', sep=",", on_bad_lines="skip")

    # Print out and save Windows EOL data.
    eol_filter = ["1511", "1607", "1703", "1709", "1803", "1809", "1903", "1909", "2004", "20H2", "21H1", "21H2"] # All the versions to be included in the report
    eol = df
    #eol['Last device update'] = pd.to_datetime(eol['Last device update'], format='%d%b%Y:%H:%M:%S.%f') # NOT DONE!!!!! CONVERT TO DATE TIME AND REMOVE ALL INACTIVE MORE THAN 1 MONTH??
    eol = eol[eol['Onboarding Status'] == "Onboarded"]
    eol = eol[eol['OS Platform'] == "Windows10"]
    eol = eol[eol['OS Version'].isin(eol_filter)] # Check if the OS Version is in the filter
    eol = eol['OS Version'].value_counts().sort_index() # Group by and sort by index 
    
    eol = pd.DataFrame({"date":file[8:18], "version":eol.index, "count":eol.values})
    eol = eol.pivot(index="date", columns="version")
    final = pd.concat([final, eol])

final.fillna(0, inplace=True)
final.to_excel(f'excel/temp/output/full.xlsx', sheet_name='Data')