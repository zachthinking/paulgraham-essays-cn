import os

# 设置你的Markdown文件所在的目录
markdown_dir = r'docs'
sidebar_path = os.path.join(markdown_dir, '_sidebar.md')


def generate_sidebar(markdown_dir, sidebar_path):
    # 获取目录中所有的.md文件
    markdown_files = [f for f in os.listdir(markdown_dir) if f.endswith('.md') and not f.startswith('_')]

    print(markdown_files)

    # 按照文件名排序
    markdown_files.sort()

    # 写入_sidebar.md文件
    with open(sidebar_path, 'w', encoding='utf-8') as sidebar_file:
        # 写入侧边栏的头部信息
        sidebar_file.write('首页\n')
        sidebar_file.write(
            '\n'.join(['- [{}](./{})\n'.format(os.path.splitext(file)[0], file) for file in markdown_files]))


# 调用函数生成_sidebar.md
generate_sidebar(markdown_dir, sidebar_path)