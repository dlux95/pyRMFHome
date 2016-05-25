try:
    import RPi.GPIO as GPIO
    from GPIORemote import GPIORemote
    #RPi usable, use GPIO Remote
    remote = GPIORemote()
    print "Using GPIO Remote"
except Exception as e:
    print e
    #No RPI Usable, use Remote without functionality
    from Remote import Remote
    remote = Remote()
    print "Using Debug Remote"