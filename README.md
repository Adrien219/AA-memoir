#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <RTClib.h>
#include <DHT.h>

// --- CONFIGURATION PINS ---
#define TRIG_PIN 2
#define ECHO_PIN 3
#define JOY_BTN 4
#define DHT_PIN 5
#define FISH_PIN 6  // Capteur obstacle IR
#define LIGHT_PIN 7
#define BUZZER_PIN 9
#define VIBREUR_PIN 10
#define RGB_R 11
#define RGB_G 12
#define RGB_B 13
#define JOY_X A0
#define JOY_Y A1
#define GAS_PIN A2
#define SOUND_PIN A3

// --- OBJETS ---
DHT dht(DHT_PIN, DHT11);
LiquidCrystal_I2C lcd(0x27, 16, 2); // Adresse I2C 0x27 ou 0x3F
RTC_DS3231 rtc;

void setup() {
  Serial.begin(115200);
  
  // Initialisation capteurs/actuateurs
  dht.begin();
  lcd.init();
  lcd.backlight();
  if (!rtc.begin()) { /* RTC non trouvé */ }

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(JOY_BTN, INPUT_PULLUP);
  pinMode(FISH_PIN, INPUT);
  pinMode(LIGHT_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(VIBREUR_PIN, OUTPUT);
  pinMode(RGB_R, OUTPUT);
  pinMode(RGB_G, OUTPUT);
  pinMode(RGB_B, OUTPUT);

  lcd.setCursor(0,0);
  lcd.print("SmartGlasses OS");
}

void loop() {
  // 1. DISTANCE ULTRASON
  digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long dist = pulseIn(ECHO_PIN, HIGH) * 0.034 / 2;

  // 2. ENVIRONNEMENT
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  int gas = analogRead(GAS_PIN);
  int sound = analogRead(SOUND_PIN);
  int ir_obs = digitalRead(FISH_PIN); // 0 si obstacle, 1 si rien
  int light = digitalRead(LIGHT_PIN); 

  // 3. JOYSTICK
  int x = analogRead(JOY_X);
  int y = analogRead(JOY_Y);
  int btn = !digitalRead(JOY_BTN); // Inversé car Pullup

  // 4. TEMPS (RTC)
  DateTime now = rtc.now();

  // 5. AFFICHAGE LCD (Local)
  lcd.setCursor(0,1);
  lcd.print(dist); lcd.print("cm ");
  lcd.print(t, 0); lcd.print("C  ");
  lcd.print(now.hour()); lcd.print(":"); lcd.print(now.minute());

  // 6. LOGIQUE DE SÉCURITÉ (Feedback direct)
  if (gas > 400 || dist < 15) {
    digitalWrite(VIBREUR_PIN, HIGH);
    digitalWrite(RGB_R, HIGH);
    digitalWrite(RGB_B, LOW);
  } else {
    digitalWrite(VIBREUR_PIN, LOW);
    digitalWrite(RGB_R, LOW);
    digitalWrite(RGB_G, HIGH); // Vert si tout va bien
  }

  // 7. ENVOI JSON VERS PYTHON
  Serial.print("{");
  Serial.print("\"dist\":"); Serial.print(dist);
  Serial.print(",\"gas\":"); Serial.print(gas);
  Serial.print(",\"temp_ext\":"); Serial.print(isnan(t) ? 0 : t);
  Serial.print(",\"hum\":"); Serial.print(isnan(h) ? 0 : h);
  Serial.print(",\"son\":"); Serial.print(sound);
  Serial.print(",\"lum\":"); Serial.print(light);
  Serial.print(",\"joy_x\":"); Serial.print(x);
  Serial.print(",\"joy_y\":"); Serial.print(y);
  Serial.print(",\"btn\":"); Serial.print(btn);
  Serial.print(",\"obs\":"); Serial.print(ir_obs);
  Serial.print(",\"time\":\""); Serial.print(now.hour()); Serial.print(":"); Serial.print(now.minute()); Serial.print("\"");
  Serial.println("}");

  delay(500);
}