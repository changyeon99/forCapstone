import RPi.GPIO as GPIO
import spidev
import pandas as pd
import matplotlib.pyplot as plt
import time

# Open Spi Bus
# SPI 버스 0과 디바이스 0을 열고
# 최대 전송 속도를 1MHz로 설정
spi = spidev.SpiDev()
spi.open(0,0) # open(bus, device)
spi.max_speed_hz = 1000000 # set transfer speed

# 아날로그 값 출력 함수
def readChannel(channel):
    data_list = [] 
    val = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((val[1]&3) << 8) + val[2]
    int_val = data
    voltage_val = (data*3.3)/1024
    val_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print('Sound int값 :', int_val)
    print('Sound voltage값 :', voltage_val)
    print(val_time)
    return val_time, int_val, voltage_val

vibration = 0 #진동 채널
vibration_list = []
# sound1 = 1 #음향1 채널
# sound2 = 2 #음향2 채널
# IR1 = 3 #적외선1 채널
# IR2 = 4 #적외선2 채널

Flame_channel = 18  # 불꽃감지

GPIO.setmode(GPIO.BCM)
GPIO.setup(Flame_channel, GPIO.IN)

try :
    while True :
        now = time.localtime()
        timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
        (now.tm_year, now.tm_mon, now.tm_mday, 
        now.tm_hour, now.tm_min, now.tm_sec))
        if GPIO.input(Flame_channel) == 0 : # 불꽃 감지시 0을 전송함                     
            print(timestamp, "화재 경보")
        val_time, int_val, voltage_val = readChannel(vibration)
        vibration_list.append([val_time, int_val, voltage_val])
        time.sleep(1)
        
except :
    print("err or Ctrl - C")
    columns = ['시각','int','voltage']
    pd_data = pd.DataFrame(vibration_list, columns=columns)
    print(pd_data)
finally :
    GPIO.cleanup()
    print("END")

# while True:
#     val = readChannel(channel)
#     int_val = val
#     voltage_val = (val*3.3)/1024
#     val_time = time.strftime('%Y-%m-%d %H:%M:%S')
#     print('Sound int값 :', int_val)
#     print('Sound int값 :', voltage_val)
#     print(val_time)
#     data_list.append([val_time, int_val, voltage_val])
#     time.sleep(1)

