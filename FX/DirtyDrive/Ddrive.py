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
import keyboard

global RECEIVED,VAL

RECEIVED = False
VAL = 0


CHUNK = 1024 * 2
MODE = 'FX'
WAV = 'samples\\bass\\bass4.wav'

p = pa.PyAudio()


PATH = "\\Audio_apps\\PureMSound\\outputs\\Ddrive.wav"


from scipy.io.wavfile import write
wav_frames = []

def update(paudio,frame,stream,buffer_size):
	global RECEIVED,VAL
	wav_file = set_output(frame)

	data_out = frame.readframes(buffer_size) 
	while len(data_out) > 0:
		stream.write(data_out)
		data_out = frame.readframes(buffer_size)
		data_out_list = list(data_out)
		if(RECEIVED):
			modified_data,data_np = set_drive(data_out_list,VAL)
			data_out = bytes(modified_data)
		else:
			data_out = bytes(data_out)
		wav_file.writeframesraw(data_out)
	
	stream.stop_stream()
	stream.close()
	paudio.terminate()


def change_drive(val):
	global RECEIVED,VAL
	RECEIVED = True
	VAL = val

def reset_to_original():
	global RECEIVED,VAL
	RECEIVED = False
	VAL = 0



def apply_fft(signal):
	amp,freq = audio_fft(signal)
	return amp,freq


def set_drive(data_in,val):
	new_data = []
	for i in range(len(data_in)):
		if data_in[i] > val:
			new_data.append(val)
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

def init():
	if(MODE == 'FX'):
		wf = wave.open(WAV, 'rb')
		stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
			channels=wf.getnchannels(),
			rate=wf.getframerate(),
			output=True)


	latency = stream.get_output_latency()
	input_device = list(p.get_default_input_device_info().values())[2]
	output_device = list(p.get_default_output_device_info().values())[2]


	get_sound_info(latency,input_device,output_device)
	return p,wf,stream,CHUNK,WAV

def get_sound_info(lat,inputd,output):
	print("Output latency: ",lat,"\n",
		"Input device(mic): ",inputd,"\n",
		"Output device: ",output)

if __name__ == '__main__':
	p,wf,stream,CHUNK,WAV = init()
	update(p,wf,stream,CHUNK)