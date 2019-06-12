import numpy as np
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D
from scipy.fftpack import fft

def get_fft(y_val, T, N, f):
	f_val=np.linspace(0.0, 1.0/(2.0*T), N//2)
	fft_val=fft(y_val)
	fft_val=2.0/N * np.abs(fft_val[:N//2])
	return f_val, fft_val

t=10
N=1000
T=t/N
f=1/T

amplitudes=[4, 6, 8, 10, 14]
frequencies=[6.5, 5, 3, 1.5, 1]

x_val=np.linspace(0, t, num=N)
y_val=[amplitudes[i]*np.sin(2*np.pi*frequencies[i]*x_val) for i in range(len(amplitudes))]
composite_y=np.sum(y_val, axis=0)

'''
y_val=[]
for i in range(len(amplitudes)):
	rate=2*np.pi*frequencies[i]
	y_val.append(amplitudes*np.sin(rate)*x_val)
'''

f_val, fft_val=get_fft(composite_y, T, N, f)

'''
plt.plot(f_val, fft_val, linestyle='-', color='blue')
plt.xlabel('Frequency [Hz]', fontsize=16)
plt.ylabel('Amplitude', fontsize=16)
plt.title('Frequency domain of the Signal', fontsize=16)
plt.show()
'''

colors=['k', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']

fig=plt.figure(figsize=(8, 8))
ax=fig.add_subplot(111, projection='3d')

ax.set_xlabel('Time [s]', fontsize=16)
ax.set_ylabel('Frequency [Hz]', fontsize=16)
ax.set_zlabel('Amplitude', fontsize=16)

new_y=[composite_y]+list(reversed(y_val))
frequencies.sort()

for i in range(0, len(new_y)):
	signal=new_y[i]
	color=colors[i]
	length=signal.shape[0]

	x=np.linspace(0, 10, 1000)
	y=np.array([frequencies[i]]*length)
	z=signal

	if i==0:
		linewidth=4
	else:
		linewidth=2

	ax.plot(list(x), list(y), zs=list(z), linewidth=linewidth, color=color)

	x=[10]*75
	y=f_val[:75]
	z=fft_val[:75]*3
	ax.plot(list(x), list(y), zs=list(z), linewidth=2, color='red')

	plt.tight_layout()

plt.show()