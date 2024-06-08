class TV:
    def __init__(self) -> None:
        self.channel =1
        self.volume=1
        self.turnedOn=False

    def turnOn(self):
        self.turnedOn=True
        return self.turnedOn

    def turnOff(self):
        self.turnedOn=False
    
    def channelUp (self):
        if self.turnOn:
            if self.channel>0 and self.channel<101:
                self.channel+=1
            else:
                print('You reached to the highest number of the channels list, cant go higher :)')
        else:
            print('The TV is off, Turn it on please :) ')
        
    def channelDown(self):
        if self.turnOn:
            if self.channel>0 and self.channel<101:
                self.channel-=1
            else:
                print('You reached to the lowest number of the channels list, cant go lower :)')                
        else:
            print('The TV is off, Turn it on please :) ')

    def setChannel(self,channelNumber):
        if self.turnedOn:
            if self.channel>0 and self.channel<101:
                self.channel=channelNumber
                #print(f' selfchannel: {self.channel} Channel number: {channelNumber}')
                # return self.channel
            else:
                print('You are number channel is out of the range! re set the correct number :) ')
        else:
            print('The TV is off, Turn it on please :) ')

    def volumeUp(self):
        if self.turnOn:
            if self.volume > 0 and self.volume < 11:
                self.volume+=1
            else:
                print('The Volume reached to the maximum level :) ')
        else:
            print('The TV is off, Turn it on please :) ')

    def volumeDown (self):
        if self.turnOn:
            if self.volume > 0 and self.volume < 11:
                self.volume-=1
            else:
                print('The Volume reached to the Minimum level :) ')
        else:
            print('The TV is off, Turn it on please :) ')

