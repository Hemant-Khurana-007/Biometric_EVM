from machine import Pin, I2C, PWM, UART
from ssd1306 import SSD1306_I2C
import framebuf
import time
import const
from pico_i2c_lcd import I2cLcd

uart = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))
uart_buf = b""


def _draw_one(oled, bmp, lcd, text):
    if bmp is None:
        oled.fill(0)
        oled.show()
        lcd.clear()
        return

    fb = framebuf.FrameBuffer(bmp, 128, 64, framebuf.MONO_VLSB)
    oled.fill(0)
    oled.framebuf.blit(fb, 0, 0)
    oled.show()

    lcd.clear()
    lcd.putstr(text)

def draw_x2(
    sda0, scl0,
    sda1, scl1,
    bmp_a, bmp_b,
    text_a, text_b):

    i2c0 = I2C(0, sda=Pin(sda0), scl=Pin(scl0), freq=400000)
    i2c1 = I2C(1, sda=Pin(sda1), scl=Pin(scl1), freq=400000)

    oled_a = SSD1306_I2C(128, 64, i2c0, 0x3C)
    oled_b = SSD1306_I2C(128, 64, i2c1, 0x3C)

    lcd_a = I2cLcd(i2c0, 0x27, 2, 16)
    lcd_b = I2cLcd(i2c1, 0x27, 2, 16)

    _draw_one(oled_a, bmp_a, lcd_a, text_a)
    _draw_one(oled_b, bmp_b, lcd_b, text_b)

    # release pins
    Pin(sda0, Pin.IN)
    Pin(scl0, Pin.IN)
    Pin(sda1, Pin.IN)
    Pin(scl1, Pin.IN)

    del oled_a, oled_b, lcd_a, lcd_b, i2c0, i2c1

def draw_x4(data):
    """
    data = [
        [text0, bmp0],
        [text1, bmp1],
        [text2, bmp2],
        [text3, bmp3],
    ]
    """

    draw_x2(
        0, 1,
        2, 3,
        data[0][1], data[1][1],
        data[0][0], data[1][0]
    )

    draw_x2(
        4, 5,
        6, 7,
        data[2][1], data[3][1],
        data[2][0], data[3][0]
    )

def draw_blank():
    blank = [
        ["", bytearray(1024)],
        ["", bytearray(1024)],
        ["", bytearray(1024)],
        ["", bytearray(1024)],
    ]
    draw_x4(blank)

buttons = [
    Pin(8, Pin.IN, Pin.PULL_UP),
    Pin(9, Pin.IN, Pin.PULL_UP),
    Pin(10, Pin.IN, Pin.PULL_UP),
    Pin(11, Pin.IN, Pin.PULL_UP),
]

leds = [Pin(p, Pin.OUT) for p in (12, 13, 14, 15)]
for l in leds:
    l.value(0)

buzzer = PWM(Pin(28))
buzzer.freq(2050)
buzzer.duty_u16(0)

last_state = [1, 1, 1, 1]

draw_blank()
while True:
    if uart.any():
        b = uart.read(1)
        if b:
            uart_buf += b

            if b == b'\n':
                cmd = uart_buf.strip().decode('ascii', 'ignore')
                uart_buf = b""
                if cmd in const.all:
                    draw_x4(const.all[cmd])
                    
                else:
                    draw_blank()
    for i in range(4):
        cur = buttons[i].value()

        if last_state[i] == 1 and cur == 0:
            leds[i].value(1)
            buzzer.duty_u16(30000)

            time.sleep(0.75)

            buzzer.duty_u16(0)
            leds[i].value(0)
            
            print(cmd+ "_" +const.all[cmd][i][2]+"\n\r")

            draw_blank()               # OFF after vote
            last_state = [1, 1, 1, 1]
            break

        last_state[i] = cur

    time.sleep(0.01)




