# Noctus – Red Team Toolkit

## Overview
Noctus is a modular red team toolkit designed for offensive security operations. It combines reconnaissance, exploitation, and post-exploitation cleanup into a single cohesive framework. The toolkit emphasizes automation, stealth, and adaptability, making it a valuable resource for ethical hackers and cybersecurity professionals.

## Features
- **Automated Reconnaissance**
  - Host discovery, port scanning, and service enumeration with Nmap  
  - Subdomain extraction from certificate transparency logs  
  - WHOIS lookups for domain intelligence  

- **Exploitation Module**
  - Metasploit RPC integration for automated exploit delivery  
  - Dynamic exploit search and selection  
  - Payload management and interactive sessions  

- **Stealth and Cleanup**
  - Log clearing on Linux and Windows systems  
  - Command history removal  
  - Temporary file deletion  

- **Modular Architecture**
  - Each stage (Recon, Exploitation, Cleanup) is implemented as an independent module  
  - New attack vectors or recon techniques can be added without disrupting the framework  

## Technical Stack
- **Language:** Python 3  
- **Libraries & Tools:**  
  - `nmap` for scanning and service detection  
  - `requests` for web requests  
  - `whois` for domain lookups  
  - `pymetasploit3` for RPC interactions  
  - `colorama` for terminal output styling  
  - Built-in modules: `socket`, `subprocess`, `platform`, `os`, `re`, `time`  

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/noctus.git
   cd noctus
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure that Nmap and Metasploit are installed and accessible from your system path.)*

## Usage
Run the main entry point:
```bash
python3 main.py
```

You will be presented with an interactive menu:
- **1. Recon** – Perform domain reconnaissance and port scanning  
- **2. Exploit** – Launch exploitation using Metasploit RPC  
- **3. Cleanup** – Clear logs, histories, and temp files for stealth operations  
- **4. Exit** – Quit the toolkit  

## Project Structure
```
├── main.py                 # Entry point for the toolkit
├── noctus_recon.py         # Reconnaissance module
├── noctus_exploitation.py  # Exploitation module
├── noctus_cleanup.py       # Cleanup module
└── Final Presentation.pdf  # Project documentation
```

## Disclaimer
This toolkit is developed for **educational purposes and authorized penetration testing only**. The authors and contributors do not take responsibility for any misuse. Always ensure you have explicit permission before testing against any system.
