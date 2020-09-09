#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :d05.py
@时间    :2020/09/09 17:58:56
@作者    :江伟
@版本    :1.0
@说明    :
'''

"""
上面的两段代码合在一起，我们就完成了“大球吃小球”的游戏（如下图所示），准确的说它算不上一个游戏，
但是做一个小游戏的基本知识我们已经通过这个例子告诉大家了，有了这些知识已经可以开始你的小游戏开发之旅了。
其实上面的代码中还有很多值得改进的地方，比如刷新窗口以及让球移动起来的代码并不应该放在事件循环中，
等学习了多线程的知识后，用一个后台线程来处理这些事可能是更好的选择。如果希望获得更好的用户体验，
我们还可以在游戏中加入背景音乐以及在球与球发生碰撞时播放音效，利用pygame的mixer和music模块，
我们可以很容易的做到这一点，大家可以自行了解这方面的知识。事实上，想了解更多的关于pygame的知识，
最好的教程是pygame的官方网站，如果英语没毛病就可以赶紧去看看啦。 如果想开发3D游戏，pygame就显得力不从心了，
对3D游戏开发如果有兴趣的读者不妨看看Panda3D。
"""