import json

info = {
    'Titulo': 'Aprender',
    'Name': 'name',
    'Clave': 'clave',

    'Ganadas': 0,
    'Perdidas': 0,

    'RachaGanadas': 0,
    'RachaGanadasMaxima': 0,

    'Seccion': 'Cerrado',
    'ModoDefault': 'None',

    'Author': 'Francisco J. Velez O.'
}

#* *************** *************** Funciones *************** *************** *#

def rescribir(name_Arch='./Usuarios/name.json', rs=["", ''], different=False): 
    file = ''
    if different: file = rs

    else:
        file = info
        file[rs[0]] = rs[1]

    with open(name_Arch, 'w') as f: 
        f.write(json.dumps(file, indent=4))

def lectura(name_Arch='./Usuarios/name.json'): 
    try:
        # Abre el archivo .agenda de modo lectura
        with open(name_Arch, 'rb') as file_read:
            # almacena el texto en una variable
            __TEXT_INFO__ = json.loads(file_read.read().decode('utf-8')) 
            
            # retorna el texto
            return __TEXT_INFO__
    except: return False

#* Halla una igualdad en dos textos
def sonIguales(txt1='', txt2=''):
    txt1 = txt1.lower().replace(' ', '').replace(';', '').replace(':', '').replace(',', '').replace('.', '').replace('\n', '')
    txt2 = txt2.lower().replace(' ', '').replace(';', '').replace(':', '').replace(',', '').replace('.', '').replace('\n', '')
    return formatear(txt1) == formatear(txt2)

#* Formatea el texto
def formatear(txt=''):
    return txt.replace('&&s', '\n')

#* Obtiene la informacion del ultimo usuario
def name_text():
    name = './Usuarios/'
    name += lectura('./Data/LastUser.json')['Usuario'].replace(' ', '_')
    name += '.json'

    texto = lectura(name.replace(' ', '_'))
    return [name, texto]

#* Modifica si esta abierta o cerrada la seccion
def seccion(modo='abierta'):
    name, text = name_text()
    text["Seccion"] = 'Abierto'

    if modo == 'abierta': text["Seccion"] = 'Abierto'
    else: text["Seccion"] = 'Cerrado'

    rescribir(name, text, True)
   
# def modoDefault(opc=''):
#     name, text = name_text()

#     c = encontrar(text, '<ModoDefault>', '</ModoDefault>')
#     varText = c.replace(c, opc)

#     if c == 'A':
#         c = '<ModoDefault> A </ModoDefault>'
#         varText = c.replace('A', opc)

#     rescribir(name, text.replace(c, varText))

#* Author: Francisco Velez
