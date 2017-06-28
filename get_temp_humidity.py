from PIGPIO import pigpio
pi = pigpio.pi()
import DHT22
import time
s=DHT22.sensor(pi,2)
while True:
    s.trigger()
    time.sleep(10)
    now = time.strftime("%c")
    print('Temperature: {:3.2f} F'.format(s.temperature()*1.8+32)+', Humidity: {:3.2f}%'.format(s.humidity()/1.)+' on '+now)
