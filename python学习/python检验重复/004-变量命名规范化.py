import os
import re
from typing import List, Set, Dict
from datetime import datetime

# 常量使用全大写+下划线命名
SUPPORTED_VIDEO_EXTENSIONS = {
    'mp4', 'MP4', 'wmv', 'WMV', 'avi', 'AVI',
    'rmvb', 'RMVB', 'rm', 'RM', 'mov', 'MOV',
    'ts', 'TS', 'vob', 'VOB', 'flv', 'FLV',
    'm4v', 'M4V', 'mkv', 'MKV'
}

EXCLUDED_FILENAME_KEYWORDS = {
    '制作', '合集', '两个', '合并', '作品', '都要'
}

IGNORED_VIDEO_IDS = {
    'SIS-037', 'TG-2022', 'IPZ-762', 'JUSD-671',
    'OFJE-212', 'FCDSS-021'
}


def get_video_files(root_dir: str) -> List[str]:
    """
    递归获取目录下所有视频文件名

    Args:
        root_dir: 要搜索的根目录路径

    Returns:
        包含所有视频文件名的列表(大写形式)
    """
    video_files = []

    for current_dir, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # 获取文件扩展名(不带点)
            file_extension = os.path.splitext(filename)[1][1:]

            if file_extension.upper() in {ext.upper() for ext in SUPPORTED_VIDEO_EXTENSIONS}:
                if not any(keyword in filename for keyword in EXCLUDED_FILENAME_KEYWORDS):
                    video_files.append(filename.upper())

    return video_files


def extract_video_id(filename: str) -> str:
    """
    从文件名中提取视频番号

    Args:
        filename: 视频文件名

    Returns:
        提取到的视频番号，未找到则返回None
    """
    # 匹配模式: 2-10个字母 + 连字符 + 3-10个数字
    match = re.match(r'([A-Za-z]{2,10}-\d{3,10})', filename)
    return match.group() if match else None


def find_duplicate_video_ids(video_files: List[str]) -> Set[str]:
    """
    找出视频文件列表中重复的番号

    Args:
        video_files: 视频文件名列表

    Returns:
        包含所有重复番号的集合
    """
    video_id_counter = {}

    for filename in video_files:
        video_id = extract_video_id(filename)
        if video_id:
            video_id_counter[video_id] = video_id_counter.get(video_id, 0) + 1

    return {vid for vid, count in video_id_counter.items() if count > 1}


def main():
    """主执行函数"""
    # 定义要扫描的目录
    first_search_dir = r"E:\\"
    second_search_dir = r"F:\\"

    # 获取两个目录下的视频文件
    first_dir_videos = get_video_files(first_search_dir)
    second_dir_videos = get_video_files(second_search_dir)
    all_video_files = first_dir_videos + second_dir_videos

    # 找出重复番号
    duplicate_video_ids = find_duplicate_video_ids(all_video_files)

    # 过滤掉要忽略的番号
    relevant_duplicates = duplicate_video_ids - IGNORED_VIDEO_IDS

    # 生成带日期的日志文件名
    current_date = datetime.now().strftime("%Y.%m.%d")
    log_filename = f"duplicate_logs_{current_date}.csv"

    # 写入日志文件
    with open(log_filename, "a", encoding="utf-8") as log_file:
        for video_id in sorted(relevant_duplicates):
            print(f"{video_id} 发现重复视频文件,请马上处理")
            log_file.write(f"{video_id}\n")


if __name__ == "__main__":
    main()