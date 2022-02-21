# -*- coding: utf-8 -*-
# contacts/main.py

"""This module provides Contacts application"""

import sys
from PyQt6.QtWidgets import QApplication
from .views import Window

def main():
    """Contacts main function"""
    # Create the applicaton
    app = QApplication(sys.argv)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop
    sys.exit(app.exec())