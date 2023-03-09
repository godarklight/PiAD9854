import backend
from registers import Register

class Interface():
    
    def __init__(self, newbackend : backend.Fake):
        self._backend = newbackend
        self.ud_is_input = True
    
    def set_phase_adjust_1(self, value):
        self._backend.set_register(Register.PhaseAdjust1B0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.PhaseAdjust1B1, value & 0xFF)

    def set_phase_adjust_2(self, value):
        self._backend.set_register(Register.PhaseAdjust2B0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.PhaseAdjust2B1, value & 0xFF)

    def set_frequency_1(self, value):
        self._backend.set_register(Register.Frequency1B0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency1B1, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.Frequency1B2, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency1B3, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.Frequency1B4, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency1B5, value & 0xFF)
    
    def set_frequency_2(self, value):
        self._backend.set_register(Register.Frequency2B0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency2B1, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.Frequency2B2, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency2B3, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.Frequency2B4, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Frequency2B5, value & 0xFF)
    
    def set_delta(self, value):
        self._backend.set_register(Register.DeltaFrequency0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.DeltaFrequency1, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.DeltaFrequency2, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.DeltaFrequency3, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.DeltaFrequency4, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.DeltaFrequency5, value & 0xFF)

    def set_update_clock(self, value):
        self._backend.set_register(Register.UpdateClock0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.UpdateClock1, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.UpdateClock2, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.UpdateClock3, value & 0xFF)
    
    def set_ramp_rate_clock(self, value):
        self._backend.set_register(Register.RampRate0, value & 0xFF)    
        value = value >> 8
        self._backend.set_register(Register.RampRate1, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.RampRate2, value & 0xFF)

    def set_control(self, value):
        self._backend.set_register(Register.Control0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Control1, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Control2, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.Control3, value & 0xFF)
    
    def set_i_multiplier(self, value):
        self._backend.set_register(Register.IMultiply0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.IMultiply1, value & 0xFF)
    
    def set_q_multiplier(self, value):
        self._backend.set_register(Register.QMultiply0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.QMultiply1, value & 0xFF)
    
    def set_ramp_rate(self, value):
        self._backend.set_register(Register.OSKRate, value & 0xFF)

    def set_q_dac(self, value):
        self._backend.set_register(Register.QDAC0, value & 0xFF)
        value = value >> 8
        self._backend.set_register(Register.QDAC1, value & 0xFF)
    
    def get_phase_adjust_1(self):
        value = 0
        value = value | self._backend.get_register(Register.PhaseAdjust1B1)
        value = value << 8
        value = value | self._backend.get_register(Register.PhaseAdjust1B0)
        return value

    def get_phase_adjust_2(self):
        value = 0
        value = value | self._backend.get_register(Register.PhaseAdjust2B1)
        value = value << 8
        value = value | self._backend.get_register(Register.PhaseAdjust2B0)
        return value
    
    def get_frequency_1(self):
        value = 0
        value = value | self._backend.get_register(Register.Frequency1B5)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency1B4)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency1B3)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency1B2)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency1B1)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency1B0)
        return value
    
    def get_frequency_2(self):
        value = 0
        value = value | self._backend.get_register(Register.Frequency2B5)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency2B4)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency2B3)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency2B2)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency2B1)
        value = value << 8
        value = value | self._backend.get_register(Register.Frequency2B0)
        return value
    
    def get_delta(self):
        value = 0
        value = value | self._backend.get_register(Register.DeltaFrequency5)
        value = value << 8
        value = value | self._backend.get_register(Register.DeltaFrequency4)
        value = value << 8
        value = value | self._backend.get_register(Register.DeltaFrequency3)
        value = value << 8
        value = value | self._backend.get_register(Register.DeltaFrequency2)
        value = value << 8
        value = value | self._backend.get_register(Register.DeltaFrequency1)
        value = value << 8
        value = value | self._backend.get_register(Register.DeltaFrequency0)
        return value
    
    def get_update_clock(self):
        value = 0
        value = value | self._backend.get_register(Register.UpdateClock3)
        value = value << 8
        value = value | self._backend.get_register(Register.UpdateClock2)
        value = value << 8
        value = value | self._backend.get_register(Register.UpdateClock1)
        value = value << 8
        value = value | self._backend.get_register(Register.UpdateClock0)
        return value

    def get_ramp_rate_clock(self):
        value = 0
        value = value | self._backend.get_register(Register.RampRate2)
        value = value << 8
        value = value | self._backend.get_register(Register.RampRate1)
        value = value << 8
        value = value | self._backend.get_register(Register.RampRate0)
        return value

    def get_i_multiplier(self):
        value = 0
        value = value | self._backend.get_register(Register.IMultiply1)
        value = value << 8
        value = value | self._backend.get_register(Register.IMultiply0)
        return value

    def get_q_multiplier(self):
        value = 0
        value = value | self._backend.get_register(Register.QMultiply1)
        value = value << 8
        value = value | self._backend.get_register(Register.QMultiply0)
        return value

    def get_ramp_rate(self):
        return self._backend.get_register(Register.OSKRate)
    
    def get_control(self):
        value = 0
        value = value | self._backend.get_register(Register.Control3)
        value = value << 8
        value = value | self._backend.get_register(Register.Control2)
        value = value << 8
        value = value | self._backend.get_register(Register.Control1)
        value = value << 8
        value = value | self._backend.get_register(Register.Control0)
        return value
    
    def get_q_dac(self, value):
        value = 0
        value = value | self._backend.get_register(Register.QDAC1)
        value = value << 8
        value = value | self._backend.get_register(Register.QDAC0)
        return value
    
    def set_ud_input(self, value):
        self.ud_is_input = value
        self._backend.set_ud_input(value)
    
    def trigger_update(self):
        return
        if (self.ud_is_input):
            self.set_update_clock(0)
        else:
            self._backend.toggle_ud()