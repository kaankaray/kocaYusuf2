from sources.imports import *
from sources.getOffsets import dwClientState, lastUpdated
from sources import globals

from cheats import wallhack as wallhackClass
from cheats import noflashhack as noflashhackClass
from cheats import radarhack as radarhackClass
from cheats import bhophack as bhophackClass
from cheats import triggerhack as triggerhackClass

from GUI import gui as guiClass

class Worker(QRunnable):
    @pyqtSlot()
    def run(self):
        with open("keybinds.json") as json_file:

            data = json.load(json_file)
            globals.wall_key = data["keybinds"]["wall_key"]
            globals.flash_key = data["keybinds"]["flash_key"]
            globals.radar_key = data["keybinds"]["radar_key"]
            globals.bhop_key = data["keybinds"]["bhop_key"]
            globals.trigger_key = data["keybinds"]["trigger_key"]
            globals.aim_key = data["keybinds"]["aim_key"]

            globals.pause_flag1 = data["flags"]["isWallEnabled"]
            globals.pause_flag2 = data["flags"]["isNoFlashEnabled"]
            globals.pause_flag3 = data["flags"]["isRadarEnabled"]
            globals.pause_flag4 = data["flags"]["isBhopEnabled"]
            globals.pause_flag5 = data["flags"]["isTriggerEnabled"]
            globals.pause_flag6 = data["flags"]["isAimEnabled"]
            guiClass.ui.updateButtons()
        while True:
            try:
                globals.pm = pymem.Pymem("csgo.exe")
                globals.client = pymem.process.module_from_name(globals.pm.process_handle, "client.dll").lpBaseOfDll
                globals.engine = pymem.process.module_from_name(globals.pm.process_handle, "engine.dll").lpBaseOfDll
                globals.engine_pointer = globals.pm.read_int(globals.engine + dwClientState)
                guiClass.ui.isCSGORunningCheck(True)

                while True:

                    if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                        if not ("csgo.exe" in (p.name() for p in psutil.process_iter())):  # If csgo is not running

                            break
                        continue
                    if keyboard.is_pressed(globals.wall_key):
                        guiClass.ui.wallhack()
                        sleep(0.2)
                    if keyboard.is_pressed(globals.flash_key):
                        guiClass.ui.noflash()
                        sleep(0.2)
                    if keyboard.is_pressed(globals.radar_key):
                        guiClass.ui.radar()
                        sleep(0.2)
                    if keyboard.is_pressed(globals.bhop_key):
                        guiClass.ui.bhop()
                        sleep(0.2)
                    if keyboard.is_pressed(globals.trigger_key):
                        guiClass.ui.trigger()
                        sleep(0.2)
                    # if keyboard.is_pressed(globals.aim_key):
                    #     globals.pause_flag6 = not globals.pause_flag6
                    #     guiClass.ui.updateButtons()
                    #     sleep(0.25)
                    try:
                        wallhackClass.execute()
                        noflashhackClass.execute()
                        radarhackClass.execute()
                        bhophackClass.execute()
                        triggerhackClass.execute()
                    except:
                        print("Smth went wrong.")
                        sleep(5)
                        continue
            except:
                guiClass.ui.isCSGORunningCheck(False)
                print("App not working")
                sleep(5);



if __name__ == '__main__':
    guiClass.execute()