import os
import msvcrt
import csv

#coleccion para almacenar vehiculo
vehiculos=[]

def limpiar():
    print("<<Press Any Key>>")
    msvcrt.getch()
    os.system("cls")

#funciones de color
def printR(texto):
    print(f"\033[31m{texto}\033[0m")
def printV(texto):
    print(f"\033[32m{texto}\033[0m")
def printA(texto):
    print(f"\033[33m{texto}\033[0m")

def menu():
    printA("Sistema gestión de Vehículos🚗")
    print("═════════════════════════════════")
    print("1.- Agregar Vehículo")
    print("2.- Listar Vehículos")
    print("3.- Eliminar Vehículo")
    print("4.- Modificar Vehículo")
    print("5.- Filtrar Vehículos por marca")
    print("6.- Generar reporte de vehículos")
    print("0.- Salir")
    print("═════════════════════════════════")

##############(C.R.U.D.)##############
marcas=("KIA","CHEVROLET","AUDI","NISSAN","OTRO")
def seleccionMarca():
    print("Marcas Disponibles")
    for i in range(len(marcas)):
        printA(f"{i+1}.- {marcas[i]} ")
    seleccion=int(input("Seleccione : "))-1#index
    #validar numero seleccionado
    if seleccion>=0 or seleccion<len(marcas):
        return marcas[seleccion]
    else:
        return None


tipos=("AUTOMOVIL","CAMIÓN","AUTOBUS","MOTOCICLETA")
def seleccionTipo():
    print("Tipos Disponibles")
    for i in range(len(tipos)):
        printA(f"{i+1}.- {tipos[i]} ")
    seleccion=int(input("Seleccione : "))-1#index
    #validar numero seleccionado
    if seleccion>=0 or seleccion<len(tipos):
        return tipos[seleccion]
    else:
        return None

def validarPatente(patente):
    for i in range(len(vehiculos)):
        if vehiculos[i][0]==patente:
            return i
    return -1 #retorna valor como guía
#AGREGAR
def agregar(patente,marca,tipo,precio,stock):
    #validar los datos
        if validarPatente(patente)==-1:
            if marca!= None:
                if tipos!=None:
                    if precio>0:
                        if stock>=0:
                            vehiculos.append((patente,marca,tipo,precio,stock))
                            printV("Vehículo registrado")
                        else:
                            printR("Stock no disponible")
                    else:
                            printR("Precio no válido")
                else:
                    printR("Tipo de vehículo no válido")
            else:
                printR("Marca no válida")
        else:
            printR("Patente duplicada")
        


#LISTAR 
def listar(vehiculos):
    for i in range(len(vehiculos)):
        if len(vehiculos)>0:
            print(f"{i+1}.- Patente: {vehiculos[i][0]} Marca: {vehiculos[i][1]} Tipo: {vehiculos[i][2]} $: {vehiculos[i][3]} STOCK: {vehiculos[i][4]}")
        else:
            printR("No existen vehículos")

#ELIMINAR
def eliminar(patente):
    pos=validarPatente("Ingrese Patente :")
    if pos>0:
        vehiculos.pop(pos)
        printV("Patente no existe")
    else:
        printR("Patente no existe")

#MODIFICAR
def modificar(patente,marca,tipo,precio,stock):
    pos=validarPatente(patente)
    if pos>=0:
        if marca!=None:
            if tipo!=None:
                if precio>0:
                    if stock>=0:
                        vehiculos.pop(pos)
                        vehiculos.append(patente,marca,tipo,precio,stock)
                    else:
                        printR("Stock no disponible")
                else:
                    printR("Precio no válido")
            else:
                printR("Tipo de vehículo no válido")
        else:
            printR("Marca no válida")
    else:
        printR("Patente no existe")


#FILTRAR
def filtrarporMarca(marca):
    if marca!=None:
        for i in range(len(vehiculos)):
            if marca==vehiculos[i][1]:
                print(f"{i+1}.- Patente: {vehiculos[i][0]} Marca: {vehiculos[i][1]} Tipo: {vehiculos[i][2]} $: {vehiculos[i][3]} STOCK: {vehiculos[i][4]}")
    else:
        printR("Marca no disponible")


#GENERAR REPORTE
def generarReporte():
    if len(vehiculos)>0:
        with open ('reporte vehículos.csv', 'w', newline='', encoding='utf-8')as f:
            escribir=csv.writer(f,delimiter=',')
            vehiculos.insert(0,["PATENTE","MARCA","TIPO","PRECIO","STOCK"])
            escribir.writerows(vehiculos)
            vehiculos.pop(0)
            printV("reporte generado")
    else:
        printR("No hay vehículos")