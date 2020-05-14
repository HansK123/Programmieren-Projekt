import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 12, brightness=0.1, auto_write=True)




def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


theaterChaseRainbow(strip, Color(127, 127, 127))