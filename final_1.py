from PyQt5 import QtCore, QtGui, QtWidgets
from error_checker import *
from dict import *
# from dec-alu-rw import *
# from ALU import *
# # from dict import *
# from iag_dp import *
# from labels import *
# from Readwrite import *


class Ui_RISCV_Simulator(object):
    #def refresh_mem():
    #def refresh_reg():
    def check_log_click(self):
        self.listWidget_2.setCurrentRow(1)
        self.listWidget_2.clear()
        data=self.textEdit.toPlainText()
        # self.listWidget_5.addItems(execute_error_chk(data.splitlines()))
        temp=data.splitlines()
        ls=[''.join(i) for i in generate_machine_code(temp)]
        for i in range(len(ls)):
            self.listWidget_2.insertItem(i,"\t\t".join([hex(i*4),hex(int(ls[i],2)),temp[i],temp[i]]))
    def run_connect(self):
        items = []
        for index in range(self.listWidget_2.count()):
            items.append(self.listWidget_2.item(index))
        for i in items:
            run(int(i.text().split()[1],2))
    def step_connect(self):
        if self.listWidget_2.currentRow()<self.listWidget_2.count():
            self.listWidget_2.setCurrentRow(self.listWidget_2.currentRow()+1)
            #run
    def reset_connect(self):
        self.
    def setupUi(self, RISCV_Simulator):
        RISCV_Simulator.setObjectName("RISCV_Simulator")
        RISCV_Simulator.resize(1440, 946)
        self.centralwidget = QtWidgets.QWidget(RISCV_Simulator)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1421, 1001))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setTabletTracking(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1081, 631))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 660, 111, 41))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.listWidget_5 = QtWidgets.QListWidget(self.tab)
        self.listWidget_5.setGeometry(QtCore.QRect(-5, 701, 1081, 141))
        self.listWidget_5.setObjectName("listWidget_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 640, 281, 51))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 40, 81, 61))
        self.pushButton_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 81, 41))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 131, 51))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(400, 180, 131, 51))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(680, 180, 131, 51))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 81, 41))
        self.pushButton_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 130, 81, 41))
        self.pushButton_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.step_connect)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 130, 81, 41))
        self.pushButton_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(360, 130, 81, 41))
        self.pushButton_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 130, 81, 41))
        self.pushButton_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(5, 231, 891, 581))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(960, 10, 431, 811))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_3.setGeometry(QtCore.QRect(5, 11, 341, 761))
        self.listWidget_3.setObjectName("listWidget_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 91, 31))
        self.label_6.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(110, 0, 41, 31))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(190, 0, 31, 31))
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(270, 0, 31, 31))
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(360, 0, 31, 31))
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.listWidget = QtWidgets.QListWidget(self.tab_4)
        self.listWidget.setGeometry(QtCore.QRect(5, 31, 411, 741))
        self.listWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(720, 830, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_4.setGeometry(QtCore.QRect(920, 820, 121, 81))
        self.listWidget_4.setObjectName("listWidget_4")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_2.clicked.connect(self.check_log_click)
        RISCV_Simulator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RISCV_Simulator)
        self.statusbar.setObjectName("statusbar")
        RISCV_Simulator.setStatusBar(self.statusbar)
        self.actionRun = QtWidgets.QAction(RISCV_Simulator)
        self.actionRun.setObjectName("actionRun")
        self.retranslateUi(RISCV_Simulator)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.pushButton_4.clicked.connect(self.run_connect)
        QtCore.QMetaObject.connectSlotsByName(RISCV_Simulator)

    def retranslateUi(self, RISCV_Simulator):
        _translate = QtCore.QCoreApplication.translate
        RISCV_Simulator.setWindowTitle(_translate("RISCV_Simulator", "MainWindow"))
        self.label.setText(_translate("RISCV_Simulator", "Error Log"))
        self.pushButton_2.setText(_translate("RISCV_Simulator", "Assemble & Simulate the editor"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RISCV_Simulator", "Editor"))
        self.pushButton_3.setText(_translate("RISCV_Simulator", "Cancel"))
        self.label_2.setText(_translate("RISCV_Simulator", "PC"))
        self.label_3.setText(_translate("RISCV_Simulator", "Machine Code"))
        self.label_4.setText(_translate("RISCV_Simulator", "Basic Code"))
        self.label_5.setText(_translate("RISCV_Simulator", "Original Code"))
        self.pushButton_4.setText(_translate("RISCV_Simulator", "Run"))
        self.pushButton_5.setText(_translate("RISCV_Simulator", "Step"))
        self.pushButton_6.setText(_translate("RISCV_Simulator", "Prev"))
        self.pushButton_7.setText(_translate("RISCV_Simulator", "Reset"))
        self.pushButton_8.setText(_translate("RISCV_Simulator", "Dump"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("RISCV_Simulator", "Registers"))
        self.label_6.setText(_translate("RISCV_Simulator", "Address"))
        self.label_7.setText(_translate("RISCV_Simulator", "+1"))
        self.label_8.setText(_translate("RISCV_Simulator", "+2"))
        self.label_9.setText(_translate("RISCV_Simulator", "+3"))
        self.label_10.setText(_translate("RISCV_Simulator", "+4"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("RISCV_Simulator", "Memory"))
        self.label_11.setText(_translate("RISCV_Simulator", "Display Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RISCV_Simulator", "Simulator"))
        self.actionRun.setText(_translate("RISCV_Simulator", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RISCV_Simulator = QtWidgets.QMainWindow()
    ui = Ui_RISCV_Simulator()
    ui.setupUi(RISCV_Simulator)
    RISCV_Simulator.show()
    sys.exit(app.exec_())
