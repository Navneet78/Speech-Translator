import os, requests, time
import languages
from xml.etree import ElementTree
import settings

class TextToSpeech(object):
    def __init__(self, subscription_key,text, output_language):
        self.subscription_key = subscription_key
        self.tts = text
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None
        self.language_pram= languages.languages[output_language]

    def get_token(self):
        fetch_token_url = "https://centralindia.api.cognitive.microsoft.com/sts/v1.0/issueToken"
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscription_key
        }
        response = requests.post(fetch_token_url, headers=headers)
        self.access_token = str(response.text)

    def save_audio(self):
        base_url = 'https://centralindia.tts.speech.microsoft.com/'
        path = 'cognitiveservices/v1'
        constructed_url = base_url + path
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
            'User-Agent': 'YOUR_RESOURCE_NAME'
        }
        xml_body = ElementTree.Element('speak', version='1.0')
        xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', self.language_pram[1])
        voice = ElementTree.SubElement(xml_body, 'voice')
        voice.set('{http://www.w3.org/XML/1998/namespace}lang', self.language_pram[1])
        voice.set('name', self.language_pram[2])
        voice.text = self.tts
        body = ElementTree.tostring(xml_body)

        response = requests.post(constructed_url, headers=headers, data=body)
        if response.status_code == 200:
            with open(settings.output_path+'sample-' + self.timestr + '.wav', 'wb') as audio:
                audio.write(response.content)
                print("\nStatus code: " + str(response.status_code) + "\nEverything Done.\n")
        else:
            print("\nStatus code: " + str(
                response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")


if __name__ == "__main__":
    subscription_key = "33ea2aa9fa6641f0ad7813285f790cc2"
    app = TextToSpeech(subscription_key)
    app.get_token()
    app.save_audio()