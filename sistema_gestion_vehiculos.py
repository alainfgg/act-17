from funcionesauto import limpiar, agregar, modificar, listar, eliminar, generarReporte, menu, printA, printR, printV, filtrarporMarca,seleccionMarca,seleccionTipo
vehiculos=[]
while True:
    limpiar()
    menu()
    opcion=input("Seleccione: ")
    if opcion=="0":
        break
    elif opcion=="1":
        printA("Agregar Vehículo")
        patente=input("Ingrese Patente (ej: xxll22) : ").upper()
        marca=seleccionMarca()
        tipo=seleccionTipo()
        precio=int(input("Ingrese precio $: "))
        stock=int(input("Ingrese stock : "))
        #pasamos los datos a la función
        agregar(patente,marca,tipo,precio,stock)
    elif opcion=="2":
        printA("Listar Vehículo")
        listar(vehiculos)
    elif opcion=="3":
        printA("Eliminar Vehículo")
        patente=input("Ingrese Patente (ej: xxll22) : ").upper()
        eliminar(patente)
    elif opcion=="4":
        printA("Modificar Vehículo")
        patente=input("Ingrese Patente (ej: xxll22) : ").upper()
        marca=seleccionMarca()
        tipo=seleccionTipo()
        precio=input("Ingrese precio $: ")
        stock=input("Ingrese stock : ")
        #pasamos los datos a la función
        modificar(patente,marca,tipo,precio,stock)
    elif opcion=="5":
        printA("Filtrar Vehículo por marca")
        marca=seleccionMarca()
        filtrarporMarca(marca)
    elif opcion=="6":
        printA("Generar reporte")
        generarReporte()
    else:
        printR("OPCIÓN NO VÁLIDA")