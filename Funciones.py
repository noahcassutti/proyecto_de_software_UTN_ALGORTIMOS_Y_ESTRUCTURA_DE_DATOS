import os
from Registros import *
import pickle


# Menu

def menu():
    print(Color.BOLD + '\t\t\t PROYECTO DE SOFTWARE' + Color.END)
    print('-' * 50)
    print('1- Cargar el contenido del archivo')
    print('2- Buscar por tag')
    print('3- Mostrar lenguajes')
    print('4- Popularidad')
    print('5- Buscar un proyecto actualizado')
    print('6- Guardar populares')
    print('7- Mostrar archivo')
    print('8- Salir del programa 🚪')
    print('-' * 50)


# Mostar los vectores ----> usar solo para verificar
def mostrar_vector(vec):
    print('Listado de proyectos')
    print('=' * 100)

    for proyecto in vec:
        print(to_string(proyecto))


# opcion 2 ---> buscar proyecto por tag

def buscar_tag(tag, vec):
    n = len(vec)
    tags = False
    for proyecto in range(n):
        for i in vec[proyecto].tags:

            if tag == i:
                star = estrellas(vec, proyecto)
                print('|Repositorio:', vec[proyecto].rep, ' |Fecha de actualizacion:', vec[proyecto].fecha,
                      ' |Estrellas:', star)
                tags = True
                break

    return tags


# opcion 4 ---> Crear matriz de meses y estrellas

def crear_matriz(vec):
    matriz = [[0] * 5 for f in range(12)]

    for i in range(len(vec)):
        date = vec[i].fecha.split('-')
        mes = int(date[1])
        star = estrellas(vec, i)
        matriz[mes - 1][star - 1] += 1

    return matriz


# Mostrar la matriz

def mostrar_matriz(matriz):
    meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
             'NOVIEMBRE', 'DICIEMBRE']
    print('ESTRELLAS  |  {:<5}|  {:<5}|  {:<5}|  {:<5}|  5'.format('1', '2', '3', '4'))
    for i in range(12):
        print('{:<10} |  {:<5}|  {:<5}|  {:<5}|  {:<5}|  {}'.format(meses[i], matriz[i][0], matriz[i][1], matriz[i][2],
                                                                    matriz[i][3], matriz[i][4]))


# guardar likes

def estrellas(vec, proyecto):
    star = 0

    if vec[proyecto].likes <= 10:
        star = 1
    elif 10.1 <= vec[proyecto].likes <= 20:
        star = 2
    elif 20.1 <= vec[proyecto].likes <= 30:
        star = 3
    elif 30.1 <= vec[proyecto].likes <= 40:
        star = 4
    elif vec[proyecto].likes > 40:
        star = 5

    return star


# crear un archivo binario
def escribir_archivo(tag, vec):
    m = open('Tag_Busqueda', 'wb')
    for i in vec:
        for j in i.tags:
            if j == tag:
                pickle.dump(i, m)
    m.close()
    nom = 'Tag_Busqueda'
    return nom


# opcion 3 ----> cantidad de proyectos por lenguaje
def proyectos_lenguaje(vec):
    iguales = False
    vector_nombres = []
    vector_cont = []

    for i in vec:

        if len(vector_cont) == 0:

            vector_nombres.append(i.lenguaje)
            vector_cont.append(1)

        else:
            for j in range(len(vector_nombres)):
                if vector_nombres[j] == i.lenguaje and iguales == False:
                    vector_cont[j] += 1
                    iguales = True

            if not iguales:
                vector_nombres.append(i.lenguaje)
                vector_cont.append(1)

            iguales = False

    return vector_nombres, vector_cont


# opcion 5 ---> buscar por repositorio
def buscar_rep(rep, vec):
    for i in range(len(vec)):
        if rep == vec[i].rep:
            return i
    return -1


# opcion 6


def guardar_populares(matriz):
    m = open('archivo_matriz.csv', "wb")
    cantidad = 0
    filas, columnas = 12, 5
    for i in range(filas):
        for j in range(columnas):

            if matriz[i][j] != 0:
                proyectos = Matriz(i + 1, j + 1, matriz[i][j])
                pickle.dump(to_String_Matriz(proyectos), m)

                cantidad += 1
    FD = 'archivo_matriz.csv'
    m.close()
    m = open('archivo_matriz.csv', 'rb')
    n = pickle.load(m)
    m.close()
    print('Archivo generado correctamente', cantidad, 'registros grabados.')


# punto 7
def mostrar_archivo():
    matriz = [[0] * 5 for f in range(12)]
    # global FD
    FD = "archivo_matriz.csv"
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        art = pickle.load(m)
        a = str_tomatriz(art)
        matriz[int(a.mes)-1][int(a.estrellas)-1] = a.proyectos
    m.close()
    mostrar_matriz(matriz)
