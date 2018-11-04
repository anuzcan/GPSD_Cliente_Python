# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_Dialog(object):
    def setupUi(self, main_Dialog):
        main_Dialog.setObjectName("main_Dialog")
        main_Dialog.resize(640, 480)
        main_Dialog.setMinimumSize(QtCore.QSize(640, 480))
        main_Dialog.setMaximumSize(QtCore.QSize(640, 480))
        main_Dialog.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(main_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(550, 210, 81, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(main_Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(440, 10, 191, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.ip_QlineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ip_QlineEdit.setClearButtonEnabled(False)
        self.ip_QlineEdit.setObjectName("ip_QlineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ip_QlineEdit)
        self.ip_server = QtWidgets.QLabel(self.formLayoutWidget)
        self.ip_server.setObjectName("ip_server")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.ip_server)
        self.port_server = QtWidgets.QLabel(self.formLayoutWidget)
        self.port_server.setObjectName("port_server")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.port_server)
        self.port_QlineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.port_QlineEdit.setObjectName("port_QlineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.port_QlineEdit)
        self.connect_server = QtWidgets.QPushButton(self.formLayoutWidget)
        self.connect_server.setObjectName("connect_server")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connect_server)
        self.stop_server = QtWidgets.QPushButton(self.formLayoutWidget)
        self.stop_server.setObjectName("stop_server")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stop_server)
        self.statusLabel = QtWidgets.QLabel(main_Dialog)
        self.statusLabel.setGeometry(QtCore.QRect(10, 451, 621, 20))
        self.statusLabel.setObjectName("statusLabel")
        self.line = QtWidgets.QFrame(main_Dialog)
        self.line.setGeometry(QtCore.QRect(10, 441, 621, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.eleve_QlineEdit = QtWidgets.QLineEdit(main_Dialog)
        self.eleve_QlineEdit.setGeometry(QtCore.QRect(20, 20, 113, 20))
        self.eleve_QlineEdit.setObjectName("eleve_QlineEdit")

        self.retranslateUi(main_Dialog)
        self.buttonBox.accepted.connect(main_Dialog.accept)
        self.buttonBox.rejected.connect(main_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(main_Dialog)

    def retranslateUi(self, main_Dialog):
        _translate = QtCore.QCoreApplication.translate
        main_Dialog.setWindowTitle(_translate("main_Dialog", "RTK Colector"))
        self.ip_server.setText(_translate("main_Dialog", "IP Servidor"))
        self.port_server.setText(_translate("main_Dialog", "Puerto"))
        self.connect_server.setText(_translate("main_Dialog", "Conectar"))
        self.stop_server.setText(_translate("main_Dialog", "Detener"))
        self.statusLabel.setText(_translate("main_Dialog", "Estado"))

