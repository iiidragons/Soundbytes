import azure.cognitiveservices.speech as speechsdk
import keys

# Replace with your subscription key and region
subscription_key = keys.azure_key
region = "centralus"

def vocalize (text):
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioOutputConfig(filename="static/file.wav") # type: ignore


    
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.


    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    
    

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted: # type: ignore
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled: # type: ignore
        cancellation_details = speech_synthesis_result.cancellation_details # type: ignore
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

