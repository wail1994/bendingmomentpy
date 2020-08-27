from numpy import *
import matplotlib.pyplot as plt

from matplotlib import animation



P=100    # = load

L=10     # = Length of Beam

LS=5     # = posiotion of load<- **I want to change the value from 0 to 10 by 0.01.**



R1 = P * (L - LS) / (L)

R2 = P * LS / (L)



SF1 = R1

SF2 = R2





x_beam = arange(0, L, .01)

p_beam = x_beam * 0





x1 = arange(0, LS, .01)

p1 = (x1 * 0 + R1)





x2 = arange(R1, -R2, -.01)

p2 = x2 * 0 + LS




x3 = arange(LS, L, .01)

p3 = -(x3 * 0 + R2)




bend1 = R1 * x1

bend2 = R1 * x3 - P * (x3 - LS)




plt.figure(figsize=(10, 8))

plt.subplots_adjust(hspace=0.5)  # left,right,bottom,top,wspace,hspace





### Shear Force Diagram

plt.subplot(2, 1, 1)

plt.plot(x_beam, p_beam, '4b')

plt.plot(x1, p1, 'r', x3, p3, 'r')

plt.plot(p2, x2, 'r')

plt.xlim(0, L)

plt.ylim(-P - 10, P + 10)

plt.xlabel('Length')

plt.ylabel('Shear Force')

plt.title('Shear Force Diagram')





### Bending Moment Diagram

plt.subplot(2, 1, 2)

plt.xlim(0, L)

plt.plot(x_beam, p_beam, '4b')

plt.plot(x1, bend1, 'r', x3, bend2, 'r')

plt.xlabel('Length')

plt.ylabel('Moment')

plt.title('Bending Moment Diagram')

plt.show()