#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

int Sound2_sensorPin = A2;

void setup() {
  Serial.begin(2000000);

  pinMode(Sound2_sensorPin, INPUT);

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

  // Serial.print("Sound2 Sensor Value: ");       
  Serial.print(Sound2_value); Serial.print(",");

  // Serial.print("Ambient = "); 
  Serial.print(mlx.readAmbientTempC()); // 주변 온도
  Serial.print(","); 
  Serial.println(mlx.readObjectTempC()); //Serial.println("*C"); // 타겟 온도
  // Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF());
  // Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F");

  delay(0.1);
}