from pydub import AudioSegment

def convert_m4a_wav(path_m4a : str):
    wav_output = "output.wav"
    
    sound = AudioSegment.from_file(path_m4a, format="m4a")
    file_handle = sound.export(wav_output, format="wav")
    
    return wav_output
    
def convert_mp3_wav(path_mp3 : str):
    wav_output = "output.wav"
    
    sound = AudioSegment.from_file(path_mp3, format="mp3")
    file_handle = sound.export(wav_output, format="wav")
    
    return wav_output