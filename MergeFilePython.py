from pydub import AudioSegment
import sys, argparse, wave, os
from gooey import Gooey, GooeyParser

@Gooey
def main():
    #Gooey parse
    parser = GooeyParser(description="Convert PCM to WAV") 
    parser.add_argument('RawPath', widget="DirChooser")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")    
    
    #Argparse
    my_parser = argparse.ArgumentParser(description='Convert PCM to WAV')

    # Add the arguments
    my_parser.add_argument('RawPath', type=str, help='the path to raw audio folder',)
    my_parser.add_argument('-v', "--verbose",action='store_true', help='increase output verbosity',)
    
    # Execute the parse_args() method
    args = parser.parse_args()


    DIRS = ["wav", "mp3"]
    os.chdir(args.RawPath) # Navigate to folder contain unconverted audio
    for dir in DIRS:
        os.mkdir(dir)
    FILES = os.listdir()
    count = 0

    #Convert PCM file to WAV
    for file in FILES:
        if os.path.isfile(file):
            with open(file, 'rb') as pcmfile:
                pcmdata = pcmfile.read()
            with wave.open(f"{DIRS[0]}\\{file}", 'wb') as wavfile: # Save file converted to sys.arg[1]
                wavfile.setparams((1, 2, 8000, 152325, 'NONE', 'NONE'))
                wavfile.writeframes(pcmdata)
                # print(f"Converted {file} to wav format!")

    os.chdir(DIRS[0]) # Navigate to wav folder
    #Mixing wav and convert to mp3
    for file in FILES:

        if file.endswith("in.wav"):

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
            mixed_file.export(f"..\\{DIRS[1]}\\{subtring}.mp3", format='mp3')
            
            if args.verbose:
                print(f"STT {count} ---> File {subtring} mix successful!")

    print("Total file mixed ---> ", count)

if __name__ == '__main__':

    main()

# # obj = wave.open('1753-000ac8ba-1641460100.835329-in.wav','r')
# # print( "Number of channels",obj.getnchannels())
# # print ( "Sample width",obj.getsampwidth())
# # print ( "Frame rate.",obj.getframerate())
# # print ("Number of frames",obj.getnframes())
# # print ( "parameters:",obj.getparams())
# # obj.close()