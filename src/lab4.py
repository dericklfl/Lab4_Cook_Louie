import pyb
import task_share
import micropython
import time
import gc
import sys

micropython.alloc_emergency_exception_buf(100)

class read_pin:
    
    def __init__(self, timer):
        self.input_pin = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.IN)
        self.output_pin = pyb.Pin(pyb.Pin.board.PC1, pyb.Pin.OUT_PP)
        self.adc = pyb.ADC(self.input_pin)
        self.output_pin.low()
        s0.put(0)
        timer.callback(self.cb)

        
    def cb(self, tim):
        
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
        q0 = task_share.Queue ('L', 1000, thread_protect = False, overwrite = False,
                               name = "Queue 0")
        
        s0 = task_share.Share ('i', 1)
        
        int_timer = pyb.Timer(1, freq = 1000)
        
        my_read_pin = read_pin(int_timer)
    
