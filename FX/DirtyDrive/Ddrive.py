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
import pyaudio as np
import wave
import struct
from sklearn import preprocessing

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

def update(paudio,frame,stream,buffer_size):
	data_out = frame.readframes(buffer_size) 
	while len(data_out) > 0:
		stream.write(data_out)
		data_out = frame.readframes(buffer_size)
		data_in = struct.unpack(str(2 * buffer_size) + 'h', data_out)
		
		modified_data = set_drive(data_in)
		data_out = struct.pack(str(2*buffer_size)+'h', *modified_data)
	stream.stop_stream()
	stream.close()
	paudio.terminate()


def apply_fft():
 	return

# -- TO DO -------
# Normalize incoming data

def set_drive(data_in):
	new_data = []
	for i in range(len(data_in)):
		if data_in[i] > -100:
			new_data.append(-100)
		else:
			new_data.append(data_in[i])
	new_data = tuple(new_data)
	
	return new_data


def set_gain():
	return

def filter():
	return


if __name__ == '__main__':
	p,wf,stream,CHUNK = init()
	update(p,wf,stream,CHUNK)
