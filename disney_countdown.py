#!/usr/bin/env python

import colorsys
import signal
import time
import datetime
from sys import exit
from PIL import Image, ImageDraw, ImageFont
import unicornhathd

day_of_trip = 27
month_of_trip = 10
year_of_trip = 2017

time_until = datetime.datetime(year_of_trip, month_of_trip, day_of_trip) - datetime.datetime.now()

TEXT = str((time_until.days+1)) + " DAYS TO GO"

FONT = ("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 12)

unicornhathd.rotation(90)
unicornhathd.brightness(1)

width, height = unicornhathd.get_shape()

img = Image.open('mickey.png')

text_x = width
text_y = 2

font_file, font_size = FONT

font = ImageFont.truetype(font_file, font_size)

text_width, text_height = font.getsize(TEXT)

text_width += width + text_x + 32

image = Image.new("RGB", ((text_width),max(16, text_height)), (0,0,0))
draw = ImageDraw.Draw(image)

draw.bitmap((text_x, 0), img) 
draw.text(((text_x*2), text_y), TEXT, fill=(255, 255, 255), font=font)
draw.bitmap(((text_width-(text_x*2)), 0), img)

try:
    while True:        
        for scroll in range(text_width - width):
            for x in range(width):
                for y in range(height):
                    pixel = image.getpixel((x+scroll, y))

                    br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb((x + scroll) / float(text_width), 1.0, 1.0)]
                    r, g, b = [float(n / 255.0) for n in pixel]
                    r = int(br * r)
                    g = int(bg * g)
                    b = int(bb * b)

                    unicornhathd.set_pixel(width-1-x, y, r, g, b)

            unicornhathd.show()
            time.sleep(0.01)

except KeyboardInterrupt:
    unicornhathd.off()
