import serial
import time
from datetime import datetime
from github import Github
import os

# GitHub 저장소 정보
repo_owner = 'changyeon99'
repo_name = 'TimingBeltData'
branch_name = 'main'
# Github 엑세스 토큰 정보
access_token = ''
# GitHub 액세스 토큰을 사용하여 인증합니다.
g = Github(access_token)
# 사용자명과 저장소명을 기반으로 저장소를 가져옵니다.
repo = g.get_user(repo_owner).get_repo(repo_name)
# 브랜치를 가져옵니다.
branch = repo.get_branch(branch_name)

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', 2000000) # 포트 번호와 통신속도를 아두이노를 동일하게 설정해야함.
# 데이터 읽기 및 저장

count = 0

try:
    while True:
        now = datetime.now() ## 현재 시각 17시 50분 00초
        if (now.second == 0) & (count==0): ## 00초이므로 시작
            count = 1
            file_name = time.strftime('%Y-%m-%d %H:%M:%S') + '.txt'
            continue
        else:
            file_name = time.strftime('%Y-%m-%d %H:%M:%S') + '.txt'
            # file_path = "C:/Users/99kit/Desktop/ABCDEF/" + file_name
            with open(file_name, 'w') as file: ## ABCDEF 폴더에 2023-05-24 17:50.txt 파일 생성
                while True:
                    start_time = datetime.now()
                    if start_time.second != now.second: ## 현 시각 01초가 되는 순간, 00초가 아니므로 if문 발동
                        with open(file_name, 'r') as file: # 파일을 저장소에 업로드합니다.
                            repo.create_file(file_name, "Upload data", file.read(), branch=branch.name)
                        os.remove(file_name) # 임시로 생성한 CSV 파일을 삭제합니다.
                        # now = datetime.now()
                        # time_difference = now.replace(second=59) - now
                        # time.sleep(time_difference.total_seconds())
                        break ## 일시정지 후 While문 탈출.
                    data = ser.readline().decode().strip() # 시리얼 포트로부터 데이터 읽기
                    file.write(data + '\n') # 데이터를 파일 저장
except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')
finally :
    print('END')