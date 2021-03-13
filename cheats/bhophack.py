from sources import globals
from sources.getOffsets import dwForceJump, dwLocalPlayer, m_fFlags
from sources.imports import time, keyboard

def execute():
    if globals.pause_flag4:
        if keyboard.is_pressed("space"):
            force_jump = globals.client + dwForceJump
            player = globals.pm.read_int(globals.client + dwLocalPlayer)
            if player:
                on_ground = globals.pm.read_int(player + m_fFlags)
                if on_ground and on_ground == 257:
                    globals.pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    globals.pm.write_int(force_jump, 4)
            time.sleep(0.002)