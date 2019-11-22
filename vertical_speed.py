import time, winsound
from tkinter import *

descent = int(input("VERT SPEED: "))

for i in range(1000, 0, descent):
    if i == 1000:
        print(i)
        winsound.PlaySound("cal/1000ft.wav", winsound.SND_FILENAME)


    elif i == 500:
        print(i)
        winsound.PlaySound("cal/500ft.wav", winsound.SND_FILENAME)


    elif i == 400:
        print(i)
        winsound.PlaySound("cal/400ft.wav", winsound.SND_FILENAME)


    elif i == 300:
        print(i)
        winsound.PlaySound("cal/300ft.wav", winsound.SND_FILENAME)


    elif i == 200:
        print(i)
        winsound.PlaySound("cal/200ft.wav", winsound.SND_FILENAME)


    elif i == 100:
        print(i)
        winsound.PlaySound("cal/100ft.wav", winsound.SND_FILENAME)


    elif i == 50:
        print(i)
        winsound.PlaySound("cal/50ft.wav", winsound.SND_FILENAME)


    elif i == 40:
        print(i)
        winsound.PlaySound("cal/40ft.wav", winsound.SND_FILENAME)


    elif i == 30:
        print(i)
        winsound.PlaySound("cal/30ft.wav", winsound.SND_FILENAME)


    elif i == 20:
        print(i)
        winsound.PlaySound("cal/20ft.wav", winsound.SND_FILENAME)


    elif i == 10:
        print(i)
        winsound.PlaySound("cal/10ft.wav", winsound.SND_FILENAME)
        print("Landed")


