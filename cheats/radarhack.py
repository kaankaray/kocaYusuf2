from sources import globals
from sources.getOffsets import dwLocalPlayer, m_iTeamNum, dwEntityList, m_bSpotted

def execute():
    if globals.pause_flag3:
        if globals.pm.read_int(globals.client + dwLocalPlayer):
            localplayer = globals.pm.read_int(globals.client + dwLocalPlayer)
            localplayer_team = globals.pm.read_int(localplayer + m_iTeamNum)
            for i in range(64):
                if globals.pm.read_int(globals.client + dwEntityList + i * 0x10):
                    entity = globals.pm.read_int(globals.client + dwEntityList + i * 0x10)
                    entity_team = globals.pm.read_int(entity + m_iTeamNum)
                    if entity_team != localplayer_team:
                        globals.pm.write_int(entity + m_bSpotted, 1)