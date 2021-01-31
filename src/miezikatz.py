#!/usr/bin/env python3

import sys, os
from datetime import datetime

import screen
import networking
from gpiozero import Button
from signal import pause

cwd = os.getcwd()

gateway_ip = ''

button_1 = Button(5)
button_2 = Button(6)
button_3 = Button(13)
button_4 = Button(19)

def scan_sy():
    screen.draw_scanning(gateway_ip)
    
    now = datetime.now()
    
    output_file_name = now.strftime("%d-%m-%Y-%H:%M:%S") + '.txt'
    exec_string = 'sudo nmap -sY ' + gateway_ip + '/24 -oN scans/' + output_file_name

    os.system(exec_string)
    
    linecount = len(open(os.path.join(cwd, 'scans/') + output_file_name).readlines())
    screen.draw_scanned(gateway_ip, linecount)

def shutdown():
    screen.draw_shutdown()
    exit()
    

if __name__ == '__main__':
    gateway_ip = networking.get_default_gateway()
    
    screen.draw_startup(gateway_ip)
    
    while True:
        button_1.when_pressed = scan_sy
        button_4.when_pressed = shutdown
        
        pause()
        
    
    
    
