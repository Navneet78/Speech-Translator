import json
import requests
import languages
API_KEY = ''   ## Eneter your own key and service region
REGION = 'centralindia'
MODE = 'dictation'
LANG = 'it-IT'
FORMAT = 'simple'


def handler(AUDIO_FILE, input_language):
    token = get_token()
    results = get_text(token, AUDIO_FILE, input_language)
    print(results)
    return (results['DisplayText'])

def get_token():
    url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': API_KEY
    }
    r = requests.post(url, headers=headers)
    token = r.content
    return(token)

def get_text(token, audio,input_language):
    url = 'https://{0}.stt.speech.microsoft.com/speech/recognition/{1}/cognitiveservices/v1?language={2}&format={3}'.format(REGION, MODE, languages.languages[input_language][1], FORMAT)
    headers = {
        'Accept': 'application/json',
        'Ocp-Apim-Subscription-Key': API_KEY,
        # 'Transfer-Encoding': 'chunked',
        'Content-type': 'audio/wav; codec=audio/pcm; samplerate=16000',
        'Authorization': 'Bearer {0}'.format(token),
        # 'Expect': '100-continue'
    }
    r = requests.post(url, headers=headers, data=stream_audio_file(audio))
    results = json.loads(r.content)
    return results

def stream_audio_file(speech_file, chunk_size=1024):
    with open(speech_file, 'rb') as f:
        while 1:
            data = f.read()
            if not data:
                break
            yield data

if __name__ == '__main__':
    handler()
