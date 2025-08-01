import cv2
import time
import subprocess
from moviepy.editor import VideoFileClip


def video_duration_1(filename):
    start = time.time()
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    end = time.time()
    spend = end - start
    print("获取视频时长方法1耗时：", spend)
    return float(result.stdout)


def video_duration_2(filename):
    start = time.time()
    clip = VideoFileClip(filename)
    end = time.time()
    spend = end - start
    print("获取视频时长方法2耗时：", spend)
    return float(clip.duration)


def video_duration_3(filename):
    start = time.time()
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num / rate
        end = time.time()
        spend = end - start
        print("获取视频时长方法3耗时：", spend)
        return duration
    return -1


if __name__ == '__main__':
    file = r".\videos\mda-mkbhvebqej3cw9yh.mp4"
    video_time_1 = video_duration_1(file)
    print(video_time_1)
    print("*" * 100)

    video_time_2 = video_duration_2(file)
    print(video_time_2)
    print("*" * 100)

    video_time_3 = video_duration_3(file)
    print(video_time_3)
