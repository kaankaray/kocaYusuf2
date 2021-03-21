from sources.imports import *
from sources.getOffsets import dwLocalPlayer, m_iTeamNum, dwGlowObjectManager, dwEntityList, m_iGlowIndex, m_iHealth
from sources import globals

def execute():
    if globals.pause_flag1:
        player = globals.pm.read_int(globals.client + dwLocalPlayer)
        playerTeam = globals.pm.read_int(player + m_iTeamNum)
        glow_manager = globals.pm.read_int(globals.client + dwGlowObjectManager)
        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = globals.pm.read_int(globals.client + dwEntityList + i * 0x10)
            if entity:
                entity_team_id = globals.pm.read_int(entity + m_iTeamNum)
                entity_glow = globals.pm.read_int(entity + m_iGlowIndex)
                entity_HP = globals.pm.read_int(entity + m_iHealth)

                if entity_team_id != playerTeam:  # Enemy
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(entity_HP/100))     # R
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1-entity_HP/100))   # G
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))                 # B
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))              # Alpha
                    globals.pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)                         # Enable glow

                elif entity_team_id == playerTeam:  # Teammate
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))                   # R
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1 - entity_HP/100))   # G
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))                   # B
                    globals.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.8))                # Alpha
                    globals.pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)                           # Enable glow