#* 1. Main 

#* Liberias Nesesarias
from functions_ import (
    rescribir, lectura, seccion, formatear, 
    sonIguales, porcentajes
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

        self.infoUser_ = lectura('./Data/LastUser.json')
        name = self.infoUser_['Usuario'].replace(' ', '_')

        self.User_ = lectura(f'./Users/{name}.json')

        self.rCorrectas = self.User_['RachaCorrectas']
        self.rCorrectasM = self.User_['RachaCorrectasMaxima']

        if self.User_['Seccion'] == 'Abierto':
                self.ui.lbl_alerta.setStyleSheet('color: rgb(82, 245, 245);')
                
                self.runHaciaDelante(
                    self.ui.lbl_alerta, 'Seccion Abierta...', time_=50
                )

                self.contSA = 0
                self.timerSA = QtCore.QTimer()
                self.timerSA.timeout.connect(self.seccionAbierta)
                self.timerSA.start(100)

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
    
    # ************ ************ Seccion Abierta ************ ************ #
    def seccionAbierta(self):
        self.contSA += 10

        if self.contSA >= 200:
            self.ui.le_usuario.setText(self.User_['Name'])
            self.ui.le_clave.setText(self.User_['Clave'])
            self.func_continuar()
            self.timerSA.stop()

    # ********* ********* Funciones del boton continuar ********* ********* #
    def func_continuar(self): 
        if self.opc_btn_cont == 'cerrar':
            self.close()
        
        if self.opc_btn_cont == 'continuar': 
            self.ui.lbl_usuario.setGeometry(-230, 100, 221, 1)
            self.ui.lbl_usuario.setText('Nombre de usuario: ')

            self.ui.lbl_clave.setGeometry(-230, 170, 71, 31)
            self.ui.lbl_clave.setText('Clave: ')
    
            self.ui.lbl_bienvenida.setGeometry(170, -130, 231, 41)
            self.ui.lbl_bienvenida.setText('Bienvenidos')

            self.ui.txte_txt.setGeometry(70, 120, 301, 131)
            self.ui.le_usuario.setGeometry(130, 65, 181, 30)
            
            self.ui.lbl_alerta.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
            self.ui.lbl_alerta.setText('')

            self.ui.lbl_progress1.setGeometry(650, 95, 211, 20)
            self.ui.lbl_progress2.setGeometry(650, 155, 151, 21)
            self.ui.lbl_rachaM.setGeometry(670, 210, 221, 30)
            self.ui.lbl_rachaA.setGeometry(670, 270, 221, 30)

            self.ui.lbl_alerta.setGeometry(165, 15, 250, 40)
            self.opc_btn_cont = 'verificar'
            
            self.run_procesos(
                lambda: self.mover(self.ui.btn_continuar, [310, 'x'], 3),
                lambda: self.mover(self.ui.btn_continuar, [270, 'y'], 10),
                
                lambda: self.run_geometry_(self.ui.fr_fondo, [320, 'height'], 10),
                lambda: self.run_geometry_(self.ui.fr_fondo, [440, 'width'], 10),
                
                lambda: self.mover(self.ui.cb_menu2, [20, 'x'], 5),

                lambda: self.runHaciaAtras(
                    self.ui.btn_continuar, self.ui.btn_continuar.text(), 
                    lambda: self.runHaciaDelante(
                        self.ui.btn_continuar, 'Verificar', time_=50
                    ), 50
                ),

                lambda: (
                    self.ui.btn_txtB.setGeometry(460, 110, 140, 41),
                    self.resize(460, 340)
                )
            )

        elif self.opc_btn_cont == 'siguiente':
            self.ui.btn_continuar.setText('')
            self.ui.lbl_alerta.setText('')
            
            def function001_():
                self.firstAprender = True
                self.aplicarModos()

            self.runHaciaDelante(
                self.ui.btn_continuar, 'Verificar',
                function001_, 100
            )
            
            self.opc_btn_cont = 'verificar'

        elif self.opc_btn_cont == 'verificar':
            if self.modoAprender == 'txtb': 
                txt = self.ui.txte_txt.toPlainText()
                txt2 = self.infor[f'Texto{self.numOpc}']['Texto']

                if sonIguales(txt2, txt):
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
                    self.ui.lbl_alerta.setText('Respuesta Correcta')
                    self.User_['Correctas'] += 5 
                    self.User_['RachaCorrectas'] += 5

                    if self.User_['RachaCorrectas'] >= self.User_['RachaCorrectasMaxima']:
                        self.User_['RachaCorrectasMaxima'] = self.User_['RachaCorrectas']

                else:
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                    self.ui.lbl_alerta.setText('Respuesta Incorrecta')
                    self.User_['Incorrectas'] -= 5 
                    self.User_['RachaCorrectas'] = 0

            if self.modoAprender == 'ctb':
                ct = self.ui.le_usuario.text()
                ct2 = self.infor[f'Texto{self.numOpc}']['Cita']
            
                if sonIguales(ct2, ct):
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
                    self.ui.lbl_alerta.setText('Respuesta Correcta')
                    self.User_['Correctas'] += 5 
                    self.User_['RachaCorrectas'] += 5

                    if self.User_['RachaCorrectas'] >= self.User_['RachaCorrectasMaxima']:
                        self.User_['RachaCorrectasMaxima'] = self.User_['RachaCorrectas']

                else:
                    self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                    self.ui.lbl_alerta.setText('Respuesta Incorrecta')
                    self.User_['Incorrectas'] -= 5 
                    self.User_['RachaCorrectas'] = 0
            
            self.runHaciaDelante(
                self.ui.btn_continuar, 'Siguiente', time_=100
            )

            self.opc_btn_cont = 'siguiente'
            n = self.User_['Name'].replace(' ', '_')
            rescribir(f'./Users/{n}.json', self.User_, True)

        elif self.modo == 'login': 
            name = self.ui.le_usuario.text().strip().replace(' ', '_')
            nameA = f'./Users/{name}.json'
            
            if name == '':
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Campo de Usuario Vacio.')
                return False

            self.User_ = lectura(nameA)
            
            if self.User_ == False:
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Nombre de Usuario Incorrecto.')
                return False
            
            c = self.ui.le_clave.text().strip()
            
            if c == '':
                self.ui.lbl_alerta.setStyleSheet('color: rgb(255, 80, 83);')
                self.ui.lbl_alerta.setText('Error: Campo de Clave Vacio.')
                return False

            if self.User_['Clave'] == self.ui.le_clave.text():
                rescribir(
                    './Data/LastUser.json', {
                        'Usuario': name.replace('_', ' '), 
                        'Fecha': strftime('El dia %d/%m/%Y, a las %H:%M:%S')
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
        
                self.ui.cb_menu1.setGeometry(-120, 30, 111, 5)
                self.ui.le_usuario.setGeometry(460, 100, 140, 30)
        
                self.ui.lbl_usuario.setGeometry(-230, 100, 221, 1)
                self.ui.lbl_clave.setGeometry(-230, 170, 71, 1)
                self.ui.le_clave.setGeometry(-210, 170, 140, 0)

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

            rescribir(f'./Users/{name}.json', ['Name', name])
            rescribir(f'./Users/{name}.json', ['Clave', clave])

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

        if opc == 'estadistica':
            n = self.User_['Name'].replace(' ', '_')
            self.User_ = lectura(f'./Users/{n}.json')
            ga_, pe_ = self.User_['Correctas'], self.User_['Incorrectas']
            rm_, ra_ = self.User_['RachaCorrectasMaxima'], self.User_['RachaCorrectas']

            self.ui.lbl_usuario.setGeometry(30, 90, 200, 30)
            self.ui.lbl_usuario.setText(f'{ga_} - Correctas')
            
            self.ui.lbl_clave.setGeometry(30, 150, 200, 30)
            self.ui.lbl_clave.setText(f'{-pe_} - Incorrectas')
    
            self.ui.lbl_bienvenida.setGeometry(30, 20, 460, 40)
            self.ui.lbl_bienvenida.setText('')

            self.runHaciaDelante(
                self.ui.lbl_bienvenida, 'Usuario: ' + self.User_['Name'], time_=100
            )

            self.ui.btn_txtB.setGeometry(560, 110, 140, 41)
            self.ui.txte_txt.setGeometry(-370, 120, 301, 131)
            self.ui.le_usuario.setGeometry(560, 100, 140, 30)
            self.opc_btn_cont = 'continuar'
            
            self.ui.lbl_alerta.setStyleSheet('color: rgb(0, 204, 0);')
            self.ui.lbl_alerta.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.lbl_alerta.setText('')
            
            self.ui.lbl_alerta.setGeometry(-330, 210, 221, 121)
            self.resize(540, 390)

            self.ui.lbl_progress1.setGeometry(250, 95, 20, 20)
            self.ui.lbl_progress2.setGeometry(250, 155, 20, 20)

            def progress():
                n = self.User_['Name'].replace(' ', '_')
                self.User_ = lectura(f'./Users/{n}.json')
                ga_, pe_ = self.User_['Correctas'], -(self.User_['Incorrectas'])

                if ga_ >= pe_: 
                    pe_ = porcentajes([20, 230], ga_, pe_)
                    ga_ = 230

                else: 
                    ga_ = porcentajes([20, 230], pe_, ga_)
                    pe_ = 230
                
                self.ui.lbl_progress1.setGeometry(250, 95, ga_, 20)
                self.ui.lbl_progress2.setGeometry(250, 155, pe_, 20)
                
            self.run_procesos(
                lambda: self.mover(self.ui.cb_menu2, [-220, 'x'], 5),
                lambda: self.run_geometry_(self.ui.fr_fondo, [370, 'height'], 10),
                lambda: self.run_geometry_(self.ui.fr_fondo, [520, 'width'], 10),

                lambda: self.mover(self.ui.btn_continuar, [370, 'x'], 10),
                
                lambda: self.mover(
                    self.ui.btn_continuar, [320, 'y'], 10,
                    lambda: self.runHaciaAtras(
                        self.ui.btn_continuar, self.ui.btn_continuar.text(), 
                        lambda: self.runHaciaDelante(
                            self.ui.btn_continuar, 'Continuar', time_ = 50
                        ), 50
                    ),
                ),

                lambda: (
                    progress(), 
                    self.ui.lbl_rachaM.setGeometry(270, 210, 220, 30),
                    self.ui.lbl_rachaA.setGeometry(270, 270, 220, 30),
                
                    self.ui.lbl_alerta.setGeometry(30, 210, 221, 121),
                    self.ui.lbl_rachaM.setText(f'{rm_} - Racha Maxima'),
                    self.ui.lbl_rachaA.setText(f'{ra_} - Racha Actual'),

                    self.ui.lbl_alerta.setText(
                        ' Respuesta: \n Correcta +5 puntos, \n Incorrecta -5 puntos.'
                    ),
                )
            )
            
        if opc == 'author' and not(self.modoMActive):
            self.ui.lbl_alerta.setStyleSheet('color: rgb(82, 245, 245);')
            opc = {'txtb' : 0, 'ctb' : 1}[self.modoAprender]
            self.mn_selec = 'author'
            
            if self.isActiveAnimation: 
                self.ui.cb_menu2.setCurrentIndex(opc)
            
            else:
                self.runHaciaDelante(
                    self.ui.lbl_alerta, 'Francisco J. Velez O.'
                )

        if opc == 'cerrar seccion':
            self.setWindowTitle('Login - Memorizando la Biblia')
            self.ui.le_usuario.setMaxLength(15)
            self.ui.le_usuario.setEnabled(True)
            self.ui.le_usuario.setText('')
            self.opc_btn_cont = 'normal'
            seccion('cerrada')

            self.run_procesos(
                lambda: self.mover(
                    self.ui.cb_menu2, [-220, 'x'], 10
                ),
                
                lambda: (
                    self.mover(self.ui.btn_continuar, [290, 'x'], 10,
                    lambda: self.ui.txte_txt.setGeometry(-370, 120, 301, 11)) 
                ),
                
                lambda: self.mover(self.ui.btn_continuar, [180, 'y'], 10),

                lambda: (
                    self.ui.cb_menu1.setGeometry(20, 30, 111, 35),
                    self.ui.le_usuario.setGeometry(260, 100, 140, 30),
                    self.ui.lbl_usuario.setGeometry(30, 100, 221, 31),
                    self.ui.lbl_clave.setGeometry(30, 170, 71, 31),
                    self.ui.le_clave.setGeometry(110, 170, 140, 30),
                    self.ui.lbl_alerta.setGeometry(30, 250, 371, 41),

                    self.ui.cb_menu1.setGeometry(20, 30, 111, 35),
                    self.ui.lbl_bienvenida.setGeometry(170, 30, 231, 41),
                    
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
        
        if opc == 'salir': self.close()

    # ******* ******* Funciones de los botones de Modos ******* ******* #
    def func_modos(self, modo=''):
        self.setWindowTitle('Ventana Principal - Memorizando la Biblia')
        self.ui.le_usuario.setMaxLength(20)
        
        self.modoMActive = True
        self.modoAprender = modo
        
        if self.modoAprender == 'txtb': self.ui.cb_menu2.setCurrentIndex(0)
        else: self.ui.cb_menu2.setCurrentIndex(1)
        
        def activeFalse(): self.modoMActive = False

        self.ui.lbl_alerta.setText('')
        self.ui.lbl_alerta.setGeometry(165, 15, 250, 40)
        
        self.ui.le_usuario.setText('')
        self.ui.le_usuario.setPlaceholderText('Cita Biblica')
        
        self.runHaciaAtras(
            self.ui.lbl_bienvenida, self.ui.lbl_bienvenida.text(),
            lambda: self.ui.lbl_bienvenida.setGeometry(170, -130, 231, 41)
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
                        self.ui.le_usuario.setGeometry(130, 65, 181, 30),
                        self.ui.txte_txt.setGeometry(70, 120, 301, 131),
                        self.aplicarModos(),
                        activeFalse()
                    ), 100
                ), 100
            )
        )
        
    def aplicarModos(self):
        self.opc_btn_cont = 'verificar'
        def ActiveAnimationFalse(): self.isActiveAnimation = False

        if self.modoAprender == 'az': 
            self.firstAprender = True
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
        it = self.iter_process(args)

        self.timerM = QtCore.QTimer()
        self.timerM.timeout.connect(lambda: self.procesos(it))
        self.timerM.start(10)

    def procesos(self, iterador):
        if not(self.activeProces): 
            self.activeProces = True

            try: next(iterador)
            except StopIteration: self.timerM.stop()

    def iter_process(self, args):
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

    # ******* ******* Cambiar Tamaño en una sola cordenada ******* ******* #
    def run_geometry_(self, objecto01=None, opc=[0, 'height/width'], time_=150, func_=False, different=False):
        self.timer01 = QtCore.QTimer()
        self.timer01.timeout.connect(lambda: self.func_geometry_(objecto01, opc, func_, different))
        self.timer01.start(time_)

    def func_geometry_(self, objecto01=None, opc=[0, 'height/width'], func_=False, different=False):
        height = objecto01.geometry().height()
        width = objecto01.geometry().width()
        x_ = objecto01.geometry().x()
        y_ = objecto01.geometry().y()
        n = 0

        if opc[1] == 'height':
            if opc[0] > height: n = +1 

            elif opc[0] == height: 
                self.activeProces = False
                if func_ != False: func_()
                self.timer01.stop()

            else: n = -1

            if not(different): objecto01.resize(width, height + n)
            else: objecto01.setGeometry(x_, y_, width, height + n)

        if opc[1] == 'width':
            if opc[0] > width: n = +1 
            
            elif opc[0] == width: 
                self.activeProces = False
                if func_ != False: func_() 
                self.timer01.stop()
            
            else: n = -1
            if not(different): objecto01.resize(width + n, height)
            else: objecto01.setGeometry(x_, y_, width + n, height)

    # ******* ******* Animacion del titulo al entrar a Modos ******* ******* #
    def func_lbl_titulo(self):
        self.setWindowTitle('Modos - Memorizando la Biblia')
        self.ui.lbl_bienvenida.setGeometry(10, 20, 420, 50)
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
    app.setWindowIcon(QtGui.QIcon('./Data/QuickAccess.ico'))
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
