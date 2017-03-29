import serial

#specifying the serial port and bnd rate begin used by the arduino
arduinoSerialData = serial.Serial('com5', 9600)

#We need to receive the data all the time
while (1==1):
    
    #waiting to see if there is data from arduino
    if (arduinoSerialData.inWaiting()>0):

        #Reading the available data and decoding it into standard characters
        myData = arduinoSerialData.readline().decode("utf-8")
        print(myData)
