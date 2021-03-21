from sources import globals
from sources.getOffsets import m_iCrosshairId, dwLocalPlayer, dwEntityList, m_iTeamNum, dwForceAttack
from sources.imports import time

def execute():
    if globals.pause_flag5:
        player = globals.pm.read_int(globals.client + dwLocalPlayer)
        entity_id = globals.pm.read_int(player + m_iCrosshairId)
        entity = globals.pm.read_int(globals.client + dwEntityList + (entity_id - 1) * 0x10)

        entity_team = globals.pm.read_int(entity + m_iTeamNum)
        player_team = globals.pm.read_int(player + m_iTeamNum)

        if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
            time.sleep(0.01)
            globals.pm.write_int(globals.client + dwForceAttack, 6)
            time.sleep(0.05)