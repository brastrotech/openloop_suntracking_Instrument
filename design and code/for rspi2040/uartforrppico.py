from machine import UART
import time
#from timer import delay
# Set up UART on pins 16 (TX) and 17 (RX) at a baud rate of 115200
uart = UART(0, baudrate=115200, tx=machine.Pin(12), rx=machine.Pin(13))
print(uart)

# Read a line of data from the UART
#data = uart.readline()
execfile("fakest.py")
uart.write(f' azimuth: {azimuth}')
uart.write(f',Elevation : {elevation}')
uart.write(f' | ')

#uart.write(b"here is the data\n")
while(1==1):
 #   pass
    # Write a line of data to the UART
    execfile("fakest.py")
    #uart.write(f'{azimuth}')
    #uart.write(',')
    #uart.write(f'{elevation}')
    #uart.write("\n")
    uart.write(f'{azimuth},{elevation}')
    print(f'{azimuth},{elevation}')
    print("sent suc")
    
    time.sleep_ms(1000)
    #uart.write("When: ", when)
    #uart.write(",where: ", location)

    #Alternatively, you can use the uart object as a file-like object
    # to read and write data:
    #uart.write(b"Hello, world!\n")
#    data = uart.readline()
 #   delay(1)
    
    


