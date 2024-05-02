from gtts import gTTS
import os


def text_to_speech(text, lang='en'):
    """Convert text to speech."""
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save the converted audio to a file
        filename = "output.mp3"
        tts.save(filename)

        # Playing the converted file
        os.system(f"start {filename}")  # 'start' works on Windows, use 'open' for macOS, or 'xdg-open' for Linux
        print("Playing the converted text...")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
text = "Hello, how are you today?"  # Example text in English
khmer_text = "សួស្តី តើអ្នកសុខសប្បាយទេ?"  # Example text in Khmer

print("English Text-to-Speech:")
text_to_speech(text, lang='en')

print("Khmer Text-to-Speech:")
text_to_speech(khmer_text, lang='km')
