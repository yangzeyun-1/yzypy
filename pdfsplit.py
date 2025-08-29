import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(pdf_path, output_folder, split_ranges):
    """
    将PDF文件拆分成多个PDF文件。

    :param pdf_path: 原始PDF文件的路径
    :param output_folder: 输出文件夹路径
    :param split_ranges: 拆分的页面范围列表，每个元素为(start, end)的元组
    """
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 打开PDF文件
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        total_pages = len(reader.pages)

        for idx, (start, end) in enumerate(split_ranges):
            # 检查页码范围是否有效
            if start < 1 or end > total_pages or start > end:
                print(f"警告: 第 {idx + 1} 组页码 ({start}-{end}) 超出范围或无效，跳过。")
                continue

            writer = PdfWriter()

            # 添加指定页面到新的PDF
            for page_num in range(start - 1, end):  # PyPDF2 使用0基索引
                writer.add_page(reader.pages[page_num])

            # 定义输出文件名
            output_filename = os.path.join(output_folder, f'split_{idx + 1}.pdf')

            # 写入新的PDF文件
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)

            print(f"已创建: {output_filename}")

# 示例使用
if __name__ == "__main__":
    pdf_path = 'UG NX Motion机构运动仿真基础及实例.pdf'          # 替换为你的PDF文件路径
    output_folder = 'split_pdfs'      # 输出文件夹名称
    split_ranges = [
        (47, 55),
        (56, 64),
        (65, 70),
        (71, 84),
        (85, 96),
        (97, 106),
        (107, 113),
        (114, 121),
        (122, 132),
        (133, 145),
        (146, 158),
        (159, 166),
        (167, 174),
        (175, 182),
        (183, 194),
        (195, 202),
        (203, 210),
        (211, 221),
        (222, 228),
        (229, 237),
        (238, 248),
        (249, 261),
        (262, 270),
        (271, 281),
        (282, 289),
        (290, 301),
        (302, 308),
        (309, 317),
        (318, 326)
    ]

    split_pdf(pdf_path, output_folder, split_ranges)