import serial
import time
from datetime import datetime
from github import Github
import os

repo_owner = 'changyeon99'
repo_name = 'TimingBeltData'
branch_name = 'main'
access_token = ''
g = Github(access_token)
repo = g.get_user(repo_owner).get_repo(repo_name)
branch = repo.get_branch(branch_name)

ser = serial.Serial('/dev/ttyACM0', 2000000)
try:
    while True:
        if int(datetime.now().strftime('%f')[:-5]) == 0:
            file_name = time.strftime('%Y-%m-%d %H:%M:%S') + '.txt'
            with open(file_name, 'w') as file:
                while True:
                    if int(datetime.now().strftime('%f')[:-5]) != 0:
                        with open(file_name, 'r') as file:
                            repo.create_file(file_name, "Upload data", file.read(), branch=branch.name)
                        os.remove(file_name)
                        now = datetime.now()
                        time_difference = now.replace(microsecond = 500000) - now
                        time.sleep(time_difference.total_seconds())
                        break
                    file.write(ser.readline().decode().strip() + '\n')
except KeyboardInterrupt:
    print("Ctrl + C")
    print('데이터 저장 중지')
finally :
    print('END')