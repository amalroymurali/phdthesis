 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.seterr(all='ignore')
plt.style.use(['science','ieee'])
plt.rcParams['figure.dpi'] = 200
plt.rcParams['savefig.dpi'] = 300
mpl.rcParams['figure.autolayout'] = True
plt.rcParams['figure.figsize'] = (3.14, 3.14*0.618)
plt.rcParams.update({'font.size': 10})
