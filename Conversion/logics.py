import speech_recognition as sr


def speech_translation(path):
    r = sr.Recognizer()
    
    try:
        with sr.AudioFile(path) as source:
            data = r.record(source)
            
        text = r.recognize_google(data, language="ru-RU")
    except:
        print("error")
        
    return text
        
        

