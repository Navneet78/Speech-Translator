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
        self.Translator_subscription_key="135c0b93f9504b4e9dad8b53f0e052c6"
        self.speech_subscription_key= "33ea2aa9fa6641f0ad7813285f790cc2"
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
    # Translator_subscription_key = "135c0b93f9504b4e9dad8b53f0e052c6"
    # speech_subscription_key= "33ea2aa9fa6641f0ad7813285f790cc2"
    # AUDIO_FILE = "C:\\Navneet\Text_to_speech\sample-20190611-1156.wav"
    AUDIO_FILE= get_audio.data
    converter= speech_convert()
    translated=converter.speech_to_speech(AUDIO_FILE)
    print(type(translated))
    # service_region= "centralindia"
    # Speech= SpeechToText(speech_subscription_key,service_region)
    # Speech.configuration()
    # text= Speech.speech_to_text()
    # text=Speech_to_text_request.handler(AUDIO_FILE)
    # translator= Translator(Translator_subscription_key)
    # translated_text= translator.translator(text)
    # text_to_speech= TextToSpeech(speech_subscription_key,translated_text)
    # text_to_speech.get_token()
    # text_to_speech.save_audio()
    # text= input()
    # app.translator(text)