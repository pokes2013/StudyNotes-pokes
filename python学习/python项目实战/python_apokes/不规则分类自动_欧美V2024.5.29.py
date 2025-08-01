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
                # print(path)

                # # 统计字母次数,字母次数超过一定次数则视为不规则,例如欧美
                total_letters = count_letters(path)
                if total_letters > 30:
                    list_vido_any.append(path)

    return list_vido_any

    # ["动漫", "无码", "韩国", "香港", "三级", "8時間"]


# 请输入路径
sss = vido_any(r"\\10.10.30.98\f\欧美专辑系列")
for video_path in sss:
    # 从绝对路径中提取完整文件名
    video_name = os.path.basename(video_path)
    # 文件路径提取,用于后面拼接
    video_dir = os.path.dirname(video_path)
    # 截取文件名的扩展名MP4
    video_name_kz = video_name.split(".")[-1]
    # 不带扩展名的文件名abc-123
    video_name_notkz = os.path.splitext(video_name)[0]
    # print(video_name)

    """
    这里的过滤非常麻烦,需要注意的是:
    文件名过滤和路径过滤一定要区分,是两码事
    """
    # 文件名关键字过滤~过滤非欧美的
    if "动漫" not in video_name_notkz and \
            "時間" not in video_name_notkz and \
            "PPT" not in video_name_notkz and \
            "Tokyo" not in video_name_notkz and \
            "1pon" not in video_name_notkz and \
            "Tokyo" not in video_name_notkz and \
            "carib" not in video_name_notkz and \
            "uncensored" not in video_name_notkz and \
            "無碼" not in video_name_notkz and \
            "UMSO-465" not in video_name_notkz and \
            "STARS" not in video_name_notkz and \
            "SSIS" not in video_name_notkz and \
            "店長" not in video_name_notkz and \
            "UNCENSORED" not in video_name_notkz and \
            "IPTD" not in video_name_notkz and \
            "fsdss" not in video_name_notkz and \
            "三级" not in video_name_notkz and \
            "三级" not in video_name_notkz and \
            "PPV" not in video_name_notkz:
        # 路径关键字过滤
        if "不全" not in video_dir and \
                "BEST" not in video_dir and \
                "無修" not in video_dir and \
                "麻豆" not in video_dir and \
                "SWAG" not in video_dir and \
                "电视剧" not in video_dir and \
                "indexes" not in video_dir:
            # print(video_path)

            # 从绝对路径中提取完整文件名
            video_name = os.path.basename(video_path)
            # 文件路径提取,用于后面拼接
            video_dir = os.path.dirname(video_path)
            # 截取文件名的扩展名MP4
            video_name_kz = video_name.split(".")[-1]
            # 不带扩展名的文件名abc-123
            video_name_notkz = os.path.splitext(video_name)[0]

            if "[欧美]" not in video_name_notkz:
                video_name_notkz = video_name_notkz + "[欧美]."
                new_name_path = video_dir + "\\" + video_name_notkz + video_name_kz
                os.renames(video_path, new_name_path)

                print("更改成功\n" + video_path + "\n" + new_name_path + "\n" * 1)
