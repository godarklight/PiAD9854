class ControlRegister():
    def __init__(self):
        #Default values
        self.comparator_powerdown = 1
        self.qdac_powerdown = 0
        self.dac_powerdown = 0
        self.digital_powerdown = 0
        self.pll_range = 1
        self.bypass_pll = 1
        self.pll_multiplier = 4
        self.clear_accumulator1 = 0
        self.clear_accumulator = 0
        self.triangle = 0
        self.source_qdac = 0
        self.mode = 0
        self.internal_update = 1
        self.bypass_inv_sinc = 0
        self.osk_en = 0
        self.osk_int = 0

    def get_register_int(self):
        value = 0
        value = value | (self.comparator_powerdown << 28)
        value = value | (self.qdac_powerdown << 26)
        value = value | (self.dac_powerdown << 25)
        value = value | (self.digital_powerdown << 24)
        value = value | (self.pll_range << 22)
        value = value | (self.bypass_pll << 21)
        value = value | (self.pll_multiplier << 16)
        value = value | (self.clear_accumulator1 << 15)
        value = value | (self.clear_accumulator << 14)
        value = value | (self.triangle << 13)
        value = value | (self.source_qdac << 12)        
        value = value | (self.mode << 9)
        value = value | (self.internal_update << 8)
        value = value | (self.bypass_inv_sinc << 6)
        value = value | (self.osk_en << 5)
        value = value | (self.osk_int << 4)
        self.clear_accumulator1 = 0
        self.clear_accumulator = 0
        return value