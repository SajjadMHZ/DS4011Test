
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QHBoxLayout, QLineEdit, QVBoxLayout

from ds import Core


class Window(QDialog):
    def __init__(self, core: Core):
        super(Window, self).__init__()
        self.setWindowTitle("My Application")
        lay = QVBoxLayout()
        self.setLayout(lay)
        self.core = core

        lay_username = QHBoxLayout()
        lay.addLayout(lay_username)
        lay_username.addWidget(QLabel("Username:"))
        lay_username.addWidget(QLineEdit())

        lay_password = QHBoxLayout()
        lay.addLayout(lay_password)
        lay_password.addWidget(QLabel("Password:"))
        lay_password.addWidget(QLineEdit())

        lay.addWidget(QPushButton("Confirm"))
        


def load_data(core: Core):
    core.add_user('smal', '13')
    core.add_user('ali', '11')


if __name__ == '__main__':
    core = Core()
    load_data(core)
    # print(core.login('reza', '15'))
    # print(core.login('smal', '13'))
    app = QApplication([])
    win = Window(core)
    win.show()
    app.exec()




