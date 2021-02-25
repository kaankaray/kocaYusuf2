import keyboard
import pymem
import pymem.process
import time
import re
from time import sleep
import os
from termcolor import colored, cprint
import requests
from datetime import datetime

from win32gui import GetWindowText, GetForegroundWindow

url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(url).json()
lastUpdated = datetime.fromtimestamp(int(response["timestamp"]))

dwEntityList = int(response["signatures"]["dwEntityList"])
dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_iHealth = int(response["netvars"]["m_iHealth"])
m_iAccountID = (int(response["netvars"]["m_iAccountID"]))
is_c4_owner = int(response["signatures"]["is_c4_owner"])
dwPlayerResource = int(response["signatures"]["dwPlayerResource"])
dwForceJump = int(response["signatures"]["dwForceJump"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_fFlags = int(response["netvars"]["m_fFlags"])
m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])
m_bSpotted = int(response["netvars"]["m_bSpotted"])


global pause_flag1, pause_flag2, pause_flag3, pause_flag4 

def main():
    def state():
        os.system('cls')
        print("Koca yusuf2 (zayif versiyon) \nUpdated:", lastUpdated.strftime("%a %d %b %Y - %H:%M"))
        print("\nWall(F5): ", 'Iyi gunundesin.' if not pause_flag1 else 'Off')
        print("No flash(F6): ", "Hoppaa" if not pause_flag2 else "Off")
        print("Radar(F7): ", "Goruyorum oc" if not pause_flag3 else "Off")
        print("bhop(F8): ", "Hop hop" if not pause_flag4 else "Off")
        
    pause_flag1 = pause_flag2 = pause_flag3 = pause_flag4 = True
    state()
    print("Bam bam modu basladi.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    state()
    sleep(2)
    while True:
        try: 
            #ESP
            if keyboard.is_pressed('f5'):
                pause_flag1 = not pause_flag1
                state()
                sleep(0.25)
            if pause_flag1:
                pass
            else:
                glow_manager = pm.read_int(client + dwGlowObjectManager)
                player = pm.read_int(client + dwLocalPlayer)
                playerTeam = pm.read_int(player + m_iTeamNum)
                for i in range(1, 32):  # Entities 1-32 are reserved for players.
                    entity = pm.read_int(client + dwEntityList + i * 0x10)
                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)
                        entity_HP = pm.read_int(entity + m_iHealth)

                        if entity_team_id != playerTeam:  # Enemy
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(entity_HP/100))   # R 
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1-entity_HP/100))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))  # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow

                        elif entity_team_id == playerTeam:  # Teammate
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   # R
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1 - entity_HP/100))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))  # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow
            #No flash
            if keyboard.is_pressed('f6'):
                pause_flag2 = not pause_flag2
                state()
                sleep(0.25)
            if pause_flag2:
                pass
            else:
                player = pm.read_int(client + dwLocalPlayer)
                if player:
                    flash_value = player + m_flFlashMaxAlpha
                    if flash_value:
                        pm.write_float(flash_value, float(0))
            #Radar Hack
            if keyboard.is_pressed('f7'):
                pause_flag3 = not pause_flag3
                state()
                sleep(0.25)
            if pause_flag3:
                pass
            else:
                if pm.read_int(client + dwLocalPlayer):
                    localplayer = pm.read_int(client + dwLocalPlayer)
                    localplayer_team = pm.read_int(localplayer + m_iTeamNum)
                    for i in range(64):
                        if pm.read_int(client + dwEntityList + i * 0x10):
                            entity = pm.read_int(client + dwEntityList + i * 0x10)
                            entity_team = pm.read_int(entity + m_iTeamNum)
                            if entity_team != localplayer_team:
                                pm.write_int(entity + m_bSpotted, 1)   
            # BHOP
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                    continue
            if keyboard.is_pressed('f8'):
                pause_flag4 = not pause_flag4
                state()
                sleep(0.25)
            if pause_flag4:
                pass
            else:
                if keyboard.is_pressed("space"):
                    force_jump = client + dwForceJump
                    player = pm.read_int(client + dwLocalPlayer)
                    if player:
                        on_ground = pm.read_int(player + m_fFlags)
                        if on_ground and on_ground == 257:
                            pm.write_int(force_jump, 5)
                            time.sleep(0.08)
                            pm.write_int(force_jump, 4)
                    time.sleep(0.002)
        except:
            time.sleep(0.2)
            continue

    
if __name__ == '__main__':
    main()

os.system('pause')