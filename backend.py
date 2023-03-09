import time
import gpiod
from registers import Register


class Fake():
    def __init__(self):
        self.registerdata = [0x0] * 38
        self.set_register(Register.UpdateClock0, 0x40)
        self.set_register(Register.Control3, 0x10)
        self.set_register(Register.Control2, 0x64)
        self.set_register(Register.Control1, 0x01)
        self.set_register(Register.Control0, 0x20)
        self.set_register(Register.OSKRate, 0x80)

    def set_register(self, address, value):
        self.registerdata[address] = value

    def get_register(self, address):
        return self.registerdata[address]


class GPIO(Fake):
    def __init__(self):
        self.gpio_init = False
        Fake.__init__(self)

    def autoconfigure(self):
        deviceID = ""
        with open('/sys/firmware/devicetree/base/model') as f:
            deviceID = f.readline()
        if ("Raspberry" in deviceID):
            self.use_pi2()
        if ("BPI-M5" in deviceID):
            self.use_banana_pi_m5()


    def use_pi2(self):
        chip0 = gpiod.Chip("/dev/gpiochip0")
        self.address0 = chip0.find_line("SDA1")
        self.address1 = chip0.find_line("SCL1")
        self.address2 = chip0.find_line("GPIO_GCLK")
        self.address3 = chip0.find_line("GPIO17")
        self.address4 = chip0.find_line("GPIO27")
        self.address5 = chip0.find_line("GPIO22")
        self.data0 = chip0.find_line("SPI_MOSI")
        self.data1 = chip0.find_line("SPI_MISO")
        self.data2 = chip0.find_line("SPI_SCLK")
        self.data3 = chip0.find_line("ID_SDA")
        self.data4 = chip0.find_line("GPIO5")
        self.data5 = chip0.find_line("GPIO6")
        self.data6 = chip0.find_line("GPIO13")
        self.data7 = chip0.find_line("GPIO19")
        self.reset = chip0.find_line("GPIO26")
        self.uclk = chip0.find_line("GPIO16")
        self.wd = chip0.find_line("GPIO20")        
        self.rd = chip0.find_line("GPIO21")
        self.configure_gpio()

    def use_banana_pi_m5(self):
        chip0 = gpiod.Chip("/dev/gpiochip0")
        chip1 = gpiod.Chip("/dev/gpiochip1")
        # Get pins
        self.address0 = chip0.find_line("CON1-P03")
        self.address1 = chip0.find_line("CON1-P05")
        self.address2 = chip0.find_line("CON1-P07")
        self.address3 = chip0.find_line("CON1-P11")
        self.address4 = chip0.find_line("CON1-P13")
        self.address5 = chip0.find_line("CON1-P15")
        self.data0 = chip0.find_line("CON1-P19")
        self.data1 = chip0.find_line("CON1-P21")
        self.data2 = chip0.find_line("CON1-P23")
        self.data3 = chip0.find_line("CON1-P27")
        self.data4 = chip0.find_line("CON1-P29")
        self.data5 = chip0.find_line("CON1-P31")
        self.data6 = chip0.find_line("CON1-P33")
        self.data7 = chip1.find_line("CON1-P35")
        self.reset = chip1.find_line("CON1-P37")
        self.uclk = chip0.find_line("CON1-P36")
        self.wd = chip1.find_line("CON1-P38")
        self.rd = chip1.find_line("CON1-P40")

        self.configure_gpio()

    def configure_gpio(self):
        # Request
        self.address0.request("AD9854-A0", gpiod.LINE_REQ_DIR_OUT)
        self.address1.request("AD9854-A1", gpiod.LINE_REQ_DIR_OUT)
        self.address2.request("AD9854-A2", gpiod.LINE_REQ_DIR_OUT)
        self.address3.request("AD9854-A3", gpiod.LINE_REQ_DIR_OUT)
        self.address4.request("AD9854-A4", gpiod.LINE_REQ_DIR_OUT)
        self.address5.request("AD9854-A5", gpiod.LINE_REQ_DIR_OUT)
        self.data0.request("AD9854-D0", gpiod.LINE_REQ_DIR_IN)
        self.data1.request("AD9854-D1", gpiod.LINE_REQ_DIR_IN)
        self.data2.request("AD9854-D2", gpiod.LINE_REQ_DIR_IN)
        self.data3.request("AD9854-D3", gpiod.LINE_REQ_DIR_IN)
        self.data4.request("AD9854-D4", gpiod.LINE_REQ_DIR_IN)
        self.data5.request("AD9854-D5", gpiod.LINE_REQ_DIR_IN)
        self.data6.request("AD9854-D6", gpiod.LINE_REQ_DIR_IN)
        self.data7.request("AD9854-D7", gpiod.LINE_REQ_DIR_IN)
        self.reset.request("AD9854-RESET", gpiod.LINE_REQ_DIR_OUT)
        self.wd.request("AD9854-WD", gpiod.LINE_REQ_DIR_OUT)
        self.rd.request("AD9854-RD", gpiod.LINE_REQ_DIR_OUT)
        self.uclk.request("AD9854-UCLK", gpiod.LINE_REQ_DIR_IN)
        self.set_addr_pins(0)
        self.rd.set_value(1)
        self.wd.set_value(1)
        self.reset.set_value(1)
        time.sleep(0.001)
        self.reset.set_value(0)
        time.sleep(0.001)
        self.gpio_init = True

    def print_registers(self):
        for testAddr in range(40):
            self.set_addr_pins(testAddr)
            time.sleep(0.001)
            self.rd.set_value(0)
            time.sleep(0.001)
            inData = self.get_data_pins()
            self.rd.set_value(1)            
            print("ADDR " + hex(testAddr) + " = " + hex(inData))

    def print_register(self, address):
        self.set_addr_pins(address)
        time.sleep(0.001)
        self.rd.set_value(0)
        time.sleep(0.001)
        inData = self.get_data_pins()
        self.rd.set_value(1)            
        print("ADDR " + hex(address) + " = " + hex(inData))

    def set_register(self, address, value):
        Fake.set_register(self, address, value)
        if (self.gpio_init == False):
            return
        self.set_addr_pins(address)
        self.set_pins_write_mode()
        time.sleep(0.001)
        self.set_data_pins(value)
        time.sleep(0.001)
        self.wd.set_value(0)
        time.sleep(0.001)
        self.wd.set_value(1)
        self.set_pins_read_mode()
        #print("UPDATED " + hex(address) + " -> " + hex(value))


    def get_register(self, address):
        Fake.get_register(self, address)

    def set_addr_pins(self, address):
        self.address0.set_value(address & 1)
        address = address >> 1
        self.address1.set_value(address & 1)
        address = address >> 1
        self.address2.set_value(address & 1)
        address = address >> 1
        self.address3.set_value(address & 1)
        address = address >> 1
        self.address4.set_value(address & 1)
        address = address >> 1
        self.address5.set_value(address & 1)

    def set_data_pins(self, value):
        self.data0.set_value(value & 1)
        value = value >> 1
        self.data1.set_value(value & 1)
        value = value >> 1
        self.data2.set_value(value & 1)
        value = value >> 1
        self.data3.set_value(value & 1)
        value = value >> 1
        self.data4.set_value(value & 1)
        value = value >> 1
        self.data5.set_value(value & 1)
        value = value >> 1
        self.data6.set_value(value & 1)
        value = value >> 1
        self.data7.set_value(value & 1)

    def get_data_pins(self):
        value = 0
        value = value | (self.data0.get_value() << 0)
        value = value | (self.data1.get_value() << 1)
        value = value | (self.data2.get_value() << 2)
        value = value | (self.data3.get_value() << 3)
        value = value | (self.data4.get_value() << 4)
        value = value | (self.data5.get_value() << 5)
        value = value | (self.data6.get_value() << 6)
        value = value | (self.data7.get_value() << 7)
        return value

    def set_pins_write_mode(self):
        self.data0.set_direction_output()
        self.data1.set_direction_output()
        self.data2.set_direction_output()
        self.data3.set_direction_output()
        self.data4.set_direction_output()
        self.data5.set_direction_output()
        self.data6.set_direction_output()
        self.data7.set_direction_output()

    def set_pins_read_mode(self):
        self.data0.set_value(0)
        self.data1.set_value(0)
        self.data2.set_value(0)
        self.data3.set_value(0)
        self.data4.set_value(0)
        self.data5.set_value(0)
        self.data6.set_value(0)
        self.data7.set_value(0)
        self.data0.set_direction_input()
        self.data1.set_direction_input()
        self.data2.set_direction_input()
        self.data3.set_direction_input()
        self.data4.set_direction_input()
        self.data5.set_direction_input()
        self.data6.set_direction_input()
        self.data7.set_direction_input()

    def set_ud_input(self, value):
        if (value):
            self.uclk.set_direction_input()
        else:
            self.uclk.set_direction_output()
            self.uclk.set_value(0)


    def toggle_ud(self):
        if (self.gpio_init == False):
            return
        self.uclk.set_value(1)
        time.sleep(0.001)
        self.uclk.set_value(0)