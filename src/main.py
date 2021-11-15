import sys
from windows.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.setupUi(ex)
    ex.setupButtons()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()