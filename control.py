import interface
import controlregister


class Control:
    def __init__(self, newinterface: interface.Interface):
        self.interface = newinterface
        self.controlregister = controlregister.ControlRegister()
        self.pll = 1
        self.ppm = 0

    def set_ppm(self, value):
        self.ppm = value

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
        self.interface.trigger_update()

    def set_osk(self, value):
        self.controlregister.osk_en = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)
        self.interface.trigger_update()

    def set_bypass_inv_sinc(self, value):
        self.controlregister.bypass_inv_sinc = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)
        self.interface.trigger_update()

    def set_internal_update(self, value):
        self.controlregister.internal_update = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)
        self.interface.trigger_update()
        self.interface.set_ud_input(value)

    # Input 0-1 0-360 deg
    def set_phase_1(self, value):
        self.interface.set_phase_adjust_1(int(value * 8192))
        self.interface.trigger_update()

    def set_phase_2(self, value):
        self.interface.set_phase_adjust_2(int(value * 8192))
        self.interface.trigger_update()

    def set_frequency_1(self, value):
        adjust_freq = value * (1 + self.ppm/1000000)
        ftw = (adjust_freq * (2 ** 48)) / (20000000 * self.pll)
        print("freq 1 is " + str(ftw))
        self.interface.set_frequency_1(int(ftw))
        self.interface.trigger_update()

    def set_frequency_2(self, value):
        adjust_freq = value * (1 + self.ppm/1000000)
        ftw = (adjust_freq * (2 ** 48)) / (20000000 * self.pll)
        self.interface.set_frequency_2(int(ftw))
        self.interface.trigger_update()

    def set_mode(self, value):
        self.controlregister.mode = value
        controlValue = self.controlregister.get_register_int()
        self.interface.set_control(controlValue)
        self.interface.trigger_update()

    def set_amplitude_i(self, value):
        self.interface.set_i_multiplier(int(value * (2 ** 11)))
        self.interface.trigger_update()

    def set_amplitude_q(self, value):
        self.interface.set_q_multiplier(int(value * (2 ** 11)))
        self.interface.trigger_update()
