import os
import time
import fcntl
import socket
import struct
import dothat.lcd as lcd
import dothat.backlight as backlight

def get_addr(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return 'Not Found!'

#def ping(ip_addr):
#       try:
#               ping.verbose_ping('192.168.0.15'), count=3)
#               upstate = 'DNS is Up @NeroPi'
#       except socket.error, e:
#               upstate = 'DNS FAILURE', e

wlan0 = get_addr('wlan0')
eth0 = get_addr('eth0')
host = socket.gethostname()


lcd.clear()

lcd.set_cursor_position(0,0)
lcd.write('{}'.format(host))

lcd.set_cursor_position(0,1)
if eth0 != 'Not Found!':
    lcd.write(eth0)
else:
    lcd.write('eth0 {}'.format(eth0))


hostname = 'www.google.co.uk'
response = os.system('ping -c 1 ' + hostname)

lcd.set_cursor_position(0,2)
while True:
        if response == 0:
                lcd.write('DNS is UP')
                backlight.rgb(50,255,50)
                time.sleep(10)
                response = os.system('ping -c 1 ' + hostname)
                lcd.set_cursor_position(0,2)
        elif response != 0:
                lcd.write('DNS is DOWN')
                backlight.rgb(255,50,50)
                time.sleep(05)
                response = os.system('ping -c 1 ' + hostname)
                lcd.set_cursor_position(0,2)
        else:
                lcd.write('Error')
                exit(0)






