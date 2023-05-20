#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

int Sound2_sensorPin = A2;
int Flame_sensorPin = 7;

void setup() {
  Serial.begin(4800);

  pinMode(Sound2_sensorPin, INPUT);
  pinMode(Flame_sensorPin, INPUT);

  while (!Serial);

  Serial.println("Adafruit MLX90614 test");

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };

  Serial.print("Emissivity = "); Serial.println(mlx.readEmissivity());
  Serial.println("================================================");
}

void loop() {

  int Sound2_value = analogRead(Sound2_sensorPin);
  int Flame_value = digitalRead(Flame_sensorPin);

  // Serial.print("Sound2 Sensor Value: ");       
  Serial.print(Sound2_value); Serial.print(",");

  // Serial.print("Ambient = "); 
  Serial.print(mlx.readAmbientTempC()); // 주변 온도
  Serial.print("*C,"); 
  Serial.print(mlx.readObjectTempC()); Serial.print("*C"); // 타겟 온도
  // Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF());
  // Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F");

  if(Flame_value == 0){
    Serial.println("Fire!!"); // 0값이 나오면 화재 발생
  }
  else{ // 평소에는 1값이 나옴.
    //Serial.println("OFF"); 
  }

  Serial.println();
  delay(1000);
}