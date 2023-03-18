#* 1. Main 

#* Liberias Nesesarias
from functions_ import (
    rescribir, lectura, seccion, formatear, sonIguales
)

from Login import Ui_Form, QtWidgets, QtCore, QtGui
from time import strftime
import random, sys

#* Animacion de Escritura
class Escritura:
      
    def runHaciaDelante(self, objecto_=None, txt_='', func_=False, time_=160): 
        self.iterador_ = txt_
        self.text_ = txt_
        self.long_ = 0

        self.objecto_ = objecto_
        self.objecto_.setText('')

        self.timer1_ = QtCore.QTimer()
        self.timer1_.timeout.connect(lambda: self.haciaDelante(func_))
        self.timer1_.start(time_)

    def haciaDelante(self, func_=False): 
        self.timerActive = True

        self.long_ += 1
        self.iterador_ = self.text_[:self.long_]
        self.objecto_.setText(self.iterador_)

        if self.long_ >= len(self.text_): 
            if func_ != False: func_()
            self.timerActive = False
            self.timer1_.stop()

    def runHaciaAtras(self, objecto_=None, txt_='', func_=False, time_=160):
        self.text_ = txt_

        self.objecto_ = objecto_
        self.objecto_.setText(self.text_)

        self.timer2_ = QtCore.QTimer()
        self.timer2_.timeout.connect(lambda: self.haciaAtras(func_))
        self.timer2_.start(time_)

    def haciaAtras(self, func_=False): 
        self.timerActive = True

        self.text_ = self.text_[:-1]
        self.objecto_.setText(self.text_)

        if self.text_ == '': 
            if func_ != False: func_()
            self.timerActive = False
            self.timer2_.stop()

#* Ventana principal
class MainApp(QtWidgets.QMainWindow, Escritura): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.isActiveAnimation = False
        self.opc_btn_cont = 'normal'
        self.firstAprender = True
        self.timerActive = False
        self.mn_selec = 'login'
        self.modoAprender = ''
        self.modo = 'login'

        self.ui.cb_menu1.activated.connect(self.func_menu1)
        self.ui.cb_menu2.activated.connect(self.func_menu2)
        self.ui.btn_continuar.clicked.connect(self.func_continuar)

        self.ui.btn_ctB.clicked.connect(lambda: self.func_modos('ctb'))
        self.ui.btn_txtB.clicked.connect(lambda: self.func_modos('txtb'))
        self.ui.btn_azar.clicked.connect(lambda: self.func_modos('az'))

        # Mover ventana
        self.ui.fr_fondo.mouseMoveEvent = self.mover_ventana
	  
    # ************ ************ mover ventana ************ ************ #
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass      
    
    # ********* ********* Funciones del boton continuar ********* ********* #
    def func_continuar(self): 
        if self.opc_btn_cont == 'cerrar':
            self.close()
        
        if self.opc_btn_cont == 'verificar':

            if self.modoAprender == 'txtb': 
                txt = self.ui.txte_txt.toPlainText()
                txt2 = self.infor[f'Texto{self.numOpc}']['Texto']

                if sonIguales(txt2, txt):
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
                    self.ui.lbl_alerta.setText('Respuesta Correcta')

                else:
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                    self.ui.lbl_alerta.setText('Respuesta Incorrecta')

            if self.modoAprender == 'ctb':
                ct = self.ui.le_usuario.text()
                ct2 = self.infor[f'Texto{self.numOpc}']['Cita']
            
                if sonIguales(ct2, ct):
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
                    self.ui.lbl_alerta.setText('Respuesta Correcta')

                else:
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                    self.ui.lbl_alerta.setText('Respuesta Incorrecta')

        elif self.modo == 'login': 
            name = self.ui.le_usuario.text().strip().replace(' ', '_')
            nameA = f'./Usuarios/{name}.json'
            
            if name == '':
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Campo de Usuario Vacio.')
                return False

            Infor = lectura(nameA)
            
            if Infor == False:
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Nombre de Usuario Incorrecto.')
                return False
            
            c = self.ui.le_clave.text().strip()
            
            if c == '':
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Campo de Clave Vacio.')
                return False

            if Infor["Clave"] == self.ui.le_clave.text():
                rescribir(
                    './Data/LastUser.json', {
                        "Usuario": name.replace('_', ' '), 
                        "Fecha": strftime('El dia %d/%m/%Y, a las %H:%M:%S')
                    }, True
                )

                self.ui.lbl_alerta.setText('')
                self.ui.lbl_alerta.setStyleSheet('border: 1px solid rgba(255, 255, 255, .0);')
                seccion('abierta')

                self.ui.lbl_bienvenida.setAlignment(QtCore.Qt.AlignCenter)
                self.ui.lbl_bienvenida.setWindowOpacity(0)

                self.runHaciaAtras(
                    self.ui.lbl_bienvenida, self.ui.lbl_bienvenida.text(),
                    self.func_lbl_titulo, 150
                )
        
                self.ui.cb_menu1.setGeometry(QtCore.QRect(-120, 30, 111, 35))
                self.ui.le_usuario.setGeometry(QtCore.QRect(460, 100, 140, 30))
        
                self.ui.lbl_usuario.setGeometry(QtCore.QRect(-230, 100, 221, 31))
                self.ui.lbl_clave.setGeometry(QtCore.QRect(-230, 170, 71, 31))
                self.ui.le_clave.setGeometry(QtCore.QRect(-210, 170, 140, 30))

                self.run_procesos(
                    lambda: self.mover(
                        self.ui.btn_continuar, [270, 'y'], 10,
                    ),

                    lambda: self.mover(
                        self.ui.btn_continuar, [20, 'x'], 5,
                    ),

                    lambda: self.mover(
                        self.ui.btn_azar, [180, 'y'], 5
                    ),
                    
                    lambda: self.mover(
                        self.ui.btn_txtB, [260, 'x'], 5
                    ),
                    
                    lambda: self.mover(
                        self.ui.btn_ctB, [40, 'x'], 5
                    ),
                )

            else:
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Clave no valida.')

        else: 
            name = self.ui.le_usuario.text().strip()

            if name == '':
                self.ui.lbl_alerta.setText('Error: Campo de Usuario Vacio.')
                return False

            clave = self.ui.le_clave.text().strip()
            self.ui.cb_menu1.setCurrentIndex(0)
            self.func_menu1()
            
            if clave == '':
                self.ui.lbl_alerta.setText('Error: Campo de Clave Vacio.')
                return False

            self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
            self.ui.lbl_alerta.setText('Cuenta Creada.')
            name = name.replace(' ', '_')

            rescribir(f'./Usuarios/{name}.json', ['Name', name])
            rescribir(f'./Usuarios/{name}.json', ['Clave', clave])

    # ******* ******* Funcion del Menu del login ******* ******* #
    def func_menu1(self): 
        opc = self.ui.cb_menu1.currentText().lower()
        opcs_ = {'login' : 0, 'crear cuenta' : 1, 'author' : 2}

        if opc == 'salir': self.close()

        elif opc == 'author':
            if not(self.timerActive):
                self.ui.lbl_alerta.setStyleSheet('color: rgb(82, 245, 245);')
                self.mn_selec = 'author'
                
                self.runHaciaDelante(
                    self.ui.lbl_alerta, 'Author: Francisco J. Velez O.'
                )

            else: self.ui.cb_menu1.setCurrentIndex(opcs_[self.mn_selec])

        elif opc == 'login': 
            if not(self.timerActive) and self.modo == 'crear cuenta':
                self.setWindowTitle('Login - Memorizando la Biblia')
                
                self.ui.lbl_alerta.setText('')
                self.ui.le_usuario.setText('')
                self.ui.le_clave.setText('')
                
                self.modo = 'login'
                self.timerActive = True
                self.mn_selec = 'login'

                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.animacion_l)
                self.timer.start(80)

            else: self.ui.cb_menu1.setCurrentIndex(opcs_[self.mn_selec])

        elif opc == 'crear cuenta': 
            if not(self.timerActive) and self.modo == 'login':
                self.setWindowTitle('Crear Cuenta - Memorizando la Biblia')
                
                self.ui.lbl_alerta.setText('')
                self.ui.le_usuario.setText('')
                self.ui.le_clave.setText('')
                
                self.mn_selec = 'crear cuenta'
                self.modo = 'crear cuenta'
                self.timerActive = True

                self.timer = QtCore.QTimer()
                self.timer.timeout.connect(self.animacion_cc)
                self.timer.start(80)

            else: self.ui.cb_menu1.setCurrentIndex(opcs_[self.mn_selec])

    # ******* ******* Funcion del Menu de la Ventana Principal ******* ******* #
    def func_menu2(self): 
        opc = self.ui.cb_menu2.currentText().lower()

        if opc == 'salir': self.close()

        if opc == 'textos biblicos':
            self.ui.lbl_alerta.setText('')
            self.isActiveAnimation = True
            self.modoAprender = 'txtb'
            self.aplicarModos()
        
        if opc == 'citas biblicas':
            self.ui.lbl_alerta.setText('')
            self.isActiveAnimation = True
            self.modoAprender = 'ctb'
            self.aplicarModos()

        if opc == 'cerrar seccion':
            self.setWindowTitle('Login - Memorizando la Biblia')
            self.ui.le_usuario.setMaxLength(15)
            self.ui.le_usuario.setEnabled(True)
            self.ui.le_usuario.setText('')
            self.opc_btn_cont = 'normal'

            self.run_procesos(
                lambda: self.mover(
                    self.ui.cb_menu2, [-220, 'x'], 10
                ),
                
                lambda: self.mover(self.ui.btn_continuar, [290, 'x'], 10,
                    lambda: self.ui.txte_txt.setGeometry(QtCore.QRect(-370, 120, 301, 131)), 
                ),
                
                lambda: self.mover(self.ui.btn_continuar, [180, 'y'], 10),

                lambda: (
                    self.ui.cb_menu1.setGeometry(QtCore.QRect(20, 30, 111, 35)),
                    self.ui.le_usuario.setGeometry(QtCore.QRect(260, 100, 140, 30)),
                    self.ui.lbl_usuario.setGeometry(QtCore.QRect(30, 100, 221, 31)),
                    self.ui.lbl_clave.setGeometry(QtCore.QRect(30, 170, 71, 31)),
                    self.ui.le_clave.setGeometry(QtCore.QRect(110, 170, 140, 30)),
                    self.ui.lbl_alerta.setGeometry(QtCore.QRect(30, 250, 371, 41)),

                    self.ui.cb_menu1.setGeometry(QtCore.QRect(20, 30, 111, 35)),
                    self.ui.lbl_bienvenida.setGeometry(QtCore.QRect(170, 30, 231, 41)),
                    
                    self.ui.le_usuario.setPlaceholderText('Usuario'),
                    self.ui.le_clave.setPlaceholderText('Clave'),

                    self.ui.lbl_bienvenida.setText('Bienvenidos'),
                    self.ui.cb_menu1.setCurrentIndex(0),
                    self.ui.lbl_alerta.setText(''),
                    self.ui.le_clave.setText('')
                )
            )
            
            self.runHaciaAtras(self.ui.btn_continuar, self.ui.btn_continuar.text(),
                lambda: self.runHaciaDelante(self.ui.btn_continuar, 'Continuar'), 150
            )


        if opc == 'author' and not(self.modoMActive):
            self.ui.lbl_alerta.setStyleSheet('color: rgb(82, 245, 245);')
            opc = {'txtb': 0, 'ctb':1}[self.modoAprender]
            self.mn_selec = 'author'
            
            if self.isActiveAnimation: 
                self.ui.cb_menu2.setCurrentIndex(opc)
            
            else:
                self.runHaciaDelante(
                    self.ui.lbl_alerta, 'Francisco J. Velez O.'
                )

    # ******* ******* Funciones de los botones de Modos ******* ******* #
    def func_modos(self, modo=''):
        self.setWindowTitle('Ventana Principal - Memorizando la Biblia')
        self.ui.cb_menu2.setCurrentIndex(0)
        self.ui.le_usuario.setMaxLength(20)
        
        self.modoMActive = True
        self.modoAprender = modo

        def activeFalse(): self.modoMActive = False

        self.ui.lbl_alerta.setText('')
        self.ui.lbl_alerta.setGeometry(QtCore.QRect(165, 15, 250, 40))
        
        self.ui.le_usuario.setText('')
        self.ui.le_usuario.setPlaceholderText('Cita Biblica')
        
        self.runHaciaAtras(
            self.ui.lbl_bienvenida, self.ui.lbl_bienvenida.text(),
            lambda: self.ui.lbl_bienvenida.setGeometry(QtCore.QRect(170, -130, 231, 41))
        )
        
        self.run_procesos(
            lambda: self.mover(
                self.ui.btn_txtB, [460, 'x'], 5,
            ),

            lambda: self.mover(
                self.ui.btn_ctB, [-140, 'x'], 5
            ),

            lambda: self.mover(
                self.ui.btn_azar, [380, 'y'], 5,
            ),            

            lambda: self.mover(self.ui.btn_continuar, [310, 'x'], 3),
            
            lambda: self.mover(
                self.ui.cb_menu2, [20, 'x'], 5,
            ),

            lambda: self.runHaciaAtras(
                self.ui.btn_continuar, self.ui.btn_continuar.text(),
                
                lambda: self.runHaciaDelante(
                    self.ui.btn_continuar, 'Verificar',

                    lambda: (
                        self.ui.lbl_alerta.setStyleSheet('border: 1px solid rgba(255, 255, 255, .15);'),
                        self.ui.le_usuario.setGeometry(QtCore.QRect(130, 65, 181, 30)),
                        self.ui.txte_txt.setGeometry(QtCore.QRect(70, 120, 301, 131)),
                        self.aplicarModos(),
                        activeFalse()
                    ), 140
                ), 140
            )
        )
        
    def aplicarModos(self):
        self.opc_btn_cont = 'verificar'
        def ActiveAnimationFalse(): self.isActiveAnimation = False

        if self.modoAprender == 'az': 
            self.modoAprender = random.choice(['txtb', 'ctb'])
        
        self.infor = lectura('./Data/textosBiblico.json')
        self.numOpc = random.randint(1, len(self.infor)) 
        
        if self.modoAprender == 'txtb':
            self.ui.le_usuario.setEnabled(False)
            self.ui.txte_txt.setEnabled(True)
            self.ui.txte_txt.setText('')
            
            if self.modoAprender == 'txtb' and self.firstAprender:
                self.firstAprender = False
                self.ui.le_usuario.setText(
                    formatear(self.infor[f'Texto{self.numOpc}']['Cita'])
                )
                ActiveAnimationFalse()

            else:
                self.runHaciaDelante(
                    self.ui.le_usuario, 
                    formatear(self.infor[f'Texto{self.numOpc}']['Cita']),
                    lambda: ActiveAnimationFalse(), 80
                )

        elif self.modoAprender == 'ctb': 
            self.ui.txte_txt.setEnabled(False)
            self.ui.le_usuario.setEnabled(True)
            self.ui.le_usuario.setText('')

            if self.firstAprender:
                self.firstAprender = False
                self.ui.txte_txt.setText(
                    formatear(self.infor[f'Texto{self.numOpc}']['Texto'])
                )
                ActiveAnimationFalse()

            else:
                self.runHaciaDelante(
                    self.ui.txte_txt, 
                    formatear(self.infor[f'Texto{self.numOpc}']['Texto']),
                    lambda: ActiveAnimationFalse(), 40
                )

    # ******* ******* Manejo de procesos de varias animaciones ******* ******* #
    def run_procesos(self, *args):
        self.activeProces = False
        it = self.iter_proces(args)

        self.timerM = QtCore.QTimer()
        self.timerM.timeout.connect(lambda: self.procesos(it))
        self.timerM.start(10)

    def procesos(self, iterador):
        if not(self.activeProces): 
            self.activeProces = True

            try: next(iterador)
            except StopIteration: self.timerM.stop()

    def iter_proces(self, args):
        for x in args: yield x()

    # ******* ******* Mover Objectos en una sola cordenada ******* ******* #
    def mover(self, objecto01=None, opc=[0, 'y/x'], time_=150, func_=False):
        self.timer01 = QtCore.QTimer()
        self.timer01.timeout.connect(lambda: self.func_move_btn(objecto01, opc, func_))
        self.timer01.start(time_)

    def func_move_btn(self, objecto01=None, opc=[0, 'y/x'], func_=False):
        x_ = objecto01.geometry().x()
        y_ = objecto01.geometry().y()
        width = objecto01.geometry().width()
        height = objecto01.geometry().height()
        n = 0

        if opc[1] == 'y':
            if opc[0] > y_: n = +1 

            elif opc[0] == y_: 
                if func_ != False: func_()
                self.activeProces = False
                self.timer01.stop()

            else: n = -1
            objecto01.setGeometry(x_, y_ + n, width, height)

        if opc[1] == 'x':
            if opc[0] > x_: n = +1 
            
            elif opc[0] == x_: 
                if func_ != False: func_() 
                self.activeProces = False
                self.timer01.stop()
            
            else: n = -1
            objecto01.setGeometry(x_ + n, y_, width, height)

    # ******* ******* Animacion del titulo al entrar a Modos ******* ******* #
    def func_lbl_titulo(self):
        self.setWindowTitle('Modos - Memorizando la Biblia')
        self.ui.lbl_bienvenida.setGeometry(QtCore.QRect(10, 20, 420, 50))
        self.opc_btn_cont = 'cerrar'
        
        self.runHaciaDelante(
            self.ui.lbl_bienvenida, 'Elige un Modo:',
            
            lambda: self.runHaciaAtras(
                self.ui.btn_continuar, 'Continuar',

                lambda: self.runHaciaDelante(
                    self.ui.btn_continuar, 'Cerrar', time_ = 80
                ), 80
            ), 50
        )

    # ********* Animaciones al entrar al login y al crear cuenta ********* #
    def animacion_l(self):
        w = self.ui.btn_continuar.geometry().width()-2
        h = self.ui.btn_continuar.geometry().height()
        x = self.ui.btn_continuar.geometry().x()+2
        y = self.ui.btn_continuar.geometry().y()

        self.ui.btn_continuar.setGeometry(x, y, w, h)

        if x >= 290:
            self.timer.stop()
            
            self.runHaciaAtras(
                self.ui.btn_continuar, 'Crear Cuenta',
                lambda: self.runHaciaDelante(self.ui.btn_continuar, 'Continuar')
            )

    def animacion_cc(self):
        w = self.ui.btn_continuar.geometry().width()+2
        h = self.ui.btn_continuar.geometry().height()
        x = self.ui.btn_continuar.geometry().x()-2
        y = self.ui.btn_continuar.geometry().y()

        self.ui.btn_continuar.setGeometry(x, y, w, h)

        if x <= 270:
            self.timer.stop()
            
            self.runHaciaAtras(
                self.ui.btn_continuar, 'Continuar',
                lambda: (self.runHaciaDelante(self.ui.btn_continuar, 'Crear Cuenta'))
            )

            self.timerActive = False
            

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    app.setWindowIcon(QtGui.QIcon("./data/QuickAccess.ico"))
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
