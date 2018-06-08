#!/usr/bin/env python
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



wlan0 = get_addr('wlan0')
eth0 = get_addr('eth0')
host = socket.gethostname()


lcd.clear()

lcd.set_cursor_position(0,0)
lcd.write('{}'.format(host))

lcd.set_cursor_position(0,1)
if eth0 == 'Not Found!':
    lcd.write('eth0 DOWN')
else:
    lcd.write(format(eth0))

nethost = 'www.google.com'

def DNSCHECK(DNS):
        response = os.system('ping -c 1 ' + DNS)
        lcd.set_cursor_position(0,2)
        if response == 0:
                lcd.write('DNS is UP')
                backlight.rgb(50,255,50)
                time.sleep(10)
        else:
                netping = os.system('ping -c 1 ' + nethost)
                if netping == 0:
                        backlight.rgb(255,255,0)
                        lcd.write('DNS is DOWN')
                else:
                        backlight.rgb(255,0,0)
                        lcd.write('Network DOWN')
#       except:
#               lcd.write('DNS CHECK FAILURE')
#               backlight.sweep(hue, 0)


while True:
        lcd.clear()

        lcd.set_cursor_position(0,0)
        lcd.write('{}'.format(host))
		
		eth0 = get_addr('eth0')
        lcd.set_cursor_position(0,1)
        if eth0 == 'Not Found!':
                lcd.write('eth0 DOWN')
        else:
                lcd.write(format(eth0))


        DNSCHECK('192.168.0.xx')
        time.sleep(10)
