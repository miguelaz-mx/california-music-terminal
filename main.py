
import pygame
import time
import os

pygame.mixer.init()

pygame.mixer.music.load("California.mp3")

MORADO = "\033[95m"
BLANCO = "\033[97m"
CIAN = "\033[96m"
RESET = "\033[0m"

#The numbers represent the seconds in the song where the lyrics appear.
letra = [
    (5, "California, en tu piel"),
    (11, "Estás sola como ayer"),
    (17, "No será tan fácil olvidar"),
    (23, "Que eras tú, siempre fuiste tú"),

    (37, "Amor, es tan corto el cariño"),
    (45, "Pero mi amor es tan largo el olvido"),
    (53, "Corazón, te olvido en la mañana"),

    (72, "California, te lloré"),
    (79, "En las olas te olvidé"),
    (86, "No será tan fácil olvidar"),
    (93, "Que eras tú, siempre fuiste tú"),

    (110, "Amor, es tan corto el cariño"),
    (118, "Pero mi amor es tan largo el olvido"),
    (126, "Corazón, te olvido en la mañana"),

    (145, "Amor, es tan corto el cariño"),
    (153, "Pero mi amor es tan largo el olvido"),
    (161, "Corazón, te olvido en la mañana"),
    (169, "California"),
    (176, "California")
]

os.system("clear")

print(MORADO + "♫ CALIFORNIA - MUSIC PLAYER ♫" + RESET)
print(CIAN + "================================" + RESET)
print(BLANCO + "Reproduciendo California.mp3..." + RESET)
print()

pygame.mixer.music.play()

inicio = time.monotonic()

indice = 0

while pygame.mixer.music.get_busy():

    tiempo = time.monotonic() - inicio

    if indice < len(letra):

        momento, texto = letra[indice]

        if tiempo >= momento:

            print(MORADO + "" + BLANCO + texto + RESET)
            indice += 1

    time.sleep(0.05)

print()
print(CIAN + " Canción terminada " + RESET)

pygame.mixer.quit()

#.. / .-.. --- ...- . / -.-- --- ..- / .- -.. .-. .. .- -. .-
