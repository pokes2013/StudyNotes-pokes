def baohan(str, bh01, bh02, bh03, bh04):
    # str = "[韩国三级][我朋友的老姐].2016.Uncut.720p.HDRip.H264-ob.mp4"
    #
    # str_YGL = "韩国"


    if (bh01 in str) == True: print("包含了：" + bh01)
    if (bh02 in str) == True: print("包含了：" + bh02)
    if (bh03 in str) == True: print("包含了：" + bh03)
    if (bh04 in str) == True: print("包含了：" + bh04)


baohan("[韩国三级][我朋友的老姐].2016.Uncut.720p.HDRip.H264-ob.mp4", "韩国", "老姐", "朋友", "2016")
