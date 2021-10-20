import matplotlib.pyplot as plt
import numpy as np
from librosa import display,core,feature,spectrum
from fft import audio_fft

WAV = 'samples\\bass\\bass4.wav'

def display_signal():
	fig, ax = plt.subplots()
	samples,sampling_freq = core.load(WAV,sr = None,mono = True, offset = 0.0, duration = None)
	D = spectrum.stft(samples)  # STFT of y
	S_db = spectrum.amplitude_to_db(np.abs(D), ref=np.max)
	img = display.specshow(S_db,x_axis='time', y_axis='linear', ax=ax)
	plt.xlabel("Time")
	plt.ylabel("Amplitude")
	fig.colorbar(img, ax=ax, format="%+2.f dB")
	plt.show()

def display_spectrum():
	samples,sampling_freq = core.load(WAV,sr = None,mono = True, offset = 0.0, duration = None)
	amp,freq = audio_fft(samples)
	plt.plot(freq,amp)
	plt.xlabel("Amplitude")
	plt.ylabel("Frequency")
	plt.show()

if __name__ == '__main__':
	display_spectrum()
