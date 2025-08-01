import os, sys, time

# file_list=["abc-123.avi", "abc-484.flv", "abc-656.m4v", "abc-147.mkv", "abc-595.mp4", "abc-444.mov", "abc-666.rm", "abc-999.rmvb", "abc-111.ts", "abc-159.vob"]
# vido_hz_list = [".avi", ".flv", ".m4v", ".mkv", ".mp4", ".mov", ".rm", ".rmvb", ".ts", ".vob", ".wmv"]
#
# full_list=[]
# for vido_hz in vido_hz_list:
#     vido_gg_list = [s for s in file_list if vido_hz in s]
#     for vido in vido_gg_list:
#         # print(vido)
#         if vido not in full_list:
#             full_list.append(vido)
# print(full_list)


print(os.system("dir /b *.mp4"))
