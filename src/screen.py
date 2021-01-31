#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

import miezifaces as faces

resdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'res')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

def draw_startup(gateway_ip):
    try:        
        epd = epd2in7.EPD()
        
        # Init
        logging.info('init and Clear')
        epd.init()
        epd.Clear(0xFF)
        
        # Declaring Fonts
        font24 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 24)
        font12 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 12)
        font35 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 35)
        
        # Drawing
        logging.info('Drawing...')
        himage = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(himage)
        
        # Title
        draw.text((10, 0), 'miezikatz', font=font24, fill=0)
        # Face
        draw.text((10, 40), faces.STARTUP_MIEZI1, font=font24, fill=0)
        draw.text((10, 65), faces.STARTUP_MIEZI2, font=font24, fill=0)
        draw.text((10, 90), faces.STARTUP_MIEZI3, font=font24, fill=0)
        # Explanation
        draw.text((10, 150), 'Ready for meowing! Press Button...', font=font12, fill=0)
        # Gateway IP
        draw.text((130, 30), 'Default Gateway', font=font12, fill=0)
        draw.text((130, 40), gateway_ip, font=font12, fill=0)
        draw.rectangle((125, 25, 250, 55), outline = 0)
        
        epd.display(epd.getbuffer(himage))    
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info('ctrl + c:')
        epd2in7.epdconfig.module_exit()
        exit()

def draw_scanning(gateway_ip):
    if gateway_ip == '':
        return
    
    try:        
        epd = epd2in7.EPD()
        
        # Init
        logging.info('init and Clear')
        epd.init()
        epd.Clear(0xFF)
        
        # Declaring Fonts
        font24 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 24)
        font12 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 12)
        font35 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 35)
        
        # Drawing
        logging.info('Drawing...')
        himage = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(himage)
        
        # Title
        draw.text((10, 0), 'miezikatz', font=font24, fill=0)
        # Face
        draw.text((10, 40), faces.STARTUP_MIEZI1, font=font24, fill=0)
        draw.text((10, 65), faces.STARTUP_MIEZI2, font=font24, fill=0)
        draw.text((10, 90), faces.STARTUP_MIEZI3, font=font24, fill=0)
        # Explanation
        draw.text((10, 150), 'Meowing at ' + gateway_ip + '/24', font=font12, fill=0)
        # Gateway IP
        draw.text((130, 30), 'Default Gateway', font=font12, fill=0)
        draw.text((130, 40), gateway_ip, font=font12, fill=0)
        draw.rectangle((125, 25, 250, 55), outline = 0)
        
        epd.display(epd.getbuffer(himage))    
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info('ctrl + c:')
        epd2in7.epdconfig.module_exit()
        exit()

def draw_scanned(gateway_ip, linecount):
    if gateway_ip == '':
        return
    
    try:        
        epd = epd2in7.EPD()
        
        # Init
        logging.info('init and Clear')
        epd.init()
        epd.Clear(0xFF)
        
        # Declaring Fonts
        font24 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 24)
        font12 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 12)
        font35 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 35)
        
        # Drawing
        logging.info('Drawing...')
        himage = Image.new('1', (epd.height, epd.width), 255)
        draw = ImageDraw.Draw(himage)
        
        # Title
        draw.text((10, 0), 'miezikatz', font=font24, fill=0)
        # Face
        draw.text((10, 40), faces.STARTUP_MIEZI1, font=font24, fill=0)
        draw.text((10, 65), faces.STARTUP_MIEZI2, font=font24, fill=0)
        draw.text((10, 90), faces.STARTUP_MIEZI3, font=font24, fill=0)
        # Explanation
        draw.text((10, 150), 'Finished! Maybe collected sth :3 ', font=font12, fill=0)
        # Gateway IP
        draw.text((130, 30), 'Default Gateway', font=font12, fill=0)
        draw.text((130, 40), gateway_ip, font=font12, fill=0)
        draw.rectangle((125, 25, 250, 55), outline = 0)
        # Linecount
        draw.text((130, 65), 'Wrote', font=font12, fill=0)
        draw.text((130, 75), str(linecount), font=font12, fill=0)
        draw.text((130, 85), 'lines to file', font=font12, fill=0)
        draw.rectangle((125, 60, 250, 100), outline = 0)
        
        epd.display(epd.getbuffer(himage))    
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info('ctrl + c:')
        epd2in7.epdconfig.module_exit()
        exit()

def draw_shutdown():    
    try:        
        epd = epd2in7.EPD()
        
        # Init
        logging.info('init and Clear')
        epd.init()
        epd.Clear(0xFF)
        
        # Declaring Fonts
        font18 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 18)
        font10 = ImageFont.truetype(os.path.join(resdir, 'consola.ttf'), 10)
        
        '''
        Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
        Himage2.paste(bmp, (50,10))
        epd.display(epd.getbuffer(Himage2))
        '''
        
        
        # Drawing
        logging.info('Drawing...')
        himage = Image.new('1', (epd.height, epd.width), 255)
        bmp = Image.open(os.path.join(resdir, 'sleeping_miezi.bmp'))
        draw = ImageDraw.Draw(himage)
        
        
        # Title
        draw.text((2, 2), 'Miezi tired. Zzzzz...', font=font18, fill=0)
        # Explanation
        draw.text((2, 18), '[ Don\'t wake her up :( ]', font=font10, fill=0)
        
        # Bitmap
        himage.paste(bmp, (25, 40))
        
        epd.display(epd.getbuffer(himage))
            
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info('ctrl + c:')
        epd2in7.epdconfig.module_exit()
        exit()


