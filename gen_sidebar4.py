import os

# 设置你的Markdown文件所在的目录
markdown_dir = 'docs'

def extract_title(md_content):
    """从Markdown内容中提取第一个标题"""
    for line in md_content.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    return '无标题'

def generate_sidebar(markdown_dir):
    # 用于存放文件路径和标题的列表
    files_with_titles = []

    # 遍历目录和子目录
    for root, dirs, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith('.md') and not file.startswith('_') and not file == 'README.md':
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    md_content = md_file.read()
                    title = extract_title(md_content)
                    if title:
                        # 将文件路径和标题添加到列表
                        files_with_titles.append((file_path, title))

    # 按照标题排序
    files_with_titles.sort(key=lambda x: x[1])

    # 将排序后的文件路径和标题转换为侧边栏内容
    sidebar_content = [
        f"* [{title}](./{os.path.relpath(file_path, markdown_dir)})"
        for file_path, title in files_with_titles
    ]

    # 写入_sidebar.md文件
    sidebar_path = os.path.join(markdown_dir, '_sidebar.md')
    with open(sidebar_path, 'w', encoding='utf-8') as sidebar_file:
        sidebar_file.write('\n'.join(sidebar_content))

# 调用函数生成_sidebar.md
generate_sidebar(markdown_dir)