import numpy as np
from cla_utils import *
import matplotlib.pyplot as plt
from tabulate import tabulate
from q2func import *

#2(c)
twoc(10) #produces plots for 2c
plt.close()

#2(d)
#changing one value
twod(1,2**(-53), 10, -1, 1)
twod(1,2**(-5), 10, -1, 1)
twod(1,2**(1), 10, -1, 1)

#changing 3 values
twod(3,2**(-53), 10, -1, 1)
twod(3,2**(-5), 10, -1, 1)
twod(3,2**(1), 10, -1, 1)

#changing five values
twod(5,2**(-53), 10, -1, 1)
twod(5,2**(-5), 10, -1, 1)
twod(5,2**(1), 10, -1, 1)

#changing 7 values
twod(7,2**(-53), 10, -1, 1)
twod(7,2**(-5), 10, -1, 1)
twod(7,2**(1), 10, -1, 1)

#changing 11 values
twod(11,2**(1), 10, -1, 1)
plt.close()

#2(e)
twoe = twoe()
plt.close()

#2(f)
#changing one value
twod(1,2**(-53), 7, -1, 1)
twof(1,2**(-5), 7, -1, 1)
twof(1,2**(1), 7, -1, 1)

#changing 3 values
twod(3,2**(-53), 7, -1, 1)
twof(3,2**(-5), 7, -1, 1)
twof(3,2**(1), 7, -1, 1)

#changing five values
twod(5,2**(-53), 7, -1, 1)
twof(5,2**(-5), 7, -1, 1)
twof(5,2**(1), 7, -1, 1)

#changing 7 values
twof(7,2**(1), 7, -1, 1)
plt.close()




