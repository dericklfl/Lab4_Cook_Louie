'''! @file      lab4.py
                This program uses the ADC on the Nucleo and an interrupt running at 1 kHz to record and print the results of a step response on a RC circuit.
    @author     Michael Cook
    @author     Derick Louie
    @date       February 14, 2022
    @copyright  (c) 2022 by Michael Cook, Derick Louie, and released under GNU Public License v3
'''

import pyb
import task_share
import micropython
import time
import gc
import sys

micropython.alloc_emergency_exception_buf(100)

class read_pin:
    '''! 
    This class reads the pin using the ADC and prints the value using an interrupt.
    '''
    def __init__(self, timer):
        '''! 
        Initializes GPIO pins, creates ADC object, and sets the output pin to low.
        @param timer Timer pin used for interrupt
        '''
        
        ## Input pin variable
        
        self.input_pin = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.IN)
        
        ## Output pin variable
        self.output_pin = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
        
        ## ADC to read input pin value
        self.adc = pyb.ADC(self.input_pin)
        self.output_pin.low()
        timer.callback(self.cb)

        
    def cb(self, tim):
        '''! 
        This function reads values from the ADC and puts them in queue.
        Once the queue is full, the values are printed to serial.
        @param tim Timer used for interrupt
        '''
        
        if not q0.full():
            time.sleep_ms(5)
            self.output_pin.high()
            q0.put(self.adc.read(), in_ISR = True)
        
        else:
            int_timer.deinit()
            
            while q0.num_in() > 0:
                print(q0.get())
                print("test")
                
            if q0.num_in() == 0:
                print("End")
                print("End")
                self.output_pin.low()

        
if __name__ == '__main__':
    
    if input():
        
        ## Queue to store ADC values
        
        q0 = task_share.Queue ('L', 1000, thread_protect = False, overwrite = False,
                               name = "Queue 0")
        
        ## Timer for interrupt
        
        int_timer = pyb.Timer(1, freq = 1000)
        
        ## read_pin object 
        
        my_read_pin = read_pin(int_timer)
    
