# Author: Elton Shumka; February 25th 2022

import matplotlib.pyplot as plt
import numpy as np
import math

def plot(positions, timepoints, velocities, accelerations, hpoint):
    fig, (sp1, sp2, sp3) = plt.subplots(1,3)
    sp1.plot(timepoints, positions, color='Red')
    sp1.axvline(hpoint)
    sp1.axhline(0, color='Black')
    sp1.set_xlabel('time (s)')
    sp1.set_ylabel('height (m)')
    sp2.plot(timepoints, velocities, color='Orange')
    sp2.axvline(hpoint)
    sp2.axhline(0, color='Black')
    sp2.set_xlabel('time (s)')
    sp2.set_ylabel('velocity (m/s)')
    sp3.plot(timepoints, accelerations)
    sp3.axvline(hpoint)
    sp3.set_xlabel('time (s)')
    sp3.set_ylabel('acceleration (m/s^2)')
    plt.show()

