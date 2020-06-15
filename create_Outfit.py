from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from designer.login import Ui_MainWindow  # импорт нашего сгенерированного файла
from designer.lk_admin import Ui_LK_admin
import sys

from bd.queries_to_the_DB import serch_user_profile, close_connection, serch_users_data

# Самое первое окно, где проходит вся авторизация и проверка на соответствие данных каждому пользователю
class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setMaxLength(10)
        self.ui.lineEdit_2.setMaxLength(15)
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButton.clicked.connect(self.data_checking)

    # Метод проверки, есть такой логин и пароль или нет
    def data_checking(self):
        try:
            user_line = self.ui.lineEdit.text()
            password_line = self.ui.lineEdit_2.text()
            for i in serch_user_profile(user_line):
                self.user = i[1] #Задаем переменную Юзер в метод
                self.password = i[2] #Задаем переменную Пароль в метод
                self.id = i[0]
                """
                Задаем переменную ID в метод. Что бы в последующем найти профиль пользователя из таблици users_data
                """
            if user_line == self.user and password_line == self.password:
                for key in serch_users_data(self.id):
                    if key[6] == 'admin':
                        self.close()
                        self.two_windo = Lk_admin()
                        self.two_windo.show()
                        close_connection()
                    if key[6] == 'nach1':
                        QMessageBox.question(self, "Авторизация пройдена", "Авторизован как Nach1",
                                            QMessageBox.Ok)
                    if key[6] == 'nach2':
                        QMessageBox.question(self, "Авторизация пройдена", "Авторизован как nach2",
                                             QMessageBox.Ok)
                    if key[6] == 'nach3':
                        QMessageBox.question(self, "Авторизация пройдена", "Авторизован как nach3",
                                             QMessageBox.Ok)
            else:
                QMessageBox.critical(self, 'Ошибка авторизации', "Ввведены не корректный логин и пароль")
        except Exception:
            QMessageBox.critical(self, 'Ошибка авторизации', "Ввведены не корректный логин и пароль")


# Окно для админа.
class Lk_admin(QtWidgets.QMainWindow):
    def __init__(self):
        super(Lk_admin, self).__init__()
        self.lk = Ui_LK_admin()
        self.lk.setupUi(self)
        QMessageBox.question(self, "Авторизация пройдена", "Вы успешно прошли авторизацию", QMessageBox.Ok)
        self.lk.pushButton.clicked.connect(self.but_one)

    def but_one(self):
        print('Второе окно открылось!')




app = QtWidgets.QApplication([])
application = Mywindow()
application.show()

sys.exit(app.exec())
