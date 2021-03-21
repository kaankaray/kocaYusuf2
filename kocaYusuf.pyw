from sources.imports import json, pymem, psutil, GetWindowText, GetForegroundWindow, QRunnable, pyqtSlot, QCoreApplication

from sources.getOffsets import dwClientState, lastUpdated
from sources import globals

from pynput import keyboard
from time import sleep

from cheats import wallhack as wallhackClass
from cheats import noflashhack as noflashhackClass
from cheats import radarhack as radarhackClass
from cheats import bhophack as bhophackClass
from cheats import triggerhack as triggerhackClass

from GUI import gui as guiClass

def on_press(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in [globals.wall_key, globals.flash_key, globals.radar_key, globals.bhop_key, globals.trigger_key]:
        if k == globals.wall_key:
            globals.pause_flag1 = not globals.pause_flag1
        elif k == globals.flash_key:
            globals.pause_flag2 = not globals.pause_flag2
        elif k == globals.radar_key:
            globals.pause_flag3 = not globals.pause_flag3
        elif k == globals.bhop_key:
            globals.pause_flag4 = not globals.pause_flag4
        elif k == globals.trigger_key:
            globals.pause_flag5 = not globals.pause_flag5

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
            # globals.aim_key = data["keybinds"]["aim_key"]

            globals.pause_flag1 = data["flags"]["isWallEnabled"]
            globals.pause_flag2 = data["flags"]["isNoFlashEnabled"]
            globals.pause_flag3 = data["flags"]["isRadarEnabled"]
            globals.pause_flag4 = data["flags"]["isBhopEnabled"]
            globals.pause_flag5 = data["flags"]["isTriggerEnabled"]
            # globals.pause_flag6 = data["flags"]["isAimEnabled"]

            guiClass.ui.updateButtons()
            guiClass.ui.retranslateUi(guiClass.MainWindow)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()  # start to listen on a separate thread

        guiClass.ui.label_2.setText(QCoreApplication.translate("MainWindow", "Updated: " + str(lastUpdated)))

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
                    try:
                        wallhackClass.execute()
                        noflashhackClass.execute()
                        radarhackClass.execute()
                        bhophackClass.execute()
                        triggerhackClass.execute()
                        # guiClass.ui.updateButtons()
                    except:
                        print("Smth went wrong.")
                        sleep(5)
                        continue
            except:
                guiClass.ui.isCSGORunningCheck(False)
                print("App not working")
                sleep(5)



if __name__ == '__main__':
    guiClass()


