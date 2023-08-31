import nmap
import csv
import datetime

ips = []

def save_to_csv(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Host'])
        writer.writerows(results)

ports = input('Input the ports you would like to scan for: ')

def scan_smb1(network, ports):
    nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)
    scanning = nm.scan(hosts=network, arguments=f'-p{ports} --open --reason -Pn -T4')
    
    # Gather string value for all IPs
    for ip in scanning['scan']:
        ips.append(ip)

scanning = scan_smb1(input('Input the IP / Network: '), ports)

date = datetime.datetime.now()
date = date.strftime("%d-%m-%Y %I%M")

filename = f'Portscanning-{date}.csv'

if(ips.__len__ == 0):
    print("There were no matches found")
else:
    save_to_csv()