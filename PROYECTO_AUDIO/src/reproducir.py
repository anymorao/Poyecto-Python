#!/usr/bin/python
import pyaudio
import wave

def reproduce(archivo):
	# length of data to read.
	chunk = 1024

	# validation. If a wave file hasn't been specified, exit.
	

	'''
	************************************************************************
	      This is the start of the "minimum needed to read a wave"
	************************************************************************
	'''
	# open the file for reading.
	wf = wave.open(archivo, 'rb')

	# create an audio object
	p = pyaudio.PyAudio()

	# open stream based on the wave object which has been input.
	stream = p.open(format =
		        p.get_format_from_width(wf.getsampwidth()),
		        channels = wf.getnchannels(),
		        rate = wf.getframerate(),
		        output = True)

	# read data (based on the chunk size)
	data = wf.readframes(chunk)

	# play stream (looping from beginning of file to the end)
	while data != '':
	    # writing to the stream is what *actually* plays the sound.
	    stream.write(data)
	    data = wf.readframes(chunk)

	# cleanup stuff.
	stream.close()    
	p.terminate()

def limpiar():
    import os
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        raise "No se puede limpiar la pantalla"
        print  "<-No se pudo borrar la pantalla->"  

