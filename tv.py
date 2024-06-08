class TV:
    def __init__(self) -> None:
        self.channel=1
        self.volume=1
        self.turnedOn=False

    def turnOn(self):
        self.turnedOn=True

    def turnOff(self):
        self.turnedOn=False

    def channelUp (self):
        if self.turnOn:
            if self.channel==100:
                print('You reached to the last channel, no more chaneel, you could go back down :) ')
            else:
                self.channel+=1
        else:
            print('Turn on the Tv first please :)')

    def channelDown(self):
        if self.turnOn:
            if self.channel==1:
                print('You reached to the first channel, no more down, you could go back up :)')
            else:
                self.channel-=1
        else:
            print('Turn on the Tv first please :)')

    def setChannel (self,number):
        if self.turnOn:
            if number>0 and number<101:
                self.channel=number
            else:
                print('You put number outside of the range! chose number between 1 and 100 :)')
        else:
            print('Turn on the Tv first please :)')

    def volumeUp (self):
        if self.turnOn:
            if self.volume==10:
                print('Maximum volume :)')
            else:
                self.volume+=1
        else:
            print('Turn on the Tv first please :)')

    def volumeDown (self):
        if self.turnOn:
            if self.volume==1:
                print('Minimum volume :) ')
            else:
                self.volume-=1
        

        