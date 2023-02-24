import backend
import interface
import control

def main():
    _backend = backend.GPIO()
    _backend.use_pi2()
    _interface = interface.Interface(_backend)
    controller = control.Control(_interface)
    #controller.set_pll(10)
    #controller.set_frequency_1(7132000)
    _backend.set_register(0x20, 0)
    controller.set_frequency_1(100000)
    controller.set_frequency_2(100000)
    _backend.print_registers()
    while (True):
        try:
            newFreq = float(input('Enter Frequency in Khz\n'))
            newFreq = int(newFreq * 1000)
            controller.set_frequency_1(newFreq)
        except ValueError:
            print("Not a number")
    
main()
