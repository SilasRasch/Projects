import csv
import nmap
import pandas as pd
import datetime

scan_results = []

def scan_smb1(network):
    nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)
    scanning = nm.scan(hosts=network, arguments='-p445,139 --script smb-protocols.nse --open --reason -Pn -T4')
    
    ips = [] # Gather string for all ips
    for ip in scanning['scan']:
        ips.append(ip)
    
    for ip in ips: # Iterate through all ips, using the string-value in the if-statement to access the underlying dict
        if "SMBv1" in scanning['scan'][ip]['hostscript'][0]['output']:
            result = (ip, 'SMBv1 enabled')
            scan_results.append(result)

# CSV saving
def save_to_csv(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Host', 'Status'])
        writer.writerows(results)

# Read the excel-file with IPs

ringsted_excel = pd.read_excel('excel/SitesAndIP.xlsx', sheet_name='Ringsted')
ringstedIP = []

for index, row in ringsted_excel.iterrows():
    if str(row['Unnamed: 1']).startswith('10.') | str(row['Unnamed: 1']).startswith('192.') | str(row['Unnamed: 1']).startswith('172.'):
        ringstedIP.append(row['Unnamed: 1'])

# Scan the IPs
date = datetime.datetime.now()
date = date.strftime("%d-%m-%Y %I%M")

filename = f'SMBv1_IPs-{date}.csv'

for network in ringstedIP:
    if __name__ == '__main__':
        print(f'Scanning {network}')
        scan_smb1(network)

if scan_results.__len__() != 0:
    save_to_csv(scan_results, filename)
    print(f'SMBv1 hosts found! Scan results saved to {filename}')
else:
    print('No SMBv1 hosts found on the network.')