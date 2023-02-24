import backend
import interface
import control

def main():
    _backend = backend.GPIO()
    _backend.use_pi2()
    _interface = interface.Interface(_backend)
    controller = control.Control(_interface)
    controller.set_pll(10)
    controller.set_osk(0)
    controller.set_frequency_1(7132000)
    while (True):
        try:
            newFreq = float(input('Enter Frequency in Khz\n'))
            newFreq = int(newFreq * 1000)
            controller.set_frequency_1(newFreq)
        except ValueError:
            print("Not a number")
    
main()
