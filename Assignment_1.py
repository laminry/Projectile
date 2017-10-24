import matplotlib.pyplot as plots
import math,numpy as np

gravity = 9.81
output = int(input("No. Graphs: "))

for x in range(output):

    velocity = int(input("Initial Velocity (m/s): "))
    angle = int(input("Angle measured in degrees: "))
    radian = (math.pi/180) * angle
    movement = (2 * velocity * (math.sin(radian))) / gravity
    height = ((velocity**2)*(math.sin(radian)**2))/(2*gravity)
    movement_1 = ((velocity ** 2) * (math.sin(radian * 2))) / gravity

    (listx,listy) = ([],[])

    for x in (np.arange(0, int(movement), 0.01)):
        x_movement = velocity * x
        x_velocity = math.cos(radian) * velocity
        y_movement = ((math.sin(radian) * velocity) * x) - (gravity * (x ** 2)) / 2
        y_velocity = (math.sin(radian) * velocity) - (gravity * x)
        listx.append(x_movement)
        listy.append(y_movement)

    plots.plot(listx, listy)

plots.show()
