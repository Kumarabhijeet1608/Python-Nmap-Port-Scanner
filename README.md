# Python-Nmap-Port-Scanner

## Overview 👀🎯
The objective of this project is to develop a Python-based port scanner utilizing the python3-nmap library. The scanner performs various network scanning techniques including OS detection, version detection, DNS brute-forcing, and multiple types of port scans (FIN, Idle, Ping, SYN, TCP, UDP), providing a comprehensive analysis of network security and identifying potential vulnerabilities.

## Requirements
- Install and update python3-nmap Library
- The user should provide the target IP address or domain name to scan.
- The user should specify the number of top ports to scan.
- Ensure that the user has appropriate permissions to perform network scans on the target. Unauthorized scanning may be illegal and unethical.
- Install Kali-Linux in the VM.
- Virtual Machine to Execute the Python Script.

For more information about the `python3-nmap` library, including installation instructions, usage examples, and API documentation, please refer to the [python3-nmap GitHub repository](https://github.com/nmmapper/python3-nmap).



## Python Script  ✔🔥
It is provived in theformat of `portscan.py`. 


## Execution Steps in Kali Linux 👩‍💻👨‍💻


- `$ nmap your-host.com --top-ports 10`
- `pwd                                     # for current working directory.`
- `sudo python3 [filename.py]              # to execute the python file.` 
- `Output will be in the form of json`


## Features 😎💰

1. **OS Detection**
2. **Version Detection**
3. **Top Ports Scan** (User-defined limit)
4. **DNS Brute Force to List Subdomains**
5. **Various Scanning Techniques:**
    - `FIN Scan   [Identifies open ports without establishing a full TCP connection.]`
    - `Idle Scan  [A stealth scan method using a third-party idle host.]`
    - `Ping Scan  [Checks the availability of hosts on a network.]`
    - `SYN Scan   [Performs a half-open scan without completing the TCP handshake.]`
    - `TCP Scan   [Connects to target ports to check their status.]`
    - `UDP Scan   [Scans for open UDP ports.]`


## Installation
To get started, clone the repository and install the required dependencies.

