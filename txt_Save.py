import serial
from datetime import datetime
# 시각 --> 년.월.일 시:분:초.xxxxxx 으로 데이터 저장됨.
# .date() --> 년.월.일
# .time() --> 시:분:초.xxxxxx

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 2000000) # 포트 번호와 통신속도를 아두이노를 동일하게 설정해야함.

# 데이터 읽기 및 저장
try:
    with open('Test_Data.txt', 'w') as file: # 파일명을 나중에 제대로 작성하기
        while True:
            now = datetime.now()
            data = ser.readline.decode().strip() # 시리얼 포트로부터 데이터 읽기
            file.write(str(now.date()) + ' ' + str(now.time()) + ',' + data + '\n') # 데이터를 파일 저장 / 시각 --> 년.월.일 시:분:초.xxxxxx 으로 데이터 저장됨.

except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')

finally :
    print('END')
