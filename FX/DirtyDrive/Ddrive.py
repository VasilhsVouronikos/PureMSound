'''
	This code implements a simple drive effect
	controling the amount of drive and gain.
	All the ajducements will be made purely
	from playing with fft of the incoming signal.

	** 
		Cliping the incoming data which are 16 bit ints
		in a certain value will have the same effect
		as a traditional analog effect pedal where
		a diode clips the signal to 0.7 volts.

		We can further do some filtering to some
		noise in certain frequencies.

	**

	Hopefully we will avoid c++ once forever.

	PureMSound we will have a GUI in the future.

'''

import numpy as np 
import os,sys
import pyaudio as pa
import wave
import struct
from sklearn import preprocessing
import librosa

PATH = "\\Audio_apps\\PureMSound\\outputs\\Ddrive.wav"

def get_current_path():
	path = os.getcwd().split("\\")
	path.pop(0)
	path.pop(len(path)-1)
	path.pop(len(path)-1)
	new_path = "\\"+"\\".join(path)
	
	return new_path

path_to_tools = get_current_path()

sys.path.insert(0,path_to_tools)



from fft import audio_fft,audio_invfft
from init_audio import init
from visualizer import display_signal
from scipy.io.wavfile import write
wav_frames = []

def update(paudio,frame,stream,buffer_size):
	wav_file = set_output(frame)

	data_out = frame.readframes(buffer_size) 
	while len(data_out) > 0:

		stream.write(data_out)
		data_out = frame.readframes(buffer_size)
		d = list(data_out)
		modified_data,data_np = set_drive(d)
		data_out = bytes(modified_data)
		wav_file.writeframesraw(data_out)
	
	stream.stop_stream()
	stream.close()
	paudio.terminate()

	


def apply_fft(signal):
	amp,freq = audio_fft(signal)
	return amp,freq

# -- TO DO -------
# Normalize incoming data

def set_drive(data_in):
	new_data = []
	for i in range(len(data_in)):
		if data_in[i] > 250:
			new_data.append(250)
		else:
			new_data.append(data_in[i])
	data_np = np.asarray(new_data, dtype=np.int16)
	new_data = tuple(new_data)
	
	return new_data,data_np


def set_gain():
	return

def filter():
	return

def set_output(frame):
	nchannels = frame.getnchannels()
	sampwidth = frame.getsampwidth()
	framerate = frame.getframerate()
	nframes = frame.getnframes()
	comptype = "NONE"
	compname = "not compressed"
	wav_file = wave.open("Ddrive.wav", "w")

	wav_file.setparams((nchannels, sampwidth, framerate, nframes,
						comptype, compname))

	return wav_file

if __name__ == '__main__':
	p,wf,stream,CHUNK,wav = init()
	update(p,wf,stream,CHUNK)
	#write_to_wav(wf,CHUNK)
