import serial
import time
from datetime import datetime
from github import Github
import os

repo_owner = 'changyeon99'
repo_name = 'jirisan'
branch_name = 'main'
access_token = '' # 토큰 기입 필요힘.
g = Github(access_token)
repo = g.get_user(repo_owner).get_repo(repo_name)
branch = repo.get_branch(branch_name)

# 매초마다 0.01초 분량의 파일 한 개를 생성하여 깃 저장소에 푸시할 목적으로 작성함.
ser = serial.Serial('/dev/ttyACM0', 2000000)
try:
    while True:
        if int(datetime.now().strftime('%f')[-6:-4]) == 0: # 1번. n.000~n.009초일 때 실행됨.
            file_name = time.strftime('%m-%d %H:%M:%S') + '.txt' # 2번. 파일명 = 월-일 시:분:n.txt
            with open(file_name, 'w') as file: # 3번. 쓰기 전용 파일임.
                while True: # 4번.
                    if int(datetime.now().strftime('%f')[-6:-4]) != 0: # 7번. n.01초일 때 실행됨.
                        with open(file_name, 'r') as file: # 8번. 2번에서 생성한 파일을 읽음.
                            repo.create_file(file_name, "", file.read(), branch=branch.name) # 9번. 8번 파일을 깃 저장소로 푸시함.
                        os.remove(file_name) # 10번. 2번 파일을 로컬 환경에서 삭제함.
                        break # 11번. while문 탈출함.
                    file.write(ser.readline().decode().strip() + '\n') # 5번. 아두이노로부터 값 받아쓴 뒤 줄 바꿈.
                    # 6번. 7번 조건을 만족하기 전까지 1번부터 5번까지 반복됨.
except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')
finally :
    print('END')