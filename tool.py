import colorama as ca
import time as ti
import os
import requests
import base64
import json
import sys

# Initialize colorama
ca.init()

# Configuration
CURRENT_VERSION = "1"  # Will be overwritten by local version.txt
GITHUB_REPO = "obliviontool/Xarma"  # Your GitHub repo
VERSION_FILE = "version.txt"  # Version file name
MAIN_SCRIPT = "tool.py"  # Main script to update

# Set working directory to script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Colors
YELLOW = ca.Fore.YELLOW
GREEN = ca.Fore.GREEN
RED = ca.Fore.RED
PURPLE = ca.Fore.MAGENTA
BLUE = ca.Fore.BLUE
WHITE = ca.Fore.WHITE
CYAN = ca.Fore.CYAN

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def holographic_intro():
    # ASCII art for each letter with progressive buildup
    x_art = [
        r"""
         \   /
          \ /
           X
          / \
         /   \
        """,
        r"""
        \     /
         \   /
          \ /
           X
          / \
         /   \
        /     \
        """
    ]
    
    a_art = [
        r"""
          /\
         /  \
        /    \
        """,
        r"""
          /\
         /  \
        /____\
        |    |
        |    |
        """
    ]
    
    r_art = [
        r"""
        |------
        |     \
        |      \
        """,
        r"""
        |------
        |     \
        |      \
        |       \
        |        \
        """
    ]
    
    m_art = [
        r"""
        |\  /|
        | \/ |
        """,
        r"""
        |\    /|
        | \  / |
        |  \/  |
        |      |
        |      |
        """
    ]
    
    a2_art = a_art  # Reuse A art for the second A
    
    # Animation sequence
    letters = [
        (x_art, "X"),
        (a_art, "A"),
        (r_art, "R"),
        (m_art, "M"),
        (a2_art, "A")
    ]
    
    # Color cycle
    colors = [ca.Fore.RED, ca.Fore.GREEN, ca.Fore.BLUE, ca.Fore.YELLOW, ca.Fore.MAGENTA, ca.Fore.CYAN]
    
    # Build up each letter with animation
    for i in range(2):  # Repeat animation twice
        for letter_art, char in letters:
            for step in letter_art:
                clear()
                color = colors[i % len(colors)]  # Cycle through colors
                print(color + step + ca.Style.RESET_ALL)
                ti.sleep(0.1)
            ti.sleep(0.2)
        
        # Show full "XARMA" at the end of each cycle
        if i == 0:
            clear()
            final_art = r"""
             \     /    /\      |------    |\    /|    /\
              \   /    /  \     |     \    | \  / |   /  \
               \ /    /____\    |      \   |  \/  |  /____\
                X    |    |     |       \  |      |  |    |
               / \   |    |     |        \ |      |  |    |
              /   \  |    |     |         \|      |  |    |
             /     \ |    |     |          \      |  |    |
            """
            print(colors[i] + final_art + ca.Style.RESET_ALL)
            ti.sleep(0.5)
    
    clear()
    # Final XARMA display
    print(ca.Fore.CYAN + r"""
 __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/ 
    """ + ca.Style.RESET_ALL)
    ti.sleep(1.5)
    clear()

def read_local_version():
    try:
        if os.path.exists(VERSION_FILE):
            with open(VERSION_FILE, 'r') as f:
                return f.read().strip()
        return None
    except Exception as e:
        print(rf"{RED}[!] Error reading local version: {str(e)}")
        return None

def get_github_version():
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{VERSION_FILE}"
        response = requests.get(url)
        
        if response.status_code == 200:
            content = json.loads(response.text)
            if 'content' in content:
                version_content = base64.b64decode(content['content']).decode('utf-8')
                return version_content.strip()
        return None
    except Exception as e:
        print(rf"{RED}[!] Error checking GitHub version: {str(e)}")
        return None

def download_file_from_github(filename):
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{filename}"
        response = requests.get(url)
        
        if response.status_code == 200:
            content = json.loads(response.text)
            if 'content' in content:
                file_content = base64.b64decode(content['content']).decode('utf-8')
                with open(filename, 'w') as f:
                    f.write(file_content)
                return True
        return False
    except Exception as e:
        print(rf"{RED}[!] Error downloading {filename}: {str(e)}")
        return False

def AutoUpdate():
    print(rf"{YELLOW}[-] Checking for updates, please hold...")
    ti.sleep(1)
    clear()
    
    # Read local version first
    local_version = read_local_version()
    if local_version:
        global CURRENT_VERSION
        CURRENT_VERSION = local_version
    
    github_version = get_github_version()
    
    if github_version is None:
        print(rf"{RED}[!] Failed to check for updates")
        ti.sleep(2)
        clear()
        return
    
    if github_version == CURRENT_VERSION:
        NoUpdatesFound()
    else:
        UpdatesFound(github_version)

def NoUpdatesFound():
    print(rf"{YELLOW}[-] Update check complete, no updates available.")
    print(rf"{CYAN}[*] Current version: {CURRENT_VERSION}")
    ti.sleep(2)
    clear()

def UpdatesFound(latest_version):
    print(rf"{GREEN}[+] Update found! New version: {latest_version}")
    print(rf"{CYAN}[*] Current version: {CURRENT_VERSION}")
    ti.sleep(2)
    clear()
    
    print(rf"{PURPLE}[-] Downloading updates...")
    ti.sleep(1)
    
    # Download version file
    if download_file_from_github(VERSION_FILE):
        print(rf"{GREEN}[+] Updated version.txt successfully")
    else:
        print(rf"{RED}[!] Failed to update version.txt")
    
    # Download main script
    if download_file_from_github(MAIN_SCRIPT):
        print(rf"{GREEN}[+] Updated {MAIN_SCRIPT} successfully")
    else:
        print(rf"{RED}[!] Failed to update {MAIN_SCRIPT}")
    
    ti.sleep(1)
    clear()
    
    print(rf"{BLUE}[+] Update process complete!")
    print(rf"{GREEN}[+] Please restart the tool to apply updates")
    ti.sleep(3)
    clear()

if __name__ == "__main__":
    try:
        holographic_intro()
        AutoUpdate()
        
        # After update check, continue with your main program
        print(rf"{CYAN}[*] Press any key to continue...")
        input()
        
    except KeyboardInterrupt:
        print(rf"{RED}[!] Operation cancelled by user")
        sys.exit(0)
