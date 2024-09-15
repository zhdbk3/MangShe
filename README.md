# 目录

- [写在前面](#写在前面)
- [MangShe](#mangshe)
    - [前情提要](#前情提要)
    - [拼音在编程中的无比优越性](#拼音在编程中的无比优越性)
    - [获取帮助](#获取帮助) <-- 不想看废话的就直接从这里开始看
    - [开始您的第一个 MangShe 程序](#开始您的第一个-mangshe-程序)
    - [代码规范/增强建议](#代码规范增强建议)

# 写在前面

:warning: 本项目仅为整活，请不要将本项目的思想带入实际编程学习和工作中！否则后果自负！

:warning: 除必要的部分外，该项目本身需尽可能遵守规范！不要被屎山反噬自身！

**分隔线以下不再代表作者立场。**

---

# MangShe

## 前情提要

[信息课本教你写屎山，这就是我们的教材？](https://www.bilibili.com/video/BV1xxHkekEyM)

> 精选评论
>
> 人固然不为他人而活，但亦无权指点他人之生活，若肯弃那好为人师之性、条框约束之习，斯人却可伴你久些，也未可知，，
> <p align="right">——Dr-杏雨欲来</p>

在看了广大网友的评论后，我醍醐灌顶，茅塞顿开，如梦初醒，深刻认识到了自己的浅薄无知与狂妄自大，以及教材在国内的无比权威性、绝对正确性，

**还有最重要的——[拼音在编程中的无比优越性](#拼音在编程中的无比优越性)。**

为此，我决定悔过自新，痛定思痛，痛改前非。为了彰显我道歉的诚意与对拼音编程的认同，并将功补过，我开发了
MangShe 编程语言——拼音版的 Python！

## 拼音在编程中的无比优越性

~~虽然很艰难，但还是出来了>..<~~

|             |         拼音         |         英文         |         中文         |
|:------------|:------------------:|:------------------:|:------------------:|
| 无需频繁地切换输入法  | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
| 无需学习英语      | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
| 无需处理麻烦的编码问题 | :heavy_check_mark: | :heavy_check_mark: |        :x:         |
| 锻炼语文能力      | :heavy_check_mark: |        :x:         |        :x:         |
| 文化自信        | :heavy_check_mark: |        :x:         | :heavy_check_mark: |
| 防御性         | :heavy_check_mark: |        :x:         |        :x:         |

欢迎对这个表格进行补充！

## 获取帮助

MangShe 是一款~~国产自研~~基于 Python 的编程语言，它做的仅是给 Python 的关键字和标识符添加了拼音别名。这意味着 MangShe 具有与
Python 完全相同的特性，并完全兼容 Python。

您可以在 `MangShe/mappings` 目录下找到以下两个文件：

- `keywords.json` - 查看 MangShe 关键字与 Python 关键字的对应关系；
- `identifiers.py` - 查看 MangShe 标识符与 Python 标识符的对应关系。

它们目前都是机翻的，所以会有很多奇奇怪怪的东西。

正如您可能已经注意到的，MangShe 当前还是 v0 阶段，一切都有可能发生变化。

## 开始您的第一个 MangShe 程序

MangShe 程序的源代码文件应以 `.ms` 为后缀名。

在 `examples/yanshi.ms` 中编写代码：

```
dingyi feibonaqi(shangxian):
    jia, yi = 0, 1
    jinguan jia < shangxian:
        dayin(jia, end=' ')
        jia, yi = yi, jia+yi
    dayin()
feibonaqi(1000)
```

然后使用 `msbyq` 编译：

```commandline
msbyq yanshi.ms
```

得到 `examples/yanshi.py`，使用 Python 运行它，即可看到输出：

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
```

## 代码规范/增强建议

MangShe 不需要这些条框约束之习！
