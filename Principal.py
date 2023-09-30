from Archivos import *
from Funciones import *
from datetime import date


# Funcion principal

def principal():
    crear = False
    b4 = b6 = False
    op = -1
    proyecto, proyecto2, cont1, cont2 = generar_arreglo()
    matriz = None
    suma = 0
    while op != 8:
        menu()
        op = int(input('Ingrese su opcion: '))

        if op == 1:
            print('-' * 50)
            print('* Proyectos Cargados:', cont1)
            print('* Omitidos:', cont2)
            print('-' * 50)
            crear = True

        elif op == 2:
            if crear:
                tag = input('Buscar por tag: ')
                ind = buscar_tag(tag, proyecto)
                if not ind:
                    print(Color.RED + 'Error!!.No existe' + Color.END)
                else:
                    guardar_tag = int(input('Quiere guardar el tag? 1- SI 2- NO: '))
                    if guardar_tag == 1:
                        archivo = escribir_archivo(tag, proyecto)
                        print(archivo)
                        print('-' * 50)
                    else:
                        print('OKEY! NO LO ESCRIBIREMOS :)')
                        print('-' * 50)
            else:
                print(Color.RED + '⛔ No se cargaron los datos' + Color.END)
                print()

        elif op == 3:
            if crear:
                cont = 0
                lenguajes, contador = proyectos_lenguaje(proyecto)

                print('Cantidad de proyectos por lenguaje:')
                for i in range(len(lenguajes)):
                    cont += 1
                    print('|', Color.BOLD + lenguajes[i] + Color.END, ':', contador[i], end=' ')
                    while cont > 5:
                        print()
                        print()
                        cont = 0
                print()
                print('-' * 50)
            else:
                print(Color.RED + '⛔ No se cargaron los datos' + Color.END)
                print()

        elif op == 4:
            if crear:
                b4 = True
                mes = int(input('Ingrese el mes que desea buscar (numero del 1 al 12): '))
                print()
                while mes < 1 or mes > 12:
                    print(Color.RED + '⛔ Error!!.Numero invalido' + Color.END)
                    mes = int(input('Ingrese el mes que desea buscar (numero del 1 al 12): '))
                matriz = crear_matriz(proyecto)
                mostrar_matriz(matriz)
                for i in range(5):
                    suma += matriz[mes-1][i]
                print('-' * 50)
                print('En el mes ', mes, ' hubo ', suma, ' actualizaciones.')
                print()
            else:
                print(Color.RED + '⛔ No se cargaron los datos' + Color.END)
                print()

        elif op == 5:
            if crear:
                rep = input("Ingrese el repositorio que desea buscar: ")
                inf = buscar_rep(rep, proyecto)
                if inf <= 0:
                    print(Color.RED + "⛔ Error!!. No existe el repositorio" + Color.END)
                else:
                    print(to_string(proyecto[inf]))
                url = int(input("Quiere cambiar el URL? 1- Si 2- NO: "))
                if url == 1:
                    proyecto[inf].url = str(input("Ingrese nueva URL: "))
                    proyecto[inf].fecha = str(date.today())
                    print(to_string(proyecto[inf]))
                elif url == 2:
                    print('El proyecto no se actualizo...')
                else:
                    print("-" * 60)
                    print(Color.RED + " ⛔ Error!!.No existe un repositorio con ese nombre" + Color.END)
            else:
                print(Color.RED + '⛔ No se cargaron los datos' + Color.END)
                print()

        elif op == 6:
            if crear and b4:
                b6 = True
                guardar_populares(matriz)

            else:
                print(Color.RED + '⛔ No se cargaron los datos. Debe pasar por las opciones 1 y 4' + Color.END)
                print()

        elif op == 7:
            if crear and b4 and b6:
                mostrar_archivo()

            else:
                print(Color.RED + '⛔ No se cargaron los datos. Debe pasar por las opciones 1, 4 y 6' + Color.END)
                print()

        elif op == 8:
            print('-' * 50)
            print('El programa finalizo')

        else:
            print('-' * 50)
            print(Color.RED + '⛔ Opcion Invalida, ingrese nuevamente' + Color.END)
            print('-' * 50)


# inicializacion

if __name__ == '__main__':
    principal()
