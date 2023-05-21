import pandas as pd

# 텍스트 파일 경로 설정
file_path1 = "파일경로.txt" # Sensors(Vibration, Sound1, IR1, Flame Sensor) 데이터 파일
file_path2 = "파일경로.txt" # Sound2, IR2 Sensor 데이터 파일

# 텍스트 파일 읽기
with open(file_path1, 'r') as file:
    lines = file.readlines()

# 데이터프레임 생성
df1 = pd.DataFrame([line.strip().split(',') for line in lines], columns=['시각','진동','음향1','적외선1','화재'])

# 데이터프레임 출력
print(df1)

with open(file_path2, 'r') as file:
    lines = file.readlines()

# 데이터프레임 생성
df2 = pd.DataFrame([line.strip().split(',') for line in lines], columns=['시각','음향2','적외선2'])

# 데이터프레임 출력
print(df2)

# 두 데이터프레임 병합
merged_df = pd.merge(df1, df2, on='시각')

# reindex()함수는 데이터 프레임의 인덱스를 변경하는데도 사용할 수 있으며 열 분할에 사용할 수 있다.
# 원하는 컬럼 순서로 데이터프레임 재정렬
columns = ['시각', '진동', '음향1', '음향2', '적외선1', '적외선2', '화재']
merged_df_reordered = merged_df.reindex(columns=columns)

Sensors_df = merged_df_reordered.reindex(columns=['시각', '진동', '음향1', '음향2', '적외선1', '적외선2'])
Flame_df = merged_df_reordered.reindex(columns=['시각', '화재'])

# 병합된 데이터프레임과 재정렬된 데이터프레임과 열 분할된 데이터프레임 출력
print(merged_df)
print(merged_df_reordered)
print(Sensors_df)
print(Flame_df)

