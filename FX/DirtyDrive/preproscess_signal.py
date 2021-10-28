# Before overdriving the signal
#    we must preproscess it to remove
#    uneccesery noises
# So we can implement a filter chain

import numpy as np
from fft import audio_fft,audio_invfft
from librosa import core
import wave


FILTER_CHAIN = {'enoise':60.0,
				'high_noise':6000.0,
				'middle_noise':300.0,
				'very_high_noise':12000.0}


def filter(data,sfreq):
	data_out = []
	amp,freq,fft_data = audio_fft(data,sfreq)
	for i in range(len(freq)):
		if(freq[i] <= FILTER_CHAIN['enoise']):
			fft_data[i] = 0.0
		if(freq[i] <= FILTER_CHAIN['high_noise']):
			fft_data[i] = 0.0
		if(freq[i] <= FILTER_CHAIN['very_high_noise']):
			fft_data[i] = 0.0
		else:
			continue
	noiseless_signal = audio_invfft(fft_data)
	return noiseless_signal

def load_audio(WAV):
	samples,sampling_freq = core.load(WAV,sr = None,mono = True, offset = 0.0, duration = None)

	return samples,sampling_freq


def run_preproscess(WAV):
	samples,sfreq = load_audio(WAV)
	noiseless_signal = filter(samples,sfreq)

	return noiseless_signal

def palyback(signal):
	
