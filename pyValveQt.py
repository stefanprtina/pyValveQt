import time
from timeit import default_timer as timer
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import pyqtgraph as pg
import sys
from transmiteri import Ui_Podesavanja

pg.setConfigOption('foreground', 'k')
pg.setConfigOption('background', 'w')

class Ui_MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.serialInst = serialCom()
        self.dataY=[]
        self.dataX =[]
        self.timer = None
        self.timeZero=0
        self.maxPressure = 0
        self.plotting = False
        self.plots = []
        self.activeplot = 0
        self.db = dbHandler(MainApp)

    def plotData(self):

        if(self.plotting):
            self.timer.stop()
        else:
            self.pen = pg.mkPen(color=(0, 0, 200), width=3)
            self.dijagramGraphicsWidget.setXRange(0, 15, padding=0)
            self.dijagramGraphicsWidget.setYRange(0, 1000, padding=0)
            self.line = self.dijagramGraphicsWidget.plot(pen=self.pen)
            self.timer = QtCore.QTimer()  # to create a thread that calls a function at intervals
            self.timer.timeout.connect(ui.updatePlot)  # the update function keeps getting called at intervals
            self.timer.setInterval(50)
            self.timer.start()
            self.plotting = True
            self.timeZero = time.time()


        self.buttonIspitivanje.setText("Zavrsi ispitivanje")

        self.maxPressure = 0

    def updatePlot(self):

        timeElapsed = time.time()-self.timeZero
        if(timeElapsed>15):
            self.dijagramGraphicsWidget.enableAutoRange(axis="x")

        analogVal = float(self.serialInst.getData())
        if(analogVal>self.maxPressure):
            self.lcdPotv1.display(analogVal)
            self.maxPressure = analogVal


        self.dataY.append(analogVal)
        self.dataX.append(timeElapsed)

        self.line.setData(self.dataX, self.dataY)

    def showSettings(self,MainApp):
        Podesavanja.show()

    def setupUi(self, MainApp):

        MainApp.setObjectName("MainApp")
        MainApp.resize(951, 600)

    #OSNOVNI PODACI

        self.centralwidget = QtWidgets.QWidget(MainApp)
        self.centralwidget.setObjectName("centralwidget")
        self.Osnovnipodaci = QtWidgets.QGroupBox(self.centralwidget)
        self.Osnovnipodaci.setGeometry(QtCore.QRect(20, 10, 311, 181))
        self.Osnovnipodaci.setObjectName("Osnovnipodaci")
        self.formLayout = QtWidgets.QFormLayout(self.Osnovnipodaci)
        self.formLayout.setObjectName("formLayout")
        self.gridOsnovniPodaci = QtWidgets.QGridLayout()
        self.gridOsnovniPodaci.setObjectName("gridOsnovniPodaci")
        self.labelGodProiz = QtWidgets.QLabel(self.Osnovnipodaci)
        self.labelGodProiz.setObjectName("labelGodProiz")
        self.gridOsnovniPodaci.addWidget(self.labelGodProiz, 2, 0, 1, 1)
        self.labelSerBroj = QtWidgets.QLabel(self.Osnovnipodaci)
        self.labelSerBroj.setObjectName("labelSerBroj")
        self.gridOsnovniPodaci.addWidget(self.labelSerBroj, 1, 0, 1, 1)
        self.labelNazPrecnik = QtWidgets.QLabel(self.Osnovnipodaci)
        self.labelNazPrecnik.setObjectName("labelNazPrecnik")
        self.gridOsnovniPodaci.addWidget(self.labelNazPrecnik, 3, 0, 1, 1)
        self.labelRadniMedij = QtWidgets.QLabel(self.Osnovnipodaci)
        self.labelRadniMedij.setObjectName("labelRadniMedij")
        self.gridOsnovniPodaci.addWidget(self.labelRadniMedij, 4, 0, 1, 1)
        self.labelLokacija = QtWidgets.QLabel(self.Osnovnipodaci)
        self.labelLokacija.setObjectName("labelLokacija")
        self.gridOsnovniPodaci.addWidget(self.labelLokacija, 0, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridOsnovniPodaci)
        self.gridInputiOsnovniPodaci = QtWidgets.QGridLayout()
        self.gridInputiOsnovniPodaci.setObjectName("gridInputiOsnovniPodaci")
        self.entryLokacijaVentila = QtWidgets.QLineEdit(self.Osnovnipodaci)
        self.entryLokacijaVentila.setObjectName("entryLokacijaVentila")
        self.gridInputiOsnovniPodaci.addWidget(self.entryLokacijaVentila, 0, 0, 1, 1)
        self.entrySerBroj = QtWidgets.QLineEdit(self.Osnovnipodaci)
        self.entrySerBroj.setObjectName("entrySerBroj")
        self.gridInputiOsnovniPodaci.addWidget(self.entrySerBroj, 1, 0, 1, 1)
        self.entryGodProizvodnje = QtWidgets.QLineEdit(self.Osnovnipodaci)
        self.entryGodProizvodnje.setObjectName("entryGodProizvodnje")
        self.gridInputiOsnovniPodaci.addWidget(self.entryGodProizvodnje, 2, 0, 1, 1)
        self.entryNazPrecnik = QtWidgets.QLineEdit(self.Osnovnipodaci)
        self.entryNazPrecnik.setObjectName("entryNazPrecnik")
        self.gridInputiOsnovniPodaci.addWidget(self.entryNazPrecnik, 3, 0, 1, 1)
        self.entryRadniMedij = QtWidgets.QLineEdit(self.Osnovnipodaci)
        self.entryRadniMedij.setObjectName("entryRadniMedij")
        self.gridInputiOsnovniPodaci.addWidget(self.entryRadniMedij, 4, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridInputiOsnovniPodaci)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(360, 130, 241, 55))
        self.layoutWidget.setObjectName("layoutWidget")
    #---------------------------------------------------------

    #IZBOR TRANSMITERA

        self.gridTransmiterIzbor = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridTransmiterIzbor.setContentsMargins(0, 0, 0, 0)
        self.gridTransmiterIzbor.setObjectName("gridTransmiterIzbor")
        self.labelIzborTransmitera = QtWidgets.QLabel(self.layoutWidget)
        self.labelIzborTransmitera.setObjectName("labelIzborTransmitera")
        self.gridTransmiterIzbor.addWidget(self.labelIzborTransmitera, 0, 0, 1, 1)
        self.listIzborTransmitera = QtWidgets.QComboBox(self.layoutWidget)
        self.listIzborTransmitera.setObjectName("listIzborTransmitera")
        self.gridTransmiterIzbor.addWidget(self.listIzborTransmitera, 1, 0, 1, 1)
    #-------------------------------------------------------------

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(360, 30, 239, 93))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")

    #COM INTERFEJSI

        self.buttonPoveziInterfejs = QtWidgets.QPushButton(self.widget)
        self.buttonPoveziInterfejs.setObjectName("buttonPoveziInterfejs")
        self.gridLayout_4.addWidget(self.buttonPoveziInterfejs, 3, 0, 1, 1)

        self.listInterfejs = QtWidgets.QComboBox(self.widget)
        self.listInterfejs.setObjectName("listInterfejs")

        print(self.serialInst.getPorts())
        self.listInterfejs.addItems(self.serialInst.getPorts())
        self.gridLayout_4.addWidget(self.listInterfejs, 2, 0, 1, 1)

        self.labelIzborInterfejsa = QtWidgets.QLabel(self.widget)
        self.labelIzborInterfejsa.setObjectName("labelIzborInterfejsa")
        self.gridLayout_4.addWidget(self.labelIzborInterfejsa, 0, 0, 1, 1)
        self.gridLayout_4.setRowStretch(0, 1)
    #---------------------------------------------------------

    #LCD VELIKI TRENUTNI PRITISAK

        self.lcdTrenutniPritisak = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdTrenutniPritisak.setGeometry(QtCore.QRect(640, 30, 271, 101))
        self.lcdTrenutniPritisak.setObjectName("lcdTrenutniPritisak")

    #---------------------------------------------------------

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 130, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 460, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(330, 430, 291, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 460, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")



        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 460, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(800, 460, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.buttonIspitivanje = QtWidgets.QPushButton(self.centralwidget)
        self.buttonIspitivanje.setGeometry(QtCore.QRect(640, 150, 281, 51))
        self.buttonIspitivanje.setObjectName("buttonIspitivanje")

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 210, 901, 211))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")



        dijPen = pg.mkPen(color=(0, 0, 200), width=3)

    #DIJAGRAMI
        self.dijagramGraphicsWidget = pg.PlotWidget(self.widget1)
        self.dijagramGraphicsWidget.setTitle("Ispitivanje br. 1")

        self.dijagramGraphicsWidget.setObjectName("dijagramGraphicsWidget")
        self.gridLayout.addWidget(self.dijagramGraphicsWidget, 0, 0, 1, 1)

        self.dijagramGraphicsWidget2 = pg.PlotWidget(self.widget1)
        self.dijagramGraphicsWidget2.setTitle("Ispitivanje br. 2")

        self.dijagramGraphicsWidget2.setObjectName("dijagramGraphicsWidget2")
        self.gridLayout.addWidget(self.dijagramGraphicsWidget2, 0, 1, 1, 1)

        self.dijagramGraphicsWidget3 = pg.PlotWidget(self.widget1)
        self.dijagramGraphicsWidget3.setTitle("Ispitivanje br. 3")
        self.dijagramGraphicsWidget3.setObjectName("dijagramGraphicsWidget3")
        self.gridLayout.addWidget(self.dijagramGraphicsWidget3, 0, 2, 1, 1)

    #---------------------------------------------------------

        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 430, 291, 31))
        self.widget2.setObjectName("widget2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

    #LCD-evi
        self.lcdPotv1 = QtWidgets.QLCDNumber(self.widget2)
        self.lcdPotv1.setObjectName("lcdPotv1")
        self.gridLayout_2.addWidget(self.lcdPotv1, 0, 0, 1, 1)

        self.lcdPzatv1 = QtWidgets.QLCDNumber(self.widget2)
        self.lcdPzatv1.setObjectName("lcdPzatv1")
        self.gridLayout_2.addWidget(self.lcdPzatv1, 0, 1, 1, 1)

        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(630, 430, 291, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")

        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.lcdPotv3 = QtWidgets.QLCDNumber(self.layoutWidget_3)
        self.lcdPotv3.setObjectName("lcdPotv3")
        self.gridLayout_5.addWidget(self.lcdPotv3, 0, 0, 1, 1)

        self.lcdPzatv3 = QtWidgets.QLCDNumber(self.layoutWidget_3)
        self.lcdPzatv3.setObjectName("lcdPzatv3")

        self.lcdPotv2 = QtWidgets.QLCDNumber(self.layoutWidget_2)
        self.lcdPotv2.setObjectName("lcdPotv2")
        self.gridLayout_3.addWidget(self.lcdPotv2, 0, 0, 1, 1)

        self.lcdPzatv2 = QtWidgets.QLCDNumber(self.layoutWidget_2)
        self.lcdPzatv2.setObjectName("lcdPzatv2")
        self.gridLayout_3.addWidget(self.lcdPzatv2, 0, 1, 1, 1)

        self.gridLayout_5.addWidget(self.lcdPzatv3, 0, 1, 1, 1)

        MainApp.setCentralWidget(self.centralwidget)
    # _______________________________________________

    #MENI
        self.menubar = QtWidgets.QMenuBar(MainApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 22))
        self.menubar.setObjectName("menubar")

        self.menuGlavni_meni = QtWidgets.QMenu(self.menubar)
        self.menuGlavni_meni.setObjectName("menuGlavni_meni")

        self.menuIzlaz = QtWidgets.QAction(MainApp)
        self.menuIzlaz.setObjectName("menuIzlaz")

        self.menuBazaPodataka = QtWidgets.QAction(MainApp)
        self.menuBazaPodataka.setObjectName("menuBazaPodataka")

        self.menuPodesavanja = QtWidgets.QAction(MainApp)
        self.menuPodesavanja.setObjectName("menuPodesavanja")
        self.menuPodesavanja.triggered.connect(self.showSettings)

        self.menuGlavni_meni.addSeparator()
        self.menuGlavni_meni.addAction(self.menuPodesavanja)
        self.menuGlavni_meni.addAction(self.menuBazaPodataka)
        self.menuGlavni_meni.addAction(self.menuIzlaz)

        self.menubar.addAction(self.menuGlavni_meni.menuAction())

        MainApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainApp)
        self.statusbar.setObjectName("statusbar")
        MainApp.setStatusBar(self.statusbar)

    #---------------------------------------------------------------


    #BUDDY SETUP
        self.labelGodProiz.setBuddy(self.entryGodProizvodnje)
        self.labelSerBroj.setBuddy(self.entrySerBroj)
        self.labelNazPrecnik.setBuddy(self.entryNazPrecnik)
        self.labelRadniMedij.setBuddy(self.entryRadniMedij)
        self.labelLokacija.setBuddy(self.entryLokacijaVentila)
        self.labelIzborTransmitera.setBuddy(self.listIzborTransmitera)
        self.labelIzborInterfejsa.setBuddy(self.listInterfejs)
    #-------------------------------------------------------------

    #Connect buttons to functions

        self.buttonPoveziInterfejs.clicked.connect(self.serialInst.open)
        self.buttonIspitivanje.clicked.connect(self.plotData)

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)
    #---------------------------------------------------------------

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "MainApp"))
        self.Osnovnipodaci.setTitle(_translate("MainApp", "Osnovni podaci ventila"))
        self.labelGodProiz.setText(_translate("MainApp", "Godina proizvodnje:"))
        self.labelSerBroj.setText(_translate("MainApp", "Serijski broj:"))
        self.labelNazPrecnik.setText(_translate("MainApp", "Nazivni prečnik"))
        self.labelRadniMedij.setText(_translate("MainApp", "Radni medijum"))
        self.labelLokacija.setText(_translate("MainApp", "Lokacija ventila:"))
        self.labelIzborTransmitera.setText(_translate("MainApp", "Izbor povezanog transmitera:"))

        self.buttonPoveziInterfejs.setText(_translate("MainApp", "Poveži"))

        self.labelIzborInterfejsa.setText(_translate("MainApp", "Izaberi interfejs:"))
        self.label.setText(_translate("MainApp", "Trenutni pritisak (bar)"))
        self.label_2.setText(_translate("MainApp", "Pritisak otvaranja (bar)"))
        self.label_3.setText(_translate("MainApp", "Pritisak zatvaranja (bar)"))
        self.label_4.setText(_translate("MainApp", "Pritisak otvaranja (bar)"))
        self.label_5.setText(_translate("MainApp", "Pritisak zatvaranja (bar)"))
        self.label_6.setText(_translate("MainApp", "Pritisak otvaranja (bar)"))
        self.label_7.setText(_translate("MainApp", "Pritisak zatvaranja (bar)"))

        self.buttonIspitivanje.setText(_translate("MainApp", "Započni ispitivanje"))
        self.menuGlavni_meni.setTitle(_translate("MainApp", "Glavni meni"))

        self.menuBazaPodataka.setText(_translate("MainApp", "Baza podataka"))
        self.menuPodesavanja.setText(_translate("MainApp", "Podešavanja"))
        self.menuIzlaz.setText(_translate("MainApp", "Izlaz"))

        #Make a list of widgets for later use
        self.plots = [self.dijagramGraphicsWidget, self.dijagramGraphicsWidget2, self.dijagramGraphicsWidget3]
        self.lcds = [[self.lcdPotv1, self.lcdPzatv1], [self.lcdPotv2, self.lcdPzatv2], [self.lcdPotv3, self.lcdPzatv3]]

class serialCom():

    def __init__(self):
        super().__init__()
        self.ser = ""

    def open(self):
        self.ser = serial.Serial(ui.listInterfejs.currentText(), 9600, timeout=0.1, )
        time.sleep(2)
        if(self.ser.inWaiting()>0):
            ui.buttonPoveziInterfejs.setText("Interfejs povezan")
            ui.buttonPoveziInterfejs.setStyleSheet("background-color: green")
            print(self.ser.readline().decode())
            return True
        return False

    def getPorts(self):
        portsAvailable = serial.tools.list_ports.comports()
        if (portsAvailable):
            serPortList = [port.device for port in portsAvailable]
        return serPortList


    def isOpen(self):
        if (self.ser.inWaiting() > 0):
            return True
        return False

    def getData(self):

        if (self.ser.inWaiting() > 0):
            data = self.ser.read(self.ser.inWaiting()).decode()
            if '\r\n' in data:
               data = data.split('\r\n')
            return data[-2]
        return False

class dbHandler(object):
    def __init__(self, MainApp):
        super().__init__()
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("transmiteri")
        connection = self.db.open()
        if(connection):
            self.query = QtSql.QSqlQuery()
            self.query.exec(
                '''CREATE TABLE IF NOT EXISTS 
                transmiteri (id int primary key, 
                'serbroj' TEXT NOT NULL, 
                'maxpritisak' INT NOT NULL, 
                'proizvodjac' TEXT NOT NULL, 
                'datumkal' TEXT NOT NULL, 
                'greskanula' VARCHAR(50) NOT NULL,
                'greskapola' VARCHAR(50) NOT NULL,
                'greskamaks' VARCHAR(50) NOT NULL)''')
        else:
            print('DB Connection error')

    def getRows(self):
        rows = self.query.exec("SELECT * FROM transmiteri")
        return rows

    def insertRow(self, data):
        querytext = "INSERT INTO transmiteri VALUES ('', '" + data[0]+"', '" + data[1] + "', '" +data[2]+"', '"+data[3]+"', '"+data[4]+"', '"+data[5]+"', '"+data[6]
        querytext+="')"
        success = self.query.exec(querytext)
        print(querytext)
        print(success)
        return success



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainApp = QtWidgets.QMainWindow()
    ui = Ui_MainApp()
    ui.setupUi(MainApp)
    Podesavanja = QtWidgets.QWidget()
    ui2 = Ui_Podesavanja(ui)
    ui2.setupUi(Podesavanja)
    MainApp.show()
    sys.exit(app.exec_())
