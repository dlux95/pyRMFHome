from application.rmflib.remotes.Remote import Remote
import time


class GPIORemote(Remote):
    B_HIGH          = 18
    B_LOW           = 22
    D_LEFT          = 24
    D_RIGHT         = 26
    B_LEFT          = 32
    D_CENTER        = 36
    D_DOWN          = 38
    D_UP            = 40

    def __init__(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((GPIORemote.B_HIGH, GPIORemote.B_LOW, GPIORemote.D_LEFT, GPIORemote.D_RIGHT, GPIORemote.B_LEFT, GPIORemote.D_CENTER, GPIORemote.D_DOWN, GPIORemote.D_UP), GPIO.OUT)

        self.currentChannel = 0
        f = open("/currentChannel", "r")
        self.setCurrentChannel(int(f.readline()))
        f.close()

    def setCurrentChannel(self, channel):
        Remote.setCurrentChannel(self, channel)

    def pressButton(self, number):
        print "GPIORemote: pressButton:", number
        import RPi.GPIO as GPIO
        GPIO.output(number, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(number, GPIO.LOW)
        time.sleep(0.2)

    def pressBackHigh(self):
        Remote.pressBackHigh(self)
        self.pressButton(GPIORemote.B_HIGH)

    def pressBackLow(self):
        Remote.pressBackLow(self)
        self.pressButton(GPIORemote.B_LOW)

    def pressFrontLeft(self):
        Remote.pressFrontLeft(self)
        self.pressButton(GPIORemote.D_LEFT)

    def pressFrontRight(self):
        Remote.pressFrontRight(self)
        self.pressButton(GPIORemote.D_RIGHT)

    def pressBackLeft(self):
        Remote.pressBackLeft(self)
        self.pressButton(GPIORemote.B_LEFT)

    def pressFrontCenter(self):
        Remote.pressFrontCenter(self)
        self.pressButton(GPIORemote.D_CENTER)

    def pressFrontDown(self):
        Remote.pressFrontDown(self)
        self.pressButton(GPIORemote.D_DOWN)

    def pressFrontUp(self):
        Remote.pressFrontUp(self)
        self.pressButton(GPIORemote.D_UP)

