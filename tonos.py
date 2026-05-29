import winsound
import time

print("Sintetizador de microtonos")
maximo_microtonos = 50
microtonos_libres = 50
microtonos_activos = 0
ejecutando  = True

while ejecutando:
    print("Panel")
    print("1-. Ver cuantos microtonos quedan libres")
    print("2-. Activar microtonos")
    print("3-. Devolver los microtonos")
    print("4-. Monitorear el estado actual de los microtonos")
    print("5-. Salir")
    opcion = float(input("Elije una opción: "))
    
    if opcion == 1:
        print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponibles para usar")
    elif opcion == 2:
        if microtonos_libres == 0:
            print("No tienes más microtonos disponibles")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quiere usar?: \n"))
                if cantidad <= 0:
                    print("Error! Tienes que activar a lo menos 1 microtono")
                elif cantidad > microtonos_libres:
                    print(f"No hay tantos microtonos, máximo disponible {microtonos_libres}")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    #for i in range(1, cantidad + 1):
                    #    print(f"Microtono {i} activado...")
                    #    winsound.Beep(440, 300)
                    #    time.sleep(0.2)
                    cancion = [
                        (311,250), (311,250),(311,500),
                        (311,250), (311,250),(311,500),
                        (311,250), (370,250),(277,250),(293,250),
                        (311,1000),
                        (320,250),(320,250),(320,250),(320,250),
                        (320,250),(311,250),(311,250),(311,125),(311,125),
                        (311,250),(293,250),(293,250),(311,255),
                        (277,500),(429,500)
                    ]
                    for i in range(len(cancion)):
                        frecuencia = cancion[i][0]
                        duracion = cancion[i][1]
                        winsound.Beep(frecuencia, duracion)
                        time.sleep(0.05)
            except ValueError:
                print("Error")
    else:
        print("Error")

       
