import os
import re
from typing import List, Set
from datetime import datetime
import pandas as pd
from openpyxl.styles import Font, Alignment  # 添加这行导入

# 常量定义
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
    """递归获取目录下所有视频文件名"""
    video_files = []

    for current_dir, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1][1:]
            if file_extension.upper() in {ext.upper() for ext in SUPPORTED_VIDEO_EXTENSIONS}:
                if not any(keyword in filename for keyword in EXCLUDED_FILENAME_KEYWORDS):
                    video_files.append(filename.upper())
    return video_files


def extract_video_id(filename: str) -> str:
    """从文件名中提取视频番号"""
    match = re.match(r'([A-Za-z]{2,10}-\d{3,10})', filename)
    return match.group() if match else None


def find_duplicate_video_ids(video_files: List[str]) -> Set[str]:
    """找出视频文件列表中重复的番号"""
    video_id_counter = {}
    for filename in video_files:
        video_id = extract_video_id(filename)
        if video_id:
            video_id_counter[video_id] = video_id_counter.get(video_id, 0) + 1
    return {vid for vid, count in video_id_counter.items() if count > 1}


def generate_excel_report(duplicate_ids: Set[str], output_path: str):
    """生成Excel格式的重复项报告"""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df = pd.DataFrame({
        "视频ID": sorted(duplicate_ids),
        "检测日期": current_date,
        "处理状态": "重复",
        "备注": ""
    })

    # 添加Excel表格样式
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="重复视频报告")

        # 获取工作表对象进行格式设置
        worksheet = writer.sheets["重复视频报告"]

        # 设置列宽
        worksheet.column_dimensions['A'].width = 20  # 视频ID
        worksheet.column_dimensions['B'].width = 20  # 检测日期
        worksheet.column_dimensions['C'].width = 15  # 处理状态
        worksheet.column_dimensions['D'].width = 30  # 备注

        # 设置标题行样式
        for cell in worksheet["1:1"]:
            cell.font = Font(bold=True)
            cell.alignment = Alignment(horizontal="center")


def main():
    """主执行函数"""
    first_search_dir = r"E:\\"
    second_search_dir = r"F:\\"

    first_dir_videos = get_video_files(first_search_dir)
    second_dir_videos = get_video_files(second_search_dir)
    all_video_files = first_dir_videos + second_dir_videos

    duplicate_video_ids = find_duplicate_video_ids(all_video_files)
    relevant_duplicates = duplicate_video_ids - IGNORED_VIDEO_IDS

    current_date = datetime.now().strftime("%Y.%m.%d")
    excel_filename = f"duplicate_logs_{current_date}.xlsx"

    generate_excel_report(relevant_duplicates, excel_filename)

    print(f"已生成Excel报告: {excel_filename}")
    print(f"发现重复视频数量: {len(relevant_duplicates)}")


if __name__ == "__main__":
    main()