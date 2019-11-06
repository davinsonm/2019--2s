# Autor: Davinson Morocho Insuaste
# Fecha: Octubre 30, 2019

# Descripcion de la Tarea
# ----------------------
# Realizar los ejercicios descritos en cada comentario.
# Escribir sus respuestas bajo el comentario respectivo.
# En todos los ejercicios, donde se pide que imprima,
# tambien escriba a que ejercicio corresponde la impresion.
#     Ejemplo de salida:
#          1b: Faltan XXXXX segundos para las 15:30

# 1. Utilice la siguiente lista de fechas

fechas =   ["13 Septiembre",
            "22 Septiembre",
            "27 Septiembre",
            "29 Septiembre",
            "3 Octubre",
            "5 Octubre",
            "10 Octubre",
            "12 Octubre",
            "17 Octubre",
            "19 Octubre",
            "24 Octubre",
            "26 Octubre",
            "3 Noviembre",
            "8 Noviembre",
            "10 Noviembre",
            "14 Noviembre",
            "17 Noviembre",
            "22 Noviembre",
            "24 Noviembre",
            "29 Noviembre",
            "31 Noviembre",
            "5 Diciembre",
            "7 Diciembre",
            "12 Diciembre",
            "14 Diciembre",
            "19 Diciembre",
            "21 Diciembre",
            "28 Diciembre"]

# 1a. Escriba un programa donde un usuario ingrese una fecha
#     Calcule cuantas fechas más hay después de esa fecha.
#     Ejemplo: 21 Diciembre -> Queda 1 fecha en el calendario
def fechades():
    print("1.A")
    print("Ingrese fecha: ")
    f=input()
    i=0
    id=0
    for date in fechas:
        id=fecha.find(date)
        if f==date:
            num=fechas.find(date)
            i+=1
        elif id>num:
            i+=1
    if i==0:
        print("No quedan fechas en el calendario")
    elif i==1:
        print("Queda 1 fecha en el calendario")
    else:
        print("Quedan %i fehcas en el calendario"%i)
fechades()

# 1b. Imprima cuantas fechas hay en cada mes
def cdmes():
    print("1.A")
    sep=[]
    oct=[]
    nov=[]
    dic=[]
    for fecha in fechas:
        if "Septiembre"in fecha:
            sep.append(fecha)
        elif "Octubre" in fecha:
            oct.append(fecha)
        elif "Noviembre" in fecha:
            nov.append(fecha)
        else:
            dic.append(fecha)
    print("Fechas en el mes de septiembre: ",sep)
    print("Fechas en el mes de octubre:", oct)
    print("Fechas en el mes de noviembre: ",nov)
    print("Fechas en el mes de diciembre: ",dic)
cdmes()

# 1c. Pida al usuario por teclado un mes entre Septiembre y Diciembre
#     Imprima cuantas fechas hay en ese mes
#     Ejemplo: Septiembre -> Hay 4 fechas en Septiembre
def fechames():
    print("1.C")
    print("ingrese un mes entre Septiembre y Diciembre")
    mes=input()
    contmes=0
    for fecha in fechas:
        m=fecha.find(mes)
        if m!=-1:
            contmes+=1
    if contmes==0:
        print("No hay fechas en el mes de ",mes)
    elif contmes==1:
        print("Hay 1 fecha en el mes de ",mes)
    else:
        print("Hay %i fechas en el mes de "%contmes,mes)
fechames()

# 1d. A continuación de 4c, imprima cuales son las fechas de ese mes
def meslista():
    print("1.D")
    print("ingrese un mes entre Septiembre y Diciembre")
    mes=input()
    lismes=[]
    contmes=0
    for fecha in fechas:
        m=fecha.find(mes)
        if m!=-1:
            contmes+=1
            lismes.append(fecha)
    if contmes==0:
        print("No hay fechas en el mes de ",mes)
    elif contmes==1:
        print("Hay 1 fecha en el mes de ",mes)
        print("La fecha es: ",lismes)
    else:
        print("Hay %i fechas en el mes de "%contmes,mes)
        print("Las fechas son: ",lismes)
meslista()
# 1e. Imprima todas las fechas que ocurren en la primera quincena del mes
def mesquin():
    print("1.E")
    quin=[]
    for fecha in fechas:
        desfe=fecha.split(" ")
        if int(desfe[0])<=15:
            quin.append(fecha)
    print("Las fechas que ocurren la primera quincena de cada mes son: ",quin)
mesquin()