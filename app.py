import backend
import interface
import control
import time

def main():
    _backend = backend.GPIO()
    _backend.autoconfigure()
    _interface = interface.Interface(_backend)
    controller = control.Control(_interface)
    controller.set_ppm(10)
    controller.set_pll(10)
    controller.set_bypass_inv_sinc(1)
    #controller.set_internal_update(0)
    controller.set_osk(0)
    #controller.set_frequency_1(1000)
    #controller.set_frequency_1(3550000)
    controller.set_frequency_1(7132000)
    #_backend.print_registers()

    debug_print = True
    while (debug_print):
        time.sleep(3000)
        _backend.print_registers()

    while (True):
        try:
            newFreq = float(input('Enter Frequency in Khz\n'))
            newFreq = int(newFreq * 1000)
            controller.set_frequency_1(newFreq)
        except ValueError:
            print("Not a number")
    
main()
