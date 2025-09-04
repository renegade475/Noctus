import nmap
import requests
import socket
import whois
import re  

def scan_ports(target):
    """Scans target with Nmap and returns open ports with full service details."""
    print("[*] Running Nmap scan...")
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV --version-all')

    open_ports = []

    for host in nm.all_hosts():
        print(f"\n[+] Scan Report for {host}:")
        for proto in nm[host].all_protocols():
            for port, port_data in nm[host][proto].items():
                service = port_data.get("name", "unknown")
                product = port_data.get("product", "").strip()
                version = port_data.get("version", "").strip()
                extrainfo = port_data.get("extrainfo", "").strip()

                service_details = service
                if product:
                    service_details += f" {product}"
                if version:
                    service_details += f" {version}"
                if extrainfo:
                    service_details += f" ({extrainfo})"

                print(f"    [+] Port {port}/{proto}: {service_details}")
                open_ports.append((port, service_details))  

    return open_ports

def extract_subdomains(domain):
    """Extracts subdomains from crt.sh."""
    print("[*] Enumerating Subdomains...")
    try:
        url = f"https://crt.sh/?q={domain}&output=json"
        response = requests.get(url, timeout=5)
        subdomains = set(re.findall(rf'\b(?:[a-zA-Z0-9-]+\.)+{domain}\b', response.text))
        return list(subdomains)
    except Exception as e:
        print(f"[-] Subdomain enumeration failed: {str(e)}")
        return []

def perform_whois_lookup(domain):
    """Performs a WHOIS lookup."""
    print("[*] Performing WHOIS Lookup...")
    try:
        w = whois.whois(domain)
        return w.text if w.text else "[-] No WHOIS data found."
    except Exception as e:
        return f"[-] WHOIS lookup failed: {str(e)}"

def run_recon(target):
    """Main reconnaissance function."""
    print(f"\n[*] Running Noctus Recon on {target}...\n")

    subdomains = extract_subdomains(target)
    open_ports = scan_ports(target)
    whois_info = perform_whois_lookup(target)

    print("\n[+] Reconnaissance Summary:")
    print(f"    [+] Found {len(subdomains)} subdomains:")
    for sub in subdomains:
        print(f"        - {sub}")

    print(f"\n    [+] Found {len(open_ports)} open ports:")
    for port, details in open_ports:
        print(f"        - Port {port}: {details}")

    print("\n[+] WHOIS Information:\n")
    print(whois_info)

    return {"subdomains": subdomains, "open_ports": open_ports, "whois_info": whois_info}

if __name__ == "__main__":
    target_domain = input("[*] Enter target domain: ").strip()
    run_recon(target_domain)
