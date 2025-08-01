import os
import re
from typing import List, Set
from datetime import datetime  # 新增导入

# 常量定义
VIDEO_EXTENSIONS = {
    'mp4', 'MP4', 'wmv', 'WMV', 'avi', 'AVI',
    'rmvb', 'rm', 'RM', 'mov', 'MOV', 'ts',
    'TS', 'vob', 'VOB', 'flv', 'FLV', 'm4v',
    'M4V', 'mkv', 'MKV'
}

EXCLUDED_KEYWORDS = {
    '制作', '合集', '两个', '合并', '作品', '都要'
}

IGNORED_IDS = {
    'SIS-037', 'TG-2022', 'IPZ-762', 'JUSD-671',
    'OFJE-212', 'FCDSS-021'
}


def get_video_files(directory: str) -> List[str]:
    """遍历目录下所有视频文件（含子目录），返回文件名列表（大写）"""
    video_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            ext = os.path.splitext(filename)[1][1:]  # 去掉点

            if ext.upper() in {e.upper() for e in VIDEO_EXTENSIONS}:
                if not any(keyword in filename for keyword in EXCLUDED_KEYWORDS):
                    video_files.append(filename.upper())

    return video_files


def extract_id(filename: str) -> str:
    """从文件名中提取番号"""
    match = re.match(r'([A-Za-z]{2,10}-\d{3,10})', filename)
    return match.group() if match else None


def find_duplicate_ids(video_files: List[str]) -> Set[str]:
    """从视频文件列表中找出重复的番号"""
    id_count = {}

    for filename in video_files:
        video_id = extract_id(filename)
        if video_id:
            id_count[video_id] = id_count.get(video_id, 0) + 1

    return {vid for vid, count in id_count.items() if count > 1}


def main():
    # 搜索两个目录中的视频文件
    dir1 = r"E:\\"
    dir2 = r"F:\\"

    video_files1 = get_video_files(dir1)
    video_files2 = get_video_files(dir2)
    all_video_files = video_files1 + video_files2

    # 找出重复的番号
    duplicate_ids = find_duplicate_ids(all_video_files)

    # 过滤掉要忽略的番号
    relevant_duplicates = duplicate_ids - IGNORED_IDS

    # 使用当前日期生成日志文件名
    current_date = datetime.now().strftime("%Y.%m.%d")  # 格式化为 YYYY.MM.DD
    log_file = f"cf_logs_{current_date}.csv"  # 生成如 cf_logs_2024.06.05.csv

    with open(log_file, "a", encoding="utf-8") as f:
        for vid in sorted(relevant_duplicates):
            print(f"{vid} 此文件重复")
            f.write(f"{vid}\n")


if __name__ == "__main__":
    main()
