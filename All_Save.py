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
        if now.second == 0:  # 현재 시각의 초가 0초인 경우에만 데이터 저장 
            file_name = 'CMPS_' + time.strftime('%Y-%m-%d %H:%M') + '.csv' # csv파일명 올바르게 수정해야함.
            data_list = []  # 데이터를 저장할 리스트
            while True:
                start_time = datetime.now()
                if start_time.minute != now.minute:
                    df = pd.DataFrame([line.strip().split(',') for line in data_list]) # 컬럼명을 올바르게 수정해야함.
                    df.to_csv(file_name) # csv파일명 올바르게 수정해야함.
                    df = pd.read_csv(file_name, encoding='cp949') # file_name
                    # df = pd.read_table("파일 위치 및 파일명", sep=',', encoding='cp949') # 해당 코드는 CSV파일이 아닌 txt파일인 경우 데이터프레임으로 변환시켜주는 코드 입니다.
                    # 딕셔너리 형태의 데이터를 추가할 시 매번 id도 추가 되기 때문에 id를 제거하기 위한 코드입니다.
                    print(df)
                    break ## 일시정지 후 While문 탈출.
                data = ser.readline().decode().strip() # 시리얼 포트로부터 데이터 읽기
                data_list.append(str(start_time.date()) + str(start_time.time()) + ',' + data)  # 데이터를 리스트에 추가


except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')

finally :
    print('END')