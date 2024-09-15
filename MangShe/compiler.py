#
# Created by MC着火的冰块 on 2024/9/10
#

import yaml


def compile_str(src: str) -> str:
    """
    将 MangShe 代码的字符串编译为 Python 代码
    :param src: MangShe 代码字符串
    :return: 编译得到的 Python 代码
    """
    # 查找替换关键字
    with open('mappings/keywords.yml', encoding='utf-8') as f:
        kw_dict: dict[str, str] = yaml.load(f, Loader=yaml.FullLoader)
    for py_kw, ms_kw in kw_dict.items():
        src = src.replace(ms_kw, str(py_kw))  # True 和 False 会被视为 bool，所以需要转换

    # 生成标识符头
    with open('mappings/identifiers.yml', encoding='utf-8') as f:
        id_dict: dict[str, str] = yaml.load(f, Loader=yaml.FullLoader)
        head = ';'.join([f'{ms_id}={py_id}' for py_id, ms_id in id_dict.items()])

    return head + '\n' + src


def compile_file(src_path: str) -> None:
    """
    将 MangShe 文件 (*.ms) 编译为为 Python 文件 (*.py)
    :param src_path: MangShe 代码文件路径，后缀名应为 .ms
    :return: None
    """
    # 替换后缀名，获取目标路径
    dst_path = src_path[:-3] + '.py'

    # 读取源代码
    with open(src_path, encoding='utf-8') as f:
        src = f.read()

    # 编译
    dst = compile_str(src)

    # 写入目标文件
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(dst)


if __name__ == '__main__':
    compile_file('../examples/yanshi.ms')
