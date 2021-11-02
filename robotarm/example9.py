from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for x in range(1,5):
    for y in range(x):
        robotArm.grab()
        for c in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for d in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()
