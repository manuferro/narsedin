#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
sys.path.append('/home/narsedin/sensirion/sht21_python')
import sht21
import espeak


from espeak import espeak
espeak.set_voice("it")
espeak.set_parameter(espeak.Parameter.Pitch, 20)
espeak.set_parameter(espeak.Parameter.Rate, 130)
espeak.set_parameter(espeak.Parameter.Range, 500)
#espeak.pitch = 10

print("TEST sh21 170415")

tmp=0.0
hum=0.0
ore=time.strftime('%H')
min=time.strftime('%M')
vore=""
vmin=""
hinit="Sono le"
print("ORE: " + time.strftime('%H')) 



if ore=="12":
    vore = "mezzogiorno"
    hinit="è"
elif ore=="13":
    vore = "L'una"
    hinit="è"
elif ore=="00":
    vore = "mezzanotte"
    hinit="è"
else:
    vore=str(int(ore))
    
if min=="00":
    vmin = "in punto"
elif min=="30":
    vmin = "e mezza"
    if ore=="12":
        vmin = "e mezzo"
else:
    vmin= "e "  +  str(int(min))


espeak.synth(hinit + " "+vore + " " + vmin + ".")

with sht21.SHT21(0) as sht21:
    print "Temperature: %s"%sht21.read_temperature()
    print "Humidity: %s"%sht21.read_humidity()
    tmp=round(sht21.read_temperature(), 1)
    hum=int(round(sht21.read_humidity(),0))
#    espeak.synth("Sono " + str(tmp) + " gradi centigradi e " + str(hum) + " percento di umidità relativa.")
    

#espeak.synth("Dlin dlon Dlin Dlon, qualche rompicazzo sta suonando alla porta")

#while espeak.is_playing:
#    time.sleep(0.1)

time.sleep(5)

print("ciao ancora")
    
