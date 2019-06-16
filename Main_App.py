from Translator import Translator
from text_to_speech import TextToSpeech
from Speech_to_text import SpeechToText
import Speech_to_text
import Speech_to_text_request
# from speechTranslatorApi import get_audio
# import speechTranslatorApi
import languages
print (languages.languages)
class speech_convert(object):
    def __init__(self):
        self.Translator_subscription_key=""
        self.speech_subscription_key= ""  ## Enter your subscription keys
        self.service_region= "centralindia"
    def speech_to_speech(self, AUDIO_FILE,input_anguage,output_language ):
        text = Speech_to_text_request.handler(AUDIO_FILE, input_anguage)
        print(text)
        translator = Translator(self.Translator_subscription_key)
        translated_text = translator.translator(text, output_language)
        text_to_speech = TextToSpeech(self.speech_subscription_key, translated_text, output_language)
        text_to_speech.get_token()
        self.FileName= 'sample-' + text_to_speech.timestr + '.wav'
        traslated_audio= text_to_speech.save_audio()
        print(type(traslated_audio))
        return traslated_audio
if __name__ == "__main__":
  
    AUDIO_FILE= get_audio.data
    converter= speech_convert()
    translated=converter.speech_to_speech(AUDIO_FILE)
    print(type(translated))
  
