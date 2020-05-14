import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True)




def theaterChaseRainbow(pixels, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, pixels(), 3):
                pixels.setPixelColor(i+q, wheel((i+j) % 255))
            pixels.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, pixels.numPixels(), 3):
                pixels.setPixelColor(i+q, 0)


theaterChaseRainbow(pixels, Color(127, 127, 127))