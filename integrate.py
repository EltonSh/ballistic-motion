# Author: Elton Shumka;  February 25th 2022

import math
import numpy as np


def integrate(Ynew, Yold, Vold, told, k1, k2, g, m, r, deltat):
    positions = list()
    timepoints = list()
    velocities = list()
    accelerations = list()
    while (Ynew >= 0):
        timepoints.append(told)
        tnew = told + deltat
        told = tnew
        positions.append(Yold)
        Ynew = Yold + (Vold)*deltat
        Yold = Ynew
        velocities.append(Vold)
        Vnew = Vold + (-g - (1/m)*k1*Vold - (1/m)*k2*Vold*abs(Vold))*deltat
        if (Vnew <= 0 and Vold > 0):
            print(f"The highest point reached: {Ynew} at time {tnew}")
            hpoint = tnew
        Vold=Vnew
        acc = -g - (1/m)*k1*Vold - (1/m)*k2*Vold*abs(Vold)
        accelerations.append(acc)
    return positions, timepoints, velocities, accelerations, hpoint
