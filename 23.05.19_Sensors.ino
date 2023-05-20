#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

int Vibration_sensorPin = A0;
int Sound1_sensorPin = A1;
// int Sound2_sensorPin = A2;
// int Flame_sensorPin = 7;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(4800);                     
  pinMode(Vibration_sensorPin, INPUT);
  pinMode(Sound1_sensorPin, INPUT);
  // pinMode(Sound2_sensorPin, INPUT);
  // pinMode(Flame_sensorPin, INPUT);

// IR_Sensor 코드(필요 없을시 지워도 무방함.)
  while (!Serial);

  // Serial.println("Adafruit MLX90614 test");

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };

  // Serial.print("Emissivity = "); Serial.println(mlx.readEmissivity());
  // Serial.println("================================================");
// IR_Sensor 코드
}

void loop() {
  // put your main code here, to run repeatedly:
  int Vibration_value = analogRead(Vibration_sensorPin);
  int Sound1_value = analogRead(Sound1_sensorPin);
  // int Sound2_value = analogRead(Sound2_sensorPin);
  // int Flame_value = digitalRead(Flame_sensorPin);

  // Serial.print("Vibration Sensor Value: ");       
  Serial.print(Vibration_value); Serial.print(",");

  // Serial.print("Sound1 Sensor Value: ");       
  Serial.print(Sound1_value); Serial.print(",");

  // Serial.print("Sound2 Sensor Value: ");       
  // Serial.print(Sound2_value); Serial.print(",");
  
  // Serial.print("Ambient = "); 
  Serial.print(mlx.readAmbientTempC()); // 주변 온도
  Serial.print("*C,"); 
  Serial.print(mlx.readObjectTempC()); Serial.print("*C"); // 타겟 온도
  // Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF()); // 주변 온도
  // Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F"); // 타겟 온도

  // if(Flame_value == 0){
  //   Serial.println("Fire!!");
  // }
  // else{
  //   //Serial.println("OFF"); 
  // }
  delay(1); // delay(1) 0.001초 간격
}