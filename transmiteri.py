# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'podesavanja.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Podesavanja(object):

    def __init__(self, parent):
        self.parent = parent

    def setupUi(self, Podesavanja):

        Podesavanja.setObjectName("Podesavanja")
        Podesavanja.resize(424, 491)

        self.gridLayout_3 = QtWidgets.QGridLayout(Podesavanja)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridGornji = QtWidgets.QGridLayout()
        self.gridGornji.setObjectName("gridGornji")
        self.listTransmiteri = QtWidgets.QListView(Podesavanja)
        self.listTransmiteri.setObjectName("listTransmiteri")
        self.gridGornji.addWidget(self.listTransmiteri, 1, 0, 1, 1)
        self.buttonBrisanje = QtWidgets.QPushButton(Podesavanja)
        self.buttonBrisanje.setMaximumSize(QtCore.QSize(200, 100))
        self.buttonBrisanje.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.buttonBrisanje.setObjectName("buttonBrisanje")
        self.gridGornji.addWidget(self.buttonBrisanje, 2, 0, 1, 1)


        self.label = QtWidgets.QLabel(Podesavanja)
        self.label.setObjectName("label")
        self.gridGornji.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridGornji, 0, 0, 1, 1)
        self.groupPodaci = QtWidgets.QGroupBox(Podesavanja)
        self.groupPodaci.setObjectName("groupPodaci")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupPodaci)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupPodaci)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)


        self.entryMaxPritisak = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryMaxPritisak.setObjectName("entryMaxPritisak")

        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entryMaxPritisak)
        self.label_3 = QtWidgets.QLabel(self.groupPodaci)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.entrySerBrojTransmitera = QtWidgets.QLineEdit(self.groupPodaci)
        self.entrySerBrojTransmitera.setObjectName("entrySerBrojTransmitera")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entrySerBrojTransmitera)

        self.label_9 = QtWidgets.QLabel(self.groupPodaci)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.entryProizvodjacTransmitera = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryProizvodjacTransmitera.setObjectName("entryProizvodjacTransmitera")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entryProizvodjacTransmitera)

        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupPodaci)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.entryDatumKalibracije = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryDatumKalibracije.setObjectName("entryDatumKalibracije")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entryDatumKalibracije)


        self.label_5 = QtWidgets.QLabel(self.groupPodaci)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.entryGreskaNula = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryGreskaNula.setObjectName("entryGreskaNula")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entryGreskaNula)


        self.label_6 = QtWidgets.QLabel(self.groupPodaci)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.entryGreskaPola = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryGreskaPola.setObjectName("entryGreskaPola")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entryGreskaPola)


        self.label_8 = QtWidgets.QLabel(self.groupPodaci)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.entryGreskMax = QtWidgets.QLineEdit(self.groupPodaci)
        self.entryGreskMax.setObjectName("entryGreskMax")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.entryGreskMax)


        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.buttonIzmjenaUnos = QtWidgets.QPushButton(self.groupPodaci)
        self.buttonIzmjenaUnos.setObjectName("buttonIzmjenaUnos")
        self.buttonIzmjenaUnos.clicked.connect(self.unesiTransmiter)
        self.gridLayout_2.addWidget(self.buttonIzmjenaUnos, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupPodaci, 1, 0, 1, 1)
        self.label.setBuddy(self.listTransmiteri)
        self.label_2.setBuddy(self.entryMaxPritisak)
        self.label_3.setBuddy(self.entrySerBrojTransmitera)
        self.label_9.setBuddy(self.entryProizvodjacTransmitera)
        self.label_4.setBuddy(self.entryDatumKalibracije)
        self.label_5.setBuddy(self.entryGreskaNula)
        self.label_6.setBuddy(self.entryGreskaPola)
        self.label_8.setBuddy(self.entryGreskMax)

        self.retranslateUi(Podesavanja)
        QtCore.QMetaObject.connectSlotsByName(Podesavanja)


    def retranslateUi(self, Podesavanja):
        _translate = QtCore.QCoreApplication.translate
        Podesavanja.setWindowTitle(_translate("Podesavanja", "Form"))
        self.buttonBrisanje.setText(_translate("Podesavanja", "Brisanje transmitera"))
        self.label.setText(_translate("Podesavanja", "Uneseni transmiteri pritiska"))
        self.groupPodaci.setTitle(_translate("Podesavanja", "Pregled i izmjena podataka"))
        self.label_2.setText(_translate("Podesavanja", "Maks. pritisak mjerenja"))
        self.label_3.setText(_translate("Podesavanja", "Serijski broj"))
        self.label_9.setText(_translate("Podesavanja", "Proizvođač i model"))
        self.label_4.setText(_translate("Podesavanja", "Datum kalibracije"))
        self.label_5.setText(_translate("Podesavanja", "Greška na 0% skale"))
        self.label_6.setText(_translate("Podesavanja", "Greška na 50% skale"))
        self.label_8.setText(_translate("Podesavanja", "Greška na 100% skale"))
        self.buttonIzmjenaUnos.setText(_translate("Podesavanja", "Unos/izmjena"))

    def unesiTransmiter(self, Podesavanja):
        data = [self.entrySerBrojTransmitera.text(), self.entryMaxPritisak.text(), self.entryProizvodjacTransmitera.text(), self.entryDatumKalibracije.text(), self.entryGreskaNula.text(), self.entryGreskaPola.text(), self.entryGreskMax.text()]
        entry = self.parent.db.insertRow(data)

    def refreshList(self, Podesavanja):
        data = self.db.getRows()

    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Podesavanja = QtWidgets.QWidget()
        ui = Ui_Podesavanja()
        ui.setupUi(Podesavanja)
        Podesavanja.show()
        sys.exit(app.exec_())
