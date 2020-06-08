from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, qApp
from designer.login import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys



from bd.queries_to_the_DB import serch_user_profile


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setMaxLength(10)
        self.ui.lineEdit_2.setMaxLength(15)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton.clicked.connect(self.data_checking)
        self.ui.pushButton_2.clicked.connect(qApp.quit)

    # Метод проверки, есть такой логин и пароль или нет
    def data_checking(self):
        user_line = self.ui.lineEdit.text()
        password_line = self.ui.lineEdit_2.text()
        for i in serch_user_profile(user_line):
            self.user = i[0]
            self.password = i[1]
        if user_line != self.user or password_line != self.password:
            QMessageBox.critical(self, 'Ошибка авторизации', "Введите корректные логин и пароль")
        else:

            Log_oute()



class Log_oute(QtWidgets.QMainWindow):
    def __init__(self):
        super(Log_oute, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        res = QMessageBox.question(self, "Авторизация пройдена", "Вы успешно прошли авторизацию", QMessageBox.Ok)
        qApp.quit()





app = QtWidgets.QApplication([])
application = Mywindow()
application.show()

sys.exit(app.exec())
