import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.fftpack
import scipy.signal
import scipy.io.wavfile
import pandas
import copy

#author: Larissa Fogaça - FFT
## audios dos passarinhos:  https://www.xeno-canto.org/403881)

fs,bc = scipy.io.wavfile.read('queroquero.wav')

# vetor de tempo criado com base na taxa de amostragem de dados
n = len(bc)
timevec = np.arange(0,n)/fs

# traçando os dados dos dois canais do áudio
plt.plot(timevec,bc)
plt.xlabel('Tempo (segundos)')
plt.title('Time domain')
plt.show()

# calculando o espectro
hz = np.linspace(0,fs/2,int(np.floor(n/2)+1))
bcpow = np.abs(scipy.fftpack.fft( scipy.signal.detrend(bc[:,0]) )/n)**2


# lendo ele
plt.plot(hz,bcpow[0:len(hz)])
plt.xlabel('Frequência (Hz)')
plt.title('Frequency domain')
plt.xlim([0,8000])
plt.show()

## análise do tempo e frequência via espectrograma

frex,time,pwr = scipy.signal.spectrogram(bc[:,0],fs)

plt.pcolormesh(time,frex,pwr,vmin=0,vmax=9)
plt.title('PAPAGAIO TESTE TCC')
plt.xlabel('Time (s)'), plt.ylabel('Frequency (Hz)')
plt.show()