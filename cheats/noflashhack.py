from sources import globals
from sources.getOffsets import dwLocalPlayer, m_flFlashMaxAlpha

def execute():
    # No flash
    if globals.pause_flag2:
        player = globals.pm.read_int(globals.client + dwLocalPlayer)
        if player:
            flash_value = player + m_flFlashMaxAlpha
            if flash_value:
                globals.pm.write_float(flash_value, float(0))