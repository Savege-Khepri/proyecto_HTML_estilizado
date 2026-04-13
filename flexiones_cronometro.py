import time
import os
import subprocess

def alarma(minutos, archivo_audio):
    # Fase 1: Conteo (con ajuste para Python 3.12)
    segundos_totales = int(minutos * 60)
    print(f"Temporizador iniciado por {minutos} min...")
    
    for i in range(segundos_totales, 0, -1):
        m, s = divmod(i, 60)
        print(f"Faltan: {m:02d}:{s:02d}", end="\r", flush=True)
        time.sleep(1)

    print("\n¡AHORA!")

    # Fase 2: Reproducción usando comandos del sistema
    # Intentamos con 'ffplay' (viene con ffmpeg) o 'aplay'
    try:
        # -nodisp evita que abra una ventana de video, -autoexit cierra al terminar
        subprocess.run(["ffplay", "-nodisp", "-autoexit", archivo_audio])
    except FileNotFoundError:
        # Si no tienes ffplay, intentamos con el comando genérico 'xdg-open'
        os.system(f"xdg-open {archivo_audio}")

# Uso:
# alarma(1, "alarma.mp3")

repeticiones = input("Ingresa el número de series para las flexiones: ")
minutos = input("Ingresa el número de minutos para el temporizador: ")

for i in range(int(repeticiones)):
    alarma(int(minutos), "./carro_sonido.mp3")
    if i < int(repeticiones) - 1:
        print(f"Serie {i + 1} completada. Descansa un momento...\n")
    else:
        print(f"Serie {i + 1} completada. ¡Buen trabajo!\n")

    if i < int(repeticiones) - 1:    
        print(f"Faltan {int(repeticiones) - i - 1}\n")