"""
This file is used to start the software.
"""

# Built in liabraries.
import json
import mysql.connector

# Created Modules.

from Software_UI.software_windows import Window
from Software_UI.setup_window import Welcome_page,terms_condition_page

root=Window()
root=root.setup_window()

page=Welcome_page(root)



