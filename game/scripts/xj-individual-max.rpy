define y_nvl = Character("袁艳",kind=nvl)
define l_nvl = Character("林琴",kind=nvl)
define x_nvl = Character("夏静",kind=nvl)
define c_nvl = Character("程祎琳",kind=nvl)
define w_nvl = Character("我",kind=nvl)
define girl_nvl = Character("女孩",kind=nvl)
define boy_nvl = Character("男孩",kind=nvl)
define teacher_nvl = Character("老师",kind=nvl)

define nc = Character(None,kind=nvl)

init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

init:

    transform lt:
        xpos 0.0 xanchor 0.0 ypos 1.7 yanchor 1.0 zoom 0.95

    transform rt:
        xpos 1.0 xanchor 1.0 ypos 1.7 yanchor 1.0 zoom 0.95

    transform ct:
        xpos 0.5 xanchor 0.5 ypos 1.7 yanchor 1.0 zoom 0.95

    define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    define hp = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

label x_indi_1:

    $_dismiss_pause = False
    
    #show 场景：病房走廊 本节出现女孩字样均为夏静 at ct with dissolve
    #场景：病房走廊
    window hide Dissolve(.7)
    $ persistent.cg_x_bf = True
    scene bf_走廊 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}人一开始是没有价值的，但是每个人出生都会被赋予不同的意义。{/color}"
    nvl_narrator "{color=#e5e5e5}而随着年龄的增长，意义的增值，人也就有了价值，意义可以消失，但价值不会。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}假设，我曾经记得某一件事，这件事有着非同凡响的意义，那么它对我来说就是有价值的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}可是如果我忘记了这件事，那么它的意义也就不复存在了。{/color}"
    nvl_narrator "{color=#e5e5e5}但是它的价值却依旧影响着我。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我到底在苦苦追寻着什么？{/color}"
    nvl_narrator "{color=#e5e5e5}我到底想要知道什么？{/color}"
    nvl_narrator "{color=#e5e5e5}请告诉我吧。{/color}"
    nvl clear

    #场景：重症病房
    window hide Dissolve(.7)
    $ persistent.cg_x_sn = True
    scene bf_室内 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}病房里面静悄悄的，没有任何人注意到我的存在。{/color}"
    nvl_narrator "{color=#e5e5e5}我也没有去吸引别人注意的想法。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我的名字叫做夏静，最喜欢观察有趣的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}除此之外没有任何娱乐的活动。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}哈….{/color}"
    nvl_narrator "{color=#e5e5e5}长长的呼了一口气，我是在跟谁介绍我自己呢。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}感觉今天的自己好像有点儿不太对劲。{/color}"
    nvl_narrator "{color=#e5e5e5}不过算了，也不是什么大事。{/color}"
    nvl clear

    window hide Dissolve(.7)
    #场景：开心的日子
    #show 女孩 小时候的夏静 at ct with dissolve
    $ persistent.cg_x_happyday = True
    scene x_阅读开心 with dissolve:
        zoom .667
    window show Dissolve(.7)

    girl_nvl "{color=#e5e5e5}呀哈哈哈哈！原来是这样！{/color}"
    nvl_narrator "{color=#e5e5e5}重症室穿着小号病号服的女孩和另外一个男孩正在开心的聊天。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我原本对于这种观测是没有任何兴趣的。{/color}"
    nvl_narrator "{color=#e5e5e5}只是这个情况稍微有点特殊。{/color}"
    nvl_narrator "{color=#e5e5e5}因为面前正在和那个男孩聊得很开心的女孩，就是孩提时期的我。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}呵呵呵….{/color}"
    nvl_narrator "{color=#e5e5e5}这种事情让我感觉到非常不解，但是同时也让我非常的兴奋。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}居然还有这种事情发生。{/color}"
    nvl_narrator "{color=#e5e5e5}我真的可以看到过去的自己。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}重症房里面就我们三个人。{/color}"
    nvl_narrator "{color=#e5e5e5}然而那两个孩子只顾着自己笑，似乎完全没有注意到我的存在。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}不过这点程度上我还是能够理解的。{/color}"
    nvl_narrator "{color=#e5e5e5}想让我和这孩子共存在同一个时刻上是理论是不可能的。{/color}"
    nvl_narrator "{color=#e5e5e5}那么只有一种可能性能够解释我现在的情况。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我和她之间必然是互不干涉的。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    # TODO 60
    #CG:开心的日子](少女注视)"
    $ persistent.cg_x_readn = True
    scene x_阅读普通 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}原本应该是这样子的。{/color}"
    nvl_narrator "{color=#e5e5e5}然而她却朝着我所在的地方投来了目光。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}先是从我的下半身看起，最后目光落在了我的脸部。{/color}"
    nvl_narrator "{color=#e5e5e5}和我眼睛对视了起来。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}为了证实她是否真的看到了我。{/color}"
    nvl_narrator "{color=#e5e5e5}我还移动几次位置，但是她还是看着我。{/color}"
    nvl_narrator "{color=#e5e5e5}有意思了，这个就很有意思了。{/color}"
    nvl clear
    
    #show x 嘲讽02 at ct with dissolve
    x_nvl "{color=#e5e5e5}呵呵呵….{/color}"
    nvl_narrator "{color=#e5e5e5}我虽然很感兴趣，但是她对于能够看到我这个存在却完全没有兴趣。{/color}"
    nvl_narrator "{color=#e5e5e5}看了我几眼之后就和男孩聊天去了。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #场景：开心的日子
    $ persistent.cg_x_happyday = True
    scene x_阅读开心 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}让我猜猜看，如果没有猜错的话，她没有应该没有看懂我的存在。{/color}"
    nvl_narrator "{color=#e5e5e5}换句话来说，她的视角里我应该就是一团奇怪的影子。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}在我的为数不多过去的记忆中，我确实有看到很多奇怪的东西。{/color}"
    nvl_narrator "{color=#e5e5e5}是在房间里独处到深夜时，疲惫间会听到房门那边传来的敲门声。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我并没有在意，但是事后想想那个房间在那阵子就只有我一个人住。{/color}"
    nvl_narrator "{color=#e5e5e5}好像有什么事情被我所忘记了一般。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}想到这里头就有点疼了，按理来说这种事情我应该特别感兴趣才对。{/color}"
    nvl_narrator "{color=#e5e5e5}但是…到底是什么原因导致了我完全没有调查这种事情的动机呢？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}想不起来，完全想不起来。{/color}"
    nvl_narrator "{color=#e5e5e5}既然想不起来的话那就不想了，想太多只会增加大脑的负担。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}比起这些，我还是对目前的现状比较感兴趣。{/color}"
    nvl_narrator "{color=#e5e5e5}就算花我一辈子的时间，我也要弄清楚到底发生了什么事情。{/color}"
    nvl clear

    # TODO 62
    #CG:开心的时间 (少女和男孩正常表情的在聊天)]"
    window hide Dissolve(.7)
    $ persistent.cg_x_readn = True
    scene x_阅读普通 with dissolve:
        zoom .667
    window show Dissolve(.7)

    #show 女孩 女孩均为夏静 at ct with dissolve
    girl_nvl "{color=#e5e5e5}你的病什么时候好啊？{/color}"
    nvl_narrator "{color=#e5e5e5}男孩翻了翻书，然后看一眼女孩。{/color}"
    nvl clear
    
    boy_nvl "{color=#e5e5e5}很快就好了。{/color}"
    nvl_narrator "{color=#e5e5e5}男孩很精神的回复到，但是双眼并没有离开手中的书。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这家伙是书虫嘛，没看到‘我’在问他吗？{/color}"
    nvl_narrator "{color=#e5e5e5}这种男生以后怎么可能找得到女朋友啊。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}虽说我对这个倒是不怎么感兴趣，但是看到年幼的自己居然被同龄的男孩子这般对待。{/color}"
    nvl_narrator "{color=#e5e5e5}多少还是有点小不爽。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}但是年幼的我好像并不是很在意男孩子的态度。{/color}"
    nvl_narrator "{color=#e5e5e5}还是很轻松的轻‘嗯’了一声就算是回答。{/color}"
    nvl clear
    
    #场景：黑屏
    #两个人正在学习 少女分神在睡觉，少年则是很认真的在听课 at ct with dissolve
    #场景：两个人正在学习
    window hide Dissolve(.7)
    $ persistent.cg_x_sleep = True
    scene x_少女睡觉 with Dissolve(.7):
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}转眼之间，场景发生了一些改变。{/color}"
    nvl_narrator "{color=#e5e5e5}映入我眼前的是在这个病房里面。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}两个孩子正在努力学习的场景。{/color}"
    nvl_narrator "{color=#e5e5e5}一个年轻的老师在她们的身旁讲课。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}令我无语的事情是，年幼的我根本一副无心听课的样子。{/color}"
    nvl_narrator "{color=#e5e5e5}难道我很小的时候就已经展露了超乎常人的天赋吗？{/color}"
    nvl clear
    
    #show x 惊讶02 at ct with dissolve
    x_nvl "{color=#e5e5e5}额…难道我这么小就已经很厉害了吗？{/color}"
    nvl_narrator "{color=#e5e5e5}完全不记得这个事情。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}夏静，你有在看课本吗？{/color}"
    nvl_narrator "{color=#e5e5e5}老师的声音在病房响起，病房很安静。{/color}"
    nvl_narrator "{color=#e5e5e5}在场的人都能清楚的听到她的声音。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}然而女孩却没有反应。{/color}"
    nvl_narrator "{color=#e5e5e5}像是没听到老师的声音一样。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}小夏…小夏….{/color}"
    nvl_narrator "{color=#e5e5e5}和印象中的老师不一样的是，老师的声音并没有发生情绪上的变化。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}反倒是更加柔和起来。{/color}"
    nvl_narrator "{color=#e5e5e5}像是对待自己的孩子一般。{/color}"
    nvl clear
    
    #show 场景：两个人正在学习 少女睁开眼睛，少年则是很认真的在写作业 at ct with dissolve
    #场景：两个人正在学习
    window hide Dissolve(.7)
    $ persistent.cg_x_study = True
    scene x_少女醒 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    girl_nvl "{color=#e5e5e5}额…嗯？{/color}"
    teacher_nvl "{color=#e5e5e5}好好看做题目啊，不然以后回学校赶不上别的同学的哦。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}女孩没有说话。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}事实上到最后我也没有去学校。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}在我短暂的人生中，并未有幸接触像是学校这样可以挥洒青春的地方。{/color}"
    nvl_narrator "{color=#e5e5e5}好像是因为发生了某一件事情，但是这件事情是什么我不记得了。{/color}"
    nvl clear
    
    boy_nvl "{color=#e5e5e5}我做完了。{/color}"
    teacher_nvl "{color=#e5e5e5}哇，真快！！{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}都做对了，满分！真聪明！{/color}"
    nvl_narrator "{color=#e5e5e5}老师笑着摸了摸男孩的头，但是男孩并没有回复老师。{/color}"
    nvl_narrator "{color=#e5e5e5}而是拿起了书接着在一旁看了起来。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}小夏，你做完没有啊？{/color}"
    teacher_nvl "{color=#e5e5e5}你在不做完，我可要告诉你妈妈了哦。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}年幼的我这个时候才显得有点慌张，拿起笔开始奋笔疾书。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}不一会儿就把题目全部做完了。{/color}"
    nvl_narrator "{color=#e5e5e5}果然小时候的我还是蛮聪明的。{/color}"
    nvl_narrator "{color=#e5e5e5}对于这种事情我还是多少有一点点自豪感的，毕竟怎么说也是自己嘛。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    teacher_nvl "{color=#e5e5e5}…….{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}小夏，你去哪？{/color}"
    girl_nvl "{color=#e5e5e5}我作业做完了。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}好的，我来看一下。{/color}"
    girl_nvl "{color=#e5e5e5}嗯。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}说着老师就开是批阅她的作业。{/color}"
    nvl_narrator "{color=#e5e5e5}女孩则是在一旁瞧着，但是马上她的神色就发生了变化。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}我作业做完了，我要出去玩，拜拜！{/color}"
    teacher_nvl "{color=#e5e5e5}等一下，你…哎，这孩子。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}小女孩就在我和老师的目光下一溜烟跑出了病房。{/color}"
    nvl_narrator "{color=#e5e5e5}趁着女孩离开了为止，我不由得蹭了过去。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}有点好奇我以前写的作业是什么。{/color}"
    nvl_narrator "{color=#e5e5e5}然而，题目我还没看清，就看到触目惊心的红叉在作业上面。{/color}"
    nvl_narrator "{color=#e5e5e5}触目惊心的红叉。{/color}"
    nvl clear

    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}红叉…….{/color}"
    nvl clear

    window hide Dissolve(.7)
    $ persistent.cg_x_bf = True
    #场景：病房走廊
    scene bf_走廊 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}眨眼之间，场景又发生了变化。{/color}"
    nvl_narrator "{color=#e5e5e5}这个变化已经是第二次发生了。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我虽然很有兴趣研究这件事情。{/color}"
    nvl_narrator "{color=#e5e5e5}但是现在我满脑子都是红叉。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}小时候的我….{/color}"
    nvl_narrator "{color=#e5e5e5}成绩原来这么沉重吗，我倒是完全都不记得了。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}不过也有可能是我自己很小就知道隐藏自己的锋芒。{/color}"
    nvl_narrator "{color=#e5e5e5}就是那种啦，本来成绩很好的，故意装作成绩不好想引起谁注意的那种。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}唔….{/color}"
    nvl_narrator "{color=#e5e5e5}她靠在走廊的墙边，玩着自己的小辫子。{/color}"
    nvl_narrator "{color=#e5e5e5}怎么看都不像是想要去玩的孩子。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}倒不如说像极了一个闹变扭的妮子。{/color}"
    nvl_narrator "{color=#e5e5e5}我好奇心装填中….{/color}"
    nvl clear
    
    # TODO 63
    #CG：委屈的少女](这张CG感觉就是夏静有特写，她我也想给一张小时候的特写，服装用另外一种 颜色 换一套简单的病房服装也可以)"
    window hide Dissolve(.7)
    $ persistent.cg_x_wq = True
    scene x_委屈 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}年幼的少女就像是受了什么极大的打击和委屈一样。{/color}"
    nvl_narrator "{color=#e5e5e5}看得让人心疼。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}而眼前这个可爱生物到底是什么？{/color}"
    nvl_narrator "{color=#e5e5e5}突然老脸一红。{/color}"
    nvl_narrator "{color=#e5e5e5}好像就是我自己。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这么夸自己，就算没人知道我是这样看我自己的。{/color}"
    nvl_narrator "{color=#e5e5e5}我也觉得有点点害臊。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}要是能跟她交流的话，我还真想上去问问她怎么了。{/color}"
    nvl_narrator "{color=#e5e5e5}发生什么事情了。{/color}"
    nvl_narrator "{color=#e5e5e5}怎么这么委屈啊。{/color}"
    nvl_narrator "{color=#e5e5e5}是谁欺负你了呀。{/color}"
    nvl_narrator "{color=#e5e5e5}只可惜….{/color}"
    nvl clear
    
    
    # TODO 64
    #CG：结束]"
    window hide Dissolve(.7)
    $ persistent.cg_x_js = True
    scene x_教室 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    teacher_nvl "{color=#e5e5e5}怎么了呀….{/color}"
    nvl_narrator "{color=#e5e5e5}不知道什么时候，房间里面的老师也跟着出来了。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}但是和之前似乎有点不太一样，包括了年少的我也是。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}两者的衣服都和我之前见到的不一样。{/color}"
    nvl_narrator "{color=#e5e5e5}加上之前的场景变换。{/color}"
    nvl_narrator "{color=#e5e5e5}我很快就理解了这一现状。{/color}"
    nvl clear
    

    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}时间线…… 是不一样的。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    $ persistent.cg_x_bf = True
    #场景：病房走廊
    scene bf_走廊 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}刚刚在房间里面发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}和眼前场景的发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}两者之间应该不是在同一天发生的。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}当然我这也是猜测，万一存在那种突然跑出去的我衣服就换掉了的可能性也是有可能的。{/color}"
    nvl_narrator "{color=#e5e5e5}纠结到各种可能性…啊，脑袋不行了。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我很容易就停下了想要了解情况的心情。{/color}"
    nvl_narrator "{color=#e5e5e5}简单的猜测我简单的认为是真实的就行了。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}我不服气….{/color}"
    teacher_nvl "{color=#e5e5e5}咦，为什么呀？{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}为什么他做的都是对的！！！！{/color}"
    teacher_nvl "{color=#e5e5e5}….{/color}"
    x_nvl "{color=#e5e5e5}…….{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}想不到小时候的我居然这么争强好胜。{/color}"
    nvl_narrator "{color=#e5e5e5}不禁觉得有些好笑。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}但是老师并没有说话，只是温柔的抚摸了一下女孩的脑袋。{/color}"
    nvl_narrator "{color=#e5e5e5}露出笑容。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    $ persistent.cg_x_bf = True
    #场景：病房走廊
    scene bf_走廊 with dissolve:
        zoom .667
    window show Dissolve(.7)

    #show 场景：走廊 模糊化效果 at ct with dissolve
    #场景：走廊" "{color=#e5e5e5}还得去想办法弄这个"
    #场景：黑屏
    
    nvl_narrator "{color=#e5e5e5}说句心里话，其实我也没有想到场景这么快就会发生改变。{/color}"
    nvl clear

    #场景：医院长廊
    window hide Dissolve(.7)
    $ persistent.cg_x_bf_n = True
    scene bf_走廊_n with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}但是实际上也没有发生什么比较大的改变。{/color}"
    nvl_narrator "{color=#e5e5e5}还是那条医院的长廊。{/color}"
    nvl_narrator "{color=#e5e5e5}也还是女孩和老师。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}她们两个偷偷摸摸的在做什么呢？{/color}"
    nvl_narrator "{color=#e5e5e5}疑惑的我不由得跟了过去。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}老师和女孩比了个‘嘘’的手势。{/color}"
    nvl_narrator "{color=#e5e5e5}就见两个人蹑手蹑脚的在并不强烈的灯光下悄悄的打开了病房的门。{/color}"
    nvl clear

    #场景：夜间的少年
    window hide Dissolve(.7)
    $ persistent.cg_x_sn_n = True
    scene x_秉烛夜读 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}她们也并没有进去，只是简单的透过门缝里面看房间里面。{/color}"
    nvl_narrator "{color=#e5e5e5}房间里本应该关掉了灯光，然而事实上，却仍然有一处被点亮。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我顺着门缝朝里面投去了视线。{/color}"
    nvl_narrator "{color=#e5e5e5}那个我并不认识的少年坐在台灯下，拿着笔似乎是在学习。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}少年有一点点疲惫，但是还是很认真的写着字。{/color}"
    nvl_narrator "{color=#e5e5e5}看到这里，老师拍拍女孩的头，然后把门轻轻的带上了。{/color}"
    nvl clear

    #场景：医院长廊
    window hide Dissolve(.7)
    $ persistent.cg_x_bf_n = True
    scene bf_走廊_n with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}如果我没猜错的话，剧情应该是这样子的：{/color}"
    nvl_narrator "{color=#e5e5e5}年幼的我在和那个男孩子竞争，但是我没有竞争过那个男孩子。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我不服气，然后这个老师就想告诉我为什么我会竞争不过那个男孩子。{/color}"
    nvl_narrator "{color=#e5e5e5}然后我就会奋发图强，努力学习。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}呵呵呵….{/color}"
    nvl_narrator "{color=#e5e5e5}真的是教科书一样的剧情。{/color}"
    nvl clear

    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}事实上，接下来的剧情也亦如我所知。{/color}"
    nvl clear

    #nvl_narrator "{color=#e5e5e5}(少女安排一张 努力学习的CG吗？ 上面的那个少年替换成少女就行)"
    # TODO 65
    #CG：夜间的少女]"
    window hide Dissolve(.7)
    $ persistent.cg_x_studyhard = True
    scene x_努力学习 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}在偷偷学到了男孩学习的方法之后。{/color}"
    nvl_narrator "{color=#e5e5e5}女孩也开始有样学样，在病房里面拿着台灯学习起来。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}虽然她做题做不出来时候的苦恼样子显得有点笨拙。{/color}"
    nvl_narrator "{color=#e5e5e5}但是她认真学习的样子真的很可爱。{/color}"
    nvl clear

    #show 场景：开心的日子 少年虚弱图 at ct with dissolve
    #场景：开心的日子
    window hide Dissolve(.7)
    $ persistent.cg_x_read_week = True
    scene x_阅读虚弱 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}场景不断的发生改变，就好似走马灯一般。{/color}"
    nvl_narrator "{color=#e5e5e5}但是唯独这幅开心的场景不断的出现。{/color}"
    nvl clear
    
    # TODO 66
    #CG：开心的日子](少年消失)"
    window hide Dissolve(.7)
    $ persistent.cg_x_read_one = True
    scene x_阅读消失 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}直到有一天，男孩已经不在继续陪年幼的我一起玩耍了。{/color}"
    nvl_narrator "{color=#e5e5e5}而年幼的我依旧什么也没有察觉，甚至还有点小窃喜。{/color}"
    nvl_narrator "{color=#e5e5e5}只要他不学习，我总有一天会超过他的。{/color}"
    nvl clear

    # TODO 67
    #CG：两人在学习](少年开始打瞌睡，女孩认真)"
    window hide Dissolve(.7)
    $ persistent.cg_x_boysleep = True
    scene x_男孩睡觉 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}唯一让女孩觉得不开心的地方就是。{/color}"
    nvl_narrator "{color=#e5e5e5}看到男孩打瞌睡的时候，老师会很关心的问男孩休息不休息。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}而每当女孩打瞌睡的时候，老师则是会让她打起精神好好努力。{/color}"
    nvl_narrator "{color=#e5e5e5}这种区别待遇让女孩觉得很不开心。{/color}"
    nvl clear

    # TODO 68
    #CG：夜间的少女](奋笔疾书版)"
    window hide Dissolve(.7)
    $ persistent.cg_x_studyhard_n = True
    scene x_夜间奋笔疾书 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}或许年幼的女孩可能并不知情，然而我却能察觉到什么。{/color}"
    nvl_narrator "{color=#e5e5e5}这让我有点不安，总觉得有什么事情要发生了。{/color}"
    nvl_narrator "{color=#e5e5e5}果不其然。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}某一次补习，男孩做完题目之后并没有看书，而是径直的躺倒床上去休息去了。{/color}"
    nvl clear
    
    #show 场景：两个人在学习 只有女孩的版本 at ct with dissolve
    #场景：两个人在学习
    window hide Dissolve(.7)
    $ persistent.cg_x_study = True
    scene x_少女醒 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}女孩并没有察觉出任何的问题，而是很认真的也在做题。{/color}"
    nvl_narrator "{color=#e5e5e5}而在这之前，虽然女孩一直都很努力，但是还是没有办法赶上男孩的速度。{/color}"
    nvl_narrator "{color=#e5e5e5}不仅仅如此，在答题的正确率上，女孩也仍然赶不上男孩。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}明明都那么努力过了，还是赶不上，或许这个男孩是比我还要聪明的人才对。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这样的人我的脑海中不应该没有记忆。{/color}"
    nvl_narrator "{color=#e5e5e5}反而会有很强烈的记忆才对。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}然而事实上，我不记得有关于这个男孩的任何事情，包括了年幼我曾住院的事情我都不记得。{/color}"
    nvl_narrator "{color=#e5e5e5}因为时间太久，我曾经住过的医院已经改建成了工厂，但是事实上通过调查，我发现我确实有过住院记录。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}不知不觉又开始钻牛角尖了。{/color}"
    nvl_narrator "{color=#e5e5e5}毕竟是小时候的事情 怎么可能记得那么清楚。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}今天的作业怎么样？？怎么样怎么样？{/color}"
    nvl_narrator "{color=#e5e5e5}女孩开开心心的就把作业交了上去。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}我….{/color}"
    nvl_narrator "{color=#e5e5e5}说到这里，老师明显的停顿了一下，像是重新调整了呼吸，把目光从床上的男孩身上撤了回来。{/color}"
    teacher_nvl "{color=#e5e5e5}好的，老师帮你看一下。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}没过多久，女孩的作业就批改完了。{/color}"
    nvl clear
    
    teacher_nvl "{color=#e5e5e5}哎呀，夏静真棒！今天的作业全部都做对了！{/color}"
    nvl_narrator "{color=#e5e5e5}老师露出了讶异的表情。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}而这份讶异就是对年幼时的我最大的表扬。{/color}"
    nvl_narrator "{color=#e5e5e5}女孩不由得翘起了小辫子。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}我作业写完啦，我要出去玩啦！{/color}"
    nvl_narrator "{color=#e5e5e5}女孩把改好的试题从老师的手上拿了回来，然后一道烟就跑出了病房。{/color}"
    nvl clear

    #场景：病房长廊
    scene bf_走廊 with dissolve:
        zoom .667

    nvl_narrator "{color=#e5e5e5}场景随之发生了变化。{/color}"
    nvl clear

    # TODO 69
    #CG:高兴的少女]&和CG委屈的少女做对比，这张是女主拿着试卷很开心的那种。{/color}"
    window hide Dissolve(.7)
    $ persistent.cg_x_happytest = True
    scene x_高兴的少女 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}女孩拿着手中的试卷。{/color}"
    nvl_narrator "{color=#e5e5e5}就好像是如获至宝一般的拿在手上，不停的看着上面一个个红勾。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}只要努力果然还是行的嘛。{/color}"
    nvl_narrator "{color=#e5e5e5}看着少女的模样，我越发的不安了起来。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我也是没由来的就不安，按道理来说这个时候我应该高兴才对啊。{/color}"
    nvl_narrator "{color=#e5e5e5}可是这份不安愈来愈严重。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}突然眼泪就止不住的流了出来。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    $ persistent.cg_x_sn = True
    scene bf_室内 with dissolve:
        zoom .667
    window show Dissolve(.7)
    

    nvl_narrator "{color=#e5e5e5}变成这种状态也会哭吗？{/color}"
    nvl clear
    
    # TODO 70
    #CG:变故]"
    window hide Dissolve(.7)
    $ persistent.cg_x_bg = True
    scene x_离世 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}手里拿着男孩经常看的书，心电图数值变成了一条直线。{/color}"
    nvl_narrator "{color=#e5e5e5}女孩站在床边，她哭了。{/color}"
    nvl_narrator "{color=#e5e5e5}我也哭了。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}无论我怎么搜寻，绞尽脑汁的回忆，我都没有找到有关于这段记忆的任何片段。{/color}"
    nvl_narrator "{color=#e5e5e5}说到底人真的有灵魂存在吗？{/color}"
    nvl_narrator "{color=#e5e5e5}如果有的话，这个场景就应该刻在我的灵魂里面一样。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    
    #show x 哭声 at ct with dissolve
    #x_nvl "{color=#e5e5e5}"
    
    nvl_narrator "{color=#e5e5e5}那么我为什么也会跟着哭？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这个男孩到底是谁？还有那个老师！{/color}"
    nvl_narrator "{color=#e5e5e5}那个老师是谁？{/color}"
    nvl_narrator "{color=#e5e5e5}为什么我会陷入这种完全无法理解的状况里面？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}刹那间，时间仿佛静止在这一刻一般。{/color}"
    nvl_narrator "{color=#e5e5e5}场景里还有着些许杂音，门外有人的声音。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}有谁在哭喊着，求着‘医生救救他吧’，‘如果医疗科技在先进一点也许能救他’{/color}"
    nvl_narrator "{color=#e5e5e5}在寂静的房间里，‘救’这个词的声音已诠释了这个场景全部的含义。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}我想救他…这是我唯一能想起来的事情。{/color}"
    nvl clear
    
    # TODO 71
    #CG:葬礼](这里程序部分想添加奇幻的音效，不一定要画CG，看工作量)"
    window hide Dissolve(.7)
    $ persistent.cg_x_zl = True
    scene x_葬礼 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}刹那间，奇幻的画面出现在了我的面前。{/color}"
    nvl_narrator "{color=#e5e5e5}有人在哭、有人在笑、有人进来了、有人离开了。{/color}"
    nvl_narrator "{color=#e5e5e5}明明是转眼之间，我却好似过了许多年。{/color}"
    nvl clear

    #场景：病房
    # TODO 72
    #CG：少女病卧](刚做完手术)"
    window hide Dissolve(.7)
    $ persistent.cg_x_sick = True
    scene x_少女病卧 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}女孩静静的躺在床上，医疗设备链接在她的身上。{/color}"
    nvl_narrator "{color=#e5e5e5}这些细线好似残破的蜘蛛网一样一面观测女孩的生命体征，一面延续着女孩的生命。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}看到这儿，我不禁疑惑了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}她为什么会躺在床上，像极了刚做完手术。{/color}"
    nvl_narrator "{color=#e5e5e5}但又好像不是。{/color}"
    nvl_narrator "{color=#e5e5e5}又是一段我记忆中不曾有的事情。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}女孩她半睁着眼，失去了神采。{/color}"
    nvl_narrator "{color=#e5e5e5}从陌生人的对话声中，我知道事情的始末。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}继男孩以后，女孩的病情似乎也发生了恶化。{/color}"
    nvl_narrator "{color=#e5e5e5}不出意外，不久之后女孩就会死去。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}就在心电图发出滴的警报声以后。{/color}"
    nvl_narrator "{color=#e5e5e5}我不由得看了看自己的身躯。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}毫无疑问，躺在床上的那个女孩就是我自己没错。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我有我曾活过的记忆。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}难道我是陷入到某个不同的时空了吗？{/color}"
    nvl_narrator "{color=#e5e5e5}在这个时空其实我已经死了。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}看着窗边眼神空洞而虚弱的女孩，我陷入沉思。{/color}"
    nvl_narrator "{color=#e5e5e5}目前还不能下这个结论。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我非常想弄清我此刻的状态，但是我更感兴趣的事情是——这个女孩究竟什么时候死。{/color}"
    nvl_narrator "{color=#e5e5e5}在别人看来或许这好像有点疯狂。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我很清楚，这个时间点必然是关键点。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}倘若床上的这个她就这样死去了。{/color}"
    nvl_narrator "{color=#e5e5e5}那么毫无疑问，我进入的是另外一个世界。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}倘若没死。{/color}"
    nvl_narrator "{color=#e5e5e5}那么在出事之前必然会发生变故。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}或许会有其他可能性，但是眼下这两种可能性是最高的。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我没有局限我的思维，还有一种可能性，虽然不高。{/color}"
    nvl_narrator "{color=#e5e5e5}那就是床上的这个女孩其实不是我的小时候，小时候的我另有其人。{/color}"
    nvl_narrator "{color=#e5e5e5}比如说我有个双胞胎姐姐之类的，或者双胞胎妹妹。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这种事情偶尔在电视上也会发生的吧。{/color}"
    nvl_narrator "{color=#e5e5e5}当然，我没有什么依据，只能是猜测。{/color}"
    nvl_narrator "{color=#e5e5e5}而前面两种可能性我倒是觉得一定会发生其中一条。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    $ persistent.cg_x_sn = True
    scene bf_室内 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}呼了一口气，不出意外的话，马上就要切换场景了。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}果然是这样。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    $ persistent.cg_x_sn = True
    scene bf_室内 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}还是同样的病房。{/color}"
    nvl_narrator "{color=#e5e5e5}还是同样的病床，唯独不一样的事情是，病床上的少女已经不在了。{/color}"
    nvl_narrator "{color=#e5e5e5}环视这这个空无一人的房间，我不由得惊喜了起来。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}这种感觉…..{/color}"
    nvl_narrator "{color=#e5e5e5}我不知道下一秒这里会发生什么。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这里就像是个随机舞台剧一般。{/color}"
    nvl_narrator "{color=#e5e5e5}帷幕拉下以后在重新拉开时，会是完全不一样的剧情展开。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}如果幕后的导演有兴趣的话，甚至能演变出一个我年少时的分裂姐妹。{/color}"
    nvl_narrator "{color=#e5e5e5}亦或者把我卷入某场车祸事件。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这样也能称得上某种程度的有趣。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我比较有感兴趣的还是女孩到底发生了什么。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}时下最理所当然的答案就是女孩已经死去了。{/color}"
    nvl_narrator "{color=#e5e5e5}那么毫无疑问我就是见证了不同时间点上我自己死亡的存在了。{/color}"
    nvl_narrator "{color=#e5e5e5}当然这是不可能…….{/color}"
    nvl clear

    # TODO 73
    #CG:床下的少女(带一点点黑眼圈)]"
    window hide Dissolve(.7)
    $ persistent.cg_x_cx_dark = True
    scene x_趴着低头 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}她想呆在床底下多久啊。{/color}"
    nvl_narrator "{color=#e5e5e5}我应该早就发现了的，可能是我对这件事情的了解程度还不太够。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}那么年幼的我到底在床下做什么呢？{/color}"
    nvl_narrator "{color=#e5e5e5}台灯散发着柔和的光，少女把病床上的白枕当做坐垫垫在胸前。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}拿着笔还有纸不知道在写些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}我靠近了些许。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    x_nvl "{color=#e5e5e5}这是在做什么啊？{/color}"
    nvl clear

    # TODO 74
    #CG：床底下的少女 (转头看着我)]"
    window hide Dissolve(.7)
    $ persistent.cg_x_cx_turn = True
    scene x_趴着普通 with dissolve:
        zoom .667
    window show Dissolve(.7)

    x_nvl "{color=#e5e5e5}诶？{/color}"
    girl_nvl "{color=#e5e5e5}嗯？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我已经非常疑惑了。{/color}"
    nvl clear

    # TODO 75
    #CG：床底下的少女(笑容)]"
    window hide Dissolve(.7)
    $ persistent.cg_x_cx_turn_smile = True
    scene x_趴着愉快 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}女孩笑了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}仿佛像是在对我说欢迎光临一样。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}当然我还是认为她不可能听到我说的话。{/color}"
    nvl_narrator "{color=#e5e5e5}这种跨时空、跨世界的对话怎么可能成立。{/color}"
    nvl clear

    # TODO 76
    #CG:床底下的少女]"
    window hide Dissolve(.7)
    $ persistent.cg_x_cx_confuse = True
    scene x_趴着疑惑 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    girl_nvl "{color=#e5e5e5}可能我真的有点点笨吧。{/color}"
    nvl_narrator "{color=#e5e5e5}她转过头去。{/color}"
    nvl_narrator "{color=#e5e5e5}专注的在做着笔记，就好像随堂一般。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}所以一定要努力学习才行。{/color}"
    girl_nvl "{color=#e5e5e5}妈妈说现在的医生治不好我们的病。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}这是什么情况，难道小时候的我得了什么奇怪的病？{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}所以一定要努力学习才行。{/color}"
    girl_nvl "{color=#e5e5e5}而且还是两人份，嘿嘿。{/color}"
    nvl clear

    # TODO 77
    #CG：床底下的少女(疑惑)]"

    nvl_narrator "{color=#e5e5e5}女孩的肩膀似乎在微微的颤抖。{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}话说….{/color}"
    nvl clear
    
    girl_nvl "{color=#e5e5e5}你是谁呀？{/color}"
    nvl clear

    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}画面到此戛然而止。{/color}"
    nvl_narrator "{color=#e5e5e5}我好像进入了记忆的断层一般。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}从头到尾没有看到任何比较完整的信息。{/color}"
    nvl_narrator "{color=#e5e5e5}别的我无法做出确切的判断。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}但是毫无疑问，这是我自己的记忆。{/color}"
    nvl_narrator "{color=#e5e5e5}那么，我为什么会出现在这里？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我追寻着我来时的记忆，却忽然发现，我完全想不起之前的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}就仿佛我是个没有过去，同样也没有未来的人。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我卡在时间的中间，不知道自己身处何处。{/color}"
    nvl_narrator "{color=#e5e5e5}不知自己为什么在这里。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我可能存在着一个误区。{/color}"
    nvl_narrator "{color=#e5e5e5}我是擅自认为那个女孩确实是小时候的我根本就没有理由。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}那应该是小时候的夏静才对。{/color}"
    nvl_narrator "{color=#e5e5e5}说到底，我….真的是夏静吗？{/color}"
    nvl clear
    

    # TODO 78
    #CG:平凡的天才](夏津的黑影)"
    window hide Dissolve(.7)
    $ persistent.cg_x_genius = True
    scene x_沉迷学习 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}画面陡然发生了变化。{/color}"
    nvl_narrator "{color=#e5e5e5}我以为我还在黑暗里面。{/color}"
    nvl_narrator "{color=#e5e5e5}但是实际上，我能看到微微的弱光。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}有谁伏案在这里。{/color}"
    nvl_narrator "{color=#e5e5e5}这个房间的环境我完全看不清。{/color}"
    nvl_narrator "{color=#e5e5e5}当我靠近的时候，少女的样子在我的面前展露出来。{/color}"
    nvl clear

    # TODO 79
    #CG：平凡的天才]"
    
    nvl_narrator "{color=#e5e5e5}她的脸上都是绷带，就好像是受伤了一样。{/color}"
    nvl_narrator "{color=#e5e5e5}而且许多都是冷敷用的。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}最为明显的还是她的手腕，肉眼可见的红肿。{/color}"
    nvl_narrator "{color=#e5e5e5}在她的身旁，有着数不清的课本。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这些东西到底是什么？{/color}"
    nvl_narrator "{color=#e5e5e5}她又在做什么？{/color}"
    nvl_narrator "{color=#e5e5e5}这段回忆到底是怎么回事？{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}就在我这么想着的时候，阵阵的黑暗将我整个包裹起来。{/color}"
    nvl_narrator "{color=#e5e5e5}就像是忽然张开的幕布，朝我围了起来。{/color}"
    nvl clear

    # TODO 80
    #CG：雨中的女孩]"
    $ persistent.cg_x_yz = True
    scene c_雨中 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}原本这应该只是一场梦的。{/color}"
    nvl_narrator "{color=#e5e5e5}无数雨点打在我的身上。{/color}"
    nvl_narrator "{color=#e5e5e5}我望着漆黑的天空。{/color}"
    nvl clear
    
    x_nvl "{color=#e5e5e5}咦？{/color}"
    nvl_narrator "{color=#e5e5e5}然而我却没有发出声音。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}我看着手中的猫。{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}这是…什么情况？{/color}"
    nvl_narrator "{color=#e5e5e5}为什么我的手上会抱着一只猫？{/color}"
    nvl_narrator "{color=#e5e5e5}这只猫是什么时候出现在我手上的?{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}随着我的疑问，记忆渐行渐远了起来。{/color}"
    nvl clear

    jump c3_2_x