import RPi.GPIO as GPIO
import time
import os

channel = 17  # BCM. 17, wPi. 0, Physical. 11(DOUT에 연결)

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME, GPIO.IN)

if __name__ == "__main__" :
    try :
        while(1) :
            now = time.localtime()
            timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
            (now.tm_year, now.tm_mon, now.tm_mday, 
            now.tm_hour, now.tm_min, now.tm_sec))
            if GPIO.input(channel) == 1 : # 평소 1을 전송함
                print(timestamp, "안전")
            else :                      # 불꽃 감지시 0을 전송함
                print(timestamp, "화재 경보")
                os.system('/home/pi/program/pushbullet.sh')            
                time.sleep(1)
    except :
        print("err or Ctrl - C")
    finally :
        GPIO.cleanup()
        print("END")