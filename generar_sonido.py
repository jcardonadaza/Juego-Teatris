import numpy as np
import wave

def generar_tono(nombre_archivo, frecuencia, duracion_ms):
    framerate = 44100
    duracion = duracion_ms / 1000
    t = np.linspace(0, duracion, int(framerate * duracion))
    tono = (np.sin(2 * np.pi * frecuencia * t) * 32767).astype(np.int16)
    with wave.open(nombre_archivo, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(framerate)
        f.writeframes(tono.tobytes())

# Crear carpeta sonidos si no existe
import os
os.makedirs("sonidos", exist_ok=True)

# Generar sonidos
generar_tono("sonidos/linea.wav", frecuencia=880, duracion_ms=150)
generar_tono("sonidos/gameover.wav", frecuencia=220, duracion_ms=600)