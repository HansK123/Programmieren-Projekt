import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30)
Ansgar=3
pixels.fill(0,0,0)
pixels[Ansgar]=((255,0,0))
