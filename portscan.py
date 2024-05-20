import subprocess
import sys
import nmap3

# Function to check if a package is installed
def check_install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to check if the nmap3 library is up-to-date
def check_update_nmap3():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "python3-nmap"])

# Check and install/update python3-nmap
check_install_package("nmap3")
check_update_nmap3()

# Import the nmap3 library
import nmap3

# Initialize Nmap scanner
nmap = nmap3.Nmap()

# OS detection
def os_detection(target):
    os_results = nmap.nmap_os_detection(target)
    return os_results

# Version detection
def version_detection(target):
    version_results = nmap.nmap_version_detection(target)
    return version_results

# Top 10 ports scan
def top_ports_scan(target, top_ports):
    args = f"-F --top-ports {top_ports}"
    scan_results = nmap.scan_top_ports(target, args=args)
    return scan_results

# DNS brute force
def dns_brute(target):
    dns_results = nmap.nmap_dns_brute_script(target)
    return dns_results

# Scanning techniques
def nmap_fin_scan(target):
    return nmap.nmap_fin_scan(target)

def nmap_idle_scan(target):
    return nmap.nmap_idle_scan(target)

def nmap_ping_scan(target):
    return nmap.nmap_ping_scan(target)

def nmap_syn_scan(target):
    return nmap.nmap_syn_scan(target)

def nmap_tcp_scan(target):
    return nmap.nmap_tcp_scan(target)

def nmap_udp_scan(target):
    return nmap.nmap_udp_scan(target)

# Main function
def main():
    target = input("Enter the target IP or domain: ")
    top_ports = input("Enter the number of top ports to scan (e.g., 10): ")

    print("Performing OS detection...")
    print(os_detection(target))

    print("Performing version detection...")
    print(version_detection(target))

    print(f"Scanning top {top_ports} ports...")
    print(top_ports_scan(target, top_ports))

    print("Performing DNS brute force...")
    print(dns_brute(target))

    print("Performing FIN scan...")
    print(nmap_fin_scan(target))

    print("Performing Idle scan...")
    print(nmap_idle_scan(target))

    print("Performing Ping scan...")
    print(nmap_ping_scan(target))

    print("Performing SYN scan...")
    print(nmap_syn_scan(target))

    print("Performing TCP scan...")
    print(nmap_tcp_scan(target))

    print("Performing UDP scan...")
    print(nmap_udp_scan(target))

if __name__ == "__main__":
    main()
