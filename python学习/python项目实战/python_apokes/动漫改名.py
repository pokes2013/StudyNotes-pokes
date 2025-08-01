import os


def count_letters(s):
    """
    统计字符串中的字母
    """

    # 移除字符串中的空格
    s = s.replace(" ", "")
    # 转换为小写统计
    s = s.lower()
    # 统计每个字母出现的次数
    letter_count = {}
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        letter_count[letter] = s.count(letter)
    # 返回总计数
    return sum(letter_count.values())


def vido_any():
    """
        文件夹下的视频文件，包含子目录 ，显示为绝对路径
    """
    list_vido_any = []
    # for vido in os.walk(os.getcwd()):
    for vido in os.walk(r"\\10.10.30.98\e\动漫筛选"):

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

                # # 统计字母次数,字母次数超过一定次数则视为不规则,例如欧美
                total_letters = count_letters(path)
                # if total_letters > 30:
                list_vido_any.append(path)

    return list_vido_any


for video_path in vido_any():
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video_path)
    # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video_path)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]

    # print(video_name_notkz)

    if "[动漫]" in video_name_notkz :
        video_name_notkz = video_name_notkz.replace("[动漫].[动漫]", "")
        print(video_name_notkz)







        # video_name_notkz = video_name_notkz + "[动漫]."
        # new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
        # # print(new_name)
        # os.renames(video_path, new_name_path)
        # print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)
    # else:
        video_name_notkz = video_name_notkz + "[动漫]."
        new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
        os.renames(video_path, new_name_path)
    #     print(new_name_path)
    #
    #     print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)