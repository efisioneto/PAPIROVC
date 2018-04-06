import numpy as np
from scipy.io.wavfile import read

a = read("f8_7mic_xm8500_disparo2_mic1.wav")
np.array(a[1],dtype=float)
print(a)

#print (a[1][10000])
