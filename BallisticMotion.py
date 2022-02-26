# 12 November 2021

import math
import numpy as np
import matplotlib.pyplot as plt
import integrate
import makeplots

# Ballistic motion with air drag is governed by the equations: (in the vertical direction)
# V = V0 - g*t - (1/m)*k1*V*t - (1/m)*k2*V^2*t
# dy/dt = V
# dV/dt = -g - (1/m)*k1*V - (1/m)*k2*V^2
# We study the case of a pebble with radius r=0.01m and mass m=0.01kg, in air
# The corresponding coefficients are k1 = c1*r and k2 = c2*r^2, where c1=3.1e-4 (kg/m)/sec and c2=0.85kg/m^3

if __name__ == "__main__":
    r = 0.04
    m = 0.01  # kg
    g = 10 # m/s^2
    c1 = 3.1e-4  
    c2 = 0.85  
    k1 = c1*r
    k2 = c2*r*r 
    deltat = 0.01  # seconds
    told = 0  # seconds
    Yold = 0  # meters
    Ynew = 0
    Vold = 300 # m/s
    Vnew = 30
    positions, timepoints, velocities, accelerations, hpoint = integrate.integrate(Ynew, Yold, Vold, told, k1, k2, g, m, r, deltat)
    makeplots.plot(positions, timepoints, velocities, accelerations, hpoint)


