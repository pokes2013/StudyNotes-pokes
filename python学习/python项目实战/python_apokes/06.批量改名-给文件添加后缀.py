import os


def rename(filess_path, hz_str):
    """
        批量给文件加后缀，例如：源文件为abx-123.pdf  目标文件为abx-123_ok.pdf ,我们在源文件名后面加了_ok
    """

    for root, dirs, files in os.walk(filess_path):
        for video in files:
            # 格式化新文件名
            wzzb = video.rfind('.')  # 定位最后一个.的位置
            qz_name = video[:wzzb]  # 截取不含扩展名的文件名
            hz_name = video[wzzb:]  # 扩展名
            result_name = qz_name + hz_str + hz_name
            # 重命名
            os.chdir(filess_path)  # 在对文件重命名之前为其指定路径
            os.rename(video, result_name)
            print(video)


rename(r"\\10.10.30.97\e\欧美-个人专辑", "[欧美]")
