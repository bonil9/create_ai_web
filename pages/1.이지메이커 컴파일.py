/* ******************************************
** EZMAKER Online (EZ-ON) code
** ******************************************/
/* <include-default> */
#include <Arduino.h> // Arduino 핵심 라이브러리 포함
#include <Wire.h> // I2C 통신 라이브러리 (사용되지 않지만 기본 포함)
#include <SoftwareSerial.h> // 소프트웨어 시리얼 통신 라이브러리 (사용되지 않지만 기본 포함)
#include "ezmaker_v2.1.h" // EZMAKER 특정 라이브러리 (사용자 환경에 따라 필요)

#define getAnalogData analogRead // 아날로그 데이터 읽기 함수 정의

/* <include-Modules> */
#include "OneWire.h" // OneWire 통신 프로토콜 라이브러리
#include "DallasTemperature.h" // DallasTemperature 센서 (DS18B20) 라이브러리

/* <lib-Default> */

/* <lib-Modules> */
// EZ_D0 핀에 연결된 OneWire 버스 초기화
OneWire oneWire_EZ_D0(EZ_D0);
// oneWire_EZ_D0 버스를 사용하는 DallasTemperature 센서 객체 생성
DallasTemperature sensors_EZ_D0(&oneWire_EZ_D0);

// EZ_D1 핀에 연결된 OneWire 버스 초기화
OneWire oneWire_EZ_D1(EZ_D1);
// oneWire_EZ_D1 버스를 사용하는 DallasTemperature 센서 객체 생성
DallasTemperature sensors_EZ_D1(&oneWire_EZ_D1);

/* <variable-Modules> */
// 추가적인 전역 변수 선언 영역 (현재 없음)

/* <declare-Modules> */
// EZ_D0 핀에 연결된 DS18B20 센서의 온도를 섭씨로 읽는 함수
float readDS18B20TempC_EZ_D0()
{
    sensors_EZ_D0.requestTemperatures(); // 센서에게 온도 측정을 요청
    return sensors_EZ_D0.getTempCByIndex(0); // 첫 번째 센서의 섭씨 온도 반환
}

// EZ_D1 핀에 연결된 DS18B20 센서의 온도를 섭씨로 읽는 함수
float readDS18B20TempC_EZ_D1()
{
    sensors_EZ_D1.requestTemperatures(); // 센서에게 온도 측정을 요청
    return sensors_EZ_D1.getTempCByIndex(0); // 첫 번째 센서의 섭씨 온도 반환
}

/* <code-setup> */
void setup() {
  // EZ_D0 및 EZ_D1 센서 초기화
  sensors_EZ_D0.begin();
  sensors_EZ_D1.begin();
  // 시리얼 통신 시작 (보드레이트 115200)
  Serial.begin(115200);
}

/* <code-loop> */
void loop() {
  // EZ_D0 센서의 온도와 EZ_D1 센서의 온도를 읽어 쉼표로 구분하여 시리얼 출력
  // String() 함수를 사용하여 float 값을 문자열로 변환
  Serial.println((String(readDS18B20TempC_EZ_D0()) + "," + String(readDS18B20TempC_EZ_D1())));
  
  // 1초 (1000 밀리초) 대기
  delay(1000);

  // 이 delay(10)은 위의 delay(1000)으로 인해 거의 의미가 없으므로 제거해도 무방합니다.
  // delay(10); 
}
