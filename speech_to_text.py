import speech_recognition as sr

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Please speak into the microphone...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("✅ Audio captured, transcribing...")

        try:
            text = recognizer.recognize_google(audio)
            print("📝 Transcription: " + text)
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
        except sr.RequestError as e:
            print(f"❌ Could not request results; {e}")

if __name__ == "__main__":
    transcribe_speech()
