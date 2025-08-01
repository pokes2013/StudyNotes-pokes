import os
import re


def file_name_list(dir):
    """
    输入一个路径，遍历这个路径及含子目录下的文件，并返回一个列表
    返回的列表中含有多有类型的文件名，需要后续过滤出视频文件
    """
    files_list = []
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            # file_path = os.path.join(parent, filename)    #显示绝对路径
            # if filename not in files_list:  # 这里有个去重复的判断
            files_list.append(filename)
    # print(files_list)        #所有文件的绝对路径
    return files_list


def filter_video(list):
    """
    将所有文件中的视频文件过滤出来
    提取将番号提取
    统一将番号转换为大写，存入到新的列表video_list，并且返回这个列表
    video_list类似['ABW-322', 'SVDVD-433', 'MIUM-093']列表

    """
    video_list = []
    for vido_name in list:
        s = vido_name.split(".")
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

            result = re.findall(r'[a-zA-Z]{2,10}-\d+', vido_name)
            for fanhao in result:
                fanhao = fanhao.upper()
                # if fanhao not in video_list:
                video_list.append(fanhao.upper())
    # print(list)
    return video_list





fff = file_name_list(r"F:\AV2021")

过滤视频的列表
video_list = filter_video(fff)




# print(vvv)

database_list = r"D:\indexes"
for vido_name in video_list:
    temp_list = [s for s in database_list if vido_name in s]
    cishu = len(temp_list)

    print(cishu)
#     frequency = len(temp_list)
#     if frequency > 1:
#         with open('chongfu_log.txt', 'w') as file:
#             file.write(vido_name, "警告！文件重复")  # 将文本写入文件
#         print(vido_name)
#         return temp_list
