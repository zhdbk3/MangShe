#
# Created by MC着火的冰块 on 2024/9/14
#

import keyword
import unicodedata
from enum import Enum, unique

from alive_progress import alive_bar

from translator import translate_batch


class StrUtils:
    @unique
    class Cases(Enum):
        """为什么只有两个值？因为 Python 的关键字和内置标识符只有这两种命名法"""
        LOWER_CASE = 0  # 纯小写
        PASCAL_CASE = 1  # 大驼峰

    @staticmethod
    def case_of(s: str) -> Cases:
        """
        获取字符串的格式
        :param s: 字符串
        :return: StrUtils.Cases 的一个枚举值
        """
        if s.islower():
            return StrUtils.Cases.LOWER_CASE
        else:
            return StrUtils.Cases.PASCAL_CASE

    @staticmethod
    def format_pinyin(pinyin: str, original: str) -> str:
        """
        格式化拼音——去除音调，并保留原文格式
        :param pinyin: 丰富的拼音
        :param original: 原文，用于检查格式
        :return: 格式化后的拼音，这应是一个合法的标识符
        """
        # 替换 ü 及其变体为 v
        vs = 'üǖǘǚǜ'
        for v in vs:
            pinyin = pinyin.replace(v, 'v')

        # 脱去声调
        pinyin = unicodedata.normalize('NFKD', pinyin).encode('ascii', 'ignore').decode()

        # 按照原文格式组合出合法标识符
        match StrUtils.case_of(original):
            case StrUtils.Cases.LOWER_CASE:
                pinyin = pinyin.lower()
            case StrUtils.Cases.PASCAL_CASE:
                pinyin = pinyin.title()
        pinyin = pinyin.replace(' ', '').replace("'", '')

        return pinyin


def generate(path: str, originals: list[str]) -> None:
    """
    生成一个映射文件
    :param path: 文件路径 (*.yml)
    :param originals: 原文列表
    :return: None
    """
    # 翻译原文列表
    with alive_bar(len(originals), force_tty=True) as bar:
        translations = translate_batch(originals, dest='zh-cn', src='en', bar=bar)

    # 整理翻译结果，里面每个元组为 (原文, 格式化的拼音, 中文)
    items: list[tuple[str, str, str]] = [
        (t.origin, StrUtils.format_pinyin(t.pronunciation, t.origin), t.text) for t in translations
    ]

    # 获取填充长度
    width = max([len(py) + len(ms) for py, ms, _ in items]) + 4

    # 生成文件内容
    content = '\n'.join([f"{py + ': ' + ms:<{width}}# {cn}" for py, ms, cn in items])
    print(content)

    # 写入文件
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


# 类型检查有点 bug，不用管它，这就是 list
generate('../MangShe/mappings/keywords.yml', keyword.kwlist + keyword.softkwlist)
generate('../MangShe/mappings/identifiers.yml', dir(__builtins__))
