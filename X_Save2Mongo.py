# DB 연동
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://capstone:smartfactory@pak.ymtzidm.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 메인 DB 생성하기
db = client['TimingBelt_Data'] # db 컨택 / 없는것도 바로 생성 가능

# DB 저장
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
            file_name = time.strftime('%Y-%m-%d %H:%M') + '.csv' # csv파일명 올바르게 수정해야함.
            coll_name = time.strftime('%Y-%m-%d %H:%M')
            data_list = []  # 데이터를 저장할 리스트
            while True:
                start_time = datetime.now()
                if start_time.second != 0:
                    df = pd.DataFrame([line.strip().split(',') for line in data_list], columns=['시각','음향2','적외선2']) # 컬럼명을 올바르게 수정해야함.
                    df.to_csv(file_name) # csv파일명 올바르게 수정해야함.
                    collection = db[coll_name] # '세부 데이터베이스 이름' --> file_name으로 변경하면 됨 / file_name = time.strftime('%Y-%m-%d %H:%M') + '.txt'
                    df = pd.read_csv(file_name, encoding='cp949') # file_name
                    # df = pd.read_table("파일 위치 및 파일명", sep=',', encoding='cp949') # 해당 코드는 CSV파일이 아닌 txt파일인 경우 데이터프레임으로 변환시켜주는 코드 입니다.
                    df_dict = df.to_dict(orient= 'records')
                    collection.insert_many(df_dict) # 딕셔너리 형태의 데이터를 세부 DB에 추가한다.
                    # 딕셔너리 형태의 데이터를 추가할 시 매번 id도 추가 되기 때문에 id를 제거하기 위한 코드입니다.
                    # print(pd.DataFrame(list(collection.find())).drop(['_id','Unnamed: 0'], axis=1))
                    os.remove(file_name) # 임시로 생성한 CSV 파일을 삭제합니다.
                    now = datetime.now()
                    time_difference = now.replace(second=59) - now
                    time.sleep(time_difference.total_seconds())
                    break ## 일시정지 후 While문 탈출.
                data = ser.readline().decode().strip() # 시리얼 포트로부터 데이터 읽기
                data_list.append(str(start_time.date()) + str(start_time.time()) + ',' + data)  # 데이터를 리스트에 추가


except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')

finally :
    print('END')