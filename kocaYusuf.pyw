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
        try:

            globals.pm = pymem.Pymem("csgo.exe")
            globals.client = pymem.process.module_from_name(globals.pm.process_handle, "client.dll").lpBaseOfDll
            globals.engine = pymem.process.module_from_name(globals.pm.process_handle, "engine.dll").lpBaseOfDll
            globals.engine_pointer = globals.pm.read_int(globals.engine + dwClientState)
        except:
            print("Koca yusuf2 (weak version) \nUpdated:", lastUpdated.strftime("%a %d %b %Y - %H:%M"))
            print("CS:GO is not running.")
            sleep(5);
            return
        while True:
            try:
                # if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                #     # if not ("csgo.exe" in (p.name() for p in psutil.process_iter())):  # If csgo is not running
                #     #    appShouldWork = False
                #     #    break
                #     continue

                wallhackClass.execute()
                noflashhackClass.execute()
                radarhackClass.execute()
                bhophackClass.execute()
                triggerhackClass.execute()
            except:
                print("Smth went wrong.")
                sleep(5)


if __name__ == '__main__':
    with open('keybinds.json') as json_file:
        data = json.load(json_file)
        wall_key = data["keybinds"]["wall_key"]
        flash_key = data["keybinds"]["flash_key"]
        radar_key = data["keybinds"]["radar_key"]
        bhop_key = data["keybinds"]["bhop_key"]
        trigger_key = data["keybinds"]["trigger_key"]
        aim_key = data["keybinds"]["aim_key"]

        pause_flag1 = data["flags"]["isWallEnabled"]
        pause_flag2 = data["flags"]["isNoFlashEnabled"]
        pause_flag3 = data["flags"]["isRadarEnabled"]
        pause_flag4 = data["flags"]["isBhopEnabled"]
        pause_flag5 = data["flags"]["isTriggerEnabled"]
        pause_flag6 = data["flags"]["isAimEnabled"]
    guiClass.execute()