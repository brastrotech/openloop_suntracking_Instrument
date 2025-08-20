from machine import Pin, UART, SoftI2C

import utime, time
gpsModule = UART(1, baudrate=9600)
print(gpsModule)
buff = bytearray(255)

TIMEOUT = False
FIX_STATUS = False
latitude = ""
longitude = ""
satellites = ""
GPStime = ""
h = ""
m = ""
s = ""

def getGPS(gpsModule):
    global FIX_STATUS, TIMEOUT, latitude, longitude, satellites, GPStime
    
    timeout = time.time() + 8
    #gpsModule.readline()
    #buff = str(gpsModule.readline())
    #print(buff)
    
    while True:
        gpsModule.readline()
        buff = str(gpsModule.readline())
        #print(buff) #debug
        parts = buff.split(',')
        
    
        if (parts[0] == "b'$GPGGA" and len(parts) == 15):
            if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):
                print(buff)
                
                latitude = convertToDegree(parts[2])
                if (parts[3] == 'S'):
                    latitude = -latitude
                longitude = convertToDegree(parts[4])
                if (parts[5] == 'W'):
                    longitude = -longitude
                satellites = parts[7]
                h = print(parts[1][0:2])
                m = print(parts[1][2:4])
                s = print(parts[1][4:6])
                GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
                GPStime = "15:43:54"
                FIX_STATUS = True
                break
                
        if (time.time() > timeout):
            TIMEOUT = True
            break
        utime.sleep_ms(1000)

def convertToDegree(RawDegrees):
    

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) 
    nexttwodigits = RawAsFloat - float(firstdigits*100) 
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) 
    return str(Converted)
i=0
while i==0:
    i = i+1
    getGPS(gpsModule)

    if(FIX_STATUS == True):
        print("Printing GPS data...")
        print(" ")
        print("Latitude: "+latitude)
        print("Longitude: "+longitude)
        print("Satellites: " +satellites)
        print("Time: "+GPStime)
        print("h"+h)
        print("m"+m)
        print("s"+s)
        print("----------------------")
        
        
       
        
        FIX_STATUS = False
        
    #if(TIMEOUT == True):
      #  print("No GPS data is found.")
       # TIMEOUT = False
latitude = "22.5994"
longitude = "72.8205"
satellites = "07"
GPStime = "11:59:54"
parts = GPStime.split(":",2)

h = parts[0]
m = parts[1]
s = parts[2]


