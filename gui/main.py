# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project-GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from joblib import load
import numpy as np
from xgboost import XGBRegressor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Predict apartaments price")
        MainWindow.resize(1600, 900)
        MainWindow.setStyleSheet("background-color: rgb(225,250,25)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.type_of_house = QtWidgets.QComboBox(self.centralwidget)
        self.type_of_house.setGeometry(QtCore.QRect(20, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.type_of_house.setFont(font)
        self.type_of_house.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(232,255,255);\n"
                                         "selection-color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "")
        self.type_of_house.setObjectName("type_of_house")
        self.type_of_house.addItem("")
        self.type_of_house.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.type_of_view = QtWidgets.QComboBox(self.centralwidget)
        self.type_of_view.setGeometry(QtCore.QRect(220, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.type_of_view.setFont(font)
        self.type_of_view.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "selection-background-color: rgb(232,255,255);\n"
                                        "selection-color: rgb(0, 0, 0);\n"
                                        "\n"
                                        "")
        self.type_of_view.setObjectName("type_of_view")
        self.type_of_view.addItem("")
        self.type_of_view.addItem("")
        self.type_of_view.addItem("")
        self.time_metro = QtWidgets.QSpinBox(self.centralwidget)
        self.time_metro.setGeometry(QtCore.QRect(470, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.time_metro.setFont(font)
        self.time_metro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.time_metro.setAlignment(QtCore.Qt.AlignCenter)
        self.time_metro.setMinimum(1)
        self.time_metro.setMaximum(60)
        self.time_metro.setProperty("value", 5)
        self.time_metro.setObjectName("time_metro")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.number_of_rooms = QtWidgets.QComboBox(self.centralwidget)
        self.number_of_rooms.setGeometry(QtCore.QRect(20, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_of_rooms.setFont(font)
        self.number_of_rooms.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "selection-background-color: rgb(232,255,255);\n"
                                           "selection-color: rgb(0, 0, 0);\n"
                                           "\n"
                                           "")
        self.number_of_rooms.setObjectName("number_of_rooms")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.number_of_rooms.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 150, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.area = QtWidgets.QSpinBox(self.centralwidget)
        self.area.setGeometry(QtCore.QRect(370, 200, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.area.setFont(font)
        self.area.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.area.setAlignment(QtCore.Qt.AlignCenter)
        self.area.setMinimum(10)
        self.area.setMaximum(1000)
        self.area.setProperty("value", 10)
        self.area.setObjectName("area")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.number_of_floors = QtWidgets.QSpinBox(self.centralwidget)
        self.number_of_floors.setGeometry(QtCore.QRect(160, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_of_floors.setFont(font)
        self.number_of_floors.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number_of_floors.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_floors.setMinimum(1)
        self.number_of_floors.setMaximum(60)
        self.number_of_floors.setProperty("value", 1)
        self.number_of_floors.setObjectName("number_of_floors")
        self.floor = QtWidgets.QSpinBox(self.centralwidget)
        self.floor.setGeometry(QtCore.QRect(20, 320, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.floor.setFont(font)
        self.floor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.floor.setAlignment(QtCore.Qt.AlignCenter)
        self.floor.setMinimum(1)
        self.floor.setMaximum(60)
        self.floor.setProperty("value", 1)
        self.floor.setObjectName("floor")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 270, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.year_of_construction = QtWidgets.QSpinBox(self.centralwidget)
        self.year_of_construction.setGeometry(QtCore.QRect(340, 320, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.year_of_construction.setFont(font)
        self.year_of_construction.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.year_of_construction.setAlignment(QtCore.Qt.AlignCenter)
        self.year_of_construction.setMinimum(1700)
        self.year_of_construction.setMaximum(5000)
        self.year_of_construction.setProperty("value", 1700)
        self.year_of_construction.setObjectName("year_of_construction")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 380, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.height_of_ceiling = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.height_of_ceiling.setGeometry(QtCore.QRect(27, 433, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.height_of_ceiling.setFont(font)
        self.height_of_ceiling.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.height_of_ceiling.setMinimum(1.0)
        self.height_of_ceiling.setObjectName("height_of_ceiling")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 380, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.number_of_bathrooms = QtWidgets.QSpinBox(self.centralwidget)
        self.number_of_bathrooms.setGeometry(QtCore.QRect(330, 430, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.number_of_bathrooms.setFont(font)
        self.number_of_bathrooms.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.number_of_bathrooms.setAlignment(QtCore.Qt.AlignCenter)
        self.number_of_bathrooms.setMinimum(1)
        self.number_of_bathrooms.setMaximum(10)
        self.number_of_bathrooms.setProperty("value", 1)
        self.number_of_bathrooms.setObjectName("number_of_bathrooms")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.metro = QtWidgets.QLineEdit(self.centralwidget)
        self.metro.setGeometry(QtCore.QRect(610, 320, 181, 31))
        self.metro.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.metro.setObjectName("metro")
        self.btn_submit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_submit.setGeometry(QtCore.QRect(670, 450, 113, 32))
        self.btn_submit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "")
        self.btn_submit.setObjectName("btn_submit")
        self.area_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.area_2.setGeometry(QtCore.QRect(640, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.area_2.setFont(font)
        self.area_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.area_2.setAlignment(QtCore.Qt.AlignCenter)
        self.area_2.setMinimum(10)
        self.area_2.setMaximum(1000)
        self.area_2.setProperty("value", 10)
        self.area_2.setObjectName("area_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(650, 150, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("")
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predict Moscow apartaments price"))
        self.type_of_house.setItemText(0, _translate("MainWindow", "Новостройка"))
        self.type_of_house.setItemText(1, _translate("MainWindow", "Вторичка"))
        self.label.setText(_translate("MainWindow", "Тип Жилья"))
        self.label_2.setText(_translate("MainWindow", "Вид из окна"))
        self.type_of_view.setItemText(0, _translate("MainWindow", "На улицу и двор"))
        self.type_of_view.setItemText(1, _translate("MainWindow", "Во двор"))
        self.type_of_view.setItemText(2, _translate("MainWindow", "На улицу"))
        self.label_3.setText(_translate("MainWindow", "Время до метро"))
        self.label_4.setText(_translate("MainWindow", "Количество комнат"))
        self.number_of_rooms.setItemText(0, _translate("MainWindow", "Студия"))
        self.number_of_rooms.setItemText(1, _translate("MainWindow", "1 комната"))
        self.number_of_rooms.setItemText(2, _translate("MainWindow", "2 комнаты"))
        self.number_of_rooms.setItemText(3, _translate("MainWindow", "3 комнаты"))
        self.number_of_rooms.setItemText(4, _translate("MainWindow", "4 комнаты"))
        self.number_of_rooms.setItemText(5, _translate("MainWindow", "5 комнат"))
        self.number_of_rooms.setItemText(6, _translate("MainWindow", "Многокомнатная "))
        self.label_5.setText(_translate("MainWindow", "Общая площадь"))
        self.label_6.setText(_translate("MainWindow", "Этаж и этажность"))
        self.label_7.setText(_translate("MainWindow", "Год постройки"))
        self.label_8.setText(_translate("MainWindow", "Высота потолков"))
        self.label_9.setText(_translate("MainWindow", "Количество ванных комнат"))
        self.label_10.setText(_translate("MainWindow", "Метро"))
        self.btn_submit.setText(_translate("MainWindow", "Готово"))
        self.label_11.setText(_translate("MainWindow", "Жилая площадь"))

    def add_func(self):
        self.btn_submit.clicked.connect(self.btn_submition)

    def btn_submition(self):

        LivingArea = self.area_2.value()
        TypeOfHouse = self.type_of_house.currentText()
        TypeOfView = self.type_of_view.currentText()
        TimeMetro = self.time_metro.value()
        NumberOfRooms = self.number_of_rooms.currentText()
        ValueArea = self.area.value()
        Floor = self.floor.value()
        NumberOfFloors = self.number_of_floors.value()
        YearOfConstruction = self.year_of_construction.value()
        Metro = self.metro.text()
        HeightOfCelling = self.height_of_ceiling.value()
        NumberOfBathrooms = self.number_of_bathrooms.value()


        data = [Metro, TimeMetro, NumberOfRooms, ValueArea, LivingArea, Floor, NumberOfFloors, YearOfConstruction, TypeOfHouse,
                HeightOfCelling, NumberOfBathrooms, TypeOfView]

        metro = ['Авиамоторная',
 'Автозаводская',
 'Академическая',
 'Александровский сад',
 'Алексеевская',
 'Алма-Атинская',
 'Алтуфьево',
 'Аминьевское шоссе',
 'Андроновка',
 'Аникеевка',
 'Аннино',
 'Арбатская',
 'Аэропорт',
 'Бабушкинская',
 'Багратионовская',
 'Балтийская',
 'Баррикадная',
 'Бауманская',
 'Беговая',
 'Белокаменная',
 'Беломорская',
 'Белорусская',
 'Беляево',
 'Бескудниково',
 'Бибирево',
 'Библиотека им. Ленина',
 'Битцевский парк',
 'Борисово',
 'Боровицкая',
 'Боровское шоссе',
 'Ботанический сад',
 'Братиславская',
 'Бульвар Адмирала Ушакова',
 'Бульвар Дмитрия Донского',
 'Бульвар Рокоссовского',
 'Бунинская аллея',
 'Бутово',
 'Бутырская',
 'ВДНХ',
 'Варшавская',
 'Верхние Лихоборы',
 'Верхние котлы',
 'Владыкино',
 'Водный стадион',
 'Войковская',
 'Волгоградский проспект',
 'Волжская',
 'Волоколамская',
 'Воробьевы горы',
 'Воронцовская',
 'Выставочная',
 'Выставочный центр',
 'Выхино',
 'Говорово',
 'Гражданская',
 'Давыдково',
 'Дегунино',
 'Деловой центр',
 'Депо',
 'Динамо',
 'Дмитровская',
 'Добрынинская',
 'Долгопрудная',
 'Домодедовская',
 'Достоевская',
 'Дубровка',
 'Жулебино',
 'ЗИЛ',
 'Зорге',
 'Зябликово',
 'Измайлово',
 'Измайловская',
 'Калитники',
 'Калужская',
 'Кантемировская',
 'Каховская',
 'Каширская',
 'Киевская',
 'Китай-город',
 'Кожуховская',
 'Коломенская',
 'Коммунарка',
 'Комсомольская',
 'Коньково',
 'Коптево',
 'Котельники',
 'Красногвардейская',
 'Краснопресненская',
 'Красносельская',
 'Красные ворота',
 'Красный Балтиец',
 'Красный Строитель',
 'Крестьянская застава',
 'Кропоткинская',
 'Крылатское',
 'Крымская',
 'Кузнецкий мост',
 'Кузьминки',
 'Кунцевская',
 'Курская',
 'Курьяново',
 'Кутузовская',
 'Ленинский проспект',
 'Лермонтовский проспект',
 'Лесопарковая',
 'Лефортово',
 'Лианозово',
 'Лихоборы',
 'Лобня',
 'Локомотив',
 'Ломоносовский проспект',
 'Лубянка',
 'Лужники',
 'Лухмановская',
 'Люблино',
 'Марк',
 'Марксистская',
 'Марьина роща',
 'Марьино',
 'Маяковская',
 'Медведково',
 'Международная',
 'Менделеевская',
 'Минская',
 'Митино',
 'Мичуринский проспект',
 'Мневники',
 'Молодежная',
 'Москва-Товарная',
 'Москворечье',
 'Нагатинская',
 'Нагорная',
 'Народное ополчение',
 'Нахимовский проспект',
 'Некрасовка',
 'Нижегородская',
 'Новогиреево',
 'Новодачная',
 'Новокосино',
 'Новокузнецкая',
 'Новопеределкино',
 'Новослободская',
 'Новохохловская',
 'Новоясеневская',
 'Новые Черемушки',
 'Одинцово',
 'Озерная',
 'Окружная',
 'Окская',
 'Октябрьская',
 'Октябрьское поле',
 'Ольховая',
 'Орехово',
 'Остафьево',
 'Отрадное',
 'Охотный ряд',
 'Павелецкая',
 'Панфиловская',
 'Парк Культуры',
 'Парк Победы',
 'Партизанская',
 'Первомайская',
 'Перерва',
 'Перово',
 'Петровский Парк',
 'Петровско-Разумовская',
 'Печатники',
 'Пионерская',
 'Планерная',
 'Площадь Гагарина',
 'Площадь Ильича',
 'Площадь Революции',
 'Подольск',
 'Покровское',
 'Покровское-Стрешнево',
 'Полежаевская',
 'Полянка',
 'Пражская',
 'Преображенская площадь',
 'Прокшино',
 'Пролетарская',
 'Проспект Вернадского',
 'Проспект Мира',
 'Профсоюзная',
 'Пушкинская',
 'Пятницкое шоссе',
 'Рабочий поселок',
 'Раменки',
 'Рассказовка',
 'Речной вокзал',
 'Рижская',
 'Римская',
 'Ростокино',
 'Румянцево',
 'Рязанский проспект',
 'Савеловская',
 'Саларьево',
 'Свиблово',
 'Севастопольская',
 'Селигерская',
 'Семеновская',
 'Серпуховская',
 'Сетунь',
 'Силикатная',
 'Славянский бульвар',
 'Смоленская',
 'Сокол',
 'Соколиная гора',
 'Сокольники',
 'Солнцево',
 'Спартак',
 'Спортивная',
 'Сретенский бульвар',
 'Стахановская',
 'Строгино',
 'Студенческая',
 'Сухаревская',
 'Сходненская',
 'Таганская',
 'Тверская',
 'Театральная',
 'Текстильщики',
 'Теплый Стан',
 'Тестовская',
 'Технопарк',
 'Тимирязевская',
 'Третьяковская',
 'Трикотажная',
 'Тропарево',
 'Трубная',
 'Тульская',
 'Тургеневская',
 'Тушинская',
 'Угрешская',
 'Улица 1905 года',
 'Улица 800-летия Москвы',
 'Улица Академика Королева',
 'Улица Академика Янгеля',
 'Улица Горчакова',
 'Улица Дмитриевского',
 'Улица Милашенкова',
 'Улица Сергея Эйзенштейна',
 'Улица Скобелевская',
 'Улица Старокачаловская',
 'Университет',
 'Филатов Луг',]

        rooms = ['Студия', '1 комната', '2 комнаты', '3 комнаты',
                 '4 комнаты', '5 комнат', 'Многокомнатная ']

        data[0] = metro.index(data[0])
        if rooms.index(data[2]) > 0: data[2] = rooms.index(data[2])
        else: data[2] = 1

        type = ['Вторичка', 'Новостройка']
        data[8] = type.index(data[8])

        view = ['Во двор', 'На улицу', 'На улицу и двор', 'Нет информации']
        data[11] = view.index(data[11])

        clf = load('boost.joblib')
        data = np.reshape(data, (1, -1))

        pred = np.round(clf.predict(data))


        price = QMessageBox()
        price.setWindowTitle("Цена")
        price.setText(str(pred))
        price.setIcon(QMessageBox.Warning)
        price.setStandardButtons(QMessageBox.Ok)

        price.exec_()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())