#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

int Flame_sensorPin = 7;

void setup() {
  Serial.begin(4800);

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

  int Flame_value = digitalRead(Flame_sensorPin);

  Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempC());
  Serial.print("*C\tObject = "); Serial.print(mlx.readObjectTempC()); Serial.println("*C");
  Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF());
  Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F");

  if(Flame_value == 0){
    Serial.println("Fire!!");
  }
  else{
    //Serial.println("OFF"); 
  }

  Serial.println();
  delay(1000);
}