import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

def get_fft(y_val, T, N, f):
	f_val=np.linspace(0.0, 1.0/(2.0*T), N//2)
	fft_val=fft(y_val)
	fft_val=2.0/N * np.abs(fft_val[:N//2])
	return f_val, fft_val

t=1
N=100000
T=t/N
f=1/T

xa=np.linspace(0, t, num=N)
xb=np.linspace(0, t/4, num=N/4)

frequencies= np.random.randint(1, 100, 4)
print(frequencies)

y1a, y1b=np.sin(2*np.pi*frequencies[0]*xa), np.sin(2*np.pi*frequencies[0]*xb)
y2a, y2b=np.sin(2*np.pi*frequencies[1]*xa), np.sin(2*np.pi*frequencies[1]*xb)
y3a, y3b=np.sin(2*np.pi*frequencies[2]*xa), np.sin(2*np.pi*frequencies[2]*xb)
y4a, y4b=np.sin(2*np.pi*frequencies[3]*xa), np.sin(2*np.pi*frequencies[3]*xb) 

composite_signal1=y1a+y2a+y3a+y4a
composite_signal2=np.concatenate([y1b, y2b, y3b, y4b])

f_val1, fft_val1=get_fft(composite_signal1, T, N, f)
f_val2, fft_val2=get_fft(composite_signal2, T, N, f)

fig, ax=plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

ax[0, 0].plot(xa, composite_signal1)
ax[1, 0].plot(xa, composite_signal2)
ax[0, 1].plot(f_val1, fft_val1)
ax[1, 1].plot(f_val2, fft_val2)

ax[0, 1].set_xlim([0, 150])
ax[1, 1].set_xlim([0, 150])

plt.tight_layout()
plt.show()