import sys
from windows.mainWindow import Ui_MainWindow as MW
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    app = MW(sys.argv)
    app.exec()


if __name__ == "__main__":
    main()