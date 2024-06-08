from tv import TV
# import time as tm
myTv=TV()
print('The statue of the TV is : ',myTv.turnedOn)
myTv.turnOn()
print('The statue of the TV is : ',myTv.turnedOn)
print('Current channel: ',myTv.channel)
myTv.setChannel(5) 
print('Current channel: ',myTv.channel)
#tm.sleep(2)
i=0
while i<16:
    myTv.volumeUp()
    print('Volume level: ',myTv.volume)
    i+=1
myTv.turnOff()
print('The statue of the TV is : ',myTv.turnedOn)
myTv.turnOn()
print(myTv.turnedOn)
myTv.setChannel(95)
print('Current channel: ',myTv.channel)
myTv.setChannel(105)
print('Current channel: ',myTv.channel)
print('Volume level: ',myTv.volume)
j=0
while j<2:
    myTv.volumeDown()
    print('Volume level: ',myTv.volume)
    j+=1

# print(myTv.channel)
# myTv.volumeUp # the virtual volume is 1 so we ll repeat this command 6 times!
# print(myTv.volumeUp())