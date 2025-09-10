import L1_ina as voltRead
import L1_log as fileLog
from time import sleep

def getVoltage():
    myBatt = voltRead.readVolts()                            # collect a reading
    return myBatt

## Only runs if __name__ is __main__, indicating the script was executed directly ##
if __name__ == "__main__":
    while True:
        sleep(1)                
        batt_voltage = getVoltage()
        #volt_str = "Robot Voltage: %.2fV" % batt_voltage
        fileLog.tmpFile(batt_voltage, "Batt_Log.txt")
