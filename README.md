# 树莓派蜂鸣播放器

通过 **PWM** 使用**无源压电蜂鸣器**播放《铁血丹心》。



## 环境

树莓派 4B

无源压电蜂鸣器

杜邦线

Raspberry Pi OS (bullseye)

Python3



## 接线图

![buzzer](https://raw.githubusercontent.com/Panda-Academy/buzzer-player/main/buzzer.jpg)





## 代码

- play.py -- 主程序
- tone.py -- 音调
- notation.py -- 简谱（想听别的曲儿，请更改此文件）



## 启动

克隆代码到本地，在 buzzer-player 目录下运行 `python player.py`，运行效果见[真·电音版《铁血丹心》](https://www.bilibili.com/video/BV1Sr4y1b7tQ?share_source=copy_web)。