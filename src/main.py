import sys
from windows.main_window import MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    w = QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()