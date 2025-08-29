import os
import random
import shutil

def assign_pdfs_to_names(names_file, pdf_folder, target_folder, assignment_file):
    """
    将PDF文件随机分配给姓名，并将PDF以姓名命名存入目标文件夹，同时将分配情况记录到日志文件中。

    :param names_file: 包含姓名的TXT文件路径
    :param pdf_folder: 存放PDF文件的文件夹路径
    :param target_folder: 目标文件夹路径，用于存放分配后的PDF文件
    :param assignment_file: 分配结果输出的TXT文件路径
    """
    # 检查并创建目标文件夹
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"已创建目标文件夹: {target_folder}")
    else:
        # 如果目标文件夹已存在，清空其中的文件（可选）
        for file in os.listdir(target_folder):
            file_path = os.path.join(target_folder, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"删除 {file_path} 失败: {e}")
        print(f"已清空目标文件夹: {target_folder}")

    # 读取姓名列表
    try:
        with open(names_file, 'r', encoding='utf-8') as f:
            names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"错误: 姓名文件未找到: {names_file}")
        return
    except Exception as e:
        print(f"读取姓名文件时出错: {e}")
        return

    if not names:
        print("姓名文件为空或格式不正确。")
        return

    # 获取PDF文件列表
    try:
        pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.jpg')]
    except Exception as e:
        print(f"读取PDF文件夹时出错: {e}")
        return

    if not pdf_files:
        print("PDF文件夹中没有找到PDF文件。")
        return

    total_pdfs = len(pdf_files)
    print(f"共找到 {total_pdfs} 个PDF文件。")

    # 打开分配结果文件，准备写入
    try:
        with open(assignment_file, 'w', encoding='utf-8') as assign_f:
            assign_f.write("任务分配结果:\n")
            assign_f.write("="*30 + "\n")
            for name in names:
                try:
                    # 随机选择一个PDF文件
                    assigned_pdf = random.choice(pdf_files)
                    source_path = os.path.join(pdf_folder, assigned_pdf)
                    target_path = os.path.join(target_folder, f"{name}.jpg")

                    # 如果目标文件已存在，避免覆盖，可以在文件名后添加序号
                    counter = 1
                    while os.path.exists(target_path):
                        name_part, ext = os.path.splitext(f"{name}.jpg")
                        target_path = os.path.join(target_folder, f"{name}_{counter}{ext}")
                        counter += 1

                    # 复制并重命名PDF文件
                    shutil.copy2(source_path, target_path)
                    print(f"已分配: {name} -> {assigned_pdf} (保存为 {os.path.basename(target_path)})")
                    # 写入分配结果到文件
                    assign_f.write(f"{name}，{assigned_pdf}\n")
                except Exception as e:
                    print(f"分配 {name} 时出错: {e}")

            print(f"所有姓名的PDF分配完成，结果已保存到 '{assignment_file}'。")
    except Exception as e:
        print(f"创建分配结果文件时出错: {e}")
        return

    # 随机分配PDF文件给每个姓名



if __name__ == "__main__":
    # 设置文件和文件夹路径
    # 请根据实际情况修改以下路径
    names_txt = 'name_list.txt'          # 包含姓名的TXT文件
    pdf_directory = 'split_pdfs'           # 存放PDF文件的文件夹
    output_directory = 'assigned_pdfs'     # 目标文件夹
    assignment_results = 'assignment_results.txt'  # 分配结果输出文件

    assign_pdfs_to_names(names_txt, pdf_directory, output_directory, assignment_results)