class Remote(object):
    def __init__(self):
        self.currentChannel = 0;

    def pressBackHigh(self):
        print "Remote: pressBackHigh"
        pass

    def pressBackLow(self):
        print "Remote: pressBackLow"
        pass

    def pressFrontLeft(self):
        print "Remote: pressFrontLeft"
        pass

    def pressFrontRight(self):
        print "Remote: pressFrontRight"
        pass

    def pressFrontCenter(self):
        print "Remote: pressFrontCenter"
        pass

    def pressBackLeft(self):
        print "Remote: pressBackLeft"
        pass

    def pressFrontDown(self):
        print "Remote: pressFrontDown"
        pass

    def pressFrontUp(self):
        print "Remote: pressFrontUp"
        pass

    def getCurrentChannel(self):
        print "Remote: getCurrentChannel"
        return self.currentChannel

    def setCurrentChannel(self, channel):
        print "Remote: setCurrentChannel", channel
