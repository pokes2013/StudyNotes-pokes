# 导入必要的模块
import os  # 用于文件和目录操作
import re  # 用于正则表达式匹配
from typing import List, Set  # 类型提示，提高代码可读性
from datetime import datetime  # 用于获取当前日期

# 常量定义部分
# 定义支持的视频文件扩展名（不区分大小写）
VIDEO_EXTENSIONS = {
    'mp4', 'MP4', 'wmv', 'WMV', 'avi', 'AVI',
    'rmvb', 'rm', 'RM', 'mov', 'MOV', 'ts',
    'TS', 'vob', 'VOB', 'flv', 'FLV', 'm4v',
    'M4V', 'mkv', 'MKV'
}

# 定义需要排除的文件名关键词
EXCLUDED_KEYWORDS = {
    '制作', '合集', '两个', '合并', '作品', '都要'
}

# 定义需要忽略的番号（即使重复也不报警）
IGNORED_IDS = {
    'SIS-037', 'TG-2022', 'IPZ-762', 'JUSD-671',
    'OFJE-212', 'FCDSS-021'
}


def get_video_files(directory: str) -> List[str]:
    """
    遍历指定目录及其子目录，获取所有视频文件名

    参数:
        directory: 要搜索的目录路径

    返回:
        包含所有视频文件名的列表（已转为大写）
    """
    # 初始化空列表存储视频文件名
    video_files = []

    # 使用os.walk遍历目录树
    # root: 当前目录路径
    # _: 子目录列表（这里用_表示我们不使用这个变量）
    # files: 当前目录下的文件列表
    for root, _, files in os.walk(directory):
        # 遍历当前目录下的所有文件
        for filename in files:
            # 使用os.path.splitext分割文件名和扩展名
            # [1]获取扩展名部分，[1:]去掉扩展名前的点
            ext = os.path.splitext(filename)[1][1:]

            # 检查扩展名是否在支持的视频扩展名列表中
            # 将所有扩展名转为大写进行比较
            if ext.upper() in {e.upper() for e in VIDEO_EXTENSIONS}:
                # 检查文件名是否不包含任何排除关键词
                if not any(keyword in filename for keyword in EXCLUDED_KEYWORDS):
                    # 将文件名转为大写并添加到列表中
                    video_files.append(filename.upper())

    return video_files


def extract_id(filename: str) -> str:
    """
    从文件名中提取番号

    参数:
        filename: 视频文件名

    返回:
        提取到的番号字符串，如果未找到则返回None
    """
    # 使用正则表达式匹配番号模式：
    # 2-10个字母 + 连字符 + 3-10个数字
    match = re.match(r'([A-Za-z]{2,10}-\d{3,10})', filename)
    # 如果匹配成功返回匹配的字符串，否则返回None
    return match.group() if match else None


def find_duplicate_ids(video_files: List[str]) -> Set[str]:
    """
    从视频文件列表中找出重复的番号

    参数:
        video_files: 视频文件名列表

    返回:
        包含所有重复番号的集合
    """
    # 初始化空字典用于统计番号出现次数
    id_count = {}

    # 遍历所有视频文件名
    for filename in video_files:
        # 提取番号
        video_id = extract_id(filename)
        # 如果成功提取到番号
        if video_id:
            # 更新番号计数（如果不存在则初始化为0再加1）
            id_count[video_id] = id_count.get(video_id, 0) + 1

    # 使用集合推导式返回出现次数大于1的番号
    return {vid for vid, count in id_count.items() if count > 1}


def main():
    """主函数，执行主要逻辑"""
    # 定义要搜索的两个目录
    dir1 = r"E:\\"
    dir2 = r"F:\\"

    # 获取两个目录下的所有视频文件
    video_files1 = get_video_files(dir1)
    video_files2 = get_video_files(dir2)
    # 合并两个目录的视频文件列表
    all_video_files = video_files1 + video_files2

    # 找出所有重复的番号
    duplicate_ids = find_duplicate_ids(all_video_files)

    # 从重复番号中过滤掉要忽略的番号（使用集合差集操作）
    relevant_duplicates = duplicate_ids - IGNORED_IDS

    # 获取当前日期并格式化为YYYY.MM.DD格式
    current_date = datetime.now().strftime("%Y.%m.%d")
    # 生成日志文件名，如cf_logs_2024.06.05.csv
    log_file = f"cf_logs_{current_date}.csv"

    # 以追加模式打开日志文件（如果不存在则创建）
    with open(log_file, "a", encoding="utf-8") as f:
        # 遍历排序后的重复番号（为了输出有序）
        for vid in sorted(relevant_duplicates):
            # 打印警告信息到控制台
            print(f"{vid} 警告：文件重复，文件重复！！！！！")
            # 将番号写入日志文件（每个番号一行）
            f.write(f"{vid}\n")


# Python标准的主程序入口
if __name__ == "__main__":
    # 调用主函数
    main()