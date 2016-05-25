try:
    import RPi.GPIO as GPIO
    from GPIORemote import GPIORemote
    #RPi usable, use GPIO Remote
    remote = GPIORemote()
except:
    #No RPI Usable, use Remote without functionality
    from Remote import Remote
    remote = Remote()