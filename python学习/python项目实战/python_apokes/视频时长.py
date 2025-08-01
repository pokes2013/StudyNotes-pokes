from moviepy.editor import VideoFileClip
# import time

def get_video_duration(filepath):
    clip = VideoFileClip(filepath)
    timelang = clip.duration
    clip.close()
    return timelang


duration = get_video_duration(r"E:\Downloads\佛爷哥五杀.mp4")




def seconds_to_time(seconds):
    # SecToConvert = 56000

    MinutesGet, SecondsGet = divmod(seconds, 60)
    HoursGet, MinutesGet = divmod(MinutesGet, 60)

    # 省略小数点
    HoursGet = int(HoursGet)
    MinutesGet = int(MinutesGet)
    SecondsGet = int(SecondsGet)

    print("视频时长：", HoursGet, "H", MinutesGet, "M", SecondsGet, "S")


seconds_to_time(duration)
