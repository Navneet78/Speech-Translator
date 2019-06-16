import azure.cognitiveservices.speech as speechsdk

class SpeechToText():
    def __init__(self, subscription_key, service_region):
        self.subscription_key = subscription_key
        self.service_region= service_region

    def configuration(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.subscription_key, region=self.service_region)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        self.recognizer= speech_recognizer

    def speech_to_text(self):
        print("Say something...")
        result = self.SetInputToWaveFile('/sample-20190611-1156.wav')
        # result=open('sample-20190611-1156.wav', 'r')
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(result.text))
            return (format(result.text))
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))

if __name__ == "__main__":
    subscription_key = ""  ## Enter here your subscription Key
    service_region= ""  ##enter your service region
    app = SpeechToText(subscription_key, service_region)
    app.configuration()
    app.speech_to_text()
