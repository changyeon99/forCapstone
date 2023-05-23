# -*- coding: utf-8 -*-
"""
Created on Tue May 23 22:35:56 2023

@author: pjk98
"""

import serial
import time
from datetime import datetime
# 시각 --> 년.월.일 시:분:초.xxxxxx 으로 데이터 저장됨.
# .date() --> 년.월.일
# .time() --> 시:분:초.xxxxxx

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 2000000) # 포트 번호와 통신속도를 아두이노를 동일하게 설정해야함.


# 데이터 읽기 및 저장
try:
    while True:
        now = datetime.now()    
        if now.second == 0:  # 현재 시각의 초가 0초인 경우에만 데이터 저장
            with open(time.strftime('%Y.%m.%d_%H:%M')+'.txt', 'w') as file: # 파일 위치 정의하기
                while True:
                    start_time = datetime.now()
                    if start_time.second != 0:
                        time.sleep(58)
                        break
                    print(start_time.second)
                    print(start_time.time())
                    data = ser.readline.decode().strip() # 시리얼 포트로부터 데이터 읽기
                    file.write(data + '\n') # 데이터를 파일 저장 / 시각 --> 년.월.일 시:분:초.xxxxxx 으로 데이터 저장됨.

except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')

finally :
    print('END')