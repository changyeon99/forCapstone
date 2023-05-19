import pandas as pd

# 텍스트 파일 경로 설정
file_path1 = "파일경로.txt" # Sensors 데이터 파일
file_path2 = "파일경로.txt" # IR, Flame Sensor 데이터 파일


# 텍스트 파일 읽기
with open(file_path1, 'r') as file:
    lines = file.readlines()

# 데이터프레임 생성
df1 = pd.DataFrame(lines, columns=['시각','진동','음향1','음향2','적외선1'])

# 데이터프레임 출력
print(df1)

with open(file_path2, 'r') as file:
    lines = file.readlines()

# 데이터프레임 생성
df2 = pd.DataFrame(lines, columns=['시각','적외선2','화재'])

# 데이터프레임 출력
print(df2)