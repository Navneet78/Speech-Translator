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


if __name__ == "__main__":
    subscription_key = "135c0b93f9504b4e9dad8b53f0e052c6"
    service_region= "centralindia"
    app = Translator(subscription_key)
    text= input()
    app.translator(text)

# subscriptionKey = '135c0b93f9504b4e9dad8b53f0e052c6'
# base_url = 'https://api.cognitive.microsofttranslator.com'
# path = '/translate?api-version=3.0'
# params = '&to=hi'
# constructed_url = base_url + path + params
# headers = {
#     'Ocp-Apim-Subscription-Key': subscriptionKey,
#     'Content-type': 'application/json',
#     'X-ClientTraceId': str(uuid.uuid4())
# }
# text= input()
# body = [{
#     'text' : text
# }]
# request = requests.post(constructed_url, headers=headers, json=body)
# response = request.json()
# print(response[0]['translations'][0]['text'])
# print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))