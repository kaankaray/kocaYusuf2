from sources.globals import pm, client, pause_flag6, engine_pointer
from sources.getOffsets import *
from sources import globals


import math
from math import *

def get_key(self):
    key = win32api.GetKeyState(0x04)
    if key == -127 or key == -128:
        key = True
    else:
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
    else:
        return True


def nanchecker(self, first, second):
    if math.isnan(first) or math.isnan(second):
        return False
    else:
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


def checkindex(self):
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
        if local:
            localplayer_team = pm.read_int(local + m_iTeamNum)
            for x in range(1):
                entity_id = pm.read_int(local + m_iCrosshairId)
                entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)
                if pm.read_int(client + dwEntityList + x * 0x10):
                    spotted = pm.read_int(entity + m_bSpottedByMask)
                    index = checkindex()
                    entity_health = pm.read_int(entity + m_iHealth)
                    entity_team = pm.read_int(entity + m_iTeamNum)
                    if localplayer_team != entity_team and entity_health > 0:  # and spotted == 1 << index:
                        entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                        localpos_x = pm.read_float(local + m_vecOrigin)
                        localpos_y = pm.read_float(local + m_vecOrigin + 4)
                        localpos_z = pm.read_float(local + m_vecOrigin + 8)

                        localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                        localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                        localpos_z_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x8)

                        bone = 8  # head
                        entitypos_x = pm.read_float(entity_bones + 0x30 * bone + 0xC)
                        entitypos_y = pm.read_float(entity_bones + 0x30 * bone + 0x1C)
                        entitypos_z = pm.read_float(entity_bones + 0x30 * bone + 0x2C) + 64

                        X, Y = calcangle(entitypos_x, entitypos_y, entitypos_z, localpos_x, localpos_y, localpos_z)
                        newdist = Distance(localpos_x_angles, localpos_y_angles, localpos_z_angles, entitypos_x,
                                           entitypos_y, entitypos_z)
                        olddist = newdist
                        target = entity
            if target:
                return target


def execute():
    # Aimbot (Not available atm.)
    if pause_flag6:
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

                    bone = 8  # head
                    enemypos1 = pm.read_float(aimplayerbone + 0x30 * bone + 0xC)
                    enemypos2 = pm.read_float(aimplayerbone + 0x30 * bone + 0x1C)
                    enemypos3 = pm.read_float(aimplayerbone + 0x30 * bone + 0x2C)

                    targetline1 = enemypos1 - localpos1
                    targetline2 = enemypos2 - localpos2
                    targetline3 = enemypos3 - localpos3

                    viewanglex = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                    viewangley = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)

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
                                pm.write_float(engine_pointer + dwClientState_ViewAngles, pitch)
                                pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, yaw)