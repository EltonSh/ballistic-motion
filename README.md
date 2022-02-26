# ballistic-motion
This is a very simple scenario from classical physics, called ballistic motion. It involves the motion of an object in 2-D, such as a projectile shot at an angle from Earth's surface, with a specified initial velocity vector.
In the ideal case, with no air drag involved, the solution can be found quite easily in analytic fashion.
However, when air drag is involved, two new terms appear in the differential equation describing the motion and the analytical solution is no longer possible. 
Therefore a numerical solution is required. Here we implement the Euler method to solve the problem. The differential equations to be solved are:
x(t+1) = x(t) + V(t)* dt
V(t+1) = V(t) + (-g - (1/m)* k1 * V(t) - (1/m)* k2 * V(t)^2)* dt
a(t) = -g - (1/m)* k1* V(t) - (1/m)* k2* V(t)^2
The coefficients k1 = c1* r  and k2 = c2* r^2, where c1 and c2 model the air drag and are called the pressure term (dominates for small velocities) and the viscous term (dominates for large velocities). Their values for air are correspondingly: c1 = 3.1e-4 (kg/m)/s and c2 = 0.85 kg/m^3. 
The plots that are produced and stored in the plots folder, are obtained for the above values of the coefficients and for the motion of a pebble with m=0.01kg and r=0.01m. 
