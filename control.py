import interface
import controlregister


class Control:
    def __init__(self, newinterface: interface.Interface):
        self.interface = newinterface
        self.controlregister = controlregister.ControlRegister()
        self.pll = 1

    def set_pll(self, value):
        self.pll = value
        if (value == 1):
            self.controlregister.bypass_pll = 1
            self.controlregister.pll_multiplier = 4
        else:
            self.controlregister.bypass_pll = 0
            self.controlregister.pll_multiplier = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)

    # Input 0-1 0-360 deg
    def set_phase_1(self, value):
        self.interface.set_phase_adjust_1(int(value * 8192))

    def set_phase_2(self, value):
        self.interface.set_phase_adjust_2(int(value * 8192))

    def set_frequency_1(self, value):
        ftw = (value * (2 ** 48)) / (20000000 * self.pll)
        self.interface.set_frequency_1(int(ftw))

    def set_frequency_2(self, value):
        ftw = (value * (2 ** 48)) / (20000000 * self.pll)
        self.interface.set_frequency_2(int(ftw))

    def set_mode(self, value):
        self.controlregister.mode = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)

    def set_amplitude_i(self, value):
        self.interface.set_i_multiplier(int(value * (2 ** 11)))

    def set_amplitude_q(self, value):
        self.interface.set_q_multiplier(int(value * (2 ** 11)))
