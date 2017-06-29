from PIGPIO import pigpio
from colorama import init
init()
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
    print(Fore.GREEN + f.renderText('  '+nowD))
    print(Fore.GREEN + f.renderText('  '+nowT))
    print("\n"*10)
    print(Fore.YELLOW + f.renderText('  T: {:3.0f} F'.format(s.temperature()*1.8+32)))
    print(Fore.CYAN + f.renderText('  H: {:3.0f}%'.format(s.humidity()/1.)))
    print("\n"*10)
