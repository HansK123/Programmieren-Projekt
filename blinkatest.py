import board
import neopixel
import time
pixels = neopixel.NeoPixel(board.D18, 30)
Ansgar=3
pixels[Ansgar]=((255,255,0))
time.sleep(5)
pixels.fill((0,0,0))
Ansgar=Ansgar+1
pixels[Ansgar]=((255,0,0))
time.sleep(5)

pixels.fill((0,0,0))
