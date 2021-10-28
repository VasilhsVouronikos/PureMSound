import os,sys

def set_settings(channels,sampling_rate,chunk,format):
	with open("settings.pms","w") as f:
		f.write("Sampling rate: "+str(sampling_rate)+"\n")
		f.write("Channels: "+str(channels)+"\n")
		if(chunk == None):
			f.write("Buffer size: "+"Default\n")
		else:
			f.write("Buffer size: "+str(chunk)+"\n")
		if(format == None):
			f.write("Format: "+"Default"+"\n")
		else:
			f.write("Format: "+format+"\n")
		

	return




def update_settings(*args):
	return