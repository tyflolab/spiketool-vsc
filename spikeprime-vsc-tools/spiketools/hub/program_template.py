from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer

hub = PrimeHub()

hub.light_matrix.show_image('HAPPY')

hub.speaker.beep(60, 0.5)
hub.speaker.beep(67, 0.5)
hub.speaker.beep(60, 0.5)