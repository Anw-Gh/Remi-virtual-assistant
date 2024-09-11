from elevenlabs.client import ElevenLabs
from elevenlabs import save, stream, Voice, VoiceSettings,play

import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as the source for input.
    with sr.Microphone() as source:
        print("Please say something...")
        
        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text
        
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None





def text_to_speech(text):
    client = ElevenLabs(
      api_key="API_KEY", # Defaults to ELEVEN_API_KEY
    )
    x = len(text)
    if x <=500:
        audio = client.generate(
          text=text,
          voice=Voice(
              voice_id='jBpfuIE2acCO8z3wKNLl',
              settings=VoiceSettings(stability=0.44, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
          ),
            
            
          model="eleven_multilingual_v2"
        )
        
        
        # play(audio,use_ffmpeg=False)
        save(audio,'temp.mp3')
        return 'done'

text ="""
hello there...
 """
text_to_speech(text)