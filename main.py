import sys
from colorama import init, Fore, Style
from noctus_recon import run_recon
from noctus_exploitation import main as run_exploitation
from noctus_cleanup import cleanup_system
import subprocess
import time
init(autoreset=True)

def start_metasploit_rpc():
    """Starts the Metasploit RPC server."""
    print(Fore.YELLOW + "[*] Starting Metasploit RPC Server...")
    try:
        subprocess.Popen(["msfconsole", "-q", "-x", "load msgrpc ServerPort=55552 Pass=kali"],
                         shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(10)  # Wait for Metasploit to initialize
        print(Fore.GREEN + "[+] Metasploit RPC started successfully!")
    except Exception as e:
        print(Fore.RED + f"[-] Error starting Metasploit RPC: {e}")


def print_banner():
    """Print the Noctus logo in the CLI."""
    print(Fore.RED + """
    ███╗   ██╗ ██████╗  ██████╗████████╗██╗   ██╗███████╗
    ████╗  ██║██╔═══██╗██╔════╝╚══██╔══╝██║   ██║██╔════╝
    ██╔██╗ ██║██║   ██║██║        ██║   ██║   ██║███████╗
    ██║╚██╗██║██║   ██║██║        ██║   ██║   ██║╚════██║
    ██║ ╚████║╚██████╔╝╚██████╗   ██║   ╚██████╔╝███████║
    ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝    ╚═════╝ ╚══════╝
    Red Team Toolkit
    """)

def main():
    target = None
    recon_results = None
    start_metasploit_rpc()
    while True:
        print_banner()
        choice = input(Fore.RED + "1. Recon\n2. Exploit\n3. Cleanup\n4. Exit\nNoctus > ")

        if choice == "1":
            print(" User chose Recon.")  # Debug print
            target = input("Enter target domain: ").strip()
            recon_results = run_recon(target)
            open_ports = recon_results.get("open_ports", [])
            print(f" Recon complete. Found {len(open_ports)} open ports.")
        elif choice == "2":
            print(" User chose Exploitation.")  # Debug print
            if not recon_results:
                print(Fore.RED + "[!] No reconnaissance data available. Run recon first.")
            else:
                open_ports = recon_results.get("open_ports", [])
                if open_ports:
                    run_exploitation(target, open_ports)
                else:
                    print(Fore.RED + "[!] No open ports found. Run recon first.")
        elif choice == "3":
            print(" User chose Cleanup.")  # Debug print
            cleanup_system()
        elif choice == "4":
            print(" Exiting...")  # Debug print
            break
        else:
            print(" Invalid choice.")  # Debug print

if __name__ == "__main__":
    print(" Script started.")  # Debug print
    main()