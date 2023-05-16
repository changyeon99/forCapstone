import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time, sys

CHANNEL = 0

# MCP3008 - 1 : 5V
# MCP3008 - 2 : 5V
# MCP3008 - 3 : GND
SCLK = 11   # Physical. 23   # MCP3008 - 4
MISO = 9    # Physical. 21   # MCP3008 - 5
MOSI = 10   # Physical. 19   # MCP3008 - 6
CE0 = 8     # Physical. 24   # MCP3008 - 7
# MCP3008 - 8 : GND
mcp = Adafruit_MCP3008.MCP3008(clk=SCLK, cs=CE0, miso=MISO, mosi=MOSI)

if __name__ == "__main__" :
    try :
        while(True) :
            #시간 설정
            now = time.localtime()
            timestamp = ("%04d-%02d-%02d %02d:%02d:%02d" % 
            (now.tm_year, now.tm_mon, now.tm_mday, 
            now.tm_hour, now.tm_min, now.tm_sec))

            values = [0]*8
            for i in range(8) :
                values[i] = mcp.read_adc(i)

            if values[CHANNEL] > 800 :
                print("%s %d (안전)" % (timestamp, values[CHANNEL]))
            elif values[CHANNEL] > 500 :
                print("%s %d (주의)" % (timestamp, values[CHANNEL]))
            else :
                print("%s %d (화재 경보)" % (timestamp, values[CHANNEL]))
            
            time.sleep(1)
    except :
        print("\nPress Ctrl - C")
    finally :
        print("END")
        sys.exit(1)