import os

# 设置你的Markdown文件所在的目录
markdown_dir = 'docs'

def generate_sidebar(markdown_dir):
    # 用于存放侧边栏内容的列表
    sidebar_content = ['* [首页](/)']

    for root, dirs, files in os.walk(markdown_dir):
        # 过滤掉以_开头的文件和目录
        dirs[:] = [d for d in dirs if not d.startswith('_')]
        files[:] = [f for f in files if f.endswith('.md') and not f.startswith('_')]

        # 如果当前目录下有文件，则添加目录到侧边栏
        if files:
            sidebar_content.append(f"* [目录名](./{os.path.relpath(root, markdown_dir)}/")
            for file in files:
                # 为每个文件生成侧边栏链接
                relative_path = os.path.relpath(os.path.join(root, file), markdown_dir)
                sidebar_content.append(f"  * [{file[:-3]}](./{relative_path})")

    # 写入_sidebar.md文件
    sidebar_path = os.path.join(markdown_dir, '_sidebar.md')
    with open(sidebar_path, 'w', encoding='utf-8') as sidebar_file:
        sidebar_file.write('\n'.join(sidebar_content))

# 调用函数生成_sidebar.md
generate_sidebar(markdown_dir)