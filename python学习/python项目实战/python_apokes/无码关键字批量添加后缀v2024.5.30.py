import os


def vido_any(pathdir):
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    # for vido in os.walk(os.getcwd()):
    for vido in os.walk(pathdir):

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
                    ss == "mkv" or ss == "MKV"
            ):
                list_vido_any.append(path)

    return list_vido_any


# 请输入路径
sss = vido_any(r"\\10.10.30.99\e")

for video_path in sss:
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video_path)
    # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video_path)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]

    if (
            "okyo" in video_name_notkz or
            "PPV" in video_name_notkz or
            "ppv" in video_name_notkz or
            "whole1" in video_name_notkz or
            "本道" in video_name_notkz or
            "东京热" in video_name_notkz or
            "无码" in video_name_notkz or
            "carib" in video_name_notkz or
            "10MU" in video_name_notkz or
            "10mu" in video_name_notkz or
            "1PON" in video_name_notkz or
            "1pon" in video_name_notkz):
        # print(video_name)

        if "无码" not in video_name_notkz:
            video_name_notkz = video_name_notkz + "[无码]."
            new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
            os.renames(video_path, new_name_path)
            print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)
