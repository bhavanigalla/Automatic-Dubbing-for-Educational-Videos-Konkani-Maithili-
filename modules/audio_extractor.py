import moviepy.editor as mp

def extract_audio(video_path):

    video = mp.VideoFileClip(video_path)

    # get actual duration
    duration = video.duration

    # use safe duration (max 60 sec OR actual video length)
    safe_duration = min(60, duration)

    video = video.subclip(0, safe_duration)

    audio_path = "temp/audio.wav"

    video.audio.write_audiofile(audio_path, fps=16000)

    return audio_path