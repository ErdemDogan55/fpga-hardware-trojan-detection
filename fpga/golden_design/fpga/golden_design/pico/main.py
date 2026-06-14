from machine import I2C, Pin, ADC
import time

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
INA = 0x40
temp_sensor = ADC(4)

def write_reg(reg, value):
    i2c.writeto_mem(INA, reg, bytes([(value >> 8) & 0xFF, value & 0xFF]))

def read_reg(reg):
    data = i2c.readfrom_mem(INA, reg, 2)
    return (data[0] << 8) | data[1]

def to_signed(val):
    if val >= 32768:
        val -= 65536
    return val

def pico_temp_c():
    raw = temp_sensor.read_u16()
    voltage = raw * 3.3 / 65535
    return 27 - (voltage - 0.706) / 0.001721

write_reg(0x00, 0x8000)
time.sleep(0.1)
write_reg(0x00, 0x4127)
write_reg(0x05, 0x0200)

while True:
    shunt_raw = to_signed(read_reg(0x01))
    bus_raw = read_reg(0x02)
    current_raw = to_signed(read_reg(0x04))
    power_raw = read_reg(0x03)

    shunt_mv = shunt_raw * 0.0025
    bus_v = bus_raw * 1.25 / 1000
    current_ma = current_raw * 1.0
    power_mw = power_raw * 25.0
    temp_c = pico_temp_c()

    print("voltage_v={:.3f}, shunt_mv={:.3f}, current_ma={:.2f}, power_mw={:.2f}, temp_c={:.2f}".format(
        bus_v, shunt_mv, current_ma, power_mw, temp_c))
    time.sleep(1)
