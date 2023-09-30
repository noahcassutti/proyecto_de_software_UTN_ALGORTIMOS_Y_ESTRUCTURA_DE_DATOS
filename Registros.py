
# Creacion de la clase
class Proyecto:
    def __init__(self, nom, rep, desc, fecha, lenguaje, likes, tags, url):
        self.nom = nom
        self.rep = rep
        self.desc = desc
        self.fecha = fecha
        self.lenguaje = lenguaje
        self.likes = likes
        self.tags = tags
        self.url = url

# colores


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Matriz:
    def __init__(self, mes, estrellas, proyectos):
        self.mes = mes
        self.estrellas = estrellas
        self.proyectos = proyectos


def to_String_Matriz(matriz):

    s = '{} | {} | {}'.format(matriz.mes, matriz.estrellas, matriz.proyectos)

    return s


# Visualizacion de cada proyecto

def to_string(proyecto):
    s = ''
    s += 'Nombre de Usuario: ' + str(proyecto.nom)
    s += ' - Repositorio: ' + str(proyecto.rep)
    s += ' - Descripcion: ' + str(proyecto.desc)
    s += ' - Fecha de Actualizacion: ' + str(proyecto.fecha)
    s += ' - Lenguaje: ' + str(proyecto.lenguaje)
    s += ' - Likes: ' + str(proyecto.likes)
    s += ' - Tags: ' + str(proyecto.tags)
    s += ' - URL: ' + str(proyecto.url)

    return s


# cargar en cada campo
def str_toproyectos(linea):
    campos = linea.split('|')
    nom = campos[0]
    rep = campos[1]
    desc = campos[2]
    fecha = campos[3]
    lenguaje = campos[4]
    likes = float(campos[5][:-1])
    tags = campos[6].split(',')
  
    url = campos[7]

    proyecto = Proyecto(nom, rep, desc, fecha, lenguaje, likes, tags, url)

    return proyecto


def str_tomatriz(linea):

    campos = linea.split('|')
    
    mes = campos[0]
    estrellas = campos[1]
    cantidad_proyectos = campos[2]

    matriz = Matriz(mes, estrellas, cantidad_proyectos)

    return matriz
