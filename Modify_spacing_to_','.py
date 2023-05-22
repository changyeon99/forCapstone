# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:08:06 2023

@author: pjk98
"""

# 텍스트 파일 경로 설정
file_path = "파일경로.txt"

# 수정할 위치와 대체할 문자열
position = 26  # 수정할 위치 (0부터 시작)

# 텍스트 파일 불러오기
with open(file_path, 'r') as file:
    lines = file.readlines()

# 띄어쓰기를 대체 문자열로 수정하고 텍스트 파일 다시 저장
with open(file_path, 'w') as file:
    for line in lines:
        modified_line = line[:position] + line[position].replace(' ', ',') + line[position:]
        file.write(modified_line)