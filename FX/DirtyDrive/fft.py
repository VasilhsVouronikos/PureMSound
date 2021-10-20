import numpy as np


def audio_fft(signal):
	fft = np.fft.fft(signal)
	amp = np.abs(fft)
	freq = np.fft.fftfreq(signal.shape[-1])
	return amp,freq


def audio_invfft():
	return