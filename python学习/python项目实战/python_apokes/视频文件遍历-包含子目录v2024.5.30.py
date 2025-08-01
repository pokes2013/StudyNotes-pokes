import os



def video_scan(pathss):

    """
         此函数是遍历视频文件，请输入您的路径，遍历出的结果包含子目录，并生成一个list
    """
    list_vido_any = []
    # 列表中的字母须小写
    kzhan_list = ["mp4", "avi", "wmv", "rmvb", "mov", "mkv"]

    for vido in os.walk(pathss):
        for j in vido[2]:
            # 遍历所得的所有文件，包含子目录的文件，i[0]是当前文件夹的绝对路径，j是文件名
            path = os.path.join(vido[0], j)

            # 以点为分隔符，分割文件名和扩展名
            # s为路径+文件名，不含扩展名
            s = path.split(".")
            # ss为扩展名
            ss = s[len(s) - 1]

            for kzhan in kzhan_list:

                # 这里有个转大写的操作
                if ss == kzhan or ss == kzhan.upper():
                    list_vido_any.append(path)

    return list_vido_any


for video in video_scan(r"F:\AV2021"):
    print(video)
