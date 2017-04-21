# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/temperature-2017-04-22-00-23-32.py"

from sense_emu import SenseHat
import os

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

# Mensaje
enviadoInf = 1
enviadoSup = 0
limiteSuperior = 30
limiteInferior = 25

while True:
    temp = sense.temp
    pixels = [red if i < temp else blue for i in range(64)]
    sense.set_pixels(pixels)

    if temp > limiteSuperior and enviadoSup == 0:
        enviadoInf = 0
        enviadoSup = 1
        os.system('/home/pi/Desktop/enviaMsjHangout.sh' + " 'La temperatura ha superado los " + str(limiteSuperior) + "ºC '")
    elif temp < limiteInferior and enviadoInf == 0:
        enviadoInf = 1
        enviadoSup = 0
        os.system('/home/pi/Desktop/enviaMsjHangout.sh' + " 'La temperatura ya ha bajado de los " + str(limiteInferior) + "ºC '")
        
        
