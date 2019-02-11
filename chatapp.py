from PySide2 import QtWidgets, QtCore
from data_conn import get_message, send_message



class MainWindow(QtWidgets.QMainWindow):

    def build(self):
        self.setCentralWidget(QtWidgets.QWidget())


        self.build_widgets()
        self.build_layouts()
        self.build_events()
        self.reset_inputs()
        self.get_username()

    def build_widgets(self):

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.get_message_callback)
        self.timer.start()

        self.text_input = QtWidgets.QLineEdit()
        self.text_input.setPlaceholderText("Message")

        self.text_input2 = QtWidgets.QLineEdit()
        self.text_input2.setPlaceholderText("Name")

        self.textedit = QtWidgets.QTextEdit()
        self.textedit.setReadOnly(True)

        self.button = QtWidgets.QPushButton()
        self.button.setText("Send")

        self.button2 = QtWidgets.QPushButton()
        self.button2.setText("Change User Name")

        self.dialog = QtWidgets.QInputDialog()

        self.label = QtWidgets.QLabel()




    def build_layouts(self):
        self.layout3 = QtWidgets.QHBoxLayout()
        self.layout3.addWidget(self.label)
        self.layout3.addWidget(self.button2)

        self.layout2 = QtWidgets.QHBoxLayout()
        self.layout2.addWidget(self.text_input)
        self.layout2.addWidget(self.button)


        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.layout3)



        self.main_layout.addWidget(self.textedit)
        self.main_layout.addLayout(self.layout2)
        self.centralWidget().setLayout(self.main_layout)

    def get_username(self):
        self.username = self.dialog.getText(self, "Name", "Write a Name")
        if self.username[1]:
            self.user = self.username[0]

        self.curruser = "Current User" + ": " + self.user
        self.label.setText(self.curruser)

    def reset_inputs(self):
        # self.text_input2.setText("")
        self.text_input.setText("")

    def build_events(self):
        self.text_input.returnPressed.connect(self.send_message_callback)
        self.text_input.returnPressed.connect(self.reset_inputs)
        self.button.clicked.connect(self.send_message_callback)
        self.button.clicked.connect(self.reset_inputs)
        self.button2.clicked.connect(self.get_username)

    def send_message_callback(self):
        send_message(self.user, self.text_input.text())

    def get_message_callback(self):
        messages_string = ""
        dic = get_message()
        for i, j in dic.items():
            for k in reversed(j):
                #print(k['sender'], k['message'])
                messages_string += k['sender'] + ": " + k['message'] + "\n"

        self.textedit.setText(messages_string)




app = QtWidgets.QApplication()
window = MainWindow()
window.setStyleSheet("""
QWidget{
    border-width: 2px;
    border-color: black;
    border-style: solid;
    color: black;
    font-size: 16px;
    }

""")
window.build()
window.show()
app.exec_()