import os
from math import *

try:
  import keyboard 
except ImportError:
  print("A module is not existing. Installing module: keyboard")
  os.system("python -m pip install keyboard")
  import keyboard

try:
  import pymem 
  import pymem.process
except ImportError:
  print("A module is not existing. Installing module: pymem")
  os.system("python -m pip install pymem")
  import pymem
  import pymem.process
  
try:
  import time 
  from time import sleep
except ImportError:
  print("A module is not existing. Installing module: time")
  os.system("python -m pip install time")
  import time
  from time import sleep
  
try:
  import re 
except ImportError:
  print("A module is not existing. Installing module: re")
  os.system("python -m pip install re")
  import re
  
try:
  from termcolor import colored, cprint 
except ImportError:
  print("A module is not existing. Installing module: termcolor")
  os.system("python -m pip install termcolor")
  from termcolor import colored, cprint 

try:
  import requests 
except ImportError:
  print("A module is not existing. Installing module: requests")
  os.system("python -m pip install requests")
  import requests
  
try:
  from datetime import datetime
except ImportError:
  print("A module is not existing. Installing module: datetime")
  os.system("python -m pip install datetime")
  from datetime import datetime

try:
  from win32gui import GetWindowText, GetForegroundWindow
  import win32api
except ImportError:
  print("A module is not existing. Installing module: pywin32")
  os.system("python -m pip install pywin32")
  from win32gui import GetWindowText, GetForegroundWindow
  import win32api
  

url = 'https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json'
response = requests.get(url).json()
lastUpdated = datetime.fromtimestamp(int(response["timestamp"]))

dwEntityList =  int(response["signatures"]["dwEntityList"])
dwGlowObjectManager = int(response["signatures"]["dwGlowObjectManager"])
m_iGlowIndex = int(response["netvars"]["m_iGlowIndex"])
m_iTeamNum = int(response["netvars"]["m_iTeamNum"])
m_iHealth = int(response["netvars"]["m_iHealth"])
m_iAccountID = (int(response["netvars"]["m_iAccountID"]))
is_c4_owner = int(response["signatures"]["is_c4_owner"])
dwPlayerResource = int(response["signatures"]["dwPlayerResource"])
dwForceJump = int(response["signatures"]["dwForceJump"])
dwForceAttack = int(response["signatures"]["dwForceAttack"])
dwLocalPlayer = int(response["signatures"]["dwLocalPlayer"])
m_fFlags = int(response["netvars"]["m_fFlags"])
m_flFlashMaxAlpha = int(response["netvars"]["m_flFlashMaxAlpha"])
m_bSpotted = int(response["netvars"]["m_bSpotted"])
m_dwBoneMatrix = int(response["netvars"]["m_dwBoneMatrix"])
m_bDormant = int(response["signatures"]["m_bDormant"])
dwClientState = int(response["signatures"]["dwClientState"])
dwClientState_ViewAngles = int(response["signatures"]["dwClientState_ViewAngles"])
m_vecOrigin = int(response["netvars"]["m_vecOrigin"])
m_vecViewOffset  = int(response["netvars"]["m_vecViewOffset"])
dwbSendPackets = int(response["signatures"]["dwbSendPackets"])
dwInput = int(response["signatures"]["dwInput"])
clientstate_last_outgoing_command = int(response["signatures"]["clientstate_last_outgoing_command"])
clientstate_net_channel = int(response["signatures"]["clientstate_net_channel"])
m_iCrosshairId = int(response["netvars"]["m_iCrosshairId"])
m_bGunGameImmunity = int(response["netvars"]["m_bGunGameImmunity"])
m_bSpottedByMask = int(response["netvars"]["m_bSpottedByMask"])



global pause_flag1, pause_flag2, pause_flag3, pause_flag4, pause_flag5, pause_flag6
trigger_key = "+"

def get_key(self) :
    key = win32api.GetKeyState(0x04)
    if key == -127 or key == -128 :
        key = True
    else :
        key = False
    return key;

def calcangle(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
    x = -atan2(dst_x - src_x, dst_y - src_y) / pi * 180.0 + 180.0
    y = asin((dst_z - src_z) / Distance(src_x, src_y, src_z, dst_x, dst_y, dst_z)) * 180.0 / pi
    return x, y

def normalizeAngles(self, viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY

def checkangles(self, x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else :
        return True

def nanchecker(self, first, second):
    if math.isnan(first) or math.isnan(second):
        return False
    else :
        return True

def calc_distance(self, current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex

    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey
    
def checkindex(self) :
    localplayer = pm.read_int(client + dwLocalPlayer)
    for y in range(64):
        if pm.read_int(client + dwEntityList + y * 0x10):
            entity = pm.read_int(client + dwEntityList + y * 0x10)
            if localplayer == entity and y:
                return y

def Magnitude(self, vec_x, vec_y, vec_z):
    return sqrt(vec_x * vec_x + vec_y * vec_y + vec_z * vec_z)

def Subtract(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
    diff_x = src_x - dst_x
    diff_y = src_y - dst_y
    diff_z = src_z - dst_z
    return (diff_x, diff_y, diff_z)

def Distance(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
    diff_x, diff_y, diff_z = Subtract(src_x, src_y, src_z, dst_x, dst_y, dst_z)
    src_x += diff_x
    src_y += diff_y
    return Magnitude(diff_x, diff_y, diff_z)

def GetBestTarget(self, local):
    while True:
        olddist = 1.7976931348623157e+308
        newdist = None
        target = None
        if local :
            localplayer_team = pm.read_int(local + m_iTeamNum)
            for x in range(1):
                entity_id = pm.read_int(local + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)
                if pm.read_int(client + dwEntityList + x * 0x10):
                    spotted = pm.read_int(entity + m_bSpottedByMask)
                    index = checkindex()
                    entity_health = pm.read_int(entity + m_iHealth)
                    entity_team = pm.read_int(entity + m_iTeamNum)
                    if localplayer_team != entity_team and entity_health > 0 :# and spotted == 1 << index:
                        entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                        localpos_x = pm.read_float(local + m_vecOrigin)
                        localpos_y = pm.read_float(local + m_vecOrigin + 4)
                        localpos_z = pm.read_float(local + m_vecOrigin + 8)
    
                        localpos_x_angles = pm.read_float(enginepointer + dwClientState_ViewAngles)
                        localpos_y_angles = pm.read_float(enginepointer + dwClientState_ViewAngles + 0x4)
                        localpos_z_angles = pm.read_float(enginepointer + dwClientState_ViewAngles + 0x8)

                        bone = 8 #head
                        entitypos_x = pm.read_float(entity_bones + 0x30 * bone + 0xC)
                        entitypos_y = pm.read_float(entity_bones + 0x30 * bone + 0x1C)
                        entitypos_z = pm.read_float(entity_bones + 0x30 * bone + 0x2C) + 64
    
                        X, Y = calcangle(entitypos_x, entitypos_y, entitypos_z, localpos_x, localpos_y, localpos_z)
                        newdist = Distance(localpos_x_angles, localpos_y_angles, localpos_z_angles, entitypos_x, entitypos_y, entitypos_z)
                        olddist = newdist
                        target = entity
            if target:
                return target




def main():
    def state():
        os.system('cls')
        print("Koca yusuf2 (weak version) \nUpdated:", lastUpdated.strftime("%a %d %b %Y - %H:%M"))
        print("\nWall(F5): ", 'You are having a good day.' if not pause_flag1 else 'Off')
        print("No flash(F6): ", "On" if not pause_flag2 else "Off")
        print("Radar(F7): ", "On" if not pause_flag3 else "Off")
        print("bhop(F8): ", "Hop hop" if not pause_flag4 else "Off")
        print("Trigger(F9): ", "On" if not pause_flag5 else "Off")
        # print("Aimbot(F10): ", "Bum bum" if not pause_flag6 else "Off")
        
    pause_flag1 = pause_flag2 = pause_flag3 = pause_flag4 = pause_flag5 = pause_flag6 = True
    
    try :
        pm = pymem.Pymem("csgo.exe")
    except :
        response = requests.get(url).json()
        lastUpdated = datetime.fromtimestamp(int(response["timestamp"]))
        os.system('cls')
        print("Koca yusuf2 (weak version) \nUpdated:", lastUpdated.strftime("%a %d %b %Y - %H:%M"))
        print("CS:GO is not running.")
        sleep(5);
        return
    state()
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_int(engine + dwClientState)
    
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
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(entity_HP/100))     # R 
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1-entity_HP/100))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))                 # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))              # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)                         # Enable glow

                        elif entity_team_id == playerTeam:  # Teammate
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))                   # R
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1 - entity_HP/100))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))                   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))                # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)                           # Enable glow
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
            # Trigger
            if keyboard.is_pressed('f9'):
                pause_flag5 = not pause_flag5
                state()
                sleep(0.25)
            if pause_flag5:
                pass
            else:
                player = pm.read_int(client + dwLocalPlayer)
                entity_id = pm.read_int(player + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                entity_team = pm.read_int(entity + m_iTeamNum)
                player_team = pm.read_int(player + m_iTeamNum)

                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    time.sleep(0.02)
                    pm.write_int(client + dwForceAttack, 6)
                    time.sleep(0.04)
            # Aimbot (Not available.)
            if keyboard.is_pressed('f13'):
                pause_flag6 = not pause_flag6
                state()
                sleep(0.25)
            if pause_flag6:
                pass
            else:
                time.sleep(0.002)

                aimlocalplayer = pm.read_int(client + dwLocalPlayer)
                aimflag = pm.read_int(aimlocalplayer + m_fFlags)
                aimteam = pm.read_int(aimlocalplayer + m_iTeamNum)
                    
                for y in range(1):

                    if pm.read_int(client + dwEntityList + y * 0x10):
                        aimplayer = GetBestTarget(aimlocalplayer)
                        aimplayerbone = pm.read_int(aimplayer + m_dwBoneMatrix)
                        gungameimmunity = pm.read_int(aimplayer + m_bGunGameImmunity)
                        aimplayerteam = pm.read_int(aimplayer + m_iTeamNum)
                        aimplayerhealth = pm.read_int(aimplayer + m_iHealth)
                        if aimplayerteam != aimteam and aimplayerhealth > 0 and gungameimmunity != 1:
                            localpos1 = pm.read_float(aimlocalplayer + m_vecOrigin)
                            localpos2 = pm.read_float(aimlocalplayer + m_vecOrigin + 4)
                            if aimflag == 263:
                                localpos3 = pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 45
                            elif aimflag == 257:
                                localpos3 = pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 62
                            elif aimflag == 256:
                                localpos3 = pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 64
                                    
                            bone = 8 #head
                            enemypos1 = pm.read_float(aimplayerbone + 0x30 * bone + 0xC)
                            enemypos2 = pm.read_float(aimplayerbone + 0x30 * bone + 0x1C)
                            enemypos3 = pm.read_float(aimplayerbone + 0x30 * bone + 0x2C)
                    
                            targetline1 = enemypos1 - localpos1
                            targetline2 = enemypos2 - localpos2
                            targetline3 = enemypos3 - localpos3
                    
                            viewanglex = pm.read_float(enginepointer + dwClientState_ViewAngles)
                            viewangley = pm.read_float(enginepointer + dwClientState_ViewAngles + 0x4)
                    
                            if targetline2 == 0 and targetline1 == 0:
                                yaw = 0
                                if targetline3 > 0:
                                    pitch = 270
                                else:
                                    pitch = 90
                            else:
                                yaw = (atan2(targetline2, targetline1) * 180 / pi)
                                if yaw < 0:
                                    yaw += 360
                                hypo = sqrt(
                                (targetline1 * targetline1) + (targetline2 * targetline2) + (targetline3 * targetline3))
                                pitch = (atan2(-targetline3, hypo) * 180 / pi)
                    
                                if pitch < 0:
                                    pitch += 360
                    
                            pitch, yaw = normalizeAngles(pitch, yaw)
                            if checkangles(pitch, yaw):
                    
                                distance_x, distance_y = calc_distance(viewanglex, viewangley, pitch, yaw)
                    
                                if distance_x < 900 and distance_y < 900:
                    
                                    if nanchecker(pitch, yaw):
                                                    
                                        pm.write_float(enginepointer + dwClientState_ViewAngles, pitch)
                                        pm.write_float(enginepointer + dwClientState_ViewAngles + 0x4, yaw)
        except:
            time.sleep(0.1)
            continue

    
    
if __name__ == '__main__':
    while True:
        main()

os.system('pause')