int vel = 130;

// left wheels
#define leftWheels_LPWM 2
#define leftWheels_RPWM 4

// right wheels
#define rightWheels_LPWM 7
#define rightWheels_RPWM 8

/*
 * forward --> rw_RPWM, lw_RPWM = True, rw_LPWM, lw_LPWM = False
 * backward --> rw_LPWM, lw_LPWM = True, rw_RPWM, lw_RPWM = False
 * left --> rw_RPWM, lw_LPWM = True, rw_LPWM, lw_RPWM = False
 * right --> rw_LPWM, lw_RPWM = True, rw_RPWM, lw_LPWM = False
 */

void go(int dir){
  // forward, backward, left, right
  String dir_names[5] = {"forward", "backward", "left", "right", "stop"};
  int dirs[5][4] = {{vel, vel, 0, 0}, {0, 0, vel, vel}, {vel, 0, vel, 0}, {0, vel, 0, vel}, {0, 0, 0, 0}};
  // in each direction array, the formation is --> {rw_RPWM, lw_RPWM, rw_LPWM, lw_LPWM}
  Serial.println(dir_names[dir]);

  analogWrite(rightWheels_RPWM, dirs[dir][0]);
  analogWrite(leftWheels_RPWM, dirs[dir][1]);
  analogWrite(rightWheels_LPWM, dirs[dir][2]);
  analogWrite(leftWheels_RPWM, dirs[dir][3]);

  delay(2000);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(leftWheels_LPWM, OUTPUT);
  pinMode(rightWheels_LPWM, OUTPUT);
  pinMode(leftWheels_RPWM, OUTPUT);
  pinMode(rightWheels_RPWM, OUTPUT);

}

void loop(){
  analogWrite(leftWheels_LPWM, vel);
  analogWrite(leftWheels_RPWM, 0);
  analogWrite(rightWheels_LPWM, vel);
  analogWrite(rightWheels_RPWM, 0);
  delay(2000);
  analogWrite(leftWheels_LPWM, 0);
  analogWrite(leftWheels_RPWM, 0);
  analogWrite(rightWheels_LPWM, 0);
  analogWrite(rightWheels_RPWM, 0);
  delay(3000);


}
