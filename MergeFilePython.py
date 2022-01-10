import wave
import os
from pydub import AudioSegment
import sys, getopt, argparse

my_parser = argparse.ArgumentParser(description='Convert Audio')

# Add the arguments
my_parser.add_argument('raw', type=str, help='the path to raw audio folder',)
my_parser.add_argument('wav', type=str, help='the path to wav audio folder',)
my_parser.add_argument('mp3', type=str, help='the path to wav audio folder',)

# Execute the parse_args() method
args = my_parser.parse_args()
os.chdir(args.raw) # Navigate to folder contain unconverted audio
FILES = os.listdir()
count = 0

for file in FILES:
    if os.path.isfile(file):
        with open(file, 'rb') as pcmfile:
            pcmdata = pcmfile.read()
        # with wave.open(f"C:\\Users\\Unknown\\Desktop\\Sample\\wav\\{file}", 'wb') as wavfile:
        with wave.open(f"{args.wav}\\{file}", 'wb') as wavfile: # Save file converted to sys.arg[1]
            wavfile.setparams((1, 2, 8000, 152325, 'NONE', 'NONE'))
            wavfile.writeframes(pcmdata)
            # print(f"Converted {file} to wav format!")

os.chdir(args.wav) # Navigate to wav folder
for file in FILES:

    if file.endswith("in.wav"):

        # print(f"STT: {count} ----> {file.split('in.wav')[0]}")
        count += 1
        subtring = file.split('-in.wav')[0]
        in_file = file
        # print(f"STT: {count} --- In File ---> {file} ")
    
    else:
        if subtring in file:
            out_file = file
            # print(f"STT: {count} --- Out File ---> {file} ")
    
        audio1 = AudioSegment.from_wav(f"./{in_file}")
        audio2 = AudioSegment.from_wav(f"./{out_file}")
        mixed_file = audio1.overlay(audio2)
        mixed_file.export(f"{args.mp3}\\{subtring}.mp3", format='mp3')
        print(f"STT {count} ---> File {subtring} mix successful!")

# # obj = wave.open('1753-000ac8ba-1641460100.835329-in.wav','r')
# # print( "Number of channels",obj.getnchannels())
# # print ( "Sample width",obj.getsampwidth())
# # print ( "Frame rate.",obj.getframerate())
# # print ("Number of frames",obj.getnframes())
# # print ( "parameters:",obj.getparams())
# # obj.close()