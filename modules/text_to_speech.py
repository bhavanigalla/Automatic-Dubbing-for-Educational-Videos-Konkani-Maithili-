from gtts import gTTS

def text_to_speech(text):

    audio_path = "temp/translated_audio.mp3"

    tts = gTTS(text)

    tts.save(audio_path)

    return audio_path