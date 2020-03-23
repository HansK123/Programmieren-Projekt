import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 12)

pixels[0] = (100, 0, 0)