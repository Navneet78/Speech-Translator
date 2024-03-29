import os, requests, uuid, json
import languages
class Translator(object):
    def __init__(self, subscriptionKey):
        self.subscriptionKey = subscriptionKey

    def translator(self, text, output_language):
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/translate?api-version=3.0'
        params = '&to='+languages.languages[output_language][0]
        constructed_url = base_url + path + params
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }
        body = [{
            'text': text
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        print(response[0]['translations'][0]['text'])
        return (response[0]['translations'][0]['text'])
