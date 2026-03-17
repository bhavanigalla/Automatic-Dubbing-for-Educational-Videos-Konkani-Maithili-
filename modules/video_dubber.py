import moviepy.editor as mp

def dub_video(video_path, audio_path):

    video = mp.VideoFileClip(video_path)
    new_audio = mp.AudioFileClip(audio_path)

    # trim or match audio to video duration
    new_audio = new_audio.subclip(0, video.duration)

    final = video.set_audio(new_audio)

    output = "temp/output_video.mp4"

    final.write_videofile(output, codec="libx264", audio_codec="aac")

    return output