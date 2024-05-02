import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()


def listen_continuously():
    # Setup the microphone
    with sr.Microphone() as source:
        print("Calibrating microphone for ambient noise... This will take a few seconds.")
        r.adjust_for_ambient_noise(source, duration=1.0)  # Adjust based on the ambient noise at startup
        print("Calibration complete. Start speaking.")

        while True:  # Infinite loop to keep listening
            try:
                print("Listening...")
                audio = r.listen(source, timeout=5)  # Listen for the next speech
                # Recognize speech using Google Web Speech API
                recognized_text = r.recognize_google(audio)
                print("You said:", recognized_text)
            except sr.WaitTimeoutError:
                print("No speech detected within timeout period. Still listening...")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
    listen_continuously()
