"""
rpgpio.py - A collection of classes and functions for handling Raspberry Pi GPIO pins.

Author: Peter Malmberg
Date: 2026-02-12
License: MIT
"""

import logging
from dataclasses import dataclass

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("RPi.GPIO not available")
    exit(1)
    
@dataclass
class RpGpio:
    id_p1: int = 0
    id_cpu: int = 0
    alternative: str = ""
    pwm: object = None

    def __str__(self) -> str:
        if self.alternative == "":
            return f"{self.id_p1:02d} GPIO{self.id_cpu:<2}"
        return f"{self.id_p1:02d} GPIO{self.id_cpu:<2} ({self.alternative})"

    def label(self) -> str:
        return f'<pre><span style="color:Blue">{self.id_p1:02d}</span> <span style="color:Green">GPIO{self.id_cpu:2d}</span> <span style="color:Purple">{self.alternative}</span></pre>'

    def name(self) -> str:
        return f"Pin {self.id_p1:2}: GPIO{self.id_cpu}"

    def is_busy(self) -> bool:
        try:
            self.setup(GPIO.IN)
        except:
            return True
        
        self.cleanup()
        return False    
    
    def input(self) -> int:
        return GPIO.input(self.id_cpu)
    
    def set_output(self, state:int) -> None:
        if state == 0:
            GPIO.output(self.id_cpu, GPIO.LOW)
        else:
            GPIO.output(self.id_cpu, GPIO.HIGH)
    
    def setup(self, direction, pull_upp) -> None:
        if direction == GPIO.IN:
            GPIO.setup(self.id_cpu, GPIO.IN ,pull_up_down=pull_upp)
        else:
            GPIO.setup(self.id_cpu, GPIO.OUT)
    
    def cleanup(self) -> None:
        if self.pwm is not None:
            self.pwm.stop()
            self.pwm = None
        
        GPIO.cleanup(self.id_cpu)
        
    def pwm_setup(self, frequency:float) -> None:
        self.pwm_stop()
        self.pwm = GPIO.PWM(self.id_cpu, frequency)
        
    def pwm_start(self, duty_cycle:float) -> None:
        if self.pwm is not None:
            self.pwm.start(duty_cycle)
    
    def pwm_stop(self) -> None:
        if self.pwm is not None:
            self.pwm.stop()
            
    def pwm_change_frequency(self, frequency:float) -> None:
        if self.pwm is not None:
            self.pwm.ChangeFrequency(frequency)
            
    def pwm_change_duty_cycle(self, duty_cycle:float) -> None:
        if self.pwm is not None:
            self.pwm.ChangeDutyCycle(duty_cycle)
        
        
    

rp_gpio_list = [
    RpGpio(3, 2, "SDA"),
    RpGpio(5, 3, "SCL"),
    RpGpio(7, 3, "GPCLK"),
    RpGpio(8, 14, "TXD"),
    RpGpio(10, 15, "RXD"),
    RpGpio(11, 17, ""),
    RpGpio(12, 18, "PCM_CLK"),
    RpGpio(13, 27, ""),
    RpGpio(15, 22, ""),
    RpGpio(16, 23, ""),
    RpGpio(18, 24, ""),
    RpGpio(19, 10, "SPI_MOSI"),
    RpGpio(21, 9, "SPI_MISO"),
    RpGpio(22, 25, ""),
    RpGpio(23, 11, "SPI_SCLK"),
    RpGpio(24, 8, "SPI_CE0"),
    RpGpio(26, 7, "SPI_CE1"),
    RpGpio(29, 5, ""),
    RpGpio(31, 6, ""),
    RpGpio(32, 12, ""),
    RpGpio(33, 13, ""),
    RpGpio(35, 19, ""),
    RpGpio(36, 16, ""),
    RpGpio(37, 26, ""),
    RpGpio(38, 20, ""),
    RpGpio(40, 21, ""),
]


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

if __name__ == "__main__":
    for gpio in rp_gpio_list:
        print(f"{str(gpio):20} {gpio.is_busy()}")
        