# 매초마다 1초 분량의 파일 한 개를 생성하여 로컬 저장소에 저장할 목적으로 작성함.
ser = serial.Serial('/dev/ttyACM0', 2000000)
try:
    while True:
        for i in range(0, 60, 1):
            if datetime.now().second == i:
                file_name = time.strftime('%m-%d %H:%M:%S') + '.txt'
                with open(file_name, 'w') as file:
                    while True: # 4번.
                        if datetime.now().second != i:
                            break 
                        file.write(ser.readline().decode().strip() + '\n')