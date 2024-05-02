import speech_recognition as sr
import noisereduce as nr
import numpy as np

# Initialize the recognizer
r = sr.Recognizer()
r.dynamic_energy_threshold = False
print("Begin")
def recognize_speech_from_mic(language='en-US'):
    # Select language
    if language not in ['en-US', 'km-KH']:
        raise ValueError("Language must be 'en-US' for English or 'km-KH' for Khmer")

    # Capture audio from the microphone
    with sr.Microphone() as source:
        #print("Please wait. Calibrating microphone...")
        # Listen for 1 second and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=1.0)# original duration=1
        print("Adjusted energy threshold to:", r.energy_threshold)

        print("Microphone calibrated. Start speaking...")
        audio = r.listen(source)
        #audio = r.listen(source, timeout=None, phrase_time_limit=10, pause_threshold=0.5)

        # audio = r.listen(source, timeout=None, phrase_time_limit=10)
        # r.pause_threshold = 0.5
        #print("Recording stopped, processing...")

    # Apply noise reduction
    audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
    reduced_noise_audio = nr.reduce_noise(y=np.frombuffer(audio_data, dtype=np.int16), sr=16000)

    # Recognize speech using Google Web Speech API
    try:
        recognized_text = r.recognize_google(audio, language=language)
        print("Recognized speech:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

while True:
    # Example usage:
    print("English recognition:")
    recognize_speech_from_mic('en-US')  # For English
    print("Khmer recognition:")
    recognize_speech_from_mic('km-KH')  # For Khmer
