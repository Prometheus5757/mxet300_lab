import L2_compass_heading as compassLib
import L1_log as fileLog
from time import sleep

def getHeading():
    heading = compassLib.get_heading()
    return heading

def calculateDirection(heading):
    direction = ""
    if(-22.5 >= heading and heading > -67.5):
        direction = "Northwest"
    elif(-67.5 >= heading and heading > -112.5):
        direction = "West"
    elif(-112.5 >= heading and heading > -157.5):
        direction = "Southwest"
    elif(157.5 <= abs(heading) and abs(heading) <= 180):
        direction = "South"
    elif(112.5 <= heading and heading < 157.5):
        direction = "Southeast"
    elif(67.5 <= heading and heading < 112.5):
        direction = "East"
    elif(22.5 <= heading and heading < 67.5):
        direction = "Northeast"
    elif(-22.5 <= heading and heading < 22.5):
        direction = "North"
    else:
        direction = "N/A"
    return direction

## Only runs if __name__ is __main__, indicating the script was executed directly ##
if __name__ == "__main__":
    while True:
        sleep(0.1)
        live_heading = getHeading() 
        direction = calculateDirection(live_heading)               
        print(round(live_heading,2), " ", direction)
        fileLog.tmpFile(live_heading, "Compass_Log.txt")
        fileLog.stringTmpFile(direction, "Direction_Log.txt")