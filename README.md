# Lab 4: First Order RC Step Response with Interrupts

This lab utilizes interrupt callbacks to read data from the ADC after outputting voltage high to a first order RC circuit.
The ADC values are sent through serial to plot the step response of the circuit.
The RC circuit consists of a 3.3uF capacitor to ground, a 100k resistor to the input and two 2.5k resistors to the output.
The calcutated RC value of this first order circuit is 0.33, equaling an expected time constant of 330ms.

---

### Step Response of RC Circuit

![RCStepResonse](/docs/plot.png)

This is the step response obtained when the input of the RC circuit is driven high.
To find the measured RC value of this circuit, the time is recorded at the point where V(t) = 0.63*Vmax = 2448mV. This gives us the time value at 1 time constant = RC.

The measured value for RC is about 352ms.

---
### Comparison of Expected vs Measured RC

The measured time constant of 352ms is roughly 6.7% higher than the expected/calculated value of 330ms. This is within the expected variance of 5% to 25%.
One likely reason for the small error is that the capacitor value may be slightly above or below the stated 3.3uF.

---
