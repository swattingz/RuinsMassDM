# Join For Support! <33      #
# https://discord.gg/84qrxhjm #
import requests 
import colorama 
import os       
from colorama import Fore  
from colorama import Style 



def greenblue(text):
    os.system(""); faded = ""
    blue = 100
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded

print(greenblue(f"""
   ▄████████      ███    █▄        ▄█       ███▄▄▄▄   
  ███    ███      ███    ███      ███       ███▀▀▀██▄ 
  ███    ███      ███    ███      ███▌      ███   ███ 
 ▄███▄▄▄▄██▀      ███    ███      ███▌      ███   ███ 
▀▀███▀▀▀▀▀        ███    ███      ███▌      ███   ███ 
▀███████████      ███    ███      ███       ███   ███ 
  ███    ███      ███    ███      ███       ███   ███ 
  ███    ███      ████████▀       █▀         ▀█   █▀  
  ███    ███                                          
[ dev // ruin kapa#4068 ]        
                                                                          
                                                                          
             ____
            / . .\\                      
            \\  ---< big slime             
             \\  /
   __________/ /
-=:___________/

"""))  

Token = input("\x1b[38;5;199m╚[\x1b[0m$user\x1b[38;5;199m] \x1b[0m Enter Token >")
content = input("\x1b[38;5;199m ╚[\x1b[0m$user\x1b[38;5;199m] \x1b[0m Message > ")
headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
mass_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
for channel in mass_dm_request:
    json = {"content": f"{content}"}
    r = requests.post(
        f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
        headers=headers,
        data=json,
    )
print(f" \x1b[38;5;199m[\x1b[0mLOG\x1b[38;5;199m] \x1b[0m Dm Sent \x1b[38;5;199m[\x1b[0m {channel['id']} \x1b[38;5;199m] \x1b[0m")