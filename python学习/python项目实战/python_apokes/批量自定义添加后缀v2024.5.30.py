# 给文件添加后缀标签

import os


def vido_any(dir_path):
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    # for vido in os.walk(os.getcwd()):
    for vido in os.walk(dir_path):

        for j in vido[2]:
            # i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            s = path.split(".")
            ss = s[len(s) - 1]

            if (ss == "mp4" or ss == "MP4" or
                    ss == "wmv" or ss == "WMV" or
                    ss == "avi" or ss == "AVI" or
                    ss == "rmvb" or ss == "rmvb" or
                    ss == "rm" or ss == "RM" or
                    ss == "mov" or ss == "MOV" or
                    ss == "ts" or ss == "TS" or
                    ss == "vob" or ss == "VOB" or
                    ss == "flv" or ss == "FLV" or
                    ss == "m4v" or ss == "M4V" or
                    ss == "mkv" or ss == "MKV"):
                # print(path)

                list_vido_any.append(path)

    return list_vido_any


video_path = r"\\10.10.30.98\e\动漫筛选"
tab = "[动漫]"

# # vido_any(video_path)


for video in vido_any(video_path):
    # # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video)

    # # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video)
    # # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]

    if tab not in video_name_notkz:
        # 不带扩展加后缀
        video_name_notkz = video_name_notkz + tab
        new_name_path = video_dir + "\\" + video_name_notkz + "." + video_name_kz
        os.renames(video, new_name_path)
        # print(new_name_path)
        print("更改成功\n" + video + "\n" + new_name_path + "\n" * 1)
        # print(new_name_path)
input('Press Enter to exit...')