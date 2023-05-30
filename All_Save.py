import pandas as pd
import os
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
        if now.second == 0:
            file_name = 'CMPS_' + time.strftime('%Y-%m-%d %H:%M') + '.csv' # csv파일명 올바르게 수정해야함.
            data_list = []
        # else:
        #     file_name = 'CMPS_' + time.strftime('%Y-%m-%d %H:%M') + '.csv' # csv파일명 올바르게 수정해야함.
        #     data_list = []  # 데이터를 저장할 리스트
            while True:
                start_time = datetime.now()
                if start_time.minute != now.minute:
                    df = pd.DataFrame([line.strip().split(',') for line in data_list])
                    print(df)
                    df.to_csv('/home/chagyeon99/Data/'+file_name) # csv파일명 올바르게 수정해야함.
                    break ## 일시정지 후 While문 탈출.
                data = ser.readline().decode().strip()
                data_list.append(str(start_time.date()) + str(start_time.time()) + ',' + data)


except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')

finally :
    print('END')