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
        GPIO.setup((B_HIGH, B_LOW, D_LEFT, D_RIGHT, B_LEFT, D_CENTER, D_DOWN, D_UP), GPIO.OUT)

        self.currentChannel = 0
        f = open("/currentChannel", "r")
        self.currentChannel = int(f.readline())
        f.close()

    def getCurrentChannel(self):
        Remote.getCurrentChannel(self)
        return self.currentChannel

    def pressButton(number):
        print "GPIORemote: pressButton:", number
        import RPi.GPIO as GPIO
        GPIO.output(number, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(number, GPIO.LOW)
        time.sleep(0.1)

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
        Remote.pressFronRight(self)
        self.pressButton(GPIORemote.D_RIGHT)

    def pressBackLeft(self):
        Remote.pressBackLeft(self)
        self.pressButton(GPIORemote.B_LEFT)

    def pressFrontCenter(self):
        Remote.pressFrontCenter(self)
        self.pressButton(GPIORemote.D_CENTER)

    def pressFrontDown(self):
        Remote.pressFrontDown(self)
        self.pressButton(GPIORemote.D_CENTER)

    def pressFrontUp(self):
        Remote.pressFrontUp(self)
        self.pressButton(GPIORemote.D_UP)

