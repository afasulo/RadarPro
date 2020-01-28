## Stalker Manual
Notes from the [Stalker Pro II reference manual](https://www.stalkerradar.com/pdf/011-0093-00%20Stalker%AE%20Pro%20II%20owner%27s%20manual%20Rev%20C.pdf)
#### Hardware
* if a 9-pin D serial extender cable is required, use a standard (straight-through) computer cable, NOT a null-modem cable which crosses the transmit and receive signals. 

#### Implementation Methods
* The radar measures speed data at a rate of just over 46 readings per second, and it sends speed data messages out its serial port at that same rate.
* 9600 8-N-1 (8 data bits, no parity and 1 stop bit)