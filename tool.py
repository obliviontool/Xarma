import colorama as ca
import time as ti
import os

# Initialize colorama
ca.init()

# OS definitions
os.system("title XARMA ^| BETA")

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

# Colors
YELLOW = ca.Fore.YELLOW
GREEN = ca.Fore.GREEN
RED = ca.Fore.RED
PURPLE = ca.Fore.MAGENTA
BLUE = ca.Fore.BLUE
WHITE = ca.Fore.WHITE
CYAN = ca.Fore.CYAN

def AutoUpdate():
    print(rf"{YELLOW}[-] Checking for updates, please hold...")
    ti.sleep(1)
    clear()
    
    # Here you would normally check for updates
    # For this example, we'll set it to False to show updates are available
    noupdates = False  # Change this based on your actual update check
    
    if noupdates:
        NoUpdatesFound()
    else:
        UpdatesFound()

def NoUpdatesFound():
    print(rf"{YELLOW}[-] Update check complete, no updates available.")
    ti.sleep(1)
    clear()

def UpdatesFound():
    print(rf"{GREEN}[+] Update check complete, updates available.")
    ti.sleep(1)
    clear()
    print(rf"{PURPLE}[-] Downloading updates, please hold...")
    ti.sleep(1)
    clear()
    print(rf"{BLUE}[+] Updates downloaded successfully.")
    ti.sleep(1)
    clear()
    print(rf"{GREEN}[+] Restart the tool to apply updates...")
    ti.sleep(1)
    clear()

# Main execution
if __name__ == "__main__":
    holographic_intro()  # Play the enhanced intro animation
    AutoUpdate()  # Run the update check
