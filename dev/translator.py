#
# Created by MC着火的冰块 on 2024/9/14
#

import asyncio
from typing import Callable, Any

from aiogoogletrans import Translator
from aiogoogletrans.models import Translated


def translate_batch(text_list: list[str], dest, src, bar: Callable[[], Any]) -> list[Translated]:
    """
    批量翻译并实时更新进度条（超级快！）
    无法连接谷歌翻译？请查看 https://github.com/Ponderfly/GoogleTranslateIpCheck
    :param text_list: 文本列表
    :param dest: 目标语言
    :param src: 源语言
    :param bar: 完成一次翻译后更新进度条的函数，无参数
    :return: Translated 对象列表
    """
    translator = Translator()

    async def translate_one(text: str) -> Translated:
        translation = await translator.translate(text, dest=dest, src=src)
        bar()
        return translation

    async def main() -> list[Translated]:
        tasks = [translate_one(text) for text in text_list]
        return await asyncio.gather(*tasks)  # 类型检查有点 bug，不用管它，这就是 list

    return asyncio.run(main())


if __name__ == '__main__':
    import time

    from alive_progress import alive_bar

    text_list = [
                    'If we don’t surrender to anxiety and depression,',
                    'there will eventually be a place for us in this world.',
                    'If you can remember my name, if you all can remember my name,',
                    'maybe I or "we" will be able to live freely one day.',
                ] * 25
    t1 = time.time()
    with alive_bar(len(text_list), force_tty=True) as bar:
        translations = translate_batch(text_list, dest='zh-cn', src='en', bar=bar)
    t2 = time.time()
    print('\n'.join([f'{t.text}\n{t.pronunciation}' for t in translations]))
    print(f'耗时：{t2 - t1}s')
