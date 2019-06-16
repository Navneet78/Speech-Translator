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
    subscription_key = "33ea2aa9fa6641f0ad7813285f790cc2"
    service_region= "centralindia"
    app = SpeechToText(subscription_key, service_region)
    app.configuration()
    app.speech_to_text()

# speech_key, service_region = "33ea2aa9fa6641f0ad7813285f790cc2", "centralindia"
# speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# print("Say something...")
#
#
# # Starts speech recognition, and returns after a single utterance is recognized. The end of a
# # single utterance is determined by listening for silence at the end or until a maximum of 15
# # seconds of audio is processed.  The task returns the recognition text as result.
# # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# # shot recognition like command or query.
# # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
# result = speech_recognizer.recognize_once()
#
# # Checks result.
# if result.reason == speechsdk.ResultReason.RecognizedSpeech:
#     print("Recognized: {}".format(result.text))
# elif result.reason == speechsdk.ResultReason.NoMatch:
#     print("No speech could be recognized: {}".format(result.no_match_details))
# elif result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = result.cancellation_details
#     print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         print("Error details: {}".format(cancellation_details.error_details))