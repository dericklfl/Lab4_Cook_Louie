'''! @file      serialplot.py
                This file runs a step response on the RC circuit through serial when a key is pressed.
                It then reads and parses the data and plots time versus voltage.
    @author     Michael Cook
    @author     Derick Louie
    @date       February 14, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import serial
from matplotlib import pyplot

## List of voltages from ADC
volt_list = []


# List of times
time_list = [*range(1,4995,5)]
runs = 0

with serial.Serial ('COM8', 115200) as s_port:
    while True:
        if input():
            s_port.write(b'A\r')
        
        while True:
            
            if(s_port.readline() == b'End\r\n'):
                break
            
            ## List of length 2 that stores the time and position values
            data = s_port.readline()
            runs += 1
            print(runs,",",data)
            
            try:
            
                ## Time converted to a string
                volt_string = str(data, 'ascii')
                
                ## Time converted to a float
                volt_float = float(volt_string)
                
                volt_list.append(volt_float)

            
            except:
                pass
        print("out of loop")
        print(volt_list)
        
        pyplot.plot(time_list, volt_list)
        pyplot.ylabel("Voltage [mV]")
        pyplot.xlabel("Time [ms]")
        pyplot.show()
        
