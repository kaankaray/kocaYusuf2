del resources_rc.py
del ui_output.py

pyuic5 -x joseph.ui -o ui_output.py
pyrcc5 resources.qrc -o resources_rc.py