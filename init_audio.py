import numpy as np
import os,sys
import pyaudio as pa
import wave
import struct

CHUNK = 1024 * 2
MODE = 'FX'
WAV = 'samples\\guitar\\acousticg.wav'

p = pa.PyAudio()

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

