import winsound
import time

print("Sintetizador de microtonos")
maximo_microtonos = 50
microtonos_libres = 50
microtonos_activos = 0
ejecutando = True

while ejecutando:
    print("\n === Panel de microtonos ===")
    print("1-. Ver cuantos microtonos quedan libres")
    print("2-. Activar microtonos")
    print("3-. Devolver los microtonos")
    print("4-. Monitorear el estado actual")
    print("5-. Salir")
    
    try:
        opcion = int(input("Elije una opción: "))
        
        if opcion == 1:
            print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponibles.")
            
        elif opcion == 2:
            if microtonos_libres == 0:
                print("No tienes más microtonos disponibles.")
            else:
                cantidad = int(input("¿Cuántos microtonos quiere usar?: "))
                if cantidad <= 0:
                    print("Error! Debes activar al menos 1.")
                elif cantidad > microtonos_libres:
                    print(f"No hay suficientes. Máximo: {microtonos_libres}")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    print(f"Activando {cantidad} microtonos...")
                    
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
                    for freq, dur in cancion:
                        winsound.Beep(freq, dur)
                        time.sleep(0.05)
                        
        elif opcion == 3:
            microtonos_libres = maximo_microtonos
            microtonos_activos = 0
            print("\n[OK] Todos los microtonos han sido devueltos.")
            
        elif opcion == 4:
            print(f"\n--- ESTADO ---")
            print(f"Activos: {microtonos_activos}")
            print(f"Libres:  {microtonos_libres}")
            
        elif opcion == 5:
            print("Saliendo del sintetizador...")
            ejecutando = False
            
        else:
            print("Opción no válida. Intenta del 1 al 5.")
            
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

       