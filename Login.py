from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    
    def __style__(self):
        with open('./style.qss', 'r') as f: style = f.read()
        return style

    def setupUi(self, Form):
        Form.setObjectName('Form')
        Form.resize(460, 340)

        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(10, 10, 440, 320))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName('fr_fondo')

        self.cb_menu1 = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_menu1.setGeometry(QtCore.QRect(20, 30, 110, 35))
        self.cb_menu1.setObjectName('cb_menu1')

        self.cb_menu1.addItem('')
        self.cb_menu1.addItem('')
        self.cb_menu1.addItem('')
        self.cb_menu1.addItem('')
        
        
        self.cb_menu2 = QtWidgets.QComboBox(self.fr_fondo)
        self.cb_menu2.setGeometry(QtCore.QRect(-220, 20, 131, 35))
        self.cb_menu2.setObjectName('cb_menu2')

        self.cb_menu2.addItem('')
        self.cb_menu2.addItem('')
        self.cb_menu2.addItem('')
        self.cb_menu2.addItem('')
        self.cb_menu2.addItem('')
        self.cb_menu2.addItem('')

        self.lbl_bienvenida = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_bienvenida.setGeometry(QtCore.QRect(170, 30, 231, 41))
        self.lbl_bienvenida.setObjectName('lbl_bienvenida')
        
        self.lbl_usuario = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_usuario.setGeometry(QtCore.QRect(30, 100, 221, 31))
        self.lbl_usuario.setObjectName('lbl_usuario')
        
        self.lbl_clave = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_clave.setGeometry(QtCore.QRect(30, 170, 71, 31))
        self.lbl_clave.setObjectName('lbl_clave')
        
        self.lbl_alerta = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_alerta.setGeometry(QtCore.QRect(30, 250, 371, 41))
        self.lbl_alerta.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alerta.setObjectName('lbl_alerta')
        
        self.le_usuario = QtWidgets.QLineEdit(self.fr_fondo)
        self.le_usuario.setGeometry(QtCore.QRect(260, 100, 140, 30))
        self.le_usuario.setMaxLength(15)
        self.le_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.le_usuario.setObjectName('le_usuario')
        
        self.le_clave = QtWidgets.QLineEdit(self.fr_fondo)
        self.le_clave.setGeometry(QtCore.QRect(110, 170, 140, 30))
        self.le_clave.setMaxLength(13)
        self.le_clave.setAlignment(QtCore.Qt.AlignCenter)
        self.le_clave.setObjectName('le_clave')
        
        self.txte_txt = QtWidgets.QTextEdit(self.fr_fondo)
        self.txte_txt.setGeometry(QtCore.QRect(-370, 120, 301, 131))
        self.txte_txt.setObjectName('textEdit')

        self.btn_azar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_azar.setGeometry(QtCore.QRect(160, 380, 120, 41))
        self.btn_azar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_azar.setObjectName('btn_azar')

        self.btn_txtB = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_txtB.setGeometry(QtCore.QRect(460, 110, 140, 41))
        self.btn_txtB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_txtB.setObjectName('btn_txtB')

        self.btn_ctB = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_ctB.setGeometry(QtCore.QRect(-140, 110, 140, 41))
        self.btn_ctB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_ctB.setObjectName('btn_ctB')

        self.btn_continuar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_continuar.setGeometry(QtCore.QRect(290, 180, 111, 31))
        self.btn_continuar.setObjectName('btn_continuar')

        self.lbl_progress1 = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_progress1.setGeometry(QtCore.QRect(650, 95, 211, 20))
        self.lbl_progress1.setText("")
        self.lbl_progress1.setObjectName("lbl_progress1")

        self.lbl_progress2 = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_progress2.setGeometry(QtCore.QRect(650, 155, 151, 21))
        self.lbl_progress2.setText("")
        self.lbl_progress2.setObjectName("lbl_progress2")

        self.lbl_rachaM = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_rachaM.setGeometry(QtCore.QRect(670, 210, 221, 30))
        self.lbl_rachaM.setObjectName("lbl_rachaM")

        self.lbl_rachaA = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_rachaA.setGeometry(QtCore.QRect(670, 270, 221, 30))
        self.lbl_rachaA.setObjectName("lbl_rachaA")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate('Form', 'Login - Memorizando la Biblia'))
        
        self.cb_menu1.setItemText(0, _translate('Form', 'Login'))
        self.cb_menu1.setItemText(1, _translate('Form', 'Crear Cuenta'))
        self.cb_menu1.setItemText(2, _translate('Form', 'Author'))
        self.cb_menu1.setItemText(3, _translate('Form', 'Salir'))

        self.cb_menu2.setItemText(0, _translate('Form', 'Textos Biblicos'))
        self.cb_menu2.setItemText(1, _translate('Form', 'Citas Biblicas'))
        self.cb_menu2.setItemText(2, _translate('Form', 'Estadistica'))
        self.cb_menu2.setItemText(3, _translate('Form', 'Author'))
        self.cb_menu2.setItemText(4, _translate('Form', 'Cerrar Seccion'))
        self.cb_menu2.setItemText(5, _translate('Form', 'Salir'))

        self.lbl_bienvenida.setText(_translate('Form', 'Bienvenidos'))
        self.lbl_usuario.setText(_translate('Form', 'Nombre de usuario: '))
        self.lbl_clave.setText(_translate('Form', 'Clave:'))
        self.lbl_alerta.setText(_translate('Form', ''))
        
        self.le_usuario.setPlaceholderText('Usuario')
        self.le_clave.setPlaceholderText('Clave')

        self.btn_azar.setText(_translate('Form', 'Al azar'))
        self.btn_txtB.setText(_translate('Form', 'Textos Biblicos'))
        self.btn_ctB.setText(_translate('Form', 'Citas Biblicas'))
        
        self.btn_continuar.setText(_translate('Form', 'Continuar'))
        self.txte_txt.setPlaceholderText('Texto Biblico')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)
    
    Form.show()
    sys.exit(app.exec_())

#* Author: Francisco Velez
