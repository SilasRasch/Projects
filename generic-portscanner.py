import nmap

ports = input('Input the ports you would like to scan for')

def scan_smb1(network, ports):
    nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
    nm = nmap.PortScanner(nmap_search_path=nmap_path)
    scanning = nm.scan(hosts=network, arguments=f'-p{ports} --open --reason -Pn -T4')

scan_smb1(input('Input the IP / Network '), ports)