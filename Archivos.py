import Registros
import os.path


# cargar en orden el Archivo en el arreglo
def add_in_order(vec, proyecto):
    n = len(vec)
    pos = n
    for i in range(n):
        if proyecto.rep < vec[i].rep:
            pos = i
            break
    vec[pos:pos] = [proyecto]


# cargar el archivo como arreglo
def generar_arreglo():
    lineas = 0
    vector = []
    vector2 = []
    cont1 = 0
    cont2 = 0
    es_igual = False
    if os.path.exists('proyectos.csv'):
        m = open("proyectos.csv", mode="rt", encoding="utf8")

        for linea in m:

            if lineas == 0:
                lineas += 1
                continue

            pro = Registros.str_toproyectos(linea)

            if len(vector) > 0:
                for i in vector:
                    if pro.rep == i.rep:
                        vector2.append(pro)
                        cont2 += 1
                        es_igual = True
                        break

            if not es_igual:

                if pro.lenguaje == '':
                    cont2 += 1
                    vector2.append(pro)

                else:
                    add_in_order(vector, pro)
                    cont1 += 1

            es_igual = False
        m.close()

    return vector, vector2, cont1, cont2
