from machine import PWM
from machine import Pin

#Klasse Led zur Ansteurung der LEDs
class Led:
    #nimmt die pin ID an und erzeugt das PWM Objekt
    def __init__(self, pin):
        self.pin = pin
        
        self.pinLED = Pin(self.pin, Pin.OUT)
        
        self.LED = PWM(self.pinLED)
        
        self.LED.duty_u16(0)
        self.LED.freq(5000)
    
    #stellt die Helligkeit der LEDs ein
    def ledBrightness(self, value):
        self.LED.duty_u16(int(value))
        #self.brightness = value
    
    #Wechselt zwischen an und aus
    def ledCycle(self):
        self.LED.duty_u16(abs(self.LEDLinks.duty_u16()-65000))
    
    #schaltet die LED aus
    def ledOff(self):
        self.LED.duty_u16(0)
    
    #schaltet die LED ein
    def ledOn(self):
        self.LED.duty_u16(65000)