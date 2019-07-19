import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 30)
Ansgar=3
pixels[3]((0,255,0))
time.sleep(10)
pixels.fill((0,0,0))
