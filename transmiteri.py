# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'podesavanja.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Podesavanja(object):
    def setupUi(self, Podesavanja):
        Podesavanja.setObjectName("Podesavanja")
        Podesavanja.resize(424, 491)
        self.gridLayout_3 = QtWidgets.QGridLayout(Podesavanja)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(Podesavanja)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Podesavanja)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 100))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Podesavanja)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Podesavanja)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.label.setBuddy(self.listView)
        self.label_2.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.lineEdit_2)
        self.label_9.setBuddy(self.lineEdit_7)
        self.label_4.setBuddy(self.lineEdit_3)
        self.label_5.setBuddy(self.lineEdit_4)
        self.label_6.setBuddy(self.lineEdit_5)
        self.label_8.setBuddy(self.lineEdit_6)

        self.retranslateUi(Podesavanja)
        QtCore.QMetaObject.connectSlotsByName(Podesavanja)

    def retranslateUi(self, Podesavanja):
        _translate = QtCore.QCoreApplication.translate
        Podesavanja.setWindowTitle(_translate("Podesavanja", "Form"))
        self.pushButton_2.setText(_translate("Podesavanja", "Brisanje transmitera"))
        self.label.setText(_translate("Podesavanja", "Uneseni transmiteri pritiska"))
        self.groupBox.setTitle(_translate("Podesavanja", "Pregled i izmjena podataka"))
        self.label_2.setText(_translate("Podesavanja", "Maks. pritisak mjerenja"))
        self.label_3.setText(_translate("Podesavanja", "Serijski broj"))
        self.label_9.setText(_translate("Podesavanja", "Proizvođač i model"))
        self.label_4.setText(_translate("Podesavanja", "Datum kalibracije"))
        self.label_5.setText(_translate("Podesavanja", "Greška na 0% skale"))
        self.label_6.setText(_translate("Podesavanja", "Greška na 50% skale"))
        self.label_8.setText(_translate("Podesavanja", "Greška na 100% skale"))
        self.pushButton.setText(_translate("Podesavanja", "Unos/izmjena"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Podesavanja = QtWidgets.QWidget()
    ui = Ui_Podesavanja()
    ui.setupUi(Podesavanja)
    Podesavanja.show()
    sys.exit(app.exec_())
