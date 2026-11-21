# код для управления электромотором робота

class RobotMotor:
    def __init__(self):
        self.speed = 0
    def set_speed(self, value):
        self.speed = max(0, min(100, value,) step=0.01, interval=0.1)
        print("Скорость моторов:", self.speed)
    def stop(self):
        self.speed = 0
        print("Моторы остановленны")

motor = RobotMotor()
while True:
    cmd = input("Введите скорость (0-100) или stop: ")
    if cmd == "stop":
        motor.stop()
        break
    if cmd.isdigit():
        motor.set_speed(int(cmd))
