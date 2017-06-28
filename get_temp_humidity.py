from PIGPIO import pigpio
pi = pigpio.pi()
import DHT22
import time
from pyfiglet import Figlet
f=Figlet(font='banner3')
s=DHT22.sensor(pi,2)
while True:
    s.trigger()
    time.sleep(10)
    nowT = time.strftime("%H:%M:%S")
    nowD = time.strftime("%m-%d-%y")
    print(chr(27)+"[2J")
    print(f.renderText('  '+nowD))
    print(f.renderText('  '+nowT))
    print("\n"*10)
    print(f.renderText('  T: {:3.0f} F'.format(s.temperature()*1.8+32)))
    print(f.renderText('  H: {:3.0f}%'.format(s.humidity()/1.)))
    print("\n"*10)
