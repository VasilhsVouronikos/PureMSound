import numpy as np
import os,sys
import pyaudio as pa
import wave
import struct

CHUNK = 1024 * 2
MODE = 'FX'
WAV = 'acousticg.wav'


def init():
	p = pa.PyAudio()
	if(MODE == 'FX'):
		wf = wave.open('acousticg.wav', 'rb')
		stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
			channels=wf.getnchannels(),
			rate=wf.getframerate(),
			output=True)

	return p,wf,stream,CHUNK,WAV

