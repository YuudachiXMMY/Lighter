define y = Character("袁艳")
define l = Character("林琴")
define x = Character("夏静")
define c = Character("程祎琳")
define w = Character("我")

define mao = Character("猫")

define unknown_c = Character("？？")
define littlegirl = Character("小女孩")
define girl = Character("女孩")
define girl1 = Character("女孩①")
define girl2 = Character("女孩②")
define girl3 = Character("女孩③")
define ta = Character("他")
define yishen = Character("医生")
define doc = Character("护士")
define doc1 = Character("护士①")
define doc2 = Character("护士②")

##SelectData#########################################################
default c1_c1_l_select = False
default c1_c1_x_select = False
default c1_c1_c_select = False

default c1_c2_l_select = False
default c1_c2_x_select = False
default c1_c2_c_select = False

default c1_c3_l_select = False
default c1_c3_x_select = False
default c1_c3_c_select = False

default c1_c4_l_select = False
default c1_c4_x_select = False
default c1_c4_c_select = False

##init##############################################################
init:
    $config.auto_voice = "voice/{id}.mp3"

    transform lt:
        xpos 0.0 xanchor 0.0 ypos 1.7 yanchor 1.0 zoom 0.95

    transform rt:
        xpos 1.0 xanchor 1.0 ypos 1.7 yanchor 1.0 zoom 0.95

    transform ct:
        xpos 0.5 xanchor 0.5 ypos 1.7 yanchor 1.0 zoom 0.95

    define vpunch = Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275)
    define hp = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)

##Image############################################################
image b = "images/black.jpg"

# 游戏在此开始。
label start:
    $narrator = narrator
    $renpy.music.set_volume(1.3, delay=0.2, channel="voice")
    
    $_dismiss_pause = False
    
    stop music fadeout 1.0
    stop sound
    
    #$ persistent.girl = True
    
    narrator "很多的事情会被遗忘在时间的长河之中。"
    narrator "有时候怎么样都回想不起来，{w}某段时间的记忆。{w}\n就好像那段时间所发生的事情被蒸发掉了一般。{w}\n回过神的时候，{w}一切已经不知道从何谈起了。"

    #menu:
    #    "附加内容的快捷的测试"
    #    "继续":
    #        jump p1
    #   
    #    "test":
    #        jump c1_3

    jump p1

label p1:
    
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    $narrator = narrator

    nvl clear
    nvl hide
    window hide dissolve

    scene street_正午 with dissolve:
        zoom .667
    mao "喵~喵。"
    narrator "一只橘黄色的野猫朝着他叫着。"
    narrator "这里是陌生的城市，陌生得有些冰冷{w}——她真的会在这里吗？"
    narrator "裹紧了衣服，{w}他轻轻地呼了一口气。{w}\n朝着市中心走去。"
    narrator "如果找到她说不定会记起所有的事情。"
    narrator "好想找到她啊，真的…好想找到她啊！"

    window hide dissolve

    scene black with Dissolve(1.0)
    
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0
    
    scene room_白天 with dissolve:
        zoom .667
    
    narrator "房间里头的气氛有些异常。"
    narrator "三个女孩分别坐在四方桌的三个方向，{w}
    向静静地趴在桌上的我投来了各种不明情绪的目光。"
    narrator "虽然我也知道她们不是在看着我，{w}但是还是有些被看得毛骨悚然，{w}真想快点从桌上溜走。"
    narrator "可是我身后那个人却紧紧地把我抱住，{w}一点也没有打算让我溜的样子。"
    narrator "喂，你过分了啊。{w}\n死丫头，跟我有什么关系啊！这都是你自己干的啊。"
    
    show l 不满07 at ct

    girl1 "刚刚你说的事情不好好解释一下吗？"
    narrator "被叫做袁艳的女孩捏住了我后颈。"
    hide l with dissolve
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "事情就是这个样子。"
    y "要解释什么呀？"
    narrator "她捏着我后颈力度稍微变大了点，{w}但是还是装作什么事情都无所谓的样子。{w}语气非常的轻松。"
    #立绘？
    show y 正常01 d:
        xpos 0.5 xanchor 0.5
        linear .3  xpos 0.0 xanchor 0.0
    show l 不满07 at rt with dissolve
    girl1 "所以说，让我们去谈恋爱是什么鬼？"
    show y 正常01 at lt with dissolve
    #show l 不满07 d with dissolve
    y "是…是啊，你看你们毕竟是花季少女，难道不应该谈恋爱吗？"
    show y 正常01 d at lt with dissolve
    show l 不满09 at rt with dissolve
    girl1 "……"
    show l 不满08 at rt with dissolve
    girl1 "我并不明白你到底在胡说八道什么东西。"
    show y 正常04 at lt with dissolve
    #show l 不满09 d with dissolve
    y "就是想让你们体验一下谈恋爱的感觉啊。"
    y"不然你们的人生该有多浪费啊。"
    show y 正常04 d at lt with dissolve
    show l 不满08 at rt with dissolve
    girl1 "你是想找茬吗？"
    #show l 不满08 d with dissolve
    show y 无措 at lt with dissolve
    y "怎…怎么可能呢？"
    hide y with dissolve
    show l 不满07 at rt
    narrator "这个女孩瞪了袁艳一眼就不说话了，她坐了下去。{w}\n似乎是对来到这里的自己非常不满。"
    hide l with dissolve
    
    show c 注视01 at ct
    girl2 "零食管饱吗？"
    hide c with dissolve
    show y 俏皮 at ct with dissolve
    y "那…那个要看你的表现啦。"
    hide y with dissolve
    show c 斜视02 at ct with dissolve
    girl2 "这样吗？"
    narrator "这个女孩似乎并不满意这个答案，{w}但是也没有继续说话。"
    hide c with dissolve
    show y 正常02 at ct with dissolve
    y "……"
    hide y with dissolve
    show x 注视01 at ct with dissolve
    girl3 "……"
    narrator "第三个女孩没有说话。"
    hide x with dissolve
    show y 正常05 at ct with dissolve
    y "那个…"
    show y 正常04 at ct with dissolve
    y "林琴。"
    hide y with dissolve
    show l 普通07 at lt with dissolve
    girl1 "……"
    #show y 正常04 with dissolve
    y "程祎琳。"
    show c 注视01 at ct with dissolve
    girl2 "……"
    #show y 正常04 with dissolve
    y "夏静。"
    show x 普通01 at rt with dissolve
    girl3 "唔？"
    show l 普通07:
        linear .3 xpos .25 xanchor .25
    show c 注视01:
        linear .3 xpos .75 xanchor .75
    show x 普通01:
        linear .3 xpos 1.25 xanchor 1.25
    show y 开心 with dissolve:
        xpos -.25 xanchor -.25
    y "这件事情就拜托你们了！"
    narrator "袁艳双手合十，做出拜托的姿势。"
    narrator ""
    show l 普通09 with dissolve:
        linear .3 xpos .25 xanchor .25
    l "…"
    narrator "第一个女孩扶了扶脑袋。"
    show l 普通08 with dissolve:
        linear .3 xpos .25 xanchor .25
    l "我拒绝。"
    hide l
    hide x
    hide c
    show y 无措 at ct with vpunch
    y "啊？"
    show y 无措 d:
        linear .3 xpos 0.0 xanchor 0.0
    show l 普通08 at rt with dissolve
    l "如果没有什么别的事情，我就先走了。"
    narrator "她淡淡地说完了这一句话，起身就准备走了。"
    show y 恼火01 at lt with dissolve
    y "拒绝得那么干脆吗？"
    show y 恼火01 d at lt with dissolve
    l "……"
    show y 恼火02 at lt with dissolve
    y "你还真要走啊！"
    hide l
    hide y
    narrator "林琴头也不回地准备离开房间。"
    
    show y 恼火02 at ct with dissolve
    y "难道你打算见死不救吗，{w}你们不谈恋爱我就会死啊！！！"
    hide y
    narrator "袁艳伸出手想要叫住准备离开的林琴。"
    
    #show l 不满07 with dissolve:
        #linear .3 xpos 1.0 xanchor 1.0
    show y 恼火04 at lt with dissolve
    y "嗯？"
    show y 恼火04 d at lt with dissolve
    show l 不满07 at rt with dissolve
    #l "我想说两件事情。"
    #show l 不满09 at rt with dissolve
    l "我想说两件事情。\n第一件事情，你死不死跟我有什么关系？以为我会同情你吗？"
    show l 不满08 at rt with dissolve
    l "第二件事情，{w}我实在是…{w}完全不知道你在胡说什么。"
    show y 恼火05 at lt with dissolve
    y "……"
    show y 恼火05 d at lt with dissolve
    show l 不满09 at rt with dissolve
    l "再见。"
    hide l
    show y 恼火01 at lt with dissolve
    y "等…{w}等一下！"
    show l 普通07 at rt with dissolve
    l "还有什么事情？"
    narrator "即便是隐隐约约要发怒的模样，{w}但是林琴还是用十分冷静的语气反问了袁艳。"
    hide l
    show y 正常02 at ct with dissolve
    y "如果…{w}我是说如果，{w}如果你知道我在胡说什么的话…"
    show y 正常01 at ct with dissolve
    y "你就会帮我吗？"
    hide y with dissolve
    show l 普通08 at ct with dissolve
    l "……"
    narrator "林琴看了袁艳一眼，{w}然后离开了房间。"
    hide l with dissolve
    pause 0.7
    show y 正常02 at ct with dissolve
    y "走…{w}走掉了。"
    hide y
    narrator "房间里头的气氛变得更加古怪了。"
    show x 嘲笑01 at ct with dissolve
    x "真是场没意思的闹剧呢，袁艳。"
    show x 嘲笑01:
        linear .3 xpos 1.0 xanchor 1.0
    show y 正常03 at lt with dissolve
    y "谈恋爱不是特别有趣吗？"
    show y 正常03 d at lt with dissolve
    show x 嘲笑02 at rt with dissolve
    x "呵呵，你真可爱。"
    hide x with dissolve
    narrator "说完她也起身离开了房间。"
    show y 恼火01 at lt with dissolve
    y "喂喂，你别走啊别走啊…{w}我一定会找到很有意思的事情的！"
    show x 假笑01 at rt with dissolve
    x "那就等你找到了再来找我吧。"
    hide x with dissolve
    narrator "夏静礼貌地笑了笑，然后推门出去了。"
    pause .5
    show y 恼火04 at lt with dissolve
    show c 注视02 at rt with dissolve
    narrator "剩下的袁艳和程祎琳对视了一会儿。"
    narrator "程祎琳也起身看样子似乎是也要走了"
    show y 恼火02 at lt with dissolve
    y "连你也要走吗？"
    show y 恼火02 d at lt with dissolve
    show c 斜视02 at rt with dissolve
    c "嗯…{w}嗯。"
    show y 恼火03 at lt with dissolve
    y "唉，走吧走吧。"
    show y 恼火02 d at lt with dissolve
    show c 注视01 at rt with dissolve
    c "嗯。"
    show c 注视02 at rt with dissolve
    pause 1.0
    show y 恼火02 at lt with dissolve
    y "……"
    show y 恼火01 at lt with dissolve
    y "你不是说要走吗？"
    show c 侧视02 at rt with dissolve
    c "嗯…"
    hide c
    show y 恼火02 at ct with dissolve
    y "……"
    hide y
    show c 侧视01 at ct with dissolve
    c "……"
    hide c
    show y 恼火02 at lt with dissolve
    y "你还有什么事情吗？"
    show y 恼火02 d at lt with dissolve
    show c 注视03 at rt with dissolve
    c "嗯…"
    show y 笑容01 at lt with dissolve
    y "难不成是…"
    narrator "袁艳突然有些期待了起来。"
    show y 笑容01 d at lt with dissolve
    show c 注视02 at rt with dissolve
    c "那个…"
    show y 笑容01 at lt with dissolve
    y "嗯嗯！！"
    show c 斜视01 at rt with dissolve
    c "你桌上的零食很好吃，{w}可以送给我一些吗？"
    hide c
    hide y
    w "噗…"
    show y 笑容02 at ct with dissolve
    y "……"
    show y 嘲讽01 at ct with dissolve
    y "你想要吗？"
    hide y
    show c 斜视02 at ct with dissolve
    c "嗯。"
    hide c
    show y 嘲讽01 at ct with dissolve
    y "……"
    show y 嘲讽02 at ct with dissolve
    y "算了算了，{w}你全部拿去吧。"
    hide y
    show c 注视01 at ct with dissolve
    c "啊，谢谢！"
    hide c
    narrator "程祎琳雀跃地把桌上所有没有吃完的零食一份一份地放到了自己随身携带的小背包里头，{w}这才心满意足地离开了房间。"
    narrator "看袁艳满脸肉痛的表情，{w}我有些忍俊不禁。"
    narrator "差点没忍住要笑出来了。"
    narrator "直到三个人全部离开了这间屋子以后，{w}我这才松了一口气。"
    narrator "然后我突然后颈一疼。"
    
    w "喵？喵喵喵！！！"
    
    show y 恐怖颜艺 at ct with vpunch:
        zoom 1.4 ypos 2.2
    y "哈…哈哈哈哈哈哈。"
    narrator "那三个人走了之后，{w}袁艳像是疯了一样狠狠的捏住了我笑着。"
    narrator "我由惊叫转变为惨叫。"
    show y 颜艺02 at ct with dissolve:
        zoom 1.4 ypos 2.2
    y "你还给我装！"
    show y 恐怖颜艺 at ct with dissolve:
        zoom 1.4 ypos 2.2
    y "我让你叫，{w}我让你叫！"
    w "痛…痛啊！{w}放手啊！{w}快放手啊！"
    show y 恐怖颜艺 at ct with dissolve
    narrator "听到我口吐人言，袁艳这才放开了手。十分不爽地看着我。"
    w "啊…差点以为要死了。"
    w "凭什么我就不能喵啊喵啊的叫了？{w}好歹我也是货真价实的猫啊！"
    w "你对神圣的猫精灵不知道尊敬一下吗？"
    show y 不爽01 at ct with dissolve
    y "哈？{w}你跟我谈尊敬？{w}你忘了是谁让事情变成这样的吗？"
    w "咳咳…{w}我就说你那个办法根本就行不通啦。"
    w "你以为这事情是把她们三个叫过来谈谈就能解决的吗？"
    w "那未免也太看不起我的诅咒了吧。"
    narrator "我挠了挠后颈还有些疼的地方，{w}有些酸酸地说道。"
    show y 嘲讽01 at ct with dissolve
    y "哈？"
    show y 不爽02 at ct with dissolve
    y "那你倒是说说该怎么办啊！{w}被诅咒的人是我啊啊喂！"
    w "……"
    w "不过你别怕，{w}也就是被诅咒了而已。"
    show y 嘲讽02 at ct with dissolve
    y "说得倒是轻巧…"
    w "谁…谁叫你在我那么虚弱的时候还敢第一个碰我呢？"
    show y 嘲讽01 at ct with dissolve
    y "难不成这种事情还要怪我吗？"
    show y 嘲讽01 at ct:
        zoom 0.95 ypos 1.75
        linear 0.75 zoom 1.4 ypos 2
    narrator "袁艳朝着我凑了过来，{w}大有一言不合就要动手的意思。"
    w "冷静你先冷静一下。"
    w "与其浪费时间来揍我，{w}你不如想想该怎么解除诅咒。"
    narrator "我伸出我的爪子，{w}装模作样地说道。"
    show y 嘲讽02 at ct with dissolve
    y "让她们谈恋爱就可以了吗？"
    show y 嘲讽01 at ct with dissolve
    y "但是我干嘛要帮别人谈恋爱？"
    show y 不爽03 at ct with dissolve
    y "我自己都没男朋友好不好！"
    w "……"
    w "都说了不是谈恋爱，是帮她们点火啦！{w}你怎么就听不懂呢？"
    show y 恼火01 at ct with dissolve
    y "点火？{w}拜托你说人话好不好？"
    w "你就别为难我了，{w}我只是只猫啊。"
    w "但是是一只很神圣的猫。"
    show y 恼火04 at ct with dissolve
    y "既然你那么神圣就帮我解除诅咒啊！"
    w "要是我能解除诅咒我就不会跟你说话了。"
    show y 恼火02 at ct with dissolve
    y "我算是服了你了。"
    show y 不爽02 at ct with dissolve
    y "我还年轻，我还不想死！麻烦你好好给我负起责任啊！"
    w "我…{w}我怎么…{w}咳咳，{w}总之你只有十天时间，{w}今天已经是第二天了，{w}再有八天…"
    show y 不爽01 at ct with dissolve
    y "闭嘴！！！{w}你给我闭嘴，我不想知道。"
    narrator "少女纤细的双手狠狠地插入发间，使劲地在揉搓，似乎这样能想出什么办法一样。"
    hide y with Dissolve(0.2)
    
    stop music fadeout 9.0
    scene black with dissolve
    
    narrator "在这里我就不得不解释一下了。"
    narrator "现在我面前这个叫做袁艳的女孩正在面临着一个现实中绝对不可能发生的事情{w}——被诅咒了。"
    narrator "诅咒从开始到发作总共有十天左右的时间。"
    narrator "诅咒一旦发作，那么袁艳的灵魂就会逐渐被侵蚀；{w}\n换一句话来说，就是感觉到非常的疼；{w}\n并随着时间的延长而越来越疼，直到诅咒结束。"
    narrator "诅咒从发作到结束的时间会因人而异，{w}但是终点都是直接指向死亡的。 "
    narrator "如果想要解除诅咒，就只有一个办法{w}——那就是点火，{w}点燃灵魂的火焰。"

    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 1.0

    scene room_白天 with dissolve:
        zoom .667

    w "通俗一点说，就是拯救一个灵魂正在崩坏消失的女孩。"
    show y 正常01 at ct with dissolve
    y "…"
    y "那么那个女孩到底是谁啊？"
    w "就是那三个女孩之一，我之前不是跟你说了吗？"
    show y  正常02 at ct with dissolve
    y "那你既然知道了就赶紧点啊，点完就帮我解除诅咒啊！"
    w "要是可以的话我早就做了。"
    show y 笑容02 at ct with dissolve
    y "你总不会说你因为诅咒小姐我而导致你力量所剩无几，{w}所以没办法用你那力量点那个什么火了吧。"
    w "……"
    show y 无措 at ct with dissolve
    y "不会是真的吧！！！！喂！"
    w "也…也没那么严重啊，{w}至少我还能点燃一个的样子，{w}然后还能剩一点点力量。"
    show y 恼火05  at ct with dissolve
    y "……"
    w "不过请放心，{w}我一定会全力协助你的！"
    show y 恼火04 at ct with dissolve
    y "你？{w}协助我？"
    w "是的！"
    narrator "这不是出于好心，{w}而是因为这个破烂诅咒居然还是连带的，{w}这丫头死了的话那我也会跟着她陪葬。"
    show y 开心 at ct with dissolve
    y "那真是谢谢你啊，{w}意思是我们现在要帮她们谈恋爱吗？"
    w "你怎么老是扯到谈恋爱上面去啊！"
    show y 恼火04 at ct with dissolve
    y "那不是你最先说的吗？"
    w "我只是说在点完火之后以恋爱为肥料滋养灵魂啊！"
    show y 恼火05 at ct with dissolve
    y "那是什么？"
    w "啊，你一会聪明一会傻我很难办的啊！"
    show y 不爽01 at ct:
        pos (0.51 , 1.65) anchor (0.5 , 1.0) zoom 0.95
        linear 0.75 zoom 1.4 ypos 2.2
    y "……"
    w "啊…{w}疼疼疼…{w}别别捏了…"
    hide y with dissolve
    narrator "完全解除诅咒一共有两道步骤:"
    narrator "第一道是点火，{w}如果点火成功了，{w}那么就可以化解诅咒带来的生命危险。"
    narrator "但是诅咒所带来的疼痛是仅仅靠点火不能解除的。"
    narrator "第二道则是…"
    w "让她们恋爱的原因就是为了滋润她们的灵魂然后慢慢地减轻你受到的疼痛啊。"
    show y 恼火04 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "你早说嘛。"
    y "那要是到时候她们失恋了怎么办。"
    w "……"
    show y 恼火01 at ct with dissolve
    y "你说话啊！"
    narrator "我则是望向了一边。"
    w "我…{w}我怎么知道，{w}反正解除诅咒就不会死了。 "
    show y 恼火02 at ct with dissolve
    y "总觉得你有事情瞒着我。"
    w "……"
    show y 正常06 at ct with dissolve
    y "不说了不说了"
    show y 正常04 at ct
    y "那三个女孩是不是都有问题？"
    w "嗯。"
    y "那有什么问题呢？"
    w "你自己问她们不就行了？"
    show y 正常05 at ct with dissolve
    y "噗，{w}你不是吧，{w}刚刚还说全力协助我。"
    w "可是我也不知道多少啊。"
    show y 恼火05 at ct with dissolve
    y "那就把你知道的全说出来啊！"
    w "…"
    w "好吧。"
    w "首先第一个女孩——林琴，{w}她是林…"
    show y 正常03 at ct with dissolve
    y "林氏集团唯一继承人，{w}性格十分严谨，{w}而且非常得不好接近。{w}但是似乎得了什么疾病，现在正在医院里头接受治疗。"
    show y 正常02 at ct with dissolve
    y "是个有钱人。"
    w "……"
    w "你…怎么知道我要说什么？"
    show y 恼火02 at ct with dissolve
    y "你以为只有她么？"
    show y 正常01 at ct with dissolve
    y "夏静，{w}这个城市里头被誉为天才一样的存在，{w}十五岁就曾获得世界级少年组医学竞赛的二等奖，{w}不知道是不是因为获奖，{w}之后在各个领域都能看得到她天才一样的身影在活跃。"
    show y 正常03 at ct with dissolve
    y "程祎琳，{w}五年前的某场隧道崩塌时唯一一名幸存者，{w}但是因为那场灾难导致了精神方面似乎有点问题的女孩。"
    show y 正常02 at ct with dissolve
    y "我说的没问题吧。"
    w "你…"
    w "你都知道你还问什么啊？"
    show y 嘲笑 at ct with dissolve
    y "别闹了好吗？"
    show y 愤怒 at ct with vpunch
    y "这都是烂大街的情报了好不好。"
    y "麻烦你跟我说说别人都不知道的情报行不行，神圣的猫精灵。"
    y "不然你除了帮忙点个火你还能干什么？"
    w "哇，用不着说得这么过分吧。"
    show y 恼火05 at ct with dissolve
    y "…"
    w "行…行，那我就告诉你。"
    w "我就还真的知道你不知道的。"
    show y 恼火04 at ct with dissolve
    y "噢？"
    show y 恼火06 at ct with dissolve
    y "说来听听。"
    narrator "看袁艳那轻蔑的表情，{w}我冷笑了一下。"
    hide y with dissolve
    
    stop music fadeout 9.0

    narrator "小丫头，{w}你还年轻着呢。"
    narrator "我引动了身体的力量，{w}直接追溯那三个女孩的灵魂。"
    narrator "然后注视着她们的灵魂，{w}我缓缓地开口说着。"
    w "林琴她现在正在找一个人。"
    w "程祎琳现在找一个人。"
    w "夏静现在在找一个人。"
    w "……"
    narrator "然后我什么也说不出来了。"
    narrator "场面有些寂静。"
    show y 恼火01 at ct with dissolve
    y "没了？"
    w "没…没了。"
    show y 恼火02 at ct with dissolve
    y "……"
    
    narrator "袁艳看我的眼神有些奇怪。"
    narrator "我则是又看向了别的地方。"

    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0
    
    show y 嘲讽01 at ct with dissolve
    y "呵呵。"
    show y 正常02 at ct with dissolve
    y "我先去做饭了，{w}明天的事情明天再说，{w}今晚先好好吃饭吧。"
    w "……"
    narrator "总觉得好像她是故意转移话题来着。"
    narrator "但是小丫头你也太天真了，难道你以为这样我就会有一点愧疚吗?"
    narrator "虽然还是有那么一丢丢的。"
    narrator "她笑着，也不知道是不是看穿了我心里的想法。"
    show y 嘲讽01 at ct with dissolve
    y "服了你了。"
    #回眸无奈的笑
    show y 嘲笑 at ct with dissolve
    y "你肚子应该也饿了吧。"
    narrator "这个名字叫做袁艳的女孩，{w}在人类之中应该算是非常奇特的一类人了吧。"
    narrator "因为一时发了善心救了奄奄一息的我，{w}然后就被我诅咒而陷入非常奇怪的事情里头去了。"
    narrator "但是就昨天和今天我对她的观察来看。"
    narrator "该说她紧张还是镇定呢？{w}还是说这家伙其实有点没心没肺呢？"
    w "是有一点点饿。"
    narrator "我现在还活着，托了这个家伙的福。"
    w "…"
    narrator "不得不说的事情是她的接受能力强出了我的想象能力。"
    narrator "尽管她起初有点慌张，但是很快又恢复了原状并迅速了解了所有情况做出了行动。"
    narrator "时常还有些不情不愿的模样{w}——大概是嫌麻烦？"
    narrator "我都不知道该怎么正确给她下一个定义。"
    #【CG：回眸思考状】
    
    show y 正常01 at ct with dissolve
    y "最近好像天气有点干燥，做点下火菜吧。"
    narrator "最重要的事情是，上述那三个问题女孩，{w}她居然能用那么奇特的方法把她们一一请到家里做客。"
    narrator "虽然聊了一些天马行空的东西，但是她还是把重要的事情传达给了三个刚认识不久的女孩。"
    narrator "她确实做到了，尽管做法上…{w}有点奇特我在这里就不说了。"
    w "你会做吗？"
    show y 正常02 at ct with dissolve
    y "……"
    #【CG：回眸无奈的笑】
    show y 笑容02 at ct with dissolve
    y "今晚还是叫外卖吧！跟昨天你喜欢吃的那一份一样。"
    narrator "那三个女孩确实很棘手，我都是这么觉得的。{w}可是她虽然做得不是很完美，但是她确实…至少应付住了那三个女孩。"
    narrator "如果是她的话，应该能够解除诅咒吧。"
    w "喵！！"
    narrator "我晃了晃脑袋。"
    narrator "她有一句话说道我心里去了"
    narrator "什么事都等先吃饱了再说吧。"

    window hide Dissolve(2)
    stop music fadeout 4.0
    scene black with Dissolve(2)
    
    narrator "距离诅咒发作还有七天。"

    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve

    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0
    scene street_正午 with Dissolve(0.7):
        zoom .667
    
    narrator "一步一步地踩在这个有些陌生的土地，他长长地叹了一口气。"
    narrator "街道上没有什么人。"
    narrator "一个女孩远远地站在马路的那一边。"
    narrator "她向他投来十分惊讶甚至有些夸张的视线。"
    narrator "他却完全想不起有在什么地方见过她。"
    narrator "他转过身去，准备离开，因为他还有更重要的事情要做。"
    girl "老师等等我！！等等我！"
    narrator "他回过头去，瞬间就愣住了。"
    narrator "那个女孩没有在意任何别人的目光，十分慌张地直接越过了斑马线朝着他跑过去。"
    narrator "好像生怕他真的离开一样。"
    girl "老师…老师！！！"
    narrator "女孩仰着头，似乎激动地说不出话来。 "
    narrator "他则是一脸不知所措地看着她。"
    narrator "她低下头，伸出手拉住了他的衣角。"
    girl "老师，你终于回来了，是回来跟我结婚的吗？"
    narrator "女孩有些开心地说道。"
    narrator "……"
    narrator "？？？？？"
    ta "等一下，我们认识吗？"
    girl "哈哈，又在说这种话了。"
    girl "咦？老师你跑什么啊！！！站住！"

    window hide Dissolve(2)
    scene black with Dissolve(2)

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 1.0
    
    scene room_白天 with Dissolve(1.0):
        zoom .667
        
    
    w "……"
    w "哇哇哇…这都早上九点多了！你还窝在床上。"
    w "你真的不打算活了吗？"
    narrator "我跳上床，踩在她的胸口上，{w}使劲地用爪子砸着少女那宛如泛春的脸色"
    show y 嘲讽06 at ct with dissolve
    y "唔…唔嘿嘿嘿…别闹…"
    w "……"
    w "笑你个鬼啊！快起床啊！！！"
    narrator "说完又是一爪子实打实地砸在了袁艳的脸上。"
    show y 恼火03 at ct with dissolve
    y "哎呀！"
    narrator "顿时，我就知道大事不妙了，好像下手太重了。"
    narrator "我连忙跳下了床，准备跑路。"
    w "喵！！！！"
    narrator "为什么半空中还能被抓住尾巴，这个袁艳反应能力比我还快的吗？？"
    narrator "……"
    show y 愤怒 at ct with dissolve
    y "说啊？你接着说啊？怎么不说了？"
    narrator "少女的眼神无比的深邃，宛如被触怒了的女神一般。"
    narrator "她看着我，却又好像是在说今天早上就要开个荤试试看。"
    w "能把我先放下来吗喵~我恐高！"
    narrator "我被她抓住两只小腿倒吊在半空中。"
    show y 不爽01 at ct with dissolve
    y "我的脸让你抓花了你说该怎么赔我？你这只死猫。"
    w "还不是你怎么叫都不醒…"
    show y 不爽02 at ct with dissolve
    y "你想说什么？"
    narrator "刚想反驳，突然发觉这个少女正在用居高临下的眼神看着我，这让我瞬间明白了我此刻的地位。"
    w "喵~喵~"
    show y 不爽01 at ct with dissolve
    y "女人睡觉的时候是不能去打扰的，你妈妈没有教过你吗？"
    w "喵~喵…别…"
    w "别晃了了别晃了！！！！要死了，啊，要死了！"
    narrator "像是摇摇乐一样我被提在半空中被上下来回晃来晃去，我感觉昨天晚上吃的、今天偷吃的东西全部都想吐出来了。"
    w "姐姐，姐姐别晃了！别晃了啊！"
    show y 恼火06 at ct with dissolve
    y "你没听懂吗？"
    w "我听懂了听懂了，求求你快把我放下来吧！"
    show y 恼火02 at ct with dissolve
    y "我怎么觉得你一点反省的意思都没有？"
    w "姐姐别晃了，我屎都要让你晃出来了！"
    narrator "多亏了我这张能说会道的小猫嘴，某个恶毒的女人在听到我说完这句话之后停止了动作。"
    show y 恼火04 at ct with dissolve
    y "啧…"
    narrator "明显地嫌弃了一声，然后一把我扔到了地上。"
    narrator "眩晕之中，我翻了个身，完好无损的落到了地上。"
    narrator "脚都还没站稳我就觉得我作为神圣的猫精灵，我也是要面子的啊。"
    narrator "得找回场子。"
    w "……"
    w "喵~唔喵！！！！"
    w "死丫头，我跟你拼了！！"
    narrator "我一跃而起，向着邪恶势力扑了过去，要把刚才损失的脸面连本带利讨回来。"
    narrator "但是我马上就后悔了。"
    narrator "只见代表着邪恶势力的袁艳随手抄起了一本比我脸还大的字典，朝着我的面门迎来。"

    stop music fadeout 2.0
    
    window hide Dissolve(1)
    scene black with Dissolve(1)
    stop music
    $renpy.music.set_volume(0.2, delay=0.2, channel="music")
    play music "music/回忆.wav" loop fadein 2.0 fadeout 1.0
    
    narrator "一瞬间我想到了远在森林的老母亲，她身体还好么？{w}多久没有回去看看她了呢？{w}等这次事情结束以后就回去看看她吧，给她带点什么礼物呢？{w}她肯定会说什么也不要，只要我平安回去就好吧。"
    narrator "真好啊，活着。"
    narrator "……"

    stop music fadeout 1.0

    pause 0.2

    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 1.0
    
    nvl clear
    nvl hide
    window hide dissolve
    #【场景：房间2】
    scene room_白天 with dissolve:
        zoom .667
    
    
    show y 俏皮 at ct with dissolve
    y "好了好了，你看这是什么呀，昨晚没吃完的烤鸡肉噢！"
    w "…"
    narrator "我脑袋一撇，压根就不想看这个面前恶毒的女人。"
    
    show y 开心 at ct with dissolve
    y "你看，还有昨天吃的牛排…"
    narrator "我身体一阵抖动，但是我是绝对不会因为这点东西而偏移自己的立场的。"
    show y 开心 at ct with dissolve
    y "你不是神圣的猫大人吗？怎么可以因为这点事情就哭鼻子呢？"
    show y 笑容01 at ct with dissolve
    y "来，吃点东西，消消火！"
    w "我告诉你，你这个恶毒的女人，我就是饿死，也不会在吃你手上的东西！"
    w "而且你昨天根本就没吃鸡肉和牛排！！！"
    show y 笑容03 at ct with dissolve
    y "这里还有昨天顺便买的猫薄荷。"
    narrator "……"
    w "猫薄荷真好吃。"
    w "……"
    narrator "我看着正坐在沙发上看着电视，时不时还哈哈一笑的袁艳，突然愣住了。"
    narrator "还没来得及舔干净的猫薄荷一下子掉到了地上。"
    w "这是写剧本的王八蛋脑子抽了吗？"
    w "在这么写下去，我是真的要跟这死丫头陪葬了啊！"
    w "不行，我不能就这样不明不白地跟着她一起死了。"
    narrator "我舔了两口已经落在地上的猫薄荷。"
    w "喂！喂！！！！ "
    show y 正常02 at ct with dissolve
    y "…"
    show y 正常01 at ct with dissolve
    y "干嘛？ "
    w "你到底还要不要去解除诅咒了啊？"
    show y 无措 at ct with dissolve
    y "！！！！"
    w "看你的表情怎么好像感觉你把这事给忘了？"
    show y 嘲讽03 at ct with dissolve
    y "（吓）"
    show y 嘲讽03 at ct with dissolve
    y "胡…胡说八道…这个可是主线任务啊！"
    w "你到是知道这是主线任务啊！！"
    w "主线任务你也会九点多起床的吗？换做我我都睡不着觉了啊好不。"
    show y 正常04 at ct with dissolve
    y "事实上昨晚你睡得比我都好，连被子都是我帮你盖好的。"
    w "…"
    w "谢了。"
    w "哇哇哇哇…不是这样的啊喂！！！！"
    w "我是说既然你知道是主线任务你就别看电视了行不行？"
    show y 正常01 at ct with dissolve
    y "这一集都开始了好不好，等看完再说嘛！"
    w "不是，我说…喂你听到没有！！！！"
    show y 正常02 at ct with dissolve
    y "听到了听到了，这里猫薄荷还有点剩，喏，都给你了，一边吃去。"
    w "喔噢…"
    narrator "当我舔完猫薄荷的时候，电视机里头偶然响起了某部动漫的结尾曲。"
    narrator "我偶然的抬了抬头看了看钟。"
    narrator "然后偶然地有些惊讶——已经一点钟了。"
    w "……"
    w "！！！！"
    w "袁艳…"
    show y 正常01 at ct with dissolve
    y "干啥？"
    narrator "她嘴里咬着一块饼干，漫不经心地拿着遥控器换台。"
    w "你看看现在几点了…"
    show y 正常03 at ct with dissolve
    y "能有几点，我才刚刚起床没多久好不好。"
    narrator "她慵懒地转过头去看一边的钟表。"
    narrator "只听见啪嗒一声，饼干掉到了地上。她回过头来看了看我。"
    narrator "我看着袁艳。"
    w "……"
    show y 无措 at ct with dissolve
    y "……"
    narrator "尴尬地对视了一小会。"
    show y 俏皮 at ct with dissolve
    y "你…你肚子饿不饿？要不要点一份外卖？"
    show y 俏皮 at ct with dissolve
    y "嘿嘿嘿。"
    w "……"
    narrator "我们对视着谁也说不出话，却也明白了大难临头这个词究竟是有多么的沉重。"
    w "没…没事，至少我现在掌握了她们的行踪。"
    w "林琴现在正待在医院；程祎琳正在十字路口瞎逛；夏静也是在十字路口那里但是不知道在干什么。"
    show y 恼火06 at ct with dissolve
    y "额，这不是跟前天一模一样么？"
    show y 恼火06 at ct with dissolve
    y "算了算了，我先去准备一下吧。"
    w "嗯，接下来你打算去找谁？"
    w "先说明一下，我们只有一次机会，希望你做足了准备以后再进行选择与判断，这之中我会尽全力协助你。"
    w "但是由于我的力量所剩无几了，所以不到万不得已，我不希望孤注一掷。"
    show y 恼火04 at ct with dissolve
    y "……"
    show y 恼火05 at ct with dissolve
    y "你说了等于没说一样。"
    show y 恼火05 at ct with dissolve
    y "她们现在分别在干啥？可不可以获取她们的视角之类的？或者远程监控她们？"
    w "如果用我的力量的话，那当然是可以的。"
    show y 恼火04 at ct with dissolve
    y "那就用吧。"
    w "这点事情也要用我的力量？"
    show y 恼火04 at ct with dissolve
    y "这是观察情报好不好？？？"
    w "什么破情报，你自己去跟踪不行嘛？"
    show y 恼火04 at ct with dissolve
    y "别闹了死猫，我一个人跟踪她们三个吗？"
    w "……"
    w "确实…好像是有点没戏。"
    show y 恼火01 at ct with dissolve
    y "关于她们的真实情报其实我们也不是完全明白的对不对？"
    w "额。"
    show y 恼火02 at ct with dissolve
    y "那我们同时观察她们三个不是更好吗？"
    w "有点道理，确实是这样。"
    w "可是…"
    show y 恼火01 at ct with dissolve
    y "还可是什么啊？赶紧观察啊！"
    w "我这个力量真的是用一点少一点啊！"
    show y 恼火01 at ct with dissolve
    y "又不会少块肉好不好。"
    show y 愤怒 at ct with dissolve
    y "我要是没解除诅咒我可是会死的啊。"
    show y 恼火01 at ct with dissolve
    y "你这么对我难道你的良心就不会痛吗？"
    w "我都说了全力协助你了，你还想要怎么样啊！"
    show y 恼火02 at ct with dissolve
    y "你脸皮怎么这么厚啊喂！"
    w "脸皮厚的是你好不好！！"
    show y 愤怒 at ct with dissolve
    y "那你赶紧为我点亮她们啊，不随时随地观察她们，我怎么可能做出判断啊！！！"
    w "你就不知道自己去收集情报吗？我力量用完了怎么办？"
    window hide dissolve
    scene black with dissolve
    stop music fadeout 7.0
    narrator "结果我们一人一猫就为了情报这件事情整整吵了大半个下午，才终于双方互相妥协。"
    
    nvl clear
    nvl hide
    window hide dissolve
    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0
    
    scene room_黄昏 with dissolve:
        zoom .667

    narrator "回过神来的时候，已经是下午四点多的时候了。"
    narrator "夕阳渐渐的染红了房间。"
    
    #【场景：天空】
    
    show y 开心 at ct with dissolve
    y "（抿了一口茶水）哈啊…"
    w "（抱着杯子伸出舌头舔了一口水。）啊…"
    show y 笑容02 at ct with dissolve
    y "生活真是美好啊。"
    w "完全找不到反驳的理由呢。"
    show y 笑容01 at ct with dissolve
    y "我们到底是为了什么而争吵的呢？完全没有找不到头绪啊，我们不是同伴吗？"
    w "是啊，我们可是命系在一条绳子上的啊，还有什么不能和解呢？"
    w "如果没有诅咒那就更好了。"
    show y 笑容03 at ct with dissolve
    y "……"
    w "……"
    narrator "我自己愣了一愣，这么惬意的场景下我究竟在说什么玩意呢。"
    show y 笑容02 at ct with dissolve
    y "这么惬意的场景下，你究竟在说什么呢？"
    show y 开心 at ct with dissolve
    y "好好享受短暂的人生不好吗？"
    w "是猫生啦。"
    show y 笑容03 at ct with dissolve
    y "说得也是呢…"
    narrator "袁艳小小地抿了一口茶水。"
    show y 笑容01 at ct with dissolve
    y "说起来，你刚刚说我们是命系在一条绳子上的是怎么回事呢？"
    w "噢，那个啊？"
    w "还不是因为诅咒是连带的嘛，你被诅咒的时候，我也会被诅咒啊。"
    show y 开心 at ct with dissolve
    y "噢，原来是这样啊。"
    w "就是这样啊。"
    narrator "袁艳又抿了一口茶。"
    narrator "我则是也抱着杯子伸出舌头舔了舔水。"
    show y 笑容02 at ct with dissolve
    y "……"
    w "……"
    narrator "然后下一个瞬间，我俩突然像是反应过来了一样。"
    show y 愤怒 at ct with dissolve
    y "！！！！"
    w "！！！！"
    narrator "她惊讶地看着我。"
    narrator "我却突然愣住了，一不留神就把这么重要的事情给说了出来。"
    show y 恐怖颜艺 at ct with dissolve
    y "这也就是说，如果我被诅咒干掉了，你也跑不了对吗？"
        
    narrator "她莫名地坏笑了起来。"
    narrator "笑得我毛骨悚然。"
    w "……"
    w "呃呃呃呃呃…"
    narrator "既然说都说了，也不差那么一点。"
    narrator "于是我换上了一副沉重的口吻。"
    w "反正如果再过那么几天我们还没法解除诅咒，诅咒不仅会降临在你身上，也会同时降临在本喵身上。"
    show y 正常02 at ct with dissolve
    y "……"
    w "喂喂，你不会想和我同归于尽吧，别啊，我家上有老下有小的…"
    show y 正常01 at ct with dissolve
    y "……"
    show y 开心 at ct with dissolve
    y "哈哈哈…"
    narrator "估计是看着我哭丧着脸的模样，袁艳捧着茶放声笑了出来。"
    w "……"
    w "喵~有什么好笑的嘛？"
    show y 笑容01 at ct with dissolve
    y "就是觉得你也会有今天啊！"
    w "也不想想这是谁造成的。"
    show y 不爽01 at ct with dissolve
    y "哇？你还反咬一口，我救你还救错了？"
    w "呃呃也不是那个意思，就是说…"
    show y 正常01 at ct with dissolve
    y "不跟你说了，我去洗澡了。"
    hide y with dissolve
    narrator "她将茶水放到了一边，径直地走向了浴室。"
    w "……"
    w "喂喂，你这丫头不会想去厕所自杀吧！！！"
    narrator "那个名为浴室的地方实在是太危险了，我是这样认为的。"
    narrator "说着，我就碎碎念的跟着她准备进到浴室里头去。"
    narrator "那晓得这个家伙无比的狠毒，在进入浴室的一瞬间发觉了我正在跟随着她。"
    narrator "马上就拎起了我，朝着我屁股就是一脚。"
    narrator "然后我就从浴室里头被踢了出来。"
    w "哇，你个没良心的，我好心……"
    show room_黄昏 with vpunch
    narrator "还没等我从地上爬起来，她就把浴室的门给关了起来。"
    
    $renpy.music.set_volume(0.5, delay=0.2, channel="music")
    play music "music/ys.mp3" loop fadein 2.0 fadeout 2.0

    pause 1.0
    narrator "不一会儿，水流声就从里头响起。"
    narrator "我身上的毛几乎全部都竖了起来，这是一种来自心底的无力感。"
    w "喂喂，你别自杀啊！！！"
    narrator "我拼命的用爪子挠着浴室的门。"
    w "喵！！！喵！！！！"
    narrator "只见浴室的门拉开了一条缝。"

    window hide dissolve
    
    $renpy.music.set_volume(0.2, delay=1.0, channel="music")
    
    scene black with Dissolve(.7)
    $ persistent.cg_ys = True
    scene cg_浴室 with Dissolve(2)
    
    
    pause 1.0
    
    narrator "穿着内衣的袁艳用居高临下的眼神看着我。"
    w "……"
    w "怎…怎么了…"
    
    #show y 内衣01 at ct with dissolve
    y "你妈妈难道没有教过你，就算想偷看女生洗澡也要花点心思吗？"
    w "鬼才想偷看你啊！我是不想你去自杀啊！"
    #show y 内衣02 at ct with dissolve
    y "…"
    narrator "看她一愣，看了看浴室里头哗啦啦的水流，又看了我浑身警备的模样，好像瞬间明白了什么一样。"
    #show y 内衣01 at ct with dissolve
    y "喔哦！！"
    w "又…又怎了吗？？？"
    #show y 内衣02 at ct with dissolve
    y "你呀不是怕水吧？"
    w "我…"
    w "胡说…胡说八道。"
    w "像我这么神圣的猫怎么会怕水。"
    narrator "只见袁艳嘴角噙着坏笑，只穿着内衣的情况下拉开了浴室的门。"
    #show y 内衣01 at ct with dissolve
    y "那要不要来陪我一起洗澡啊？看你好像也好几天没有洗澡了的样子。"
    w "……"
    narrator "看着里头水流从喷洒器里头喷涌而出，我却退却了一步又一步。"
    #show y 内衣02 at ct with dissolve
    y "…"
    #show y 内衣01 at ct with dissolve
    y "来嘛客官！"
    narrator "袁艳笑眯眯地朝着我招手。"
    #show y 内衣03 at ct with dissolve
    y "你要是不来，我怎么敢洗澡啊，会死的。"
    #show y 内衣02 at ct with dissolve
    y "会死的噢！！ "
    w "……"
    w "你不洗澡不行嘛？"
    #show y 内衣01 at ct with dissolve
    y "那怎么行？我可是女生啊，女生不洗澡的话比死还要难受的。"
    w "……"
    #show y 内衣03 at ct with dissolve
    y "没有你…"
    #show y 内衣02 at ct with dissolve
    y "你要是不来的话…万一我真的死了。"
    narrator "说着她就做出了一副掩面的模样。"
    narrator "这让我又犹豫不决了起来。"
    #show y 内衣02 at ct with dissolve
    y "……"
    narrator "看我这副模样， 袁艳好像又多少觉得有些无聊了。"
    #show y 内衣01 at ct with dissolve
    y "喂，你到底是来还是不来啊，不来我去洗澡了。"
    w "我…"
    #stop music fadeout 4.0

    #"决定跟随着她一起前去洗澡。"
    #"决定让她把门开着，好让我随时注意她的安全。"

    menu:
        "决定跟随她一起前去洗澡":
            jump prologue_c1_1
            
        "决定让她把门开着，让我随时注意她的安全":
            jump prologue_c1_2
            
label prologue_c1_1:
    $_dismiss_pause = False
    
    narrator "在这里犹豫也不是办法。"
    narrator "我朝着前面踏出了一步。"
    w "真拿你没办法呢，既然你都这么请求我了。"
    #show y 内衣01 at ct with dissolve
    y "嘿嘿嘿…"
    
    nvl clear
    nvl hide
    window hide Dissolve(1)
    scene black with Dissolve(1)
    
    scene ys_1 with Dissolve(.7):
        zoom .667
    
    
    narrator "进入到浴室之后，袁艳关上了浴室的门。"
    narrator "我则是站在浴室的角落，这个位置刚好保证自己不会被水给溅到，又可以好好观察袁艳。"
    narrator "让她不至于陷入险境，必要的时候就算是动用力量救她也在所不惜。"
    show y 内衣01 at ct with dissolve
    y "……"
    show y 内衣02 at ct:
        pos (0.51 , 1.65) anchor (0.5 , 1.0) zoom .95
        linear 0.75 zoom 1.4 ypos 2.2
    y "嗯…"
    show y 内衣03 at ct:
        zoom 1.4 ypos 2.2
    y "总觉得，被你盯着感觉有些不自在。"
    w "你赶紧洗完赶紧出去。"
    narrator "咦？怎么感觉这个浴室有点热乎乎的。"
    show y 内衣01 at ct:
        zoom 1.4 ypos 2.2
    y "你不会有什么奇怪的想法吧，虽然你只是猫。"
    w "麻烦你矫正一下，我是一只神圣的猫。"
    show y 内衣02 at ct:
        zoom 1.4 ypos 2.2
        linear 0.7 pos (0.51 , 1.65) anchor (0.5 , 1.0) zoom .95
    y "是吗？"
    narrator "这里的空气有些不太适应。"
    show y 内衣02 at ct:
        pos (0.51 , 1.65) anchor (0.5 , 1.0) zoom .95
        linear 0.7 zoom 1.2 pos (0.51 , 2.0) anchor (0.5 , 1.0)
    narrator "就在她准备脱掉内衣的时候，我们两个视线又一次对上了。"
    show y 内衣02 at ct:
        zoom 1.2 pos (0.51 , 2.0) anchor (0.5 , 1.0)
        linear 1.25 pos (0.51 , 1.75) anchor (0.5 , 1.0)
        pause 0.6
        linear 0.5 pos (0.51 , 2.0) anchor (0.5 , 1.0)
    pause 2.6
    show y 内衣03 at ct:
        zoom 1.2 pos (0.51 , 2.0) anchor (0.5 , 1.0)
    y "……"
    show y 内衣03 at ct with vpunch:
        zoom 1.2 pos (0.51 , 2.0) anchor (0.5 , 1.0)
    w "啊嚏…"
    show y 内衣02 at ct with dissolve
    y "果然你还是出去吧。"
    w "为啥？我必须在这里保护你。"
    show y 内衣01 at ct
    y "我觉得你还是出去比较好。"
    w "不行，我不能就这样…"
    show y 内衣02 at ct with vpunch
    y "都说叫你出去了。"
    hide y with hpunch
    narrator "她把我拎起来，打开浴室的门，扔了出去。"
    w "你这个恶毒的女人……"
    narrator "只见她关上了浴室的门，我瞬间愣住了。"
    narrator "难道是因为想要让我离开那危险的地方？"
    narrator "我有些感动。"
    narrator "这丫头，还是挺讲义气的嘛。"
    narrator "我有些无力趴在地上，看着镜子里头自己颓废的模样。"
    w "咦？"
    narrator "我英俊的脸孔上，不知道何时，鼻血已经流出来很长了。"
    
    jump prologue_1

label prologue_c1_2:
    $_dismiss_pause = False

    w "…我还是不进去了。"
    #show y 内衣02 at ct with dissolve
    y "欸？那我该怎么办啊。"
    w "你把门开着怎么样？我随时注意你的安全。"
    w "如果你有危险，我会不惜一切代价使用力量把你救出来的。"
    #show y 内衣01 at ct with dissolve
    y "还有这种操作？"
    w "所以说你快点洗完出来啦。"
    #show y 内衣02 at ct with dissolve
    y "……"
    narrator "袁艳皱着眉头。"
    #show y 内衣03 at ct with dissolve
    y "这样吗？"
    #show y 内衣01 at ct with dissolve
    y "还真是搞不清你脑袋里头到底在想些什么东西啊！"
    
    nvl clear
    nvl hide
    window hide Dissolve(1)
    scene black with Dissolve(1)
    
    scene ys_1 with Dissolve(.7):
        zoom .7
    
    
    narrator "她走进了浴室，却并没有把门关上。"
    scene ys_1:
        zoom .7
        linear 1.0 zoom 0.8 xpos -250 ypos -50
    pause 1.0
    scene ys_1:
        zoom 0.8 xpos -250 ypos -50
        linear .7 xpos -256 ypos -50
        linear .7 xpos -250 ypos -50
        linear .7 xpos -256 ypos -56
        linear .7 xpos -250 ypos -44
        linear .7 xpos -250 ypos -50
        repeat
    pause .3
    narrator "我蹲在门的外头，眼睛一眨不眨的盯着袁艳所在的位置。"
    scene ys_1:
        zoom 0.8 xpos -250 ypos -50
        linear .3 xpos -100
    pause .3
    scene ys_1:
        zoom 0.8 xpos -100 ypos -50
        linear .7 xpos -106 ypos -50
        linear .7 xpos -100 ypos -50
        linear .7 xpos -106 ypos -56
        linear .7 xpos -100 ypos -44
        linear .7 xpos -100 ypos -50
        repeat
    narrator "现在她正在操作洒头，调整水流的位置——安全。"
    narrator "现在她正准备洗头发，好像洗好了——安全。"
    narrator "现在她正准备脱掉内衣，准备开始那所谓的洗澡。"
    narrator "我知道，接下来才是最关键的时候。"
    narrator "所以，我瞪大了眼睛，想要把浴室里头的一动一响都注意到，不放过任何可能招致危险的东西。"
    narrator "尤其是袁艳她本人的情况。"
    scene ys_1:
        zoom .8  xpos -100 ypos -50
        linear .7 zoom .667 xpos 0 ypos 0
    pause 1.1
    show y 内衣02 at ct with dissolve
    y "……"
    show y 内衣03 at ct:
        pos (0.51 , 1.65) anchor (0.5 , 1.0) zoom .95
        linear 0.75 zoom 1.4 pos (0.48 , 2.2)
    y "emmmmmm…"
    show y 内衣01 at ct with vpunch:
        zoom 1.4 pos (0.48 , 2.2) anchor (0.5 , 1.0)
    y "哇，受不了了！！！"
    hide y with dissolve
    narrator "突然一个黑色的物体从她手里脱手而出，我则是一时没有反应过来，或者说…"
    narrator "其实我反应过来了{w}——因为我是用脸朝着那个物体接去。"
    narrator "我知道我能力很优秀，所以我理所当然的接住了半空飞过来的不明物体。"
    scene ys_1 with hpunch:
        zoom .667
    narrator "然后，‘啪’的一声，浴室的大门被关上了。"
    narrator "那不明物体从我脸上滑落之后，我瞬间就愣住了。"
    w "？？？？"
    narrator "发生了什么？？"
    narrator "我愣愣的趴在了地上，不觉视线落到了镜子里头。"
    narrator "只见英俊的脸孔上，不知道何时，鼻血已经流出来很长了。"

    jump prologue_1

label prologue_1:
    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide Dissolve(1.0)
    scene black with Dissolve(1)

    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    narrator "我擦了擦鼻血，对浴室里头的那丫头简直无语了。"
    narrator "这个事情怎么说也是她挑起来的吧。"
    w "真是搞不懂这女人。"
    narrator "碎碎念了一句，然后头也不回地慢悠悠地朝着客厅的沙发走去。"

    nvl clear
    nvl hide
    window hide dissolve
    scene kt_夜晚 with Dissolve(1.5):
        zoom .667
    narrator "望着逐渐变暗的天色，我靠着沙发先伸了个懒腰。"
    narrator "沙发和我的爪子接触的时候发出了\'滋滋\'的摩擦声。"
    narrator "舒服些以后，我开始窝在沙发上享受着这静谧的时光。"
    w "……"
    narrator "总感觉好像把什么重要的事情抛在脑后了。"
    narrator "我摇着尾巴，慢慢开始有些不自在了。"
    w "emmmmm…"
    narrator "我终于意识到了，太悠闲了，悠闲的跟放了假一样。"
    narrator "我望着浴室的方向。"
    narrator "这真的是被诅咒吗？而且诅咒还有不到七天就要发作了啊。"
    narrator "要么是我想太多了，要么就是那个在洗澡的丫头神经太过大条了点。"
    narrator "很显然后者可能性更加的高吧。"
    w "…"
    show y 开心 at ct with dissolve
    y "呼…洗完澡就是舒服。"
    narrator "她拎着湿漉漉的头发穿好了衣服，从浴室里头出来。"
    narrator "在我默默的注视之下把头发吹干。"
    narrator "她坐到了沙发另一边，手里拿着一盒牛奶。"
    show y 嘲讽02 at ct with dissolve
    y "哈！这个时候喝酸奶真的是太爽了。"
    w "……"
    show y 嘲讽01 at ct with dissolve
    y "怎么了？肚子饿了吗？"
    show y 笑容01 at ct with dissolve
    y "我刚刚洗完澡心情还不错，说吧，你想吃些什么？"
    w "……"
    show y 笑容02 at ct with dissolve
    y "嗯？"
    w "唉。"
    narrator "我无奈的叹了一口气。"
    w "你怎么看起来跟之前完全不一样了啊？"
    show y 正常01 at ct with dissolve
    y "不一样？怎么说？"
    w "开始你还那么着急，现在怎么跟没意识到自己是被诅咒的人一样啊！"
    show y 恼火06 at ct with dissolve
    y "我说你就不能别提起这件事情？我都快被逼疯了。"
    w "……"
    w "快被逼疯的是我好不啦。"
    w "你看看你今天，都做了些什么？"
    w "哪里有半点像是被逼疯的样子？"
    show y 正常05 at ct with dissolve
    y "还不是因为你，既然能帮我监视这三个人的情报，为什么老是不同意呢？这是我今天唯一能做的事情啊！"
    w "啥？"
    show y 正常05 at ct with dissolve
    y "你笨嘛？我今天找她们能干什么？靠烂大街的情报去接近她们吗？"
    show y 正常04 at ct with dissolve
    y "那跟昨天发生的情况会有什么差别？"
    w "…"
    w "行吧行吧。"
    show y 正常06 at ct with dissolve
    y "打住，该吃饭的时候先吃饭吧。"
    narrator "她打断了我的话。"
    show y 正常04 at ct with dissolve
    y "已经是这个时候，肚子饿了吧？今天还是先做点吃的吧。"
    show y 正常04 at ct with dissolve
    y "然后晚点的时候在谈这件事。"
    w "……"
    narrator "我本来还打算说点什么，但是袁艳已经起身到厨房里头去了。"
    narrator "望着逐渐消失的夕阳，我长长的叹了一口气。"
    
    window hide Dissolve(2)
    scene black with Dissolve(2)
    stop music fadeout 1.0
    
    narrator "【序章：完】"
    narrator "诅咒发作倒计时还剩七天。"
    
    jump c1
    
label c1:
    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0
    
    scene street_夜晚 with dissolve:
        zoom .667
    
    #（色调变换）
    narrator "那个女孩在追他。"
    narrator "他慌张的穿梭在人群之中，喧闹的人群让他的心情无比的烦躁。"
    narrator "为什么他会逃跑？那还用说吗？她居然说要跟他结婚！！"
    narrator "虽然他觉得很高兴，但是他真的从来没有见过她啊。"
    girl "……"
    narrator "所以说，到底是怎么发生了什么啊？"
    ta "救命啊！！！！"
    
    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 1.0

    scene room_夜晚 with Dissolve(1.0):
        zoom .667
    
    ###2
    # TODO
    
    narrator "我静静坐在郑重其事的袁艳面前。"
    w "准备好了么？"
    show y 正常02 at ct with dissolve
    y "嗯。"
    w "那么你现在会先找谁呢？"
    show y 正常03 at ct with dissolve
    y "她们三个应该都没有睡吧。"
    w "……"
    w "嗯，三个人都没有睡。"
    stop music fadeout 1.0
    narrator "袁艳嘴角微微上扬，说出了答案。"
    
    menu:
        "这个人果然是——"
        
        "林琴":
            jump c1_c1_l
            
        "程祎琳":
            jump c1_c1_c
            
        "夏静":
            jump c1_c1_x

label c1_c1_l:
    $_dismiss_pause = False
    
    $c1_c1_l_select = True

    w "是她么？"
    w "跟我想得差不多呢。"
    show y 
    y "额…我根本就没怎么思考啊。"
    w "总之开始了，不过一开始会有点痛。"
    w "忍住了。"

    $renpy.music.set_volume(0.2, delay=0.2, channel="music")
    play music "music/采样预警1.wav" loop fadein 3.0 fadeout 2.0

    #施法
    narrator "随即，我闭上了眼，{w}将原本所剩无几的力量缓缓地从身体里头引出来，{w}然后注入了面前女孩的胸口。"
    show y 不爽02 at ct with dissolve
    y "哇…死猫你干什么！！"
    narrator "我没有回答，专心地把力量继续引导出来。"
    show y 不爽01 at ct with dissolve
    y "停啊停啊！！！我心那边好烫！！！快起火了！！！"
    narrator "我没有理会她的呼。"
    show y 不爽02 at ct with dissolve
    y "死猫！~！！！快停啊！！！！！"
    show y 不爽03 at ct with dissolve
    y "！！！！！"
    w "咳咳咳…"
    hide y with dissolve

    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0

    narrator "袁艳的身体像是断线的风筝一般倒了下去，栽倒在床上一动不动，眼神失去了光泽就仿佛死去了一般。"
    w "死丫头，你想得太简单了吧。"
    w "要想接近在黑暗中的心灵，就必须先点燃自己的心灵啊。"
    w "点燃自己的灵魂，又怎么会不痛呢？"
    w "……"
    w "好像说出了什么很了不起的话！！！"
    narrator "我擦了擦鼻子流出的鲜血，看着爪子上的血迹，又看着已经意识脱离了的袁艳，有些凄惨地笑了笑。"
    w "我说袁艳啊，你可一定要解除诅咒啊，不然我可真完了。"
    narrator "把血迹舔了几下以后，慢悠悠地爬了上了床，靠在了她的身旁闭上了眼睛，睡了过去。"

    #show l None
    
    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    stop music fadeout 1.0
    
    scene bf_夜晚 with dissolve:
        zoom .667

    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0
    
    
    show l 普通02 at ct with dissolve
    l "……"
    doc "小琴啊，吃点什么吧？"
    show l 普通02 at ct with dissolve
    l "嗯，放在那里吧，想吃的话我就会吃的。"
    narrator "她笑着看着面前的护士，十分有礼貌的拒绝了。"
    doc "每次你都没吃吧。"
    doc "在这样下去你会越来越虚弱的，还有昨天你怎么又偷偷跑出医院了？"
    #show l None
    l "……"
    #show l None
    l "没呢，就是出去玩玩。"
    doc "唉…"
    doc "你早点睡吧。"
    show l 普通01 at ct with dissolve
    l "嗯。"
    narrator "护士叹了口气，推门走出了病房。"
    hide l with dissolve
    show y 正常04 at ct with dissolve
    y "这家伙看起来真的病得不轻。"
    w "这点上我还是比较赞同你的。"
    show y 
    y "话说死猫，你到底干了什么鬼，怎么那么痛啊！还有为什么我会出现在这里啊。"
    w "咳咳，你现在可是完全脱离你的身躯，可以随时观察她了，你还想要怎么样啊。"
    show y 正常06 at ct with dissolve
    y "话虽然这么说，可是我怎么感觉被骗了。"
    w "额，我骗你干什么？"
    show y 正常04 at ct with dissolve
    y "我一开始还以为是那种蹲在家里像是那种魔法镜一样的方式观察她。"
    w "什么东西？"
    show y 正常02 at ct with dissolve
    y "就是那种跟摄像头一样的东西啦，可以随时随地的监视人的那种。"
    w "还有那种监视的办法吗？"
    show y 正常03 at ct with dissolve
    y "虽然跟想象中的不太一样，但是这样行动或许也比较方便就是了。"

    show l 普通01 at rt with dissolve
    show y 正常03:
        linear .3 xpos 0.0 xanchor 0.0
    l "嗯？"
    narrator "她看向了我们所在的方向，就好像看到了我们两个一样。"
    show y 无措 at lt with vpunch
    y "！！！"
    w "！！！！"
    show y 无措 at lt with dissolve
    y "她…她不会看到我们了吧。"
    w "怎么可能…"
    w "我们现在可是灵魂状态啊！！"
    narrator "噗，好像又说漏嘴了什么事情。"
    narrator "不过看袁艳的样子，似乎没有听清。"
    show l 普通03 at rt with dissolve
    l "袁艳么…"
    show y 无措 at lt with vpunch
    y "！！！！！"
    w "！！！！"
    show y 无措 at lt with dissolve
    y "天啊！死猫，她发现我们了！！！"
    w "怎…怎么可能啊！！！还有你能别一口一个死猫叫吗大姐！"
    show l 普通02 at rt with dissolve
    l "帮我谈恋爱吗？真是在搞笑啊。"
    show l 普通03 at rt with dissolve
    l "呵呵呵…我哪里来的时间啊，我连她都找不到。"
    show y 正常01 at lt with dissolve
    y "…"
    w "……"
    narrator "我们彼此尴尬地对视了一下，这个女孩好像是在自言自语。"
    show y 正常02 at lt with dissolve
    y "好端端的干嘛提起我啊，吓我一大跳。"
    stop music fadeout 1.0
    narrator "\‘砰\’"
    show y 无措 at lt with vpunch
    y "！！！"
    
    hide y
    hide l
    
    #【CG：崩坏的女孩】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_dxj = True
    scene cg_发狂的大小姐 with Dissolve(2)
    
    pause 1.0
    
    #show l None
    l "为什么会找不到她？呵呵呵…为什么会找不到呢？"
    
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0

    #show l None
    #l "呵呵呵…"
    #show l None
    #l "为什么会找不到呢？"
    narrator "她粗暴的扯掉了扎在身上的输液管的针孔。"
    narrator "用十分夸张的方式把输液瓶从高架台上拉了下来，瓶子随即掉在了地上，所幸的是瓶子上有保护套，并没有摔碎。"
    narrator "她撕扯着乳白色的床单。"
    narrator "鲜血从女孩的手背流了出来，染红了她手中碎裂的床单。"
    narrator "她就这么闹着，不知道什么时候才会结束。"
    narrator "我和袁艳就这么愣愣地看着她发疯。"
    narrator "渐渐地她好像有点累了。"
    narrator "手上的动作迟缓了下来。"
    narrator "泪水从她的眼角滑落，就好像一个无助的孩子。"
    narrator "她轻轻地撕扯着一开始被大力扯碎的床单。"

    scene bf_夜晚 with Dissolve(0.7):
        zoom .667
    
    $renpy.music.set_volume(0.2, delay=1.5, channel="music")
    
    show y 正常02 at lt with dissolve
    
    y "……"
    w "……"
    show l 注视02 at rt with dissolve
    l "你跑到哪里去了啊。"
    show l 注视02 at rt with dissolve
    l "到底在哪里才能找到你啊。"
    show l 注视01 at rt with dissolve
    l "我好想见你啊。"
    narrator "小声地呜咽声在病房里头回荡着。"
    narrator "我和袁艳一脸\‘啥情况\’的表情对望着。"

    w "……"
    w "这…这是发生了什么情况啊？"
    show y 正常02 at lt with dissolve
    y "额，你问我我怎么知道啊，你不是神猫么，这也要问我。"
    w "不是说关于她的事情我真的就知道她只是在找一个人吗。"
    show y 正常03 at lt with dissolve
    y "emmmmmmm…"
    w "你这是什么声音，你是想打架吗？"
    show y 正常01 at lt with dissolve
    y "啊？"
    w "我告诉你，这种状态下的你可是打不过我的！我告诉你！我告诉你哦…喂…"
    w "站住啊！我还没说完你怎么走了啊，你去哪啊！！"
    
    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0
    
    scene bf_夜晚 with dissolve:
        zoom .667
    #【场景：医院走廊】

    
    doc1 "唉…"
    doc2 "怎么了？又是那个丫头吗？"
    doc1 "可不是嘛，都快愁死我了。"
    doc1 "经常不肯吃不肯喝的，虽然很听话却不跟我配合，这么下去我这个月的绩效分怕是又要被扣光了。"
    doc2 "那丫头到底怎么了？她来了特殊病房都快一年多了都没出院，到底得了什么病啊？"
    doc1 "我倒是觉得这孩子没啥病，只是让人觉得有些异常，但是又说不上来哪里异常。"
    doc2 "啊？怎么说呢？"
    doc1 "我跟你说吧，你可得替我保密啊。"
    doc1 "怎…怎么了？我肯定替你保密，我发四！"
    doc1 "就是…虽然这样的情况很少，偶然我去查房的时候，这个丫头房间里头的床单都是破破烂烂的。"
    doc1 "上面还有血迹，而且输液瓶也掉在地上，有几次还是碎的。"
    doc1 "虽然她说是自己不小心从床上摔下来造成的，可是这哪里说得通啊。"
    narrator "看着两个护士离去。"
    show y 正常01 at ct with dissolve
    y "……"
    w "喂，你丫干嘛呢？"
    w "居然不听完我说话，还脱离观察范围跑到外面来。"
    show y 正常02 at ct with dissolve
    y "……"
    w "你听到没，我在说话呢！"
    show y 正常05 at ct with dissolve
    y "闭嘴你这只死猫，你没看到本小姐正在努力收集情报么？"
    w "哈？脱离观察对象来收集？你丫到底知道不知道你离观察对象越远，我能量消耗越大啊混蛋！"
    show y 正常04 at ct with dissolve
    y "额，是这样吗？"
    w "就是这样啊！"
    show y 正常05 at ct with dissolve
    y "真麻烦啊你，又不是所有情报都是正面可以打听到的。"
    show y 正常06 at ct with dissolve
    y "你以为你整天看她吃喝拉撒就能解决问题嘛？"
    w "你要收集情报，难道还有比全天观察她更好的方法吗？你又不会潜入心灵。"
    show y 正常01 at ct with dissolve
    y "潜入心灵？？？"
    w "！！！！"
    w "说漏嘴了！！！我的妈呀！"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "先回去吧。"
    w "……"
    narrator "这家伙突然的笑容看得我浑身的毛都炸了，毛骨悚然应该就是用来形容这种感觉吧。"
    w "真…真的要回去吗？"
    w "你都观察完了吗？"
    show y 
    y "你呀废话怎么那么多，你当我不累的啊！"
    narrator "我差点没叫出声来。"
    w "喵！你呀这才来了多久啊！"
    show y 恼火04 at ct with dissolve
    y "你再说我就睡在这里了。"
    w "……"
    narrator "袁艳看着我。"
    w "好…好…"
    w "这就回去，这就回去。"
    narrator "我连忙开口。"
    w "可能会有点疼，你忍着点。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 恼火01 at ct with vpunch
    y "什…么？？那我不回去了！！！"
    show y 恼火02 at ct with vpunch
    y "我不…"
    hide y with dissolve
    narrator "在她说完下一句的时候，我就闭上眼睛将她送了回去。"
    narrator "至于她的叫喊我那是一句也没听到。"
    narrator "送走了袁艳以后，我则是看了还留在病房里头的那个正在呜咽的女孩。"
    stop music fadeout 6.0
    scene black with Dissolve(.7)
    w "……"
    w "会是你吗？"
    narrator "我自言自语地说着，然后点燃了自己准备回去。"
    nvl clear
    nvl hide
    window hide Dissolve(2)
    
    jump c1_2

label c1_c1_c:
    $_dismiss_pause = False

    $c1_c1_c_select = True

    w "是她么？"
    w "跟我想得差不多呢。"
    show y 嘲讽04 at ct with dissolve
    y "额…我根本就没怎么思考啊。"
    w "总之开始了，不过一开始会有点痛。"
    w "忍住了。"
    
    stop music
    $renpy.music.set_volume(0.2, delay=0.2, channel="music")
    play music "music/采样预警1.wav" loop fadein 3.0 fadeout 2.0

    #施法
    narrator "随即，我闭上了眼，将原本所剩无几的力量缓缓地从身体里头引出来，然后注入了面前女孩的胸口。"
    show y 不爽01 at ct with vpunch
    y "哇…死猫你干什么！！"
    narrator "我没有回答，专心地把力量继续引导出来。"
    show y 不爽01 at ct with vpunch
    y "停啊停啊！！！我心那边好烫！！！快起火了！！！"
    narrator "我没有理会她的呼喊。"
    show y 不爽02 at ct with vpunch
    y "死猫！~！！！快停啊！！！！！"
    show y 不爽01 at ct with vpunch
    y "！！！！！"
    w "咳咳咳…"
    hide y with dissolve
    
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0

    narrator "袁艳的身体像是断线的风筝一般倒了下去，栽倒在床上一动不动，眼神失去了光泽就仿佛死去了一般。"
    w "死丫头，你想得太简单了吧。"
    w "要想接近在黑暗中的心灵，就必须先点燃自己的心灵啊。"
    w "点燃自己的灵魂，又怎么会不痛呢？"
    w "……"
    w "好像说出了什么很了不起的话！！！"
    narrator "我擦了擦鼻子流出的鲜血，看着爪子上的血迹，又看着已经意识脱离了的袁艳，有些凄惨地笑了笑。"
    w "我说袁艳啊，你可一定要解除诅咒啊，不然我可真完了。"
    narrator "把血迹舔了几下以后，慢悠悠地爬了上了床，靠在了她的身旁闭上了眼睛，睡了过去。"

    nvl clear
    nvl hide
    window hide dissolve
    stop music fadeout 1.0
    scene black with dissolve
    #【场景：街道】
    scene street_夜晚 with dissolve:
        zoom .667
    
    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0
    
    
    show c 注视01 at rt with dissolve
    c "嗯…"
    narrator "她似乎有些犹豫地站在十字路口，但是让她烦恼的好像并不是十字路口所带来的要去哪个方向的问题。"
    narrator "她望着两只手拿着的物品。"
    narrator "一边是薯片，另一边则是蚕豆。 "
    w "……"
    show y 正常05 at lt with dissolve
    y "嗯…"
    w "干什么？你看出了点什么吗？"
    show y 正常04 at lt with dissolve
    y "确实很难。"
    narrator "袁艳表情充斥着严肃，仿佛面临很重大的问题一样。"
    w "欸？很难什么很难？这个家伙难道很难对付吗？没法观察吗？"
    show y 正常06 at lt with dissolve
    y "各种意义上都是，根本就是史诗级的棘手啊。"
    w "这…这么难的吗？不会的吧。"
    show y 正常06 at lt with dissolve
    y "……"
    w "……"
    show y 恼火01 at lt with vpunch
    y "果然我不能对我的薯片见死不救！！！"
    w "啊？"
    w "……"
    w "？？？？？？"
    show y 愤怒 at lt with dissolve
    y "那个是她昨天从我那里拿走的东西啊！！！我要去救它，它正在朝我求救。"
    narrator "袁艳哭丧着脸指着正准备选择薯片的程祎琳对我非常没有出息地说道。"
    narrator "如果有镜子的话，我真想看看自己此时此刻的表情。"
    narrator "我抚上了眼睛，不想看一路朝着程祎琳小跑过去的袁艳。"
    narrator "即便如此，耳边还是传来了她那奇怪的惨叫声。"
    show y 嘲讽05 at lt with dissolve
    y "小薯…别怕！我就来救你了！啊啊啊啊，你这个死女人居然真敢下口真敢下口啊！"
    show y 愤怒 at lt with vpunch
    y "我饶不了你啊！！！！"
    narrator "……"
    narrator "袁艳半跪在正小口小口咬着薯片的程祎琳面前，泪如雨下。"
    w "我…我说，你这也太夸张了吧！"
    show y 愤怒 at lt with dissolve
    y "住嘴！死猫，你根本不知道这包薯片对我的意义。"
    w "……"
    w "反正你又没办法影响到她。"
    w "现在你就是灵魂状态而已。"
    narrator "噗，我去啊，怎么又不小心说漏嘴了。"
    narrator "我看了看袁艳，似乎她没有听到的样子。"
    show y 不爽02 at lt with dissolve
    y "这是何等痛苦的事情啊！啊，老天爷啊，你为何要这么对我…烤肉的薯片啊…"
    stop music fadeout 1.0
    w "……"
    show c 侧视02 at rt with dissolve
    c "唔…"
    show c 恶心01 at rt with dissolve
    c "唔!!!!"
    
    #【CG：被恶心的女孩】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_sw = True
    scene cg_泪水中的守望 with Dissolve(2)

    pause 1.0
    
    
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0

    narrator "就在我们说话的档口，程祎琳突然将薯片扔到了地上，捂住了嘴。"

    y "难道是被我吓到了？"
    narrator "虽然之前见过她也是捂住嘴巴的，以为那是洁癖，但是这一次似乎有点不一样。"
    narrator "她躬着身子，仿佛随时会吐出来一般。"
    narrator "眼泪不断地从她的眼角流下来。"
    narrator "瞳孔也在不断的变化着。"
    narrator "哪怕是我都知道，此刻她一定正在经历什么痛苦的事情。"
    
    
    #【CG:泪水中的守望】
    
    narrator "突然间，不知为何，她突然抬起头来。"
    narrator "在十字路口张望着，仿佛在寻找着什么。"
    narrator "弯着身子，她朝着前面走去。"
    narrator "配合着夜色，身处十字路口的她显得异常的诡异。"
    
    #【CG：结束】
    scene black with Dissolve(.7)
    stop music fadeout 1.0

    scene street_夜晚 with dissolve:
        zoom .667
    
    stop music
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0
    
    show y 不爽02 at ct with dissolve
    y "……"
    w "……"
    show y 正常02 at ct with dissolve
    y "她不会是生病了吧？"
    w "就算你这么问我我也不知道啊，而且你不是说她精神有问题么。"
    show y 正常01 at ct with dissolve
    y "这倒是，但是要是病了怎么办，回去给她打120吧。"
    w "打120是什么东西？"
    show y 正常02 at ct with dissolve
    y "额，以你的智商我很难跟你解释清楚。"
    w "喂！"
    
    #【CG:暴食的女孩】

    narrator "程祎琳撕开了蚕豆的包装袋，大口大口地望嘴里塞着蚕豆。"
    narrator "仿佛饿了许久的孩子一般。"
    narrator "然后一边流着眼泪一边拼命地咀嚼着。"
    show y 正常03 at ct with dissolve
    y "……"
    w "……"
    
    #【CG：结束】
    #scene street_白天 with dissolve
    scene black with Dissolve(.7)
    stop music fadeout 1.0

    scene street_夜晚 with dissolve:
        zoom .667
    
    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    narrator "该说什么东西呢，总之我和袁艳被面前戏剧性的变化弄得有些不知所措。"
    narrator "袁艳的表情有些复杂地在变换着。"
    show y 正常03 at ct with dissolve
    y "总觉得…"
    show y 正常03 at ct with dissolve
    y "事情比我们想象中还要复杂呢。"
    w "……"
    w "我觉得是你被妄想症给迫害了。"
    show y 正常05 at ct with dissolve
    y "还…还好吧。"
    show y 正常04 at ct with dissolve
    y "不过她到底是个什么情况啊？"
    w "我…我可不知道。"
    show y 正常05 at ct with dissolve
    y "是是是，还好我压根没指望过你。"
    w "你这样对神圣的我可是一种侮辱。"
    w "你是想跟我打架吗？"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常02 d at ct with dissolve
    narrator "她听完我说话以后，只是看了看我，没有说话。"
    narrator "可能也是因为之前自己在接触程祎琳的时候发现她完全没法触碰到她所以明白她现在的情况。"
    narrator "在这种情况下，就算我在怎么嚣张，她也是对我毫无办法的。"
    narrator "虽然我觉得好像有什么不对，但是不管怎么样，这回是我扳回了一局吧。"
    w "……"
    narrator "心里稍微有些小窃喜，但是却还是很凝重地看着程祎琳的一切行动。"
    narrator "没过多久，程祎琳似乎缓和了过来。"
    narrator "擦干眼泪以后，似乎已经完全恢复我们最初见到她时的状态了。"
    narrator "她拉了拉身上的小包的带子，独自一人离开了十字路口。"

    scene black with Dissolve(.7)

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0

    scene street_夜晚 with dissolve:
        zoom .667

    show y 正常02 at ct with dissolve
    y "……"
    show y 正常01 at ct with dissolve
    y "结束了呢。"
    w "好像是这么回事。"
    show y 正常02 at ct with dissolve
    y "我们也回去吧。"
    show y 正常03 at ct with dissolve
    y "不过总觉得有点被骗了的感觉呢。"
    narrator "袁艳松了一口气一般的笑着。"
    w "怎…怎么了？"
    show y 正常02 at ct with dissolve
    y "我一开始还以为是那种蹲在家里像是那种魔法镜一样的方式观察她。"
    w "什么东西？"
    show y 正常01 at ct with dissolve
    y "就是那种跟摄像头一样的东西啦，可以随时随地地监视人的那种。"
    w "还有那种监视的办法吗？"
    show y 正常02 at ct with dissolve
    y "虽然跟想象中的不太一样，但是这样行动或许也比较方便就是了。"
    show y 正常01 at ct with dissolve
    y "突然出现在十字路了口这里真的是把我吓了一跳啊。"

    w "你都观察完了吗？"
    show y 正常05 at ct with dissolve
    y "基本上有点想法了吧，不过你废话怎么那么多啊，赶紧送我回去睡觉啊！"
    w "喵！你呀这才来了多久啊！而且明明话比较多的人是你好不好？"
    show y 正常04 at ct with dissolve
    y "你的意思是我很罗嗦吗？"
    w "难…难道不是吗？"
    narrator "原本还有点胆怯，但是一想到现在我们的状态——就觉得已经没有什么好怕的了。"
    show y 正常06 at ct with dissolve
    y "你要是在不送我回去，我就到处去溜达了。"
    w "……"
    w "啊啊啊，别别！千万别，你要是离观察对象越远，我力量也会流失得越多的。"
    narrator "袁艳看着我，那眼神好像在说\‘那你这只死猫还不快点送我回去？\’。"
    w "好…好…"
    w "这就回去，这就回去。"
    narrator "我连忙开口。"
    w "可能会有点疼，你忍着点。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 恼火01 at ct with vpunch
    y "什…么？？那我不回去了！！！"
    show y 恼火02 at ct with vpunch
    y "我不…"
    hide y with dissolve
    narrator "在她说完下一句的时候，我就闭上眼睛将她送了回去。"
    narrator "至于她的叫喊我那是一句也没听到。"
    narrator "送走了袁艳以后，世界都仿佛安静了。"
    narrator "我看着那个渐渐离去的有些娇小的身影。"
    stop music fadeout 6.0
    scene black with Dissolve(.7)
    w "会是你吗？如果是就好了呢……"
    narrator "我自言自语地说着，然后点燃了自己准备回去。"
    nvl clear
    nvl hide
    window hide Dissolve(2)

    jump c1_2

label c1_c1_x:
    $_dismiss_pause = False

    $c1_c1_x_select = True

    w "是她么？"
    w "跟我想得差不多呢。"
    show y 正常02 at ct with dissolve
    y "额…我根本就没怎么思考啊。"
    w "总之开始了，不过一开始会有点痛。"
    w "忍住了。"

    stop music
    $renpy.music.set_volume(0.2, delay=0.2, channel="music")
    play music "music/采样预警1.wav" loop fadein 3.0 fadeout 2.0
    
    #施法
    narrator "随即，我闭上了眼，将原本所剩无几的力量缓缓地从身体里头引出来，然后注入了面前女孩的胸口。"
    show y 无措 at ct with vpunch
    y "哇…死猫你干什么！！"
    narrator "我没有回答，专心地把力量继续引导出来。"
    show y 无措 at ct with vpunch
    y "停啊停啊！！！我心那边好烫！！！快起火了！！！"
    narrator "我没有理会她的呼喊。"
    show y 无措 at ct with vpunch
    y "死猫！~！！！快停啊！！！！！"
    show y 无措 at ct with vpunch
    y "！！！！！"
    w "咳咳咳…"
    hide y with dissolve
    
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0
    
    narrator "袁艳的身体像是断线的风筝一般倒了下去，栽倒在床上一动不动，眼神失去了光泽就仿佛死去了一般。"
    w "死丫头，你想得太简单了吧。"
    w "要想接近在黑暗中的心灵，就必须先点燃自己的心灵啊。"
    w "点燃自己的灵魂，又怎么会不痛呢？"
    w "……"
    w "好像说出了什么很了不起的话！！！"
    narrator "我擦了擦鼻子流出的鲜血，看着爪子上的血迹，又看着已经意识脱离了的袁艳，有些凄惨地笑了笑。"
    w "我说袁艳啊，你可一定要解除诅咒啊，不然我可真完了。"
    narrator "把血迹舔了几下以后，慢悠悠地爬了上了床，靠在了她的身旁闭上了眼睛，睡了过去。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    stop music fadeout 1.0
    
    #【场景：街道】
    scene street_夜晚 with dissolve:
        zoom .667

    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0
    
    
    show y 正常02 at ct with dissolve
    y "……"
    w "你干嘛停下来啊。"
    show y 正常03 at ct with dissolve
    y "这家伙果然很奇怪啊。"
    w "你说谁？"
    show y 正常04 at ct with dissolve
    y "还能有谁？我们观察的是谁啊？"
    w "夏静？为什么这么说？"
    show y 正常06 at ct with dissolve
    y "你自己看咯。"
    narrator "顺着袁艳指着的地方，我看见一个女孩十分自然地在街道上走着。"
    narrator "而这个女孩就是夏静。"
    show y 正常06 at ct with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show x 普通02 at rt with dissolve
    x "……"
    w "她有什么奇怪的吗？"
    show y 嘲笑 at lt with dissolve
    y "你眼睛难道长屁股上去了吗？"
    show y 愤怒 at lt with dissolve
    y "谁让你只看她了，你忘了你之前说过什么吗？"
    w "喂喂，你放尊重点行不行？我之前说过什么了？"
    w "你想打架吗你？"
    show y 嘲讽01 at lt with dissolve
    y "你眼睛睁大点，看看前面那个是谁？"
    w "……"
    narrator "我接着看了下去。"
    stop music fadeout 1.0
    w "？？？？"
    w "她…她怎么也在这？？？"
    
    #【CG：被恶心到的女孩】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_sw = True
    scene cg_泪水中的守望 with Dissolve(2)

    stop music
    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0

    pause 1.0
    

    narrator "她躬着身子，仿佛随时会吐出来一般。"
    narrator "眼泪不断地从她的眼角流下来。"
    narrator "瞳孔也在不断地变化着。"
    narrator "哪怕是我都知道，此刻她一定正在经历什么痛苦的事情。"
    #show x 普通01 at rt with dissolve
    x "……"
    
    #【CG:泪水中的守望】
    
    narrator "突然间，不知为何，她突然抬起头来。"
    narrator "在十字路口张望着，仿佛在寻找着什么。"
    narrator "弯着身子，她朝着前面走去。"
    narrator "配合着夜色，身处十字路口的她显得异常的诡异。"

    scene black with Dissolve(.7)
    stop music fadeout 1.0
    
    #【CG：结束】
    scene street_夜晚 with dissolve:
        zoom .667
    
    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    show y 正常02 at ct with dissolve
    y "……"
    w "……"
    show y 恼火02 at ct with dissolve
    y "你好歹说点什么啊，夏静难不成现在是在跟踪程祎琳？"
    w "偶…偶然吧。"
    w "这个世界上巧合还真的是多呢。"
    w "话说程祎琳那边是什么鬼？"
    show y 正常04 at ct with dissolve
    y "我怎么知道她什么鬼，大概是病了吧。"
    w "神经病就是那样的？"
    #show y 
    y "…"
    #show y 
    y "她那只是普通的呕吐吧。"
    w "你不是说她有点精神不正常吗？"
    w "那不就是神经病发作的模样吗？"
    show y 正常05 at ct with dissolve
    y "我倒是觉得神经病发作的时候跟你是一样的。"
    w "喂喂！你这是挑衅身为伟大的猫精灵的我吗？"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常01 at ct with dissolve
    y "夏静为什么会跟着程祎琳呢？"
    narrator "袁艳不着痕迹地把话题带了过去。"
    w "都说了是凑巧吧。"
    show y 正常03 at ct with dissolve
    y "那行吧，暂时就这样了。"
    show y 正常01 at ct with dissolve
    y "我们也回去吧。"
    show y 正常02 at ct with dissolve
    y "不过总觉得有点被骗了的感觉呢。"
    narrator "袁艳松了一口气一般的笑着。"
    w "怎…怎么了？"
    show y 正常03 at ct with dissolve
    y "我一开始还以为是那种蹲在家里像是那种魔法镜一样的方式观察她。"
    w "什么东西？"
    show y 正常02 at ct with dissolve
    y "就是那种跟摄像头一样的东西啦，可以随时随地地监视人的那种。"
    w "还有那种监视的办法吗？"
    show y 正常04 at ct with dissolve
    y "虽然跟想象中的不太一样，但是这样行动或许也比较方便就是了。"
    show y 正常05 at ct with dissolve
    y "突然出现在十字路了口这里真的是把我吓了一跳啊。"

    w "你都观察完了吗？"
    show y 正常04 at ct with dissolve
    y "基本上有点想法了吧，不过你废话怎么那么多啊，赶紧送我回去睡觉啊！"
    w "喵！你呀这才来了多久啊！而且明明话比较多的人是你好不好？"
    show y 正常05 at ct with dissolve
    y "你的意思是我很罗嗦吗？"
    w "难…难道不是吗？"
    show y 正常06 at ct with dissolve
    y "你要是在不送我回去，我就到处去溜达了。"
    w "……"
    w "啊啊啊，别别！千万别，你要是离观察对象越远，我力量也会流失得越多的。"
    narrator "袁艳看着我，那眼神好像在说‘那你这只死猫还不快点送我回去？’。"
    w "好…好…"
    w "这就回去，这就回去。"
    narrator "我连忙开口。"
    w "可能会有点疼，你忍着点。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 恼火01 at ct with vpunch
    y "什…么？？那我不回去了！！！"
    show y 恼火02 at ct with vpunch
    y "我不…"
    hide y with dissolve
    narrator "在她说完下一句的时候，我就闭上眼睛将她送了回去。"
    narrator "至于她的叫喊我那是一句也没听到。"
    stop music fadeout 5.0
    scene black with Dissolve(.7)
    narrator "送走了袁艳以后，世界都仿佛安静了。"
    narrator "我看着那个渐渐离去的一前一后的两个身影。"
    w "真的会是巧合吗？"
    narrator "我自言自语地说着，然后点燃了自己准备回去。"
    narrator "却在无言之中，夏静突然回过了头。"
    nvl clear
    nvl hide
    window hide Dissolve(2)
    
    jump c1_2

    
label c1_2:
    $_dismiss_pause = False
    
    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667

    stop music
    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 1.0 fadeout 2.0
    
    
    narrator "喧闹中，我们总算是完成了一个人的观察。"
    w "……"
    narrator "我皱了皱眉头。"
    show y 正常02 at ct with dissolve
    y "……"
    w "……"
    show y 正常01 at ct with dissolve
    y "emmmmm？"
    w "所以你emmmm个什么劲啦！快把本喵放下来啊喂！你个死丫头！"
    narrator "我一脸凶恶的朝着面前的女孩张牙舞爪。"
    narrator "但是她似乎毫不在意。"
    narrator "因为我稍微比她回来得晚一点，她居然敢一脸无邪的微笑捏住我的双腿，把我提到半空中晃荡。"
    show y 正常01 at ct with dissolve
    y "你不是要跟我打架吗？"
    show y 正常02 at ct with dissolve
    y "好像刚刚很嚣张啊？"
    w "……"
    w "不好意思，神圣的喵是真的可以为所欲为的。"
    narrator "我啊什么都好，就是有一个坏习惯。"
    narrator "那就是始终会贯彻与恶势力做斗争的信念，永远不向恶势力低头。"
    narrator "……"
    w "姐姐我错了！我错了！我真的错了！"
    w "别晃了别晃了，我要吐了，我真的要吐了！"
    show y 正常04 at ct with dissolve
    y "你真的知错了吗？"
    w "我知错了知错了，以后再也不敢嚣张了。"
    show y 正常03 at ct with dissolve
    y "噢，那就好。"
    w "……"
    narrator "就当我觉得可以得救了以后……"
    show y 正常04 at ct with dissolve
    y "那灵魂状态是什么东西，给我解释一下。"
    w "！！！！"
    w "这…这可是我们一族最大的秘密…"
    show y 正常05 at ct with dissolve
    y "……"
    narrator "她看了我一眼。"
    show y 正常06 at ct with dissolve
    y "我允许你重新组织一下语言。"
    w "别…别别晃…我说，我说还不行吗？"
    show y 正常04 at ct with dissolve
    y "嗯，我会根据你说的内容考虑一下。"
    w "……"
    w "咳咳，其实是这样的。"
    w "其实你观察她们的时候，你自身的灵魂是脱离了你的肉体。"
    show y 正常05 at ct with dissolve
    y "啥？"
    w "嗯，是这样的。"
    w "虽然我知道你会很惊讶，但是我也没有想到你居然会这么惊讶。"
    w "果然对于凡人来说，这些事情告诉你们还是太早了些吧。"
    show y 正常04 at ct with dissolve
    y "不是，死猫，你说的什么鬼？"
    show y 正常02 at ct with dissolve
    y "灵魂状态？"
    w "只有死前才会有这样的状态。"
    show y 正常01 at ct with dissolve
    y "噗？？？"
    show y 正常01 at ct with dissolve
    y "我没听错吧，死前？"
    w "对啊，有什么问题吗？"
    show y 正常03 at ct with dissolve
    y "当然有问题啊！"
    show y 正常04 at ct with dissolve
    y "也就是我每次观察她们的时候都经历了濒死状态吧！"
    w "差不多是这样。"
    show y 正常05 at ct with dissolve
    y "我去，怪不得疼了一会儿就很恍惚，原来是…"
    w "……"
    w "你看着我干啥啊？"
    w "我该说的都说了啊。"
    show y 正常05 at ct with dissolve
    y "总觉得有点恼火，你干嘛不告诉我。"
    w "我…我干嘛要告诉你啊？"
    w "告诉了你你就会不观察了吗？"
    show y 正常04 at ct with dissolve
    y "那倒是不会。"
    show y 正常06 at ct with dissolve
    y "毕竟在怎么说也不是真的死了。"
    w "要是没弄好搞不好真的会死。"
    show y 正常05 at ct with dissolve
    y "你说了什么吗？"
    w "…"
    w "我是说你福大命大怎么可能会死呢。"
    show y 正常05 at ct with dissolve
    y "…"
    w "别拉了别拉了，脸要碎了碎了啊！"
    show y 颜艺02 at ct with dissolve
    y "我现在内心悲痛欲绝，而且这份悲痛正在逐渐转变为杀意。"
    narrator "……"
    narrator "不知道多久，她终于放开了手。"
    narrator "反应过来的我则是飞快地翻了个身，安全地落到了地上。"
    narrator "一阵一阵眩晕伴随着屈辱感冲上脑海。"
    narrator "我是谁啊，我可是前无古人后无来者、独一无二、最神圣的猫精灵啊。"
    w "……"
    w "小…丫头，我跟你拼…"
    narrator "袁艳带着淡淡地杀意朝着我笑了笑，晃了晃手上比我脑袋还大的字典。"
    w "拼一张床睡可以吗？"
    show y 正常01 at ct with dissolve
    y "……"
    show y 正常02 at ct with dissolve
    y "当然…当然不行啊。"
    show y 正常03 at ct with dissolve
    y "当然不行啊！你又不肯洗澡，等你洗完澡再说。"
    show y 正常01 at ct with dissolve
    y "还有，你身上还有血迹，怎么回事？"
    narrator "她看着我，露出了奇怪的表情。"
    w "你干什么？"
    narrator "她把我抱了起来，仔细的端详了一会儿。"
    narrator "然后起身到浴室那边去拿了一条湿润的毛巾过来，坐到我的边上把我又抱了起来。"
    w "你…要干什么啊？"
    narrator "冰冷的触感轻轻地触及了我的鼻尖。"
    show y 正常04 at ct with dissolve
    y "别动。"
    w "痒啊！"
    show y 正常05 at ct with dissolve
    y "忍一下啊。"
    w "……"
    w "嗯…"
    narrator "……"
    
    stop music fadeout 1.0
    
    #【场景：无灯房间】
    scene room_夜晚 with dissolve:
        zoom .667

    stop music
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    narrator "盖上了一张毯子，我睡在了地上。"
    narrator "尽管那个死丫头已经昏沉沉的睡过去了，房间里头回响着她轻轻的呼吸声。"
    narrator "可是我有点儿睡不着。"
    narrator "诅咒迫近的感觉环绕在我的周围。"
    narrator "仿佛只要伸出爪子触碰一下，它就会将我吸入周围的黑暗之中一般。"
    w "喵…"
    narrator "袁艳她不知道诅咒到底是什么东西，可是我是知道的。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)

    $renpy.music.set_volume(0.3, delay=0.2, channel="music")
    play music "music/彷徨.wav" loop fadein 1.0 fadeout 2.0
    
    #【场景：街道】
    scene street_正午 with dissolve:
        zoom .667
    
    
    girl "老师！！！"
    narrator "她大声地呼喊着，竭尽全力地追逐着。"
    narrator "他紧紧地皱着眉头，这丫头究竟要追多久啊！"
    narrator "至于吗，又不是欠了她钱。"
    narrator "突然一只手从某个角落伸出将他拉住，然后拽到了拐角处那边。"
    narrator "而之前那个女孩则是头也没回地冲了过去，似乎并没有发现他已经不在大路上了。"
    narrator "就在他松一口气的时候。"
    girl2 "老师…真的是..你。“
    ”另外一个女孩失神地看着他。"
    narrator "她的语气颤抖着。"
    narrator "他却觉得大难临头。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    
    narrator "距离诅咒发作还剩六天"

    ###############################################################

    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    
    #【场景：医院】
    scene yy_前台 with Dissolve(0.7):
        zoom .667
    
    show y 正常02 at ct with dissolve
    y "……"
    w "……"
    w "哈欠…"
    w "喵，你今天怎么这么一大早就起来了，怎么还跑到医院来了。"
    show y 正常01 at ct with dissolve
    y "带你去看医生啊。"
    w "啥？"
    w "我…我没病啊！"
    w "喂，你别走啊！你跟我说清楚啊！"
    narrator "看着袁艳离去的背影，我连忙跟了上去。"
    doc "欸？这位小妹妹，我们医院不允许把宠物带进医院。"
    show y 正常03 at ct with dissolve
    y "它不是我宠物啊，它自己跟过来的。"
    doc "可是…可是…"
    w "喵喵~~~"
    w "谁是宠物了！！！"
    narrator "正当我一跃而起叫出来的时候，袁艳突然一脚把我踢开了。"
    doc "额…我刚刚是不是听到那只猫说话了。"
    show y 开心 at ct with dissolve
    y "不，你听错了。"
    show y 恼火02 at ct with dissolve
    y "死猫，你这么光明正大地跟着我我怎么去看她，在这样今天晚上就把你烹了。"
    w "什……喵~"
    show y 恼火02 at ct with dissolve
    y "还不快走？！"
    narrator "我一愣，看着使劲朝我使眼色的袁艳，我瞬间明白了什么，叫了一声后暂时地跑离了医院，像一只猫一样。"
    doc "……"
    narrator "但是总觉得护士的脸色有点奇怪，似乎对袁艳的做法有些不太认同。"
    doc "小妹妹你还真是不喜欢动物呢。"
    show y 正常02 at ct with dissolve
    y "是啊，太麻烦了所以一点也不喜欢。"
    show y 正常03 at ct with dissolve
    y "不说了，有个叫做林琴的女孩应该在你这个医院吧，她在哪个病房？"
    narrator "护士的表情忽然就变了，变得有些不自在了。"
    doc "她…确实是在我们医院，不过见她的话要提前预约的啊。"
    show y 正常03 at ct with dissolve
    y "emmmmm…"
    doc "这个是有原因的啦，不过你是她的什么人呢？见她有什么事呢?"
    doc "方便的话请你在这里登记一下。"
    show y 正常04 at ct with dissolve
    y "哈？这么麻烦的吗？"
    narrator "袁艳有些不耐烦的样子。"
    narrator "我远远都看得出来。"
    doc "抱…抱歉。"
    narrator "那个护士似乎看起来有些诚恐，不如说莫名其妙地对袁艳有一些多余的畏惧。"
    show y 正常05 at ct with dissolve
    y "那算了，其实我也懒得去见她，不过至少让我知道她住哪个病房吧。"
    doc "欸？"
    show y 正常04 at ct with dissolve
    y "回去好交差啦，我觉得回去说老样子也没关系的。"
    show y 俏皮 at ct with dissolve
    y "但是起码我得知道她住哪里吧。"
    doc "噢噢，好…好的。"
    doc "林琴住在重症科的休养室病房，在三楼重症科最里头的那个房间里头。"
    show y 笑容01 at ct with dissolve
    y "嗯，我知道了。"
    show y 笑容02 at ct with dissolve
    y "我先走了。"
    doc "您慢走。"
    narrator "袁艳摆了摆手。"
    narrator "从医院里头走了出来。"
    show y 正常04 at ct with dissolve
    y "…"
    show y 正常05 at ct with dissolve
    y "你差不多也该出来了吧，我知道你看到了。"
    w "…"
    w "额，话说你到底想干啥啊。"
    w "还有那个女人怎么感觉把你当成什么大人物了一样？"
    show y 正常06 at ct with dissolve
    y "估计是因为林琴吧。"
    w "林琴？"
    w "啥？"
    show y 正常04 at ct with dissolve
    y "毕竟她的身份不简单啊，我估计。"
    w "……"
    w "那现在你要怎么办？"
    w "还要去见她吗？"
    show y 正常04 at ct with dissolve
    y "当然啊，见是肯定要见的，而且以后我还要她来主动见我。"
    w "额…"
    w "可是现在我们要怎么去见她啊？好像不让我们进去啊。"
    show y 正常05 at ct with dissolve
    y "嘿嘿嘿…你不知道么？世界上所有的业务在一开始的时候都是这样艰难的…"
    show y 正常06 at ct with dissolve
    y "没有从来没被拒绝过的推销员啊！"
    w "这跟推销员有半毛钱关系吗？话说推销员是什么鬼啊。"
    show y 笑容01 at ct with dissolve
    y "来吧，我教你怎么进去。"
    narrator "我半信半疑地跟着袁艳走了起来。"
    narrator "……"
    narrator "可是我万万没有想到的事情是…"
    
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    
    #【场景：三楼走廊】
    scene yy_走廊 with Dissolve(0.7):
        zoom .667
    
    
    w "冲…冲上来了？"
    narrator "我还没反应过来。"
    show y 无措 at ct with dissolve
    y "咦？怎么那边还有个医生？"
    narrator "连接走廊深处房间的道路上，还有一个白发苍苍的老医生正在那儿翻着文件。"
    w "额，你想怎么样？"
    show y 正常02 at ct with dissolve
    y "必须越过他溜到林琴的房间里头去了。"
    w "所以呢？"
    narrator "袁艳看了看我，若有所思地笑了笑。"
    w "……"
    narrator "……"
    show y 恼火01 at ct with dissolve
    y "医生医生…"
    show y 恼火02 at ct with dissolve
    y "快救救我的猫吧！他快死了快死了啊！"
    yishen "额，小姑凉你别着急你别着急。"
    show y 恼火02 at ct with dissolve
    y "医生你快救救我的猫吧！"
    narrator "袁艳用她的外套将我的身体裹住，然后换了一个发型突然从大门冲了进去，快得前台护士一时都没有看清。"
    narrator "等我回过神来的时候，我已经被这丫头无比浮夸的演技给震惊住了。 "
    w "……"
    yishen "小姑凉你冷静一下冷静一下！"
    show y 恼火05 at ct with dissolve
    y "……"
    show y 恼火04 at ct with dissolve
    y "让我怎么冷静啊，我的猫咪快要死了啊，我最喜欢的猫咪快要死了啊！"
    show y 恼火05 at ct with dissolve
    y "医生，你快救救它啊，好不容易能遇见你。医生，你一定要救救它啊。"
    w "……"
    narrator "这演技我真的是服了，真的想看看那个医生此时此刻的表情。"
    yishen "小姑凉，来，先让我看看你的小猫咪，刚好我也学过一些…"
    show y 恼火04 at ct with dissolve
    y "额…"
    show y 不爽01 at ct with dissolve
    y "你这个老流氓！！！"
    narrator "然后把我朝着医生抛了过去，自己反而先从走廊里头溜了。"
    yishen "！！！"
    w "喵！！！"
    narrator "撞到医生的脸之后，我想都没想，朝着医生脸连蹬了好几脚，我真不是故意的。"
    narrator "然后趁着医生都还没反应过来的时候，叼着袁艳的衣服飞快地跟着袁艳一起溜了。"
    yishen "……"
    yishen "呸呸呸。"
    yishen "这猫不是好好的吗？"
    yishen "那姑娘到底是来干什么的啊？"
    narrator "老医生挠了挠自己头上的白发。没想太多，继续翻阅起了文件。"

    #【场景：病房】
    scene bf_白天 with dissolve:
        zoom .667
    
    show y 恼火01 at ct with dissolve
    y "呼呼…"
    w "喵…"
    narrator "我放下了嘴上叼着的衣服。"
    show y 恼火02 at ct with dissolve
    y "！！！"
    show y 恼火01 at ct with dissolve
    y "喂，死猫，地上这么脏你也把我衣服丢在地上？"
    w "……"
    show y 恼火05 at ct with dissolve
    y "衣服上还有你的口水！！！"
    show y 恼火04 at ct with dissolve
    y "你知不知道我这件衣服多贵啊！！都快一两百块了啊！你怎么赔我啊喂。"
    w "喵…"
    show y 恼火04:
        linear .3 xpos 0.0 xanchor 0.0
    show l 惊异01 at rt with dissolve
    l "……"
    show y 恼火05 at lt with dissolve
    y "喂，你说话啊，你给我说话啊！"
    narrator "我说你要是有这份闲工夫倒是把衣服捡起来擦干净啊！"
    narrator "好想吐槽，但是袁艳掐着我的脖子，使劲地摇来摇去，让我一句话都说不出来。"
    show l 慌张02 at rt with dissolve
    l "你…们？"
    show y 正常05 at lt with dissolve
    y "额…"
    narrator "袁艳听到我们之外的声音以后立刻停下了动作，若无其事地捡起了衣服，穿了上去。"
    w "喵。"
    show y 正常04 at lt with dissolve
    y "咳咳，哦哟，这不是林琴吗？早上好啊！"
    narrator "袁艳不着痕迹地整理了一下自己身上的衣服，带着刚刚什么事情都与现在她无关的笑容。"
    narrator "十分冷静的同刚从病床上起来的林琴打了个招呼。"
    show l 不满02 at rt with dissolve
    l "早上好，话说你们怎么知道我在这里的？"
    narrator "林琴丝毫没有慌张，反而接下了袁艳的话语。"
    show y 笑容02 at lt with dissolve
    y "不是说了吗？我要帮你谈恋爱啊。"
    show l 普通01 at rt with dissolve
    l "…"
    show l 普通02 at rt with dissolve
    l "你不觉得你挺烦的吗？"
    show y 开心 at lt with dissolve
    y "还好吧，毕竟我是真心想要帮你啊。"
    show l 普通02 at rt with dissolve
    l "帮我？"
    show l 普通03 at rt with dissolve
    l "别搞笑了，你只是想帮你自己吧。"
    show y 正常05 at lt with dissolve
    y "…"
    show y 正常04 at lt with dissolve
    y "确实，我没法否定呢。"
    narrator "对话这就接上了？甚至连我们出现在这里都没有问，而是直奔主题？ "
    show y 正常05 at lt with dissolve
    y "但是我也确实是要帮你谈恋爱啊。"
    show l 普通02 at rt with dissolve
    l "谈恋爱有什么用么？"
    show l 普通03 at rt with dissolve
    l "我又跟谁谈呢？"
    show y 正常04 at lt with dissolve
    y "只要用心去找，就肯定可以找得到的吧。"
    narrator "袁艳好像是在鼓励林琴，但却又是另一个语气，宛如话里有话一样。"
    show l 普通01 at rt with dissolve
    l "……"
    show l 惊异 at rt with dissolve
    l "什么意思？"
    narrator "林琴在听完袁艳说的话以后，突然就眼神一变，甚至连病房里头对的气温都瞬间上升了许多。"
    show y 开心 at lt with dissolve
    y "是啊，什么意思呢？"
    show l 不满01 at rt with dissolve
    l "我再问你，你刚刚说的那句话是什么意思？"
    narrator "她从病床上站了起来，一股扑面而来的压力陡然升起。"
    show y 笑容01 at lt with dissolve
    y "如果方法不对的话，是什么都找不到的吧。"
    show l 不满02 at rt with dissolve
    l "…"
    narrator "袁艳却不以为然地说道。"
    narrator "林琴似乎愣住了。"
    show l 普通02 at rt with dissolve
    l "那到底该怎么办呢？怎样才能找的到呢？"
    show y 笑容02 at lt with dissolve
    y "呵呵…"
    narrator "袁艳笑了笑，没有说话。"
    w "喵喵喵？"
    narrator "她们两个到底在聊什么玩意？我怎么完全听不懂？感觉都好像话里有话一样。"
    narrator "所以才说人类真的是奇怪啊，连这种不明其意的对话都能谈下去真的是各种意义上都很了不起。"
    show y 笑容03 at lt with dissolve
    y "这么快又饿了？回去再给你喂吃的。"
    w "喵？"
    narrator "我有说过我饿了吗？拜托你走走心好不好。"
    narrator "虽然我很开心你关心我，但是你跟我说话的时候能不能不要看着林琴？"
    narrator "我有点抓狂，差点忍不住想要吐槽她了。"
    show l 普通03 at rt with dissolve
    l "……"
    show l 普通01 at rt with dissolve
    l "说吧，你有什么条件？"
    show y 笑容03 at lt with dissolve
    y "说的也是呢，要开个什么条件呢？"
    show l 普通02 at rt with dissolve
    l "先让我确认一下吧。"
    show l 普通01 at rt with dissolve
    l "我可以相信你手中的消息吧？"
    show y 笑容02 at lt with dissolve
    y "你在说什么呢？我怎么有点听不懂。"
    show l 普通03 at rt with dissolve
    l "……"
    show l 不满02 at rt with dissolve
    l "你到底是在耍我还是在装傻？"
    #show l None
    l "还是说你觉得我拿不出你想要的东西？"
    show y 不爽01 at lt with dissolve
    y "所以说让你好好谈恋爱啊——作为一个女孩子，没有遇见迟早会遇见的。"
    show l 不满01 at rt with dissolve
    l "够了！你给我出去。"
    show y 笑容01 at lt with dissolve
    y "这就要我走了吗？你确定？"
    show y 笑容03 at lt with dissolve
    y "难道你就不好奇我是怎么找到你的吗？"
    show l 不满01 at rt with dissolve
    l "这关我什么事？"
    show y 正常04 at lt with dissolve
    y "你还真是不够聪明呢。"
    show l 普通01 at rt with dissolve
    l "那你还真的很让人烦躁啊，想说什么就快点说，我不想对你发火。"
    narrator "袁艳似乎有一点动摇，老实说听到林琴说这句话的时候我联想到了昨晚的那一幕。"
    show y 正常04 at lt with dissolve
    y "我…既然能找到你，也自然能够让你见到那个人。"
    show l 普通03 at rt with dissolve
    l "谈恋爱就免了，我真的没那个心情。"
    show y 正常02 at lt with dissolve
    y "我既然说了，那真的就只是谈恋爱吗？"
    show y 正常01 at lt with dissolve
    y "难道你就不想找到那个人么？"
    show y 正常03 at lt with dissolve
    y "你应该找了很久才是吧。"
    narrator "袁艳突然笑了起来。"
    narrator "林琴却突然愣住了，似乎十分的震惊。"
    show l 惊异 at rt with dissolve
    l "你…你难道可以找到她？？？？"
    show y 开心 at lt with dissolve
    y "我这里可没有什么消息噢？"
    show l 惊异 at rt with dissolve
    l "……"
    show l 惊异 at rt with dissolve
    l "那到底是什么你快说啊！！！"
    narrator "突然林琴有些狂躁地吼了出来。"
    show y 正常01 at lt with dissolve
    y "等…你见到她你就知道了。"
    narrator "袁艳似乎在咬着牙齿，但仍然保持着镇定。"
    show l 普通02 at rt with dissolve
    l "你说什么？？"
    show y 正常04 at lt with dissolve
    y "就如字面意思。"
    show l 不满02 at rt with dissolve
    l "我…可以见到她？"
    show y 笑容03 at lt with dissolve
    y "呵呵，没别的事情我就先走啦。"
    narrator "说完，袁艳就一把把我抱住，不知道为什么我却能感觉到袁艳的手在颤抖。"
    show l 惊异 at rt with dissolve
    l "等一下。"
    show y 开心 at lt with dissolve
    y "还…还有什么事情呢？"
    show l 普通02 at rt with dissolve
    l "你真的就只是打算让我谈恋爱吗？"
    show y 笑容03 at lt with dissolve
    y "除此之外，如果因为你谈恋爱而让我变得轻松一点的话会是一件很不错的事情呢。"
    show l 普通01 at rt with dissolve
    l "那现在我需要做什么?"
    show y 笑容03 at lt with dissolve
    y "今天晚上，去我家里吧。"
    show y 笑容02 at lt with dissolve
    y "你可以去吗？"
    show l 普通01 at rt with dissolve
    l "为什不是现在呢？"
    show y 开心 at lt with dissolve
    y "请客人的话，当然不能只请你一个人啊。"
    show l 普通01 at rt with dissolve
    l "…"
    narrator "她看了看我们。"
    narrator "似乎是忍住了自己的躁动。"
    show l 普通03 at rt with dissolve
    l "这样么，我知道了。"
    show l 不满01 at rt with dissolve
    l "你最好保证你说的是真的。"
    show l 不满01 at rt with dissolve
    l "不然的话…"
    show y 开心 at lt with dissolve
    y "那我会在家里静静等你们来的。"
    narrator "袁艳笑了笑打断了林琴的话。"
    show l 普通01 at rt with dissolve
    l "…不好意思，失礼了。"
    show y 笑容03 at lt with dissolve
    y "嘿嘿。"

    #【场景：走廊】
    scene yy_走廊 with dissolve:
        zoom .667
    
    
    narrator "关上了病房的门。"
    w "…"
    show y 嘲讽04 at ct with dissolve
    y "呼呼…"
    narrator "她突然奔跑了起来"

    #【场景：街道】
    nvl clear
    nvl hide
    window hide dissolve
    scene river_白天 with Dissolve(.2):
        zoom .667
    $renpy.pause(.3,hard=True)

    #【场景：商店】

    #【场景：十字路口】
    scene street_白天 with Dissolve(.8):
        zoom .667
    $renpy.pause(1.0,hard=True)
    
    
    w "别…别跑了大姐，大姐别跑了。"
    show y 愤怒 at ct with dissolve
    y "啊啊啊啊。"
    narrator "听到我的呼喊声之后，她这才有停下来的意思。"
    w "我说你跑什么啊？你刚刚不是说得挺好的吗？效果好像还不错的吧。"
    show y 正常02 at ct with dissolve
    y "呼…"
    narrator "她大口地喘着气，好一会儿才回我。"
    show y 正常02 at ct with dissolve
    y "要…要死人了。"
    w "欸？"
    narrator "袁艳她一脸慌张，似乎还在发抖。"
    w "不是吧？？？"
    w "这么夸张？"
    show y 无措 at ct with dissolve
    y "啊？"
    w "你怎么眼泪都流出来了。"
    show y 正常05 at ct with dissolve
    y "有吗？"
    narrator "她似乎是完全没有意识到。"
    w "哇，说着说着你鼻涕都流出来了。"
    show y 愤怒 at ct with dissolve
    y "去死啊你居然敢骗我，你信不信我戳瞎你眼睛。"
    w "别！"
    narrator "我赶紧用爪子挡住了眼睛。"
    show y 正常02 at ct with dissolve
    y "……"
    narrator "不过，似乎这样她就缓过来许多，不一会儿就恢复了原状。"
    w "……"
    show y 恼火02 at ct with dissolve
    y "看什么？"
    narrator "袁艳的脸上写着不满。"
    w "你不至于吧，这么害怕的吗？"
    show y 恼火01 at ct with dissolve
    y "我怎么知道。"
    show y 恼火02 at ct with dissolve
    y "只是觉得当时她是有点想弄死我的感觉，会怕不是很正常吗？"
    w "……"
    w "我可是完全没觉得你怕过啊！你的心到底是怎么长的啊？？？"
    show y 恼火01 at ct with dissolve
    y "我怕的话还要跟你说的吗？"
    w "……"
    w "好像确实不需要。"
    show y 恼火05 at ct with dissolve
    y "那不就是了。"
    show y 正常05 at ct with dissolve
    y "……"
    w "那我们接下来去干什么？"
    show y 正常04 at ct with dissolve
    y "嗯…去找那个神经有点问题的女孩吧。"
    w "什么？"
    show y 正常04 at ct with dissolve
    y "喏，就是那个家伙。"
    show y 正常04 with dissolve:
        linear .15 xpos 0.0 xanchor 0.0
    show c 注视02 at rt with dissolve
    c "……"
    narrator "十字路口的那儿，女孩静静地站在红绿灯的一旁。"
    show y 俏皮 at lt with dissolve
    y "喲~"
    narrator "还不等我反应过来，袁艳又已经凑上去打招呼了。"
    w "…"
    narrator "好歹征求一下我的意见啊。"
    show c 斜视01 at rt with dissolve
    c "噢！（似乎是稍微回应一下）"
    show y 俏皮 at lt with dissolve
    y "想不到我们又见面了呢！我已经给你准备了好东西。"
    show c 注视01 at rt with dissolve
    c "喔！（似乎有点兴致高涨）"
    show y 笑容01 at lt with dissolve
    y "今晚就在我家，我请。"
    show c 张嘴01 at rt with dissolve
    c "哦！！！！！"
    w "？？？"
    show y 开心 at lt with dissolve
    y "那我就在家里等你咯。"
    show c 斜视02 at rt with dissolve
    c "好~~~~~~~"
    show y 笑容02 at lt with dissolve
    y "那我们先走啦！"
    hide y
    show c 注视03 at ct with dissolve
    c "请慢走！"
    narrator "女孩深情款款地鞠了一躬。"
    narrator "那眼神就仿佛跟期待着玩具的小孩子一模一样。"
    hide c with dissolve
    show y 笑容02 at ct with dissolve
    narrator "我只能目瞪口呆地跟着袁艳在街道上溜达起来。"
    w "……"
    w "这就…完了？？"
    show y 正常04 at ct with dissolve
    y "完了啊。"
    w "完了？？？"
    show y 正常05 at ct with dissolve
    y "不然呢？"
    narrator "她故作惊讶地看着我。"
    show y 正常04 at ct with dissolve
    y "你难道不知道吃货之间的对话都是直指核心的吗？"
    w "还…还有这种说法吗?"
    show y 正常06 at ct with dissolve
    y "这你就不知道了。"
    show y 正常05 at ct with dissolve
    y "等级相同的对手，对话可是很简洁的。"
    w "啊？"
    w "好的好的，我知道了我知道了。"
    w "那么接下来果然是去找她了么？"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "只见袁艳望着别处，吹起了口哨。"
    narrator "装作完全没有听到我说话的样子。"
    w "喂！"
    w "你不会完全不想去吧？"
    show y 嘲笑 at ct with dissolve
    y "……"
    narrator "我就这么看着她。"
    show y 不爽03 at ct with dissolve
    y "啊…是啦是啦，我是不想去找她啦。"
    w "……"
    show y 不爽02 at ct with dissolve
    y "看到她那样你就想去找她了么？"
    show y 正常06 at ct with dissolve
    y "我可不想以后被她鬼鬼祟祟的跟踪。"
    w "……"
    w "我个人还是觉得她挺不错的，再说那不是巧合吗？"
    show y 正常05 at ct with dissolve
    y "那你就自己去找她好了。"
    show y 正常06 at ct with dissolve
    y "反正我是不想去的。"
    w "你疯了吗？我可是只猫啊！"
    show y 正常04 at ct with dissolve
    y "你也知道你是只猫啊！"
    w "不是，我是一只神圣的猫啊！"
    show y 正常05 at ct with dissolve
    y "那你就去找她啊！"
    w "不去。"
    show y 正常04 at ct with dissolve
    y "那不就是了，那我们不去找她吧。"
    w "你说的对，就这么愉快的决定了。"
    narrator "袁艳伸出了爪子，我伸出了自己的手。"
    narrator "友好得不分你我的握了起来。"
    narrator "一人一猫有史以来第一次达成共识。"
    narrator "我们彼此相望，仿佛已是多年的挚友，彼此露出认同这项决定的眼神。"
    w "可是…如果你要找的女孩子是她呢？"
    narrator "听到我的话，袁艳愣了愣。"
    narrator "犹豫了好一会儿才终于弱弱地说着。"
    show y 恼火06 at ct with dissolve
    y "……"
    show y 恼火04 at ct with dissolve
    y "要不给她打个电话好了。"
    w "打谁？"
    show y 恼火02 at ct with dissolve
    y "打个电话啊！"
    show y 恼火01 at ct with dissolve
    y "就是远距离通信。"
    w "那是什么？"
    show y 恼火06 at ct with dissolve
    y "就是可以实现远距离联系的魔法。"
    w "魔…魔法？？"
    show y 恼火04 at ct with dissolve
    y "……"
    narrator "于是我就看着袁艳从口袋里头拿出了一块白色的盒子放在耳朵上。"
    w "？？？"
    show y 正常02 at ct with dissolve
    y "幸好昨天留了她的电话号码，说心里话我真的一点都不想见…"
    show y 正常01 d at ct with dissolve
    y "喂？"
    #"此处暗影表示打电话"
    show y 正常01 d with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show x 嘲笑02 at rt with dissolve
    x "有很好玩的事情吗？"
    show y 嘲讽05 at lt with dissolve
    y "额，有。"
    show x 嘲笑01 at rt with dissolve
    x "什么时候？在哪里？"
    show y 嘲讽04 at lt with dissolve
    y "今晚六点，在我家，同样是那个房间。"
    show x 反驳01 at rt with dissolve
    x "嗯，现在就去。"
    show y 嘲笑 at lt with dissolve
    y "驳回，如果你现在来我会取消你参与这件事的资格。"
    show x 反驳02 at rt with dissolve
    x "你觉得这对我有用吗？"
    show y 嘲讽01 at lt with dissolve
    y "没用。"
    show y 嘲讽02 at lt with dissolve
    y "但是会让事情变得一点意思都没有的话呢。"
    show x 反驳03 at rt with dissolve
    x "……"
    show x 反驳01 at rt with dissolve
    x "好，我知道了。"
    hide x with dissolve
    narrator "似乎是说完了。"
    narrator "袁艳收起了盒子，松了一口气。"
    w "刚刚你跟她说话了？"
    show y 正常01 at ct with dissolve
    y "嗯，是啊。"
    w "这么神奇？"
    show y 正常02 at ct with dissolve
    y "就是这么神奇。"
    w "……"
    w "不过你为什么今天会一个一个把她们聚起来呢？"
    show y 正常03 at ct with dissolve
    y "当然是有我的理由啊，先回去吧。"
    w "喵！"

    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    
    
    unknown_c "……"
    
    scene street_白天 with dissolve:
        zoom .667
    
    narrator "我感觉到了有一股极为熟悉的气息在附近。"
    
    w "袁艳…"
    w "夏静好像在这附近，而且还发现我们了。"
    show y 无措 at ct with dissolve
    y "噗？？？什么？"
    show y 嘲笑 at ct with dissolve
    y "我就知道…"
    show y 嘲讽05 at ct with dissolve
    y "咳咳，你冷静！冷静！保持冷静！！！不要慌！"
    w "……"
    narrator "最先要冷静的人是你才对吧。"
    w "要怎么做？"
    show y 嘲讽02 at ct with dissolve
    y "首先要装作什么也没发生，然后...."
    w "然后？"
    show y 嘲讽03 at ct with dissolve
    y "然后面带微笑…对对对，就是这样，自然地回去。（滑稽的笑容）"
    hide y
    narrator "我舔了舔爪子，看着袁艳有些蹩脚的演技，实在是不知道该怎么去提醒她。"
    narrator "回过头时，却和夏静对上了眸子。"
    w "……"
    show x 嘲笑01 at ct with dissolve
    x "……"
    narrator "她看着我。"
    narrator "我也要看着她。"
    show x 嘲笑02 at ct with dissolve
    x "~~~"
    narrator "不知为何，她却突然笑了，让人有点头皮发麻的那种。"
    narrator "难道是发现了什么吗？"
    w "喵~"
    narrator "叫了一声，然后跟上了已经快走远的袁艳的身影。"

    #【场景：房间】
    scene room_白天 with dissolve:
        zoom .667
    
    show y 正常02 at ct with dissolve
    y "啊，累死我了。"
    narrator "袁艳毫无顾忌地倒在了沙发上，一副生无可恋的模样。"
    narrator "我踩着优雅的步子，站在了沙发的边缘一侧。"
    narrator "注视着她。"
    narrator "她则是盯着天花板愣神。"
    narrator "一愣就是十来分钟。"
    narrator "我则是实在是忍不住开口询问起了她。"
    w "上午才过去一半，距离晚上还有这么长的时间你没有什么打算吗？"
    show y 正常03 at ct with dissolve
    y "噢…"
    show y 正常02 at ct with dissolve
    y "打算啊…"
    narrator "袁艳似乎还有些愣神，完全没反应过来。"
    w "喵！"
    narrator "我一下窜到了她的肚子上，打算打滚的时候她轻轻地抱住我。"
    narrator "她略带无神的眼睛柔和地盯着我。"
    narrator "双手就从我脑袋起摸了下去。"
    narrator "喂喂，你摸哪里呢！！！"
    narrator "好像还挺舒服。"
    show y 正常01 at ct with dissolve
    y "是啊，接下来该怎么办呢。"
    show y 正常01 at ct with dissolve
    y "…"
    w "……"
    show y 开心 at ct with dissolve
    y "别想太多了，先吃点东西，看看电视吧。"
    narrator "她眯着眼睛笑着，想把事情丢在一旁。"
    w "……"
    narrator "她缓缓地起身，把我丢到一旁，从冰箱里头拿出了一些零食。"
    narrator "又回到了沙发边上。"
    show y 笑容01 at ct with dissolve
    y "来，来。吃东西吃东西，你的猫薄荷也给你准备了！"
    w "哇！！！"
    narrator "我一跃而起抱住了她丢过来的猫薄荷。"
    narrator "袁艳笑着打开了电视，吃起了零食。"
    narrator "房间里头电视机的声音哗啦啦的响着，我是不知道在干啥，只是感觉这个时候的袁艳哪里有些不一样了。"
    narrator "我舔着猫薄荷，一面舒服得打滚，一面观察着她。"
    narrator "她好像有点心不在焉，眼神完全没有放在电视上面。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "emmmmm…"
    show y 正常05 at ct with dissolve
    y "喂，别吃了。"
    w "喵！好痛！你踢我干什么？？？"
    narrator "突然之间，袁艳像是搞懂了什么一样，照着我屁股就是一脚。"
    show y 正常01 at ct with dissolve
    y "赶紧送我去观察她们，死一次就死一次吧。"
    w "……"
    w "可是你也犯不着给我来一脚吧。"
    show y 正常02 at ct with dissolve
    y "少废话，你以为猫薄荷是白给你吃的啊。"
    w "喵？你还收利息的啊！！！"
    show y 正常01 at ct with dissolve
    y "快点给我办事啊你！"
    w "知道了知道了！"
    w "那你这一次要先观察谁？"
    show y 正常05 at ct with dissolve
    y "这还用说吗？"
    show y 正常04 at ct with dissolve
    y "当然是——"

    menu:
        "林琴":
            jump c1_c2_l
        
        "夏静":
            jump c1_c2_x
        
        "程祎琳":
            jump c1_c2_c

            
label c1_c2_l:
    $_dismiss_pause = False

    $c1_c2_l_select = True
    
    scene room_白天:
        zoom .677

    show y 正常04 at ct with dissolve
    y "当然是林琴啊。"
    w "我就知道会是她。"
    show y 正常05 at ct with dissolve
    y "你又是怎么知道的啊。"
    w "毕竟我是神圣的猫啊！"
    show y 正常06 at ct with dissolve
    y "好了好了，废话就别说了，你废话总是那么多。"
    w "…"
    narrator "我翻了翻眼皮。"
    narrator "废话多的也不知道是谁。"
    w "可能会有点疼，你忍着点。"
    show y 正常02 at ct with dissolve
    y "呸。"
    w "……"
    narrator "我当作没听到。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    
    narrator "没有多想，直接使用了力量。"
    narrator "只见她袁艳栽倒在沙发上，一动不动得像是一具死尸。"
    w "这死丫头要是不说话还像个人。"
    narrator "走到没有舔完的猫薄荷面前，静静地享受了一段只属于自己的猫薄荷时间。"
    narrator "然后闭上眼睛跟随着袁艳所在的地方而去。"
    
    scene bf_白天 with dissolve:
        zoom .667

    show y 正常02 at ct with dissolve
    y "……"
    w "你…你愣在这里干什么啊？"
    show y 正常03 at ct with dissolve
    y "emmmmm"
    w "怎么了啊？"
    narrator "袁艳皱着眉头，就是不肯说话。"
    narrator "我顺着她的目光看去。"
    show y 正常03 at ct with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show l 普通02 at rt with dissolve
    l "……"
    narrator "那个原本是我们观察对象的女孩子，就一直在那儿发呆。"
    narrator "当然，周围遍地狼藉，{w}\n具体发生了什么不用拿头想也知道。"
    w "…"
    w "从什么时候开始的这家伙发呆？"
    show y 正常01 at lt with dissolve
    y "不知道。"
    show y 正常03 at lt with dissolve
    y "反正我来到在这里她就一直在发呆。"
    w "这叫我们怎么观察啊？"
    show y 正常01 at lt with dissolve
    y "我也这么想，估计她会发呆到晚上。"
    show y 正常02 at lt with dissolve
    y "那要不我们就回去吧，别在这里浪费时间。"
    w "赞成。"
    hide y 正常02 with dissolve
    w "……"
    narrator "总觉得有点不太对。"
    narrator "我举起了爪子，阻止了袁艳准备离开病房的动作。"
    w "等一下等一下，噢不——少女请留步！"
    show y 笑容01 at lt with dissolve
    y "噢，神圣的猫咪喲，还有什么事情吗？"
    w "这句话我很喜欢，没错我就是神圣的，哈哈哈。"
    show y 嘲讽02 at lt with dissolve
    y "也就是回去的时候你还有点用，稍微奉承一下你而已。"
    w "啊，你刚刚说什么？"
    show y 开心 at lt with dissolve
    y "我说你非常伟大。"
    w "那肯定，我一直都很伟大啊！！哈哈哈哈…"
    narrator "我挠着脑袋，哈哈地笑了起来。"
    narrator "刚刚我要说什么来着…"
    w "……"
    w "不对！我们到底是来干什么的啊！？"
    show y 笑容02 at lt with dissolve
    y "来观察对象的啊。"
    w "噢，是啊…"
    w "……"
    w "你还知道是来观察对象的啊？？？？"
    show y 正常04 at lt with dissolve
    y "是啊，还有几天来着？七天还是六天？"
    w "你够了！！"
    w "都被诅咒了你就不能有点紧迫感吗？"
    show y 正常05 at lt with dissolve
    y "我很有紧迫感的好不好？"
    w "你这跟出来玩一样的态度很难让人相信啊。"
    w "你是真不知道诅咒到底有多么可怕啊？？"
    show y 正常04 at lt with dissolve
    y "额，反正可不可怕它都在那里，该吃吃，该睡睡。"
    y "还能怎么样？"
    show y 正常05 at lt with dissolve
    y "我已经在努力了，还要做出拼命的模样吗？"
    w "额…"
    w "额…"
    show y 正常01 at lt with dissolve
    y "还有你看看这女人，一副快死了模样还有什么好观察的，赶紧观察下一个对象去。"
    w "可是你这才来多久啊，就要回去。"
    w "你当我的力量不值钱的啊。"
    hide y
    narrator "……"
    narrator "尽管是这么说着，最后还是拗不过袁艳这个丫头，还是被她忽悠回来了。"
    
    jump c1_3


label c1_c2_c:
    $_dismiss_pause = False

    $c1_c2_c_select = True
    
    scene room_白天:
        zoom .667

    show y 正常02 at ct with dissolve
    y "当然是程祎琳啊。"
    w "我就知道会是她。"
    show y 正常01 at ct with dissolve
    y "你又是怎么知道的啊。"
    w "毕竟我是神圣的猫啊！"
    show y 正常03 at ct with dissolve
    y "好了好了，废话就别说了，你废话总是那么多。"
    w "…"
    narrator "我翻了翻眼皮。"
    narrator "废话多的也不知道是谁。"
    w "可能会有点疼，你忍着点。"
    show y 正常05 at ct with dissolve
    y "呸。"
    w "……"
    narrator "我当作没听到。"

    narrator "没有多想，直接使用了力量。"
    narrator "只见她袁艳栽倒在沙发上，一动不动地像是一具死尸。"
    w "这死丫头要是不说话还像个人。"
    narrator "走到没有舔完的猫薄荷面前，静静地享受了一段只属于自己的猫薄荷时间。"
    narrator "然后闭上眼睛跟随着袁艳所在的地方而去。"
    
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    #【场景：街道】
    scene street_白天 with dissolve:
        zoom .667
    
    
    w "噗，你在干什么呢？"
    narrator "我叫住正在摇摇晃晃走路的袁艳。"
    show y 正常05 at ct with dissolve
    y "当然是模仿啊！"
    w "模仿谁？"
    show y 正常04 at ct with dissolve
    y "喏！"
    narrator "袁艳朝着远处街道上一个挽着背包摇摇晃晃朝前面走着的少女指了过去。"
    narrator "这个少女似乎已经成了整个街道最吸引人注意得女孩。"
    w "……"
    w "你怕不是疯了哦。"
    w "她发疯你也跟着发什么疯？"
    show y 正常02 at ct with dissolve
    y "不是有个名人说过吗？"
    show y 正常03 at ct with dissolve
    y "模仿是最好的老师，我想试着模仿她然后感受一下她的感觉。"
    w "……"
    w "那你有什么感觉？"
    show y 正常03 at ct with dissolve
    y "感觉自己像个傻子，还好没人看到。"
    w "……"
    w "确实是没人看得到。"
    narrator "袁艳看着我，眼神有点奇怪。"
    w "…"
    w "我总觉得我被侮辱了。"
    show y 正常01 at ct with dissolve
    y "我也觉得心情很复杂，各种意义上。"
    w "在补充一下，我是神圣的猫。"
    narrator "我们两个人的对话完全不在一根弦上。"
    narrator "就这么跟着夏静摇摇晃晃地一直走，然后有一句没一句话的搭着话。"
    narrator "时不时相互怼一下。"
    w "……"
    w "这不是在观察，这是在消磨时间啊喂！"
    narrator "我突然反应过来，大声吼道。"
    show y 正常02 at ct with dissolve
    y "你声音小点，我要是被你刮聋了你赔得起吗？"
    w "不是不是啊！"
    show y 正常04 at ct with dissolve
    y "怎么了？"
    w "我们不是被诅咒了吗？"
    show y 正常05 at ct with dissolve
    y "好像是有这么一回事，所以怎么了吗？"
    w "……"
    w "你还问怎么了……"
    w "我们被诅咒了啊，时间这么少…"
    show y 正常04 at ct with dissolve
    y "不是还有六七天吗？"
    narrator "这丫头的心是怎么长的啊，能找个机会挖出来看一看么。"
    narrator "我心里浮现出这么个想法。"
    show y 正常02 at ct with dissolve
    y "干嘛，用这种眼神看我，今晚你是想喝炖猫汤吗？"
    w "不是，你好歹有点紧迫感啊，怎么觉得你是出来散步的？"
    show y 正常01 at ct with dissolve
    y "emmmmm，你说的有道理。"
    w "是把。"
    narrator "总算是说服她了。"
    show y 开心 at ct with dissolve
    y "那就回去吧。"
    narrator "袁艳冲着我笑了笑。"
    w "……"
    w "哈？我没听错吧？"
    show y 笑容01 at ct with dissolve
    y "对啊，回去啊！"
    w "你这才出来多久啊？"
    w "你不观察对象了吗？"
    show y 笑容02 at ct with dissolve
    y "你看看那个傻子一样不知道在干嘛的家伙，还有什么好观察的。"
    w "……"
    narrator "袁艳叫嚷着，似乎已经没有什么想法了。"
    show y 正常05 at ct with dissolve
    y "而且，她就在我们家周围瞎溜达你没发现么？"
    w "咦，好像还真的是。"
    show y 正常02 at ct with dissolve
    y "走吧，我们回去。"
    show y 正常01 at ct with dissolve
    y "趁还有时间去观察一下另外两个对象，别再这里浪费时间。"
    narrator "在看向袁艳时，她微微的笑着。"
    narrator "然而我却愣住了。"
    narrator "我已经完全猜不透这个明明只是个人类的小丫头了。"
    narrator "但是，我却没有之前那么担心了。"
    narrator "这家伙还是有好好考虑过自己的处境的嘛。"
    w "那就回去吧，稍微有点疼，你忍着点。"
    show y 愤怒 at ct with dissolve
    y "……"
    show y 愤怒 at ct with dissolve
    y "我去你这只死猫，今天我非要把你煮了不可。"
    narrator "……"
    hide y with dissolve
    narrator "送走了袁艳。"
    narrator "我伫立在街道上，看着远处的身影。"
    narrator "久久才叹了一口气。"
    
    jump c1_3


label c1_c2_x:
    $_dismiss_pause = False

    $c1_c2_x_select = True
    
    scene room_白天:
        zoom .667
    
    show y 正常02 at ct with dissolve
    y "当然是夏静啊！"
    w "……"
    w "我去？为什么会是她？"
    show y 正常01 at ct with dissolve
    y "你干嘛那么吃惊？"
    w "我以为你…"
    show y 正常03 at ct with dissolve
    y "你以为什么，我最先选她就是为了长痛不如短痛啊。"
    w "好吧好吧。"
    w "谁叫我是如此神圣的猫呢？就当舍命陪丫头了吧。"
    show y 正常01 at ct with dissolve
    y "喂，你只是只猫啊，你那么怕干什么。"
    w "…"
    narrator "我翻了翻眼皮。"
    w "可能会有点疼，你忍着点。"
    show y 正常04 at ct with dissolve
    y "呸。"
    w "……"
    narrator "我当作没听到。"
    narrator "没有多想，直接使用了力量。"
    narrator "只见她袁艳栽倒在沙发上，一动不动地像是一具死尸。"
    w "这死丫头要是不说话还像个人。"
    narrator "走到没有舔完的猫薄荷面前，静静地享受了一段只属于自己的猫薄荷时间。"
    narrator "然后闭上眼睛跟随着袁艳所在的地方而去。"

    #【街道】
    scene street_白天 with dissolve:
        zoom .667
    
    w "喂，你在干嘛？"
    show y 恼火05 at ct with dissolve
    y "…"
    w "喂，你听到我说话没？"
    show y 恼火02 at ct with dissolve
    y "闭…闭嘴啊你。"
    narrator "袁艳的语气有些莫名其妙的感觉。"
    narrator "我顺着她的目光看了过去。"
    narrator "那个叫做夏静的女孩子十分正常地在路上走着。"
    narrator "只是这么看的话，一点异常也没有。"
    narrator "但是，在她的前面，有着另外一个女孩{w}——程祎琳。"
    narrator "那个女孩正摇摇摆摆地在道路上走动着，非常的惹人注目。"
    narrator "而夏静则是隐藏在人群之中，不仔细看的话似乎会觉得她也是看热闹的那一类人。"
    narrator "但是只有我们明白。"
    narrator "这个女孩很古怪。"
    narrator "如果说之前的跟踪是巧合的话，那么这一次就有点说不过去了。"
    narrator "她在跟踪程祎琳。"
    narrator "我和袁艳对视一眼，似乎确认了彼此眼中的想法。"
    show y 正常04 at ct with dissolve
    y "这家伙果然是在跟踪她啊。"
    w "……"
    show y 正常05 at ct with dissolve
    y "这是一个很不错但是有点令人觉得恶心的情报。"
    w "你不喜欢被人跟踪吗？"
    show y 
    y "是有一些。"
    w "那要不我们就回去吧，反正情报已经入手了。"
    show y 正常04 at ct with dissolve
    y "这才刚来多久啊？"
    show y 正常06 at ct with dissolve
    y "你忘了我们被诅咒了吗？"
    w "只要你没忘我就不会忘的。"
    w "只是觉得这对你来说太沉重了。"
    w "你不是说了吗？该吃的时候吃，该睡的时候睡吗？"
    show y 正常05 at ct with dissolve
    y "我确实说过。"
    w "那还有些时间就过得轻松一点呗。"
    w "喵~"
    show y 正常02 at ct with dissolve
    y "哈…你怎么突然变得这么老实了？"
    w "喂，我好歹也是有自己的考量的好不好。"
    show y 正常01 at ct with dissolve
    y "不是很懂，不过我也确实想回去了。"
    show y 正常03 at ct with dissolve
    y "待在这里也没有什么意义了。"
    w "那就回去吧。"
    w "嗯。"
    narrator "罕见的，我们再一次达成了共识。"
    w "稍微有点疼，你忍着点。"
    show y 愤怒 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "疼就疼吧。"
    hide y with dissolve
    narrator "送走了袁艳。"
    narrator "我伫立在街道上，看着逐渐远去的身影。"
    narrator "长长地叹了一口气。"
    
    jump c1_3

label c1_3:
    $_dismiss_pause = False
    
    #【场景：房客厅】
    scene kt_夜晚:
        zoom .667
    
    show y 正常02 at ct with dissolve
    y "……"
    w "……"
    narrator "夜晚什么时候降临的我们已经记不清了，回过神的时候。"
    narrator "今天邀约的人已经全部如期赴约了。"
    narrator "然而我是有点懵的，看袁艳的表情我猜她估计也差不了多少。"
    narrator "因为她们到来的时候我们还在边吵架边吃饭。"
    narrator "不过还好我机灵，她们突然出现在客厅的时候我及时改口‘喵喵喵’才没有被发现。"
    narrator "只是这么看起来就好像袁艳在逗猫的场景，让我觉得无法接受。"
    show y 正常05 at ct with dissolve
    y "你这只死猫，出门回来的时候不知道关门吗？"
    w "…"
    w "喵？？？？"
    show y 正常05 at ct with dissolve:
        linear .3 xpos -0.08 xanchor 0.0
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "…"
    show x 考虑01 with dissolve:
        xpos .75 xanchor .75
    x "…"
    show c 侧视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……"
    narrator "对一只猫怒吼，指责他不会关门的事情，摆明了另有所指啊。 "
    narrator "但是…只有我知道这丫头是真的说我没关门的事情。"
    show y 愤怒 with dissolve:
        xpos -0.08 xanchor 0.0
    y "喵什么喵？你哑巴了吗？说话啊？"
    w "喵？？"
    narrator "虽然很想说话，但是被那三个女孩盯着，我怎么也说不出口。"
    narrator "感觉说出口就会出大事，索性就只‘喵喵喵’的叫得了。"
    narrator "袁艳似乎还打算继续无视那三个女孩。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "……"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "咳咳，该说正事了吧，请不要浪费时间。"
    narrator "林琴打算打破这个局面。"
    narrator "袁艳歪着脑袋看了看。"
    show y 正常04 at ct with dissolve:
        xpos -0.08 xanchor 0.0
    y "你不觉得你们这么出现在我家里很没礼貌吗？"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "……"
    show x 嘲笑02 with dissolve:
        xpos .75 xanchor .75
    x "那么我们重来一次好了。"
    narrator "夏静突然对着正准备发作的袁艳笑着说道，轻松化解了这一尴尬的局面。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……"
    show y 正常06 with dissolve:
        xpos -0.08 xanchor 0.0
    y "就这么办。"
    show x 嘲笑01 with dissolve:
        xpos .75 xanchor .75
    x "呵呵."
    hide x with dissolve
    narrator "似乎是觉得解决这个困境非常简单，起身离开了客厅，并到大门外去了。"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "失礼了，是我太心急了。"
    hide l with dissolve
    narrator "林琴微微欠了欠身，然后跟着夏静离开了。"
    show c 侧视02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……"
    show c 斜视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "重来有零食吃吗？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "不重来就一定没有。"
    show c 斜视02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "嗯嗯，我知道了。"
    hide c with dissolve
    narrator "程祎琳仿佛是得到了什么指示一样，屁颠屁颠地跑了出去。"
    w "……"
    w "蛮厉害的嘛，居然能掌握主场。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 嘲讽05 at ct with dissolve
    y "饶了我吧，我完全没想到要说什么啊。"
    narrator "只见袁艳身子一拉耸下来，刚刚的气势瞬间瘪了。"
    w "我去，刚刚还觉得你很厉害来着。"
    w "喂喂，她们都敲门了，你有点出息啊喂！"
    show y 嘲笑 at ct with dissolve
    y "你别在那里叫行不行，你行你上啊！"
    w "……"
    show y 嘲笑 at ct with dissolve
    y "明明就知道喵喵叫。"
    w "因为种种原因我是不能说话的。"
    show y 嘲笑 at ct with dissolve
    y "让她们知道你的存在会怎么样吗？"
    w "…"
    w "我咋知道。"
    w "大概会被杀掉吧。"
    show y 正常01 at ct with dissolve
    y "被她们知道你会说人话就会让事情变得更麻烦吗？"
    w "会相当麻烦。"
    show y 正常02 at ct with dissolve
    y "那就算了。"
    show y 正常03 at ct with dissolve
    y "扯上你们就已经够麻烦了。"
    narrator "袁艳叹了一口气，双手插在兜里，去客厅开门了。"

    show y 正常03 at ct with dissolve:
        linear .3 xpos -0.08 xanchor 0.0
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "……"
    show x 假笑02 with dissolve:
        xpos .75 xanchor .75
    x "……"
    show c 注视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "喔，吃零食咯！"
    show y 开心 with dissolve:
        xpos -0.08 xanchor 0.0
    y "总之欢迎你们再一次来到这里，能接待你们几位我很荣幸。"
    narrator "袁艳笑着，仿佛之前发生的事情从来没有发生过一样。"
    show y 笑容01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "那我就开门见山地说了。"
    show y 笑容02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "跟上次不一样的事情是。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "……"
    show y 开心 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我希望跟你们进行一场交易。"
    show l 注视08 with dissolve:
        xpos .25 xanchor .25
    l "交易这个东西，是指双方拿出彼此认为价值相等的东西进行交换才对吧。"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "是这样没错。"
    show l 注视09 at lt with dissolve:
        xpos .25 xanchor .25
    l "那么你的条件是什么？"
    show l 注视07 at lt with dissolve:
        xpos .25 xanchor .25
    l "从我明白你那边有我想要的事物起，你就没有提及过你想要的东西。"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "嗯，所以呢？"
    show l 注视07 at lt with dissolve:
        xpos .25 xanchor .25
    l "我只能认为你别有所图。"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你说我有你想要的，那个东西能在你那边价值多少呢？"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "…"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "和我的生命等值。"
    show y 无措 with vpunch:
        xpos -0.08 xanchor 0.0
    y "！！！"
    narrator "袁艳有些吃惊。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "怎么了吗？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "额，没什么。"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "那正好。"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "交易是等值的呢。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "你的意思是？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你忘了吗？之前我说过希望你能救我的命吧。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "……"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "抱歉，我有点听不懂你说的话。"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "没事，你不用弄懂这个有点复杂的问题。"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "因为我自己都不怎么懂。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "那我该怎么做？"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "很简单，就是需要你谈恋爱而已，其余的交给我。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "这个话你有说过。"
    narrator "我伫立在桌子上，看着她们飞速地交换着自己的意见。"
    narrator "果然还是人类比较厉害啊。"
    narrator "而另外两个人则是非常安静地等待两个人交涉完。"
    narrator "我舔了舔嘴唇。"
    narrator "心里只剩了感叹。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "如果我谈恋爱你就能活下来吗？"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "这个我也说不准。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "怎么说？"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "设定有点复杂，我打个比方：你们三个只有一个人是可以救我的人 "
    narrator "袁艳看着三个人，顿了顿说道。"
    narrator "三个人你望望我我看看你表示有些不太理解。"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "但是我并不知道你们谁是那个可以救我的人。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "剩下来的那几天，我会观察你们究竟谁是符合我要求的那个人。"
    show y 正常06 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我会在几天后做出决定。"
    show x 注视01 with dissolve:
        xpos .75 xanchor .75
    x "决定之后你会怎么做呢？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我会实现那个人的愿望。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "如果错了的话呢？"
    show y 开心 with dissolve:
        xpos -0.08 xanchor 0.0
    y "那么麻烦你们替我买口棺材收尸。"
    show c 注视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……"
    show l 惊异03 with dissolve:
        xpos .25 xanchor .25
    l "你到底是什么人？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "这个问题对你来说很重要吗？"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "…"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "你是谁跟我没关系。"
    show y 笑容01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "对，你只需要谈恋爱，那件事我就有可能会替你实现。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "只需要做这些？"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "嗯，而且最多几天而已，如果我死了的话大概就随你们怎么办了。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "你有什么证据？"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "相反我不死的话，愿望就都可能实现也说不定。"
    show x 注视02 with dissolve:
        xpos .75 xanchor .75
    x "等一下，你说你可以实现我们的愿望？"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "是的。"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "不过是你们其中一个。"
    show x 反驳02 with dissolve:
        xpos .75 xanchor .75
    x "那你知道我们的愿望是什么吗？"
    narrator "程祎琳突然抬起头来看着袁艳，似乎等待着她的回答。"
    narrator "林琴也停止了追问，似乎跟程祎琳一样也想要知道这个答案。"
    narrator "果然这个叫做夏静的女孩子有点厉害。"
    narrator "我看着夏静心里想到。"
    narrator "就算前面聊得再怎么火热朝天，她也会直指问题的关键，然后旁敲侧击得出情报。"
    narrator "就看袁艳怎么应对了，接下来的回答可能会直接让讨论结束。"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……"
    show y 正常03 with dissolve:
        xpos -0.08 xanchor 0.0
    y "不知道。"
    w "……"
    narrator "我去，就这个回答，你要死啊！"
    narrator "我差点没跳起来一爪子跟这女人拼了。"
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "你什么意思？"
    show y 开心 with dissolve:
        xpos -0.08 xanchor 0.0
    y "就是这个意思。"
    show l 不满08 with dissolve:
        xpos .25 xanchor .25
    l "你是想死吗？"
    narrator "林琴看起来非常的愤怒。"
    narrator "而在一旁的程祎琳则是有些失望的表情，收拾一下似乎有点想走。"
    narrator "只有夏静什么也没说。"
    narrator "场面非常的寂静。"
    show x 反驳01 with dissolve:
        xpos .75 xanchor .75
    x "你应该还有话没说吧。"
    narrator "率先打破寂静的是夏静。"
    narrator "袁艳愣了愣。"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我真是跟你这样的聪明人合不来呢。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "是，我还有话要说。"
    narrator "袁艳站起身来，走到冰箱面前从里面拿了几盒牛奶然后扔给了三个人。"
    narrator "还倒了一盒牛奶给我后拿着自己那份重新做回了位置上。"
    narrator "三个女孩都没有说话。"
    narrator "只有程祎琳一点也不客气地接过牛奶说了声谢谢。"
    show y 开心 with dissolve:
        xpos -0.08 xanchor 0.0
    y "口有点渴了，不好意思。"
    show y 笑容02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我们继续。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "说到你们的愿望，我怎么可能知道？ "
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我们才认识多久啊？"
    show x 闭眼 with dissolve:
        xpos .75 xanchor .75
    x "……"
    show y 正常06 with dissolve:
        xpos -0.08 xanchor 0.0
    y "但是我也有知道的事情。"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "就是你们三个人都在找人吧。"
    narrator "……"
    show c 张嘴01 with vpunch:
        xpos 1.25 xanchor 1.25
    narrator "‘铛’的一声程祎琳的牛奶盒子掉在了地上。"
    show l 惊异03 with vpunch:
        xpos .25 xanchor .25
    l "！"
    show x 惊异 with vpunch:
        xpos .75 xanchor .75
    x "！"
    narrator "三个人带着十分震惊且古怪地眼神看向了袁艳。"
    narrator "接下来客厅就是一片死寂。"
    w "……"
    narrator "只有我有些无语，这不是我之前跟她说过的情报吗？"
    narrator "明明她之前还嫌弃这点情报太少了。"
    show l 慌张07 with dissolve:
        xpos .25 xanchor .25
    l "没有别的事情的话，我先走了。"
    show c 张嘴02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "我…我也是。"
    hide l with dissolve
    hide c with dissolve
    narrator "两个人起了身，似乎有点慌张。"
    narrator "袁艳则是额头有汗渗了出来。"
    narrator "咦？失败了？刚刚效果不是很好的吗？她们看上去很震惊的样子啊。"
    narrator "不应该啊，不应该啊。"
    narrator "大概是走到门边的时候，林琴突然又回来了。"
    show l 慌张08 with dissolve:
        xpos .25 xanchor .25
    l "这个手机里头有我唯一的联系方式。"
    show l 慌张09 with dissolve:
        xpos .25 xanchor .25
    l "如果…我是说如果…如果那个可以拯救你的人是我的话，请用这个联系我！"
    show l 慌张07 with dissolve:
        xpos .25 xanchor .25
    l "恋爱这边，我会努力的，请你放心。"
    narrator "林琴十分认真地递给了袁艳一部看起来就十分昂贵的精密手机。"
    show c 张嘴01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "我…我会经常来你这里的！！！"
    narrator "程祎琳也跟着回来，还有些拘谨地朝着袁艳一鞠躬二鞠躬三鞠躬。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……"
    w "……"
    show y 嘲笑 with dissolve:
        xpos -0.08 xanchor 0.0
    y "是…是吗？那就好。"
    narrator "袁艳有些松了一口气接过林琴手上的手机。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "真的是不好意思了，如果没别的事情的话，我先走了。"
    hide l with dissolve
    show c 侧视02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "噢，我…我也是。"
    hide c with dissolve
    narrator "看着两个人离去的背影，袁艳皱了皱眉头。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "等一下。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "还有什么事吗？"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "没…"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "好的，那我先走了。"
    hide l with dissolve
    pause 0.7
    show l 普通08:
        xpos .25 xanchor .25
    l "…"
    narrator "走两步，林琴又回过头来。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "恋爱那边我会努力的。"
    narrator "她很认真地说道。"
    show c 斜视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "我…我也是我也是。"
    narrator "她也很认真的说道。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "那…那就拜托你们了。"
    hide l with dissolve
    hide c with dissolve
    narrator "然后两个人就彻底从这个客厅消失了。"
    narrator "但是看到这一系列的对话我只想说：{w}\n我呸，你们以为这是在拉皮条吗？"
    show x 惊讶01 at rt with dissolve
    x "我呸，你们以为这是在拉皮条吗？"
    w "喵喵喵？"
    narrator "咦咦？？？"
    show y 嘲笑 at lt with dissolve
    y "额…其实我也觉得有点不对劲。"
    show x 惊讶01 at rt with dissolve
    x "你们之间不会产生了什么奇怪的化学反应吧。"
    show y 正常05 at lt with dissolve
    y "……"
    show y 嘲讽03 at lt with dissolve
    y "你瞎说什么呢，在怎么说我也只可能喜欢男人啊。"
    narrator "夏静摇了摇头。"
    show x 惊讶02 at rt with dissolve
    x "完全看不出来。"
    show y 嘲讽04 at lt with dissolve
    y "要是我喜欢女孩子那你岂不是很危险？"
    show x 惊讶01 at rt with dissolve
    x "……"
    show x 考虑01 at rt with dissolve
    narrator "夏静看了看袁艳。"
    narrator "从上往下打量了一遍。"
    show y 正常04 at lt with dissolve
    y "……"
    show x 考虑02 at rt with dissolve
    narrator "然后夏静从下又往上打量了她一遍，接着来回巡视，最终目光定在某一个位置停了下来。"
    show y 正常05 at lt with dissolve
    y "喂…你想干嘛。"
    narrator "看得出来，袁艳被看得心里发毛。"
    narrator "其实我心里都有点发毛。"
    show x 假笑01 at rt with dissolve
    x "嗯…"
    show y 正常04 at lt with dissolve
    y "……"
    show x 假笑02 at rt with dissolve
    x "如果是你的话，我应该没有问题。"
    show y 无措 at lt with dissolve
    y "嘶…"
    narrator "听得出来，袁艳她很明显地倒吸了一口凉气。"
    narrator "夏静缓缓地露出了笑容。"
    narrator "笑得房间里头的空气都降低了好几度。"
    show y 嘲讽04 at lt with dissolve
    y "咱们还是…还是谈正事吧，嘿嘿嘿。"
    show x 注视01 at rt with dissolve
    x "正事？"
    show y 笑容01 at lt with dissolve
    y "就是…就是关于你愿望的事情啊。"
    show x 注视02 at rt with dissolve
    x "噢，原来还有这回事啊！"
    show y 无措 at lt with dissolve
    y "你别给忘了啊！！！"
    show x 无奈01 at rt with dissolve
    x "开玩笑的，说到我的愿望啊……"
    narrator "夏静又开始打量起了袁艳。"
    show y 正常05 at lt with dissolve
    y "……"
    show y 正常04 at lt with dissolve
    y "emmmmm"
    show y 无措 at lt with dissolve
    y "我怎么觉得现在我的危险比较大。"
    show x 怜悯02 at rt with dissolve
    x "我的愿望嘛…"
    show y 无措 at lt with dissolve
    y "喂，你别乱来啊，我跟你讲，你别乱来啊…"
    show x 怜悯01 at rt with dissolve
    x "是什么好呢？"
    show y 无措 at lt with dissolve
    y "我跟你说，你要是敢说我我就以死明志然后…"
    show x 怜悯02 at rt with dissolve
    x "能不能帮我回忆一段往事呢？"
    show y 嘲笑 at lt with dissolve
    y "然后…留得清白在人间…"
    show y 嘲讽01 at lt with dissolve
    y "额…"
    show y 嘲笑 at lt with dissolve
    y "你刚刚说什么可以再说一遍吗？我怀疑我听错了。"
    show x 嘲笑01 at rt with dissolve
    x "哈哈哈，你的反应真的是太搞笑了。"
    show x 嘲笑02 at rt with dissolve
    x "你是搞笑艺人来的吗？"
    show y 正常04 at lt with dissolve
    y "……"
    show y 正常05 at lt with dissolve
    y "也不想想这是谁的错？"
    w "……"
    narrator "笑声渐渐地在客厅响起，又渐渐消失。"
    show x 闭眼 at rt with dissolve
    x "我好像忘记了一件事情。"
    narrator "夏静微微地颔首。"
    show y 正常04 at lt with dissolve
    y "是非常非常重要的事情吗？"
    show x 注视02 at rt with dissolve
    x "嗯，是非常非常重要的事情"
    narrator "她取下了眼镜，无比悲哀和无奈的表情从她的脸上渐渐地浮现。"
    narrator "仿佛完全变了一个人一样。"
    show x 注视03 at rt with dissolve
    x "要是你真的可以实现愿望的话。"
    show x 注视02 at rt with dissolve
    x "就让我回忆起有关于我忘记的那件事情的所有回忆吧"
    show x 注视01 at rt with dissolve
    x "做得到的话我什么事情都答应你。"
    show x 注视02 at rt with dissolve
    x "不惜一切代价…"
    narrator "听到这里，我嘴巴张得老大。"
    narrator "这…这是什么展开？"
    show y 正常04 at lt with dissolve
    y "……"
    show y 正常05 at lt with dissolve
    y "你…搞错了什么吧。"
    narrator "但是袁艳的语气却变化了起来。"
    show y 正常03 at lt with dissolve
    y "我能实现的就只有那个可以救我命的那个女孩的愿望。"
    show x 反驳02 at rt with dissolve
    x "能救你命的女孩只有一个。"
    show x 反驳01 at rt with dissolve
    x "那为什么那个女孩不能是我？"
    show y 正常02 at lt with dissolve
    y "额。"
    show y 正常03 at lt with dissolve
    y "没法反驳。"
    w "……"
    narrator "我还以为她想说啥，结果刚开口又让人打回原型。"
    show x 无奈01 at rt with dissolve
    x "也就是这一场交易，我很希望同你做。"
    show y 正常05 at lt with dissolve
    y "…"
    show y 笑容01 at lt with dissolve
    y "你能这么觉得就太好了。"
    show y 开心 at lt with dissolve
    y "我…我也很高兴呢。"
    show x 注视02 at rt with dissolve
    x "但是…"
    show y 正常02 at lt with dissolve
    y "怎么了？"
    show x 怜悯02 at rt with dissolve
    x "我还想跟你做一场交易。"
    show y 正常05 at lt with dissolve
    y "哈？啥交易？"
    narrator "夏静这个时候却突然莫名其妙地笑了起来。"
    narrator "看着她的笑容，我有种不好的预感。"
    show x 怜悯01 at rt with dissolve
    x "通过这几次跟你对话，我觉得你真的是个非常有趣的人啊。"
    show y 正常04 at lt with dissolve
    y "……"
    narrator "袁艳瞬间愣住了，默默地双手环在胸口，咽了一口唾沫。"
    show y 正常05 at lt with dissolve
    y "所…所以呢？"
    show x 怜悯02 at rt with dissolve
    x "哈哈…"
    show x 怜悯01 at rt with dissolve
    x "所以想要多知道一些你的事情。"
    narrator "我嘴巴张得老大，这…这这这这是什么情况啊？？？"
    show y 无措 at lt with dissolve
    y "你…你你你你你不会真的喜欢女孩子吧？？？"
    show x 怜悯02 at rt with dissolve
    x "这可说不准啊…"
    show y 无措 at lt with dissolve
    y "不是吧…不可能，我不会答应你的！！！"
    narrator "袁艳义正言辞地说道。"
    show y 无措 at lt with dissolve
    y "哇…"
    show y 无措  with dissolve
    y "你做什么…"
    
    
    #【cg:低语者】(1)
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_eyz = True
    scene cg_耳语者 with Dissolve(2)
    
    pause 1.0
    
    narrator "夏静带着笑容突然靠近袁艳。"
    narrator "她的长发在半空中飘舞着。"
    narrator "在我的视角看起来袁艳好像被夏静亲了一样。"
    w "……"
    
    
    #【CG：低语者】（2）
    #scene black with Dissolve(.7)
    #window hide dissolve
    #$renpy.pause(3,hard=True)
    #$ persistent.cg_eyz = True
    #scene cg_耳语者 with Dissolve(2)
    
    #pause 1.0
    #
    narrator "但是实际上，真正的情况是夏静只是贴在袁艳耳边。"
    narrator "袁艳的脸红扑扑的，看上去非常的奇怪。"
    narrator "夏静微微张合着嘴唇，说了一些话之后。"
    narrator "袁艳脸上的红晕就如潮水般褪下，取而代之的是无比的惊讶。"
    
    #【CG:结束】
    scene kt_夜晚 with dissolve:
        zoom .667

    show y 嘲讽04 at lt  with dissolve
    y "咳咳，你说的是真的吗？"
    show x 假笑01 at rt with dissolve
    x "你说呢？"
    narrator "夏静带着笑容看着袁艳。"
    w "喵？"
    show x 假笑02 at rt with dissolve
    x "怎么样？要做吗？"
    show y 正常05 at lt  with dissolve
    y "emmmmm…"
    narrator "袁艳的眼珠子在眼睛里头不停地打转，我看着都觉得有些好笑。"
    show y 正常04 at lt  with dissolve
    y "…"
    show y 正常06 at lt  with dissolve
    y "在加上你就成交！！！！"
    narrator "最终她好像是下了决定一样说道。"
    show x 假笑02 at rt with dissolve
    x "你终于变成我想要的那样吗？"
    show y 正常02 at lt  with dissolve
    y "你别误会，我是说刚刚你说的那件事的基础上再算上你一个。"
    show x 怜悯02 at rt with dissolve
    x "呵呵。"
    show x 怜悯03 at rt with dissolve
    x "嗯…那就这样吧。"
    show x 怜悯01 at rt with dissolve
    x "还有，你这只猫叫什么名字啊？"
    show y 无措 at lt  with dissolve
    y "哈！？"
    w "喵？？？"
    show x 惊讶01 at rt with dissolve
    x "你们…反应怎么这么大？"
    show y 嘲讽03 at lt  with dissolve
    y "啊？不，这只猫是我刚从外边捡回来没多久的。"
    show y 嘲讽03 at lt  with dissolve
    y "还没取名字呢。"
    show x 嘲笑01 at rt with dissolve
    x "这样啊。"
    show y 无措 at lt  with dissolve
    y "怎…怎么了吗？"
    show x 假笑01 at rt with dissolve
    x "嗯…没有，它很可爱。"
    narrator "夏静朝着我笑了笑，我却莫名其妙地觉得浑身发冷。"
    w "喵~"
    hide x with dissolve

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
    
    narrator "然后夏静就带着胜利的笑容离开了。"
    narrator "我则是跟着和丢了魂一样的袁艳一起前往了房间。"
    narrator "她有气无力地倒在了床上。"
    narrator "用四个字来形容她现在的样子就是——失魂落魄。"
    narrator "我很好奇，夏静究竟跟她说了什么。"
    narrator "跳上了床，蹲在袁艳的一旁。"
    show y 正常02 at ct with dissolve
    y "死猫…你给我下去。"
    narrator "她有气无力地说着我。"
    w "为啥？"
    show y 正常01 at ct with dissolve
    y "你的爪子刚从地上爬过的，脏。"
    w "……"
    w "都这种时候你还在在意这种小事。"
    w "快跟我说说那个家伙跟你说了些啥？"
    w "哎哟…"
    narrator "突然感觉到后劲一疼，我整只猫让她提了起来，毫不客气地朝着床下一抛。"
    w "你干什么啊！"
    show y 恼火05 at ct with dissolve
    y "不是跟你说了你爪子脏别往床上爬吗？"
    narrator "她从床上坐了起来，半天才开口说话。"
    show y 恼火04 at ct with dissolve
    y "夏静是想跟我交换情报。"
    w "交换情报？"
    w "还需要交换什么情报？"
    w "你们不是在做交易吗？"
    show y 正常02 at ct with dissolve
    y "正经说的话，那三个女孩子我们认识的时间太短了。"
    show y 正常03 at ct with dissolve
    y "所以，我们其实对那三个女孩子一点都不了解。"
    show y 正常04 at ct with dissolve
    y "之前的事情也都是顺势说出来的。"
    show y 正常05 at ct with dissolve
    y "但是，事情能发展到这一步我也没有想到。"
    show y 正常04 at ct with dissolve
    y "至于交易…你懂的吧。"
    w "……"
    w "你根本就没想好下一步怎么做吧。"
    show y 正常06 at ct with dissolve
    y "嗯。"
    w "我就知道，反正也没怎么期待你能想好下一步。"
    w "所以你做成这样就已经很不错了！"
    show y 恼火02 at ct with dissolve
    y "去死吧你！"
    narrator "一个枕头从床上飞向了我，但是这种东西怎么可能打中如此敏捷的我呢？"
    narrator "我优雅地躲了过去。"
    show y 正常01 at ct with dissolve
    y "所以夏静想要跟我交换情报的时候我答应了。"
    w "顺便还加了夏静她自己的情报？"
    show y 恼火02 at ct with dissolve
    y "嗯，我把她也算入了里面。"
    w "那想必她要换的情报对她来说肯定很重要吧。"
    show y 恼火01 at ct with dissolve
    y "那不是废话么。"
    w "那你有她想要的情报吗？"
    show y 正常01 at ct with dissolve
    y "……"
    w "欸？"
    w "你不会要说你没有吧？"
    show y 嘲讽03 at ct with dissolve
    y "额…"
    narrator "她眼神朝着一边看去了。"
    w "那林琴要找的那个人你有头绪吗？"
    w "还有那个叫程祎琳的丫头，你知道怎么实现她们的愿望吗？"
    show y 正常05 at ct with dissolve
    y "……"
    narrator "看着完全不说话的袁艳我就愣住了。"
    narrator "因为我已经知道答案了。"
    w "你还真是的什么都没有想好啊！"
    show y 正常04 at ct with dissolve
    y "没想好…不是很正常吗？"
    show y 正常05 at ct with dissolve
    y "日子总要过的，我不能因为不知道怎么办就等死吧。"
    show y 正常06 at ct with dissolve
    y "我又不是神，该妥协的总得妥协。"
    w "你…你这不是在欺骗她们么？"
    show y 正常04 at ct with dissolve
    y "我哪里欺骗她们了？"
    show y 正常05 at ct with dissolve
    y "伟大的波斯诗人什么迪留下了一句话。"
    show y 正常06 at ct with dissolve
    y "善意的虚伪胜过引起争端的事实。"
    show y 正常04 at ct with dissolve
    y "我知道你想说什么。"
    w "额…"
    show y 正常02 at ct with dissolve
    y "但是，我们是在帮她们啊！对，帮她们啊！"
    w "那你打算怎么办？"
    show y 正常01 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "总会有解决办法的，之前她们三个不也是狠狠地拒绝了我吗？"
    show y 正常02 at ct with dissolve
    y "还不是被我拉回来了。"
    w "好像的确是这么回事。"
    show y 笑容01 at ct with dissolve
    y "看吧，果然是这样！"
    show y 开心 at ct with dissolve
    y "所以总会有办法的啦！！！"
    narrator "袁艳突然就笑起来了。"
    w "说是这样说啦。"
    w "可是你看起来怎么跟穷途末路一样？"
    show y 恐怖颜艺 at ct with dissolve
    y "哇……"
    narrator "袁艳大叫一声，有些抓狂打朝我吼道。"
    show y 不爽03 at ct with dissolve
    y "这还不是穷途末路是什么啊喂！"
    w "嘶…哇，你刚刚不是还说总会有办法嘛？？？"
    show y 不爽01 at ct with dissolve
    y "有办法的话我还在这里跟你瞎扯淡？"
    w "哇，你别把闹钟砸过来啊，会出猫命的啊！"
    narrator "……"
    narrator "大概十分钟左右过去了。"
    w "……"
    narrator "看着满地的狼藉，我算是无语了，所谓的女性这种生物是真的可怕。"
    w "额…累了吗？"
    narrator "我小心翼翼地问着在床上抱着膝盖的袁艳。"
    show y 正常02 at ct with dissolve
    y "嗯，累了。"
    narrator "她也不做作，十分干脆地回答了我。"
    show y 正常01 at ct with dissolve
    y "唉算了，不想了，洗洗睡吧。"
    w "我看你是该睡睡了。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    
    narrator "……"
    narrator "距离诅咒发作还剩五天"
    
    
    ##############################################################
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    
    #【场景：街道】
    scene street_正午 with Dissolve(0.7):
        zoom .667
    
    narrator "小巷子里头的女孩子愣愣地看着她。"
    narrator "他却总觉得有什么不对，而这种感觉不是现在才有的。"
    narrator "自从踏入这座城市他就有感觉到，这种不对劲一直缠绕在他的心头。"
    narrator "仿佛总有一部分残缺了一般。"
    ta "额，我们…真的认识吗？"
    narrator "说着女孩朝着我凑了过来，不由分说地在我身上摸索了起来。"
    ta "哇。你干什么？"
    girl "啊，找到了。"
    girl "老师没有把我忘了呢。"
    narrator "她开心地笑着，手里拿着我都不知道什么时候放在口袋里头的挂件。"
    narrator "那个挂件不管怎么看都不像是男人会带在身上的。"
    ta "呵…"
    narrator "他笑了起来，总觉得有什么荒唐的事情围绕着他展开了。"
    girl "老师你笑什么啊？"
    ta "没呢。"
    narrator "他温柔地回答道。"
    ta "看！"
    girl "嗯？"
    ta "有飞机！！！！"
    narrator "他指着女孩身后。"
    girl "诶诶诶诶？真的吗？"
    narrator "趁着女孩子回过头的一瞬间，他转身十分狼狈地又跑了起来。"
    ta "所以说我为什么一定要跑啊！"

    #【场景：房间】
    scene room_白天 with Dissolve(1.0):
        zoom .667
    
    w "额。"
    narrator "我看着窗前洒落下来的阳光，不知道该干啥。"
    narrator "而那个叫做袁艳的女孩子，目光涣散地靠在床头发呆。"
    narrator "从早上七点多一直发呆到九点多，一动不动，期间连厕所都不去。"
    narrator "我也不知道该怎么跟她搭话。"
    show y 正常02 at ct with dissolve
    y "唉。"
    narrator "她叹了一口气，这个时候她才注意到我。"
    show y 正常01 at ct with dissolve
    y "啊，死猫你醒了啊？"
    narrator "我醒过来都四五个小时了好不好。"
    w "嗯，醒了。"
    show y 开心 at ct with dissolve
    y "诶嘿嘿，肚子饿不饿？"
    w "有点饿了。"
    show y 笑容01 at ct with dissolve
    y "那我去给你做点东西吃吧。"
    w "噢…好..好啊。"
    narrator "我没敢告诉她我早上起来的时候其实已经翻了冰箱偷了点东西吃。"
    narrator "其中还有她之前嘱咐我不准让我偷吃的东西。"
    narrator "看着袁艳逐渐向厨房里头走过去，虚汗也慢慢地从我身体的各个毛孔渗出来。"
    narrator "十来分钟之后…"
    narrator "袁艳端着一盘飘着香味的食物出来了，非常随意地往我面前一放。"
    narrator "然后又走到了床边，钻进被子里——跟之前一模一样打靠在床头发呆。"
    narrator "我吃了两口盘子里头的东西差点没被咸出屎来。"
    w "喵！！！"
    narrator "我干脆懒得吃了，朝着袁艳扑了过去，实在是看不下去她这副规模样了。"
    show y 无措 at ct with dissolve
    y "啊，你干什么啊？"
    narrator "袁艳有些惊讶但是却没啥力气地对我说着。"
    w "够了！你这幅模样真是让人看不下去。"
    w "我们现在去观察那三个女孩吧？"
    show y 不爽03 at ct with dissolve
    y "很疼的啊死猫，去一次疼个半死。"
    w "你要是在慢吞吞的，诅咒发作的时候比这个还疼。"
    show y 无措 at ct with dissolve
    y "啥？"
    show y 恼火01 at ct with dissolve
    y "不会吧？"
    w "我骗你干啥？"
    show y 恼火02 at ct with dissolve
    y "……"
    show y 恼火01 at ct with dissolve
    y "那还等什么啊，赶紧去啊！"
    w "……"
    w "你刚刚还跟死鱼一样呢。"
    show y 笑容01 at ct with dissolve
    y "嗨呀，女孩子都很善变的啦。"
    w "那你要观察谁呢？"
    show y 正常04 at ct with dissolve
    y "还用想吗？当然是——"

    menu:
        "林琴":
            jump c1_c3_l
            
        "夏静":
            jump c1_c3_x
            
        "程祎琳":
            jump c1_c3_c

label c1_c3_l:
    $_dismiss_pause = False

    $c1_c3_l_select = True
    
    scene room_白天:
        zoom .667

    show y 正常04 at ct
    y "这还用说吗？当然是林琴啊？"
    w "没想到你对她会这么感兴趣。"
    show y 正常05 at ct with dissolve
    y "别扯淡，我只是觉得她很有可能就是那个快玩完了的女孩而已。"
    w "呵，我倒是觉得你比她还要像玩完了的女孩。"
    show y 恼火04 at ct with dissolve
    y "去死啊你，我本来就快玩完了还用得着你说。"
    narrator "袁艳皱着眉头，一脸不爽地说道。"
    w "哇，不是吧，别啊！你死了我也要跟着你陪葬啊！"
    show y 正常05 at ct with dissolve
    y "要不是命只有一条，我还真想跟你同归于尽试试。"
    w "……"
    w "咳咳，姐姐您瞧您说的。"
    narrator "这是为了生存，这是为了生存！"
    narrator "我在心里给自己强调着。"
    w "您的命多尊贵啊，怎么能跟我这样的贱猫比呢。"
    show y 正常02 at ct with dissolve
    y "……"
    show y 恼火05 at ct with dissolve
    y "你别恶心我了，赶快带我去观察林琴。"
    show y 恼火04 at ct with dissolve
    y "别磨磨蹭蹭的。"
    w "噢，是是是。"
    narrator "……"
    narrator "看着像是一具死尸一样倒在床一侧的袁艳，我怒由心生，铤而走险——窜上了床。"
    w "哈哈哈！我就在床上踩怎么了。"
    w "我还要往你身上踩。"
    narrator "我还跳上了袁艳身上蹦跶。"
    narrator "床上到处是我的猫爪印，连袁艳身上都不例外。"
    narrator "久而久之我却只感觉到了各种意义上的罪恶感。"
    w "……"
    narrator "并没有想象中的成就感。"
    narrator "停止了自己罪恶般的行为，蜷缩在袁艳的跟前，闭上眼睛，追随她的灵魂过去了。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    #【场景：医院病房】
    scene bf_白天 with dissolve:
        zoom .667
    
    show y 正常04 at ct with dissolve
    y "其实我一直在想…"
    w "…"
    w "在想啥？"
    show y 正常05 at ct with dissolve
    y "我可能对林琴的期待是不是高了一点点，所以导致我现在稍微…"
    show y 正常04 at ct with dissolve
    y "只是稍微噢，有那么一点点小小的失望。"
    w "啊，你在说什么？"
    show y 正常05 at ct with dissolve
    y "不不不，很有可能其实是我想得太美好了。"
    show y 正常02 at ct with dissolve
    y "我重新来过。"
    w "……"
    show y 正常04 at ct with dissolve
    y "其实我一直在想。"
    show y 正常02 at ct with dissolve
    y "会不会是我对人类的期待高了些，所以导致我现在有点儿失望。"
    show y 正常01 at ct with dissolve
    y "就是那个啦，比如看上去挺好吃的菜吃到嘴里却想吐的那种感觉。"
    w "怎么还上升到人类的地步了，到底发生了啥？"
    show y 开心 at ct with dissolve
    y "呵呵呵…"
    show y 开心 at ct with dissolve
    y "发生了什么你不会自己看啊。"
    narrator "袁艳指着病床上的那个女人，一脸自己家儿子没出息的表情悲愤地说道。"
    narrator "我当然是顺着袁艳的目光朝着她看去。"
    w "额…"
    w "好像也没什么啊。"
    narrator "正如我所见，在我面前的那个女孩其实什么也没做，她仅仅只是躺在床上，用我的话来说就是普通地躺在床上，正常地发着呆。"
    narrator "我反而是不理解为什么袁艳对此如此的愤慨。"
    show y 恼火05 at ct with dissolve
    y "是吗？"
    narrator "但是不知道为什么，听到我这么说之后，袁艳反而用一副悲痛欲绝地眼神看着我，而且这份悲痛欲绝正在逐渐转换成一股莫名其妙的杀意。"
    w "等…等一下！我觉得这肯定是有原因的！"
    show y 恼火04 at ct with dissolve
    y "噢？那你倒是说说看，都发生了这种事情。"
    show y 恼火02 at ct with dissolve
    y "她还能没事人一样坐那的理由是啥？"
    w "我…我怎么知道。"
    w "虽然我是不知道你到底在期待什么啦。"
    show y 恼火01 at ct with dissolve
    y "难道这个时候她不应该开始积极准备谈恋爱吗?"
    show y 恼火02 at ct with dissolve
    y "我都已经把话说得这么清楚啊！"
    show y 恼火01 at ct with dissolve
    y "起码有点动作吧。"
    w "……"
    w "难道你们人类谈恋爱是那种想谈就可以谈得到的吗？"
    show y 正常02 at ct with dissolve
    y "那倒没有。"
    w "是吗？"
    show y 正常01 at ct with dissolve
    y "但是她明明说不用我担心却一点动作都没有。"
    w "这有什么问题吗？"
    show y 正常04 at ct with dissolve
    y "有！当然有，你听我说。 "
    w "啥？"
    show y 正常05 at ct with dissolve
    y "恋爱这种东西可是不会亲自送上门来的。"
    show y 正常04 at ct with dissolve
    y "一见钟情也好、日久生情也好，都是要有人迈出第一步才有可能的。"
    show y 正常05 at ct with dissolve
    y "你看她就这样躺在这里看得我心都揪起来了。"
    w "……"
    narrator "说句实话，我听不懂。"
    show y 正常01 at ct with dissolve
    y "嘛，以你的智商估计也不会懂啦。"
    w "那你就不要说出来呀啊喂。"
    narrator "袁艳摊了摊手，稍微有些无奈地看着我。"
    show y 正常04 at ct with dissolve
    y "一会回去的时候咱们就动身去见她吧。"
    show y 正常02 at ct with dissolve
    y "不然这状况持续下去就很不妙了啊。"
    w "你要去找她，我倒是没有意见。"
    w "但是麻烦你下次别再把我往那个医院里的老头身上扔了行吗？"
    w "我也是有洁癖的啊。"
    show y 开心 at ct with dissolve
    y "不会的不会的，请放心。"
    narrator "她看了我一眼，却露出了莫名其妙的笑容，这让我感觉到非常地不安。"
    w "那你现在打算怎么办？"
    show y 笑容01 at ct with dissolve
    y "那还用说？"
    narrator "她给我递了一个理所当然的眼神。"
    show y 开心 at ct with dissolve
    y "当然是怼到她们面前去手把手教她们谈恋爱啊。"
    w "……"
    narrator "我总觉得好像针对错了目标。"
    narrator "这个时候重要的不应该是恋爱吧。"
    w "等…等一下！"
    show y 恼火02 at ct with dissolve
    y "干啥？"
    narrator "她朝我投来了疑惑的视线。"
    w "这个时候重要的不应该是谈恋爱吧！！！"
    show y 正常01 at ct with dissolve
    y "…"
    show y 正常02 at ct with dissolve
    y "那重要的是什么？"
    w "我们最终的目的不是为了找到究竟哪个女孩子心灵快崩溃了吗？"
    show y 正常01 at ct with dissolve
    y "听你这么一说还有点道理。"
    w "你不是把这事给忘了吧！！！"
    show y 正常04 at ct with dissolve
    y "简直胡说八道，我看起来像是那么容易忘事的家伙吗？"
    narrator "袁艳说这话的时候没有丝毫犹豫，信誓旦旦得像是真的一样。"
    w "……"
    w "你救我的那天晚上吃的是啥？"
    narrator "袁艳很明显地愣了一下。"
    narrator "然后眯了眯眼睛，照着我的屁股就踢了一脚。"
    narrator "当然在这种状态下， 袁艳的脚从我的身体里头穿了过去，并没有实际地踢到我。"
    show y 恼火05 at ct with dissolve
    y "你脑子是不是有坑啊，都过去多少天了我怎么记得吃的什么？"
    w "额，我都记得好不好。"
    show y 恼火04 at ct with dissolve
    y "那你记得就记得咯，关我什么事。"
    w "……"
    w "额，姑且我还是问一下…"
    show y 正常05 at ct with dissolve
    y "问啥？"
    w "你会不会是记忆力有点残疾？"
    show y 无措 at ct with dissolve
    y "噗！"
    w "你怎么了？"
    narrator "袁艳愣愣地看了我一眼。"
    show y 嘲笑 at ct with dissolve
    y "你这形容词还真是有点…微妙的精辟啊。"
    w "额，那是，我是谁啊！这个世界上最最最最…"
    show y 嘲讽01 at ct with dissolve
    y "得得得，给你点好脸色你尾巴都翘到天上去了。"
    w "啊？"
    narrator "听袁艳这么说我不由得看向了自己的尾巴，并没有翘起来啊，我有些奇怪地挠了挠并不能挠到的脑袋。"
    narrator "非常地疑惑袁艳说的话。"
    narrator "但是又不知道从哪里质疑起。"
    show y 正常02 at ct with dissolve
    y "不过我记忆力确实是有点差就是了。"
    w "这…这样吗？那下次记住就行了。"
    w "那你接下来还去她那里吗？"
    show y 正常03 at ct with dissolve
    y "先把剩下的两个丫头都观察完再说吧。  "
    w "嗯。"
    narrator "这次的袁艳在回去时没有大喊大叫，只是微微的皱了皱眉头。"
    narrator "她莫名其妙地看了一眼林琴又看了看我叹了口气便消失在这个地方。"
    narrator "空气莫名其妙的安静，我立在病房的角落观察者在床上发呆的林琴。"
    narrator "她现在的样子和在袁艳家里那个气势汹汹的家伙完全是两个人。"
    narrator "我不由得回想起了之前她发狂的模样，总觉得她马上又要突然爆发。"

    narrator "看着她的模样，我觉得应该会是这样。 "
    w "在这个方面我还这没有袁艳果断啊。"
    narrator "微微地张了张嘴，心里默默地计算着时间。"
    narrator "总觉得下一秒会发生什么变化。"
    narrator "可惜事实总是会跟想法不一样，这个叫林琴的丫头分明已经是已经发呆到一种暂时醒不过来的境界了。"
    narrator "对于这样的她我到底在期待些什么，想要看到什么呢。"
    w "唉。"
    narrator "这副模样倒也不是完全没有收获。"
    narrator "至少在某种方面来说倒是加重了她的嫌疑，让我判断有一些依据了而已。"
    narrator "如果她就是那个崩溃的女孩，那么现在我就能让诅咒解除了。"
    narrator "当然如果错了的话，我跟袁艳就要一起死翘翘了，所以我现在还不敢赌。"
    narrator "至少现在还不敢…还有——五天，不还有三天。"
    narrator "差不多，那个就快要来了才对…"
    narrator "长长地叹了一口气，带着对未来无比的担忧，我又看了一眼依旧还在发呆的女孩，然后离开了这个安静的病房。"

    jump c1_4


label c1_c3_c:
    $_dismiss_pause = False

    $c1_c3_c_select = True
    
    scene room_白天:
        zoom .667

    show y 正常04 at ct
    y "这还用说吗？当然是程祎琳啊？"
    w "没想到你对她会这么感兴趣。"
    show y 正常05 at ct with dissolve
    y "别扯淡，我只是觉得她很有可能就是那个快玩完了的女孩而已。"
    w "呵，我倒是觉得你比她还要像玩完了的女孩。"
    show y 恼火02 at ct with dissolve
    y "去死啊你，我本来就快玩完了还用得着你说。"
    narrator "袁艳皱着眉头，一脸不爽地说道。"
    w "哇，不是吧，别啊！你死了我也要跟着你陪葬啊！"
    show y 恼火04 at ct with dissolve
    y "要不是命只有一条，我还真想跟你同归于尽试试。"
    w "……"
    w "咳咳，姐姐您瞧您说的。"
    narrator "这是为了生存，这是为了生存！"
    narrator "我在心里给自己强调着。"
    w "您的命多尊贵啊，怎么能跟我这样的贱猫比呢。"
    show y 恼火01 at ct with dissolve
    y "……"
    show y 恼火02 at ct with dissolve
    y "你别恶心我了，赶快带我去观察林琴。"
    show y 恼火04 at ct with dissolve
    y "别磨磨蹭蹭的。"
    w "噢，是是是。"
    narrator "……"
    narrator "看着像是一具死尸一样倒在床一侧的袁艳，我怒由心生，铤而走险——窜上了床。"
    w "哈哈哈！我就在床上踩怎么了。"
    w "我还要往你身上踩。"
    narrator "我还跳上了袁艳身上蹦跶。"
    narrator "床上到处是我的猫爪印，连袁艳身上都不例外。"
    narrator "久而久之我却只感觉到了各种意义上的罪恶感。"
    w "……"
    narrator "并没有想象中的成就感。"
    narrator "停止了自己罪恶般的行为，蜷缩在袁艳的跟前，闭上眼睛，追随她的灵魂过去了。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667
    
    
    show y 正常05 at ct with dissolve
    y "唔…"
    narrator "跟上次不一样的事情是。"
    narrator "今天的程祎琳很正常地就坐在长椅上吃薯片。"
    narrator "正常到很难让人想到她究竟有什么地方是不正常的。"
    narrator "或者说觉得她不正常的家伙才不正常才对。"
    show y 正常03 at ct with dissolve
    y "唔…嗯…"
    narrator "对，没错就是这样。"
    narrator "在远处看着她的我不由得这么想到。"
    narrator "再然后就是，一脸痴样凑到女孩边上的流着口水的家伙是不正常的。"
    narrator "对，没错就是这样。"
    narrator "在远处看着她的我不由得这么想到。"
    show y 正常04 at ct with dissolve
    y "啊…"
    w "那个…袁艳小姐。"
    w "虽然我只知道这个小丫头看不到你。"
    w "但是我还是能看得见你的。"
    show y 正常04 at ct with dissolve
    y "去去去。"
    show y 正常05 at ct with dissolve
    y "我这是在观察，我这是在观察你懂吗？"
    w "是…是吗？"
    w "人类观察别人还会流口水的吗？"
    narrator "袁艳一愣，然后像是反应过来了一样不紧不慢地擦了擦自己的口水。"
    narrator "然后直起了身子，看向了我。"
    narrator "看起来她很不爽，像是想抓着我揍一顿一样。"
    narrator "当然，在这里我是完全不害怕她的——我说真的。"
    show y 恼火05 at ct with dissolve
    y "怎么了？看得见我你就不起了？"
    w "……"
    w "没…没呢，就是想问问你在干啥？"
    show y 恼火06 at ct with dissolve
    y "你没看见我在认真地观察她吗？"
    w "原来如此原来如此。"
    show y 恼火04 at ct with dissolve
    y "知道了就好。"
    w "……"
    w "额…"
    narrator "估计是看到我支支吾吾的样子，刚准备投入新一轮‘观察’的袁艳不耐烦地双手环抱着自己的腰。"
    show y 正常05 at ct with dissolve
    y "你要说什么就快说。"
    w "那你观察她这样吃东西有什么结论吗？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "结论啊，当然是有的啊。"
    show y 正常04 at ct with dissolve
    y "你当我是谁啊。"
    w "那还真是厉害。"
    show y 恼火05 at ct with dissolve
    y "哼哼。"
    w "那是什么结论呢？"
    show y 恼火04 at ct with dissolve
    y "结论就是我也想吃。"
    w "……"
    narrator "虽然早就料到不会是什么好结局了，但是你好歹犹豫一下啊。"
    show y 
    y "还有一件事。"
    narrator "听到她这么说我马上就竖起了耳朵，袁艳这死丫头啊就是喜欢吊人胃口。"
    narrator "玩弄那三个丫头就算了，怎么这回把我都给算进去了啊。"
    narrator "真拿她没办法。"
    narrator "不过好在她至少还是知道做点正事的。"
    show y 正常05 at ct with dissolve
    y "我是认真的。"
    narrator "她非常地、无比郑重地、煞有其事地看着我然后说出了这句话。"
    w "……"
    narrator "我是认真的…"
    narrator "是认真的…"
    narrator "认真的…"
    narrator "真的…"
    narrator "的…"
    narrator "……"
    narrator "这几个字的声音不断地在我耳朵里来回摩擦，不断地在我脑海里头张狂地扩散。"
    narrator "如果能够打到她的话，我一定毫不犹豫冲上去就是一爪子。"
    narrator "我什么也不想干只想把这丫头的现在一副认真的嘴脸给撕得稀巴烂。"
    show y 正常05 at ct with dissolve
    y "看得出来。"
    show y 正常04 at ct with dissolve
    y "像你这样的死猫肯定是没办法理解身为吃货应该有的执着。"
    show y 正常05 at ct with dissolve
    y "身为一名吃货。"
    show y 正常02 at ct with dissolve
    y "只要是吃不死，就往死里吃，虽然我还没有达到那个程度。"
    show y 正常01 at ct with dissolve
    y "但是惦记吃这一点我比你要强几百倍。"
    narrator "袁艳甚至还像是比划一样伸出手指指着我。"
    w "完全不明白你到底在自豪个什么东西。"
    w "但是你能不能不要老想着吃啊，你是来观察人家的啊。"
    show y 正常04 at ct with dissolve
    y "…"
    show y 正常05 at ct with dissolve
    y "好像真的是这样子。"
    w "就是这样子好不啦。"
    show y 正常04 at ct with dissolve
    y "那你还别说，我还真没观察出什么东西来。"
    w "所以说你到底在自豪个什么劲啦。"
    narrator "就在我们争吵的期间，一个很熟悉的人突然出现在了这里。"
    narrator "我和袁艳瞬间就停止了争吵。"
    narrator "因为来的人居然是那个叫做夏静的女孩。"
    narrator "她手里很明显提着一大包零食向程祎琳走了过去。"
    show y 正常02 at ct with dissolve
    y "额…"
    w "喵？"
    show y 正常04 at ct with dissolve
    y "死猫…跟你说件事。"
    w "说啥？"
    show y 正常05 at ct with dissolve
    y "其实…我记忆力有点不太好。"
    w "……"
    w "所以呢？你到底想说啥？"
    show y 正常02 at ct with dissolve
    y "我是不是之前说错话了？"
    w "不明白你的意思。"
    show y 恼火04 at ct with dissolve
    y "她们两个为什么会凑到一块去了？"
    show y 恼火05 at ct with dissolve
    y "最可恨的是为什么夏静会给程祎琳买零食？"
    narrator "我无语地看着一本正经咬牙切齿的袁艳。"
    w "我看你恨的重点是后面这个问题吧。"
    narrator "……"

    #【CG：别有用心的馈赠】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_byyx = True
    scene cg_别有用心的馈赠 with Dissolve(2)
    
    pause 1.0
    
    #show x None
    x "你好像很喜欢吃零食，我特地给你买了不少哦。"
    narrator "夏静停在程祎琳所坐着的椅子面前，把手中包装着明显是零食的一袋子朝着程祎琳递了过去。"
    narrator "程祎琳拿着薯片的手一瞬间愣在了半空。"
    narrator "她歪着脑袋看着夏静，似乎很疑惑出现在这里的她。"
    narrator "但是她却目不转睛地盯着夏静手中的那袋零食。"
    narrator "从我们的角度来看，一眼就能看出程祎琳心里面所想的东西。"
    #show x None
    x "不要吗？"
    narrator "程祎琳似乎是在内心纠结了一下，但是在最后不知道被什么东西战胜了。"
    narrator "皱着的眉头松开来，然后咧开嘴接过了夏静手里头的零食。"
    #show c
    c "嘿嘿嘿，谢谢你惹…"
    #show c
    c "我叫程祎琳，你叫什么啊？"
    
    #【CG::结束】
    scene river_白天 with dissolve:
        zoom .667
    
    w "……"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常01 at ct with dissolve
    y "死猫。"
    w "怎么了？"
    show y 正常01 at ct with dissolve
    y "姑且还是确认一下。"
    w "确认啥？"
    show y 正常02 at ct with dissolve
    y "这几天发生的事情不是在梦里头发生的吧。"
    w "干啥问这个？"
    show y 正常04 at ct with dissolve
    y "少废话，你快告诉我。"
    w "我以我的猫格担保，之前的事情都是发生过的。"
    show y 正常04 at ct with dissolve
    y "这样啊，唉。"
    w "你叹什么气啊？"
    show y 正常05 at ct with dissolve
    y "没，只是有点感叹，这个世界还真有这样的人存在啊。"
    show y 正常04 at ct with dissolve
    y "明明见过几次了却记不住别人的名字。"
    show y 正常05 at ct with dissolve
    y "说她是个有问题的人丝毫不为过啊。"
    w "这点上我不是早就提醒过你了吗？"
    show y 正常04 at ct with dissolve
    y "唉…"
    hide y with dissolve
    narrator "……"
    narrator "当然夏静并没有对这个表现得很意外。"
    narrator "相反她反而很自然地介绍起了自己。"
    show x 假笑02 at rt with dissolve
    x "我的名字叫做夏静。"
    show x 假笑01 at rt with dissolve
    x "是和你一起同那个叫袁艳的女人相遇的伙伴。"
    show c 侧视02 at lt with dissolve
    c "噢…"
    show c 斜视01 at lt with dissolve
    c "是这样吗？"
    #上下摇动
    narrator "夏静不着痕迹地点了点头。"
    narrator "程祎琳则是若有所思地盯着手上的一袋零食。"
    show c 斜视02 at lt with dissolve
    c "那吃一些伙伴的零食也是没关系的吧。"
    narrator "……"
    hide c with dissolve
    hide x with dissolve
    show y 恼火01 at ct with dissolve
    y "这是什么逻辑啊！话说你们哪里看起来像伙伴了！"
    w "额，你犯得着这样吐槽吗？"
    narrator "其实我内心是知道的，袁艳为什么会这么激动。"
    narrator "从她两眼发光盯着那一袋零食我就知道了。"
    w "话说你想吃不知道自己去买啊。"
    show y 恼火02 at ct with dissolve
    y "…"
    show y 恼火01 at ct with dissolve
    y "你懂个屁啦。"
    show y 恼火04 at ct with dissolve
    y "你听好了，所谓的零食。"
    show y 愤怒 at ct with dissolve
    y "只有在别人那里的时候是最好吃的。"
    w "……"
    w "这是什么歪道理啊！！"
    show y 正常02 at ct with dissolve
    y "不过说来也很奇怪。"
    w "奇怪什么？"
    show y 正常04 at ct with dissolve
    y "就算见过好几次，我也不认为夏静有理由去给程祎琳买零食。"
    w "所以呢？"
    show y 正常05 at ct with dissolve
    y "如果不是夏静脑袋犯抽了想跟程祎琳这个女孩讨论少女该讨论的青春话题。"
    show y 正常05 at ct with dissolve
    y "那就是说明这行为应该是有所预谋的。"
    show y 正常04 at ct with dissolve
    y "只是我现在还没办法判断而已。"
    w "……"
    narrator "被袁艳这么一说我在看看那两个长椅那边的两个女孩。"
    narrator "还真有那么一点不协调的味道。"
    narrator "夏静那样子的女孩会对程祎琳有兴趣确实也有点出乎我的意料之外。"
    w "那我们要继续观察吗？"
    show y 正常02 at ct with dissolve
    y "自己想。"
    hide y with dissolve
    narrator "说完袁艳就有些无语地继续看向那两个人，看样子是打算继续观察了。"
    narrator "虽然我也是看不出来什么东西，姑且也只能跟着看了。"
    narrator "但是事实上，在这之后的很长时间里头，夏静也只是坐在程祎琳的旁边。"
    narrator "程祎琳除了在打开袋子翻翻里头的零食皱了皱眉毛以外，到没有别的比较可疑的动作。"
    narrator "把夏静送的一袋零食放到一边吃自己的零食估计也是为了之后在慢慢来吃。"
    show x 假笑02 at rt with dissolve
    x "你好像并不是很喜欢我给你送的零食呢。"
    show c 斜视01 at lt with dissolve
    c "……"
    show c 斜视02 at lt with dissolve
    c "嗯，不喜欢。"
    narrator "她很明确地表明了自己的态度，在这之余还不忘塞一口薯片在嘴里。"
    show x 假笑01 at rt with dissolve
    x "这样啊，那我先走了。"
    hide x with dissolve
    narrator "看着夏静离去的背影，我和袁艳不由得陷入了沉思。"
    hide c with dissolve
    show y 正常04 at ct with dissolve
    y "emmm……"
    w "你又有什么新的发现吗？"
    show y 正常06 at ct with dissolve
    y "暂时…没有。"
    w "那还要继续观察吗？"
    show y 正常04 at ct with dissolve
    y "不了，我想回去。"
    w "额…好吧。"

    narrator "这次的袁艳在回去时没有大喊大叫，只是微微地皱了皱眉头。"
    narrator "她莫名其妙地看了一眼程祎琳又看了看我。"
    narrator "叹了口气便消失在这个地方。"
    narrator "随着她的离开，空气突然变得很安静。"
    narrator "总觉得会发生什么。"
    narrator "看着她的模样，我觉得应该会是这样。 "
    w "在这个方面我还这没有袁艳那丫头果断啊。"
    narrator "微微地张了张嘴，心里默默的计算着时间。"
    narrator "但是程祎琳什么也没有做，只是坐在长椅上忘我的吃着零食，仿佛世界只有她一个人一般。"
    narrator "对这样的她我到底在期待些什么，想要看到什么呢。"
    w "唉。"
    narrator "倒也不是完全没有收获。"
    narrator "至少在某种方面来说倒是加重了她的嫌疑，让我判断有一些依据了而已。"
    narrator "如果她就是那个崩溃的女孩，那么现在我就能让诅咒解除了。"
    narrator "当然如果错了的话，我跟袁艳就要一起死翘翘了，所以我现在还不敢赌。"
    narrator "至少现在还不敢…还有——五天，不还有三天。"
    narrator "差不多，那个就快要来了才对…"
    narrator "长长地叹了一口气，带着对未来无比的担忧，我又看了一眼依旧还在吃零食的女孩，然后离开了这个地方。"

    jump c1_4

#夏静
label c1_c3_x:
    $_dismiss_pause = False

    $c1_c3_x_select = True
    
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667
    narrator "总觉得袁艳的心情不是很好的样子。"
    narrator "主要原因应该还是来自于我们所观察的对象。"
    narrator "那个叫做夏静的女孩。"
    w "你看上去心情不是很好啊。"
    show y 正常04 at ct with dissolve
    y "唉。"
    w "怎么了？"
    show y 正常05 at ct with dissolve
    y "跟这样的家伙做交易真让人感觉到毛骨悚然。"
    narrator "我顺着袁艳注视的地方看了过去。"
    
    #【CG：隐藏的守望者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_swz = True
    scene cg_隐藏的守望者 with Dissolve(2)

    pause 1.0
    
    narrator "夏静静静地依着河边的栅栏，看着城市那边的天空。"
    narrator "好像在思考着什么又好像不是。"
    narrator "微风将她的长发轻轻地吹起，远远看起来仿佛她就是画里头的人物一样。"
    narrator "可惜我不是很会欣赏这样的东西。"
    w "也没什么特别的啊？"
    #show y None
    y "睁大你的死猫眼，看仔细了。"
    
    #【CG：结束】
    scene black with Dissolve(.7)

    scene river_白天 with dissolve:
        zoom .667
    
    narrator "我又不理解地看了看夏静。"
    narrator "然而我却惊奇地睁大了眼睛，就在夏静另一个方向的不远处。"
    narrator "有一个熟悉的身影在那儿。"
    narrator "她不断地把手伸进一个包装袋里头，然后抓起一把把薯片就往嘴里塞。"
    narrator "这个女孩虽然话不多，但是却也让我印象非常的深刻。"
    narrator "她就是那个名字叫做程祎琳的女孩，袁艳曾说过她是某一场灾难里头的幸存者。"
    narrator "那么这个时候我在回过头来看夏静就变得有些不一样了。"
    
    #【CG：隐藏的守望者】
    #scene black with Dissolve(.7)
    #window hide dissolve
    #$renpy.pause(3,hard=True)
    #$ persistent.cg_swz = True
    #scene cg_隐藏的守望者 with Dissolve(2)
    
    #pause 1.0
    
    narrator "如果是正常的情况绝对没办法发现的。"
    narrator "夏静的目光并不是看着城市的那一边。"
    narrator "真正所观察的，应该是在另一个方向的那个名为程祎琳的女孩。"
    show x 惊讶01 at ct with dissolve
    x "嗯？"

    #【CG:结束】
    #scene river_白天 with dissolve:
    #    zoom .667
    narrator "然后就在这个时候发生了一件非常诡异的事情。"
    narrator "夏静朝着我和袁艳所在的方向投来了疑惑的视线。"
    narrator "那个眼神就如同看见了我们两个人一样。"
    narrator "当然，她并没有看见我们。"
    narrator "理由就是她很快又恢复了之前的状态，继续观察起了程祎琳。"
    hide x with dissolve
    show y 恼火02 at ct with dissolve
    y "喂，死猫。"
    w "干…干啥，话说我不叫死猫，请叫我神圣的…"
    w "…没什么，你继续说吧。"
    show y 正常02 at ct with dissolve
    y "……	"
    narrator "袁艳无语地看了看我一眼，然后说道。"
    show y 正常01 at ct with dissolve
    y "你觉不觉得夏静她有点奇怪？"
    w "我知道你想说什么。"
    w "虽然我也很惊讶啦，但是她是不可能看的见我们的存在的。"
    w "这点我有绝对的自信。"
    show y 正常04 at ct with dissolve
    y "我不是说这个啦。"
    w "啊？"
    show y 正常05 at ct with dissolve
    y "虽然我记忆力不怎么好，但是我隐约记得夏静像是发现我们的事情好像在之前也发生过。"
    w "我不记得有发生过这种事啊。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "好吧…不说这个了，总而言之。"
    show y 正常04 at ct with dissolve
    y "目前可以确定的事情是她一直保持着观察程祎琳的状态。"
    show y 正常05 at ct with dissolve
    y "但是原因暂时不太清楚。"
    w "嗯，这点我也看出来了。"
    w "但是这有什么线索吗？"
    show y 恼火04 at ct with dissolve
    y "谈不上什么线索。"
    show y 恼火05 at ct with dissolve
    y "夏静不是说要跟我做交易吗？"
    show y 正常05 at ct with dissolve
    y "我觉得，她现在做的事情应该跟我的交易有联系才对。"
    w "……"
    w "得得得，信了你的邪了。"
    w "现在我估摸着那丫头就算是放个屁你都会觉得跟你交易有联系了。"
    show y 恼火02 at ct with dissolve
    y "呸，死猫你又皮痒了是不是？"
    w "……"
    w "不是，我是说你有什么依据证明她做的事情跟你的交易有关系呢？"
    w "毕竟你看…之前她也有跟踪程祎琳不是吗？"
    show y 正常04 at ct with dissolve
    y "当然是…"
    narrator "袁艳被我一席话说得无地自容，话在嘴边一直打转。"
    narrator "这种让她吃瘪的感觉不知道怎的…有点…愉悦…"
    show y 嘲讽03 at ct with dissolve
    y "这是女人的直觉…大概。"
    narrator "连自己都不确定的直觉能有多准啊。"
    narrator "我连吐槽她的心思都没有了。"
    w "所以有什么用吗？"
    w "就算你知道了又能怎么样啊？"
    show y 正常04 at ct with dissolve
    y "总觉得这个夏静有些不对劲。"
    show y 正常05 at ct with dissolve
    y "你说她会不会可能就是我们要找的那个女孩？"
    w "你疯啦，这么早就下结论。"
    show y 正常04 at ct with dissolve
    y "我很冷静。"
    show y 笑容01 at ct with dissolve
    y "不过刚刚是开玩笑的。"
    narrator "我不由得松了一口一气。"
    show y 笑容02 at ct with dissolve
    y "难不成我说是谁你就会对谁使用你那个....那个什么来着？"
    w "点火。"
    show y 笑容01 at ct with dissolve
    y "对对对，难不成我说是谁你就点谁的火吗？"
    w "……"
    narrator "我无奈地看了看袁艳，然后更加无奈地点了点头。"
    w "是我的话大概就只能赌一把了，因为我不是很懂你们这些人类的心思。"
    w "但是我来赌的话风险实在是太大了。"
    w "与其这样不如交给同为人的你来抉择。"
    w "所以我除了相信你我不会做出别的判断。"
    show y 正常05 at ct with dissolve
    y "…"
    show y 正常04 at ct with dissolve
    y "是吗？"
    w "嗯。"
    show y 正常04 at ct with dissolve
    y "想不到你也有这么正经的时候，要是一开始就这么正经就好了。"
    w "我一直都很正经的好不好。"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常01 at ct with dissolve
    y "算了，继续保持观察吧，我倒是很想知道她们究竟会发生些什么。"
    w "其实我一直搞不太懂你到底想要观察什么啦。"
    show y 正常03 at ct with dissolve
    y "我想回去了。"
    narrator "袁艳似乎有些疲惫地地说道。"
    w "…"
    w "好吧。"
    narrator "令我意外的事情是——"
    narrator "这次的袁艳在回去时没有大喊大叫，只是微微地皱了皱眉头。"
    narrator "她莫名其妙地看了一眼夏静又看了看我。"
    narrator "叹了口气便消失在这个地方。"
    narrator "随着她的离开，空气突然变得很安静。"
    narrator "我注视着夏静。"
    narrator "总觉得会发生什么。"
    narrator "看着她的模样，我觉得应该会是这样。 "
    w "在这个方面我还这没有袁艳那丫头果断啊。"
    narrator "微微地张了张嘴，心里默默地计算着时间。"
    narrator "但是夏静什么也没有做，只是像思考问题一样注视着不远处的程祎琳，除此之外什么也没有做。"
    narrator "对这样的她我到底在期待些什么，想要看到什么呢。"
    w "唉。"
    narrator "倒也不是完全没有收获。"
    narrator "至少在某种方面来说倒是加重了她的嫌疑，让我判断有一些依据了而已。"
    narrator "如果她就是那个崩溃的女孩，那么现在我就能让诅咒解除了。"
    narrator "当然如果错了的话，我跟袁艳就要一起死翘翘了，所以我现在还不敢赌。"
    narrator "至少现在还不敢…还有——五天，不还有三天。"
    narrator "差不多，那个就快要来了才对…"
    narrator "长长地叹了一口气，带着对未来无比地担忧，我又看了一眼依旧还站在那里的女孩，然后离开了这个地方。"
    
    jump c1_4


label c1_4:
    $_dismiss_pause = False
    
    nvl clear
    nvl hide
    window hide Dissolve(1)
    scene black with Dissolve(2)
    #【场景：房间】
    scene room_白天 with Dissolve(1.0):
        zoom .667
    
    narrator "我，是一只猫。"
    narrator "但是并非是一只普通的猫。"
    narrator "非要说的话，那也只能称谓为非常神圣的猫。"
    narrator "由于族落传统的原因，我没有办法将有关于自己种族的事情告知其他物种。"
    narrator "不过这也并不影响我身为这个神秘种族一员应有的尊严。"
    narrator "就算是受到胁迫、遭遇不测也是如此。"
    w "所以…就算你把我两条腿绑起来又怎么样？"
    narrator "你觉得我就会屈服吗？"
    narrator "我看着面前笑眯眯的女孩心里不由得这样想到。"
    narrator "虽然不好的预感愈来愈强烈，但是内心尊严所驱使的这份意志是不会轻易妥协的。"
    w "你说话啊？"
    narrator "我气势汹汹地侧躺在地上，朝着什么也没做的就站在房间里头的袁艳吼道。"
    narrator "袁艳也不理我，只是笑着在那里吃零食。"
    narrator "对，真的就只是在那里吃零食。"
    narrator "或许她是以为用这种招数可以折磨到我，不过这未免也太小看我了。"
    narrator "我对人类的零食其实一点兴趣都没有。"
    show y 笑容01 at ct with dissolve
    y "啊啦，是时候吃午饭了呢。"
    narrator "她故作惊讶地说道。"
    show y 嘲笑 at ct with dissolve
    y "早上因为起晚了没能好好吃早饭呢，真可惜。"
    narrator "虽然内容只是在谈早饭的事情，但是不知道为什么总觉得有点…"
    w "哇，恶心死了。"
    w "你当你是哪个国家的贵族吗？"
    hide y with dissolve
    narrator "她并没有理会我的吐槽。"
    narrator "起身到厨房去了。"
    narrator "不一会儿厨房就传来了噼里啪啦的声音。"
    narrator "她到底在干什么？"
    narrator "我不由得有些疑惑起来。"
    narrator "难不成是想在我面前吃东西？"
    narrator "可是她刚刚不是已经在我面前吃零食了吗？"
    narrator "以为这样就能对付我未免也太天真了点吧。"
    narrator "但是很快我就明白天真的…是我。"
    narrator "就在不久之后。"
    narrator "袁艳带着淡雅的笑容离开厨房回到了房间。"
    narrator "手上还端着一盘不可名状的黑乎乎一团的东西。"
    show y 正常02 at ct with dissolve
    y "知道我为什么只点外卖吃嘛？"
    w "……"
    narrator "她把那一盘散发着焦臭味的东西放到了我的面前。"
    narrator "答案估计就是这个了。"
    narrator "她想干嘛？杀猫灭口吗？"
    show y 笑容01 at ct with dissolve
    y "现在给你两条路。"
    show y 开心 at ct with dissolve
    y "一、吃了这个。"
    show y 开心 at ct with dissolve
    y "二…"
    narrator "然后她不知道从哪里抽出一把水果刀，突然插到了我的头顶。"
    narrator "吓得我一激灵。"
    narrator "不用说，不服从的下场一定会非常的惨。"
    w "…"
    w "我吃我吃…"
    w "能帮我解开绳子吗？"
    # TODO
    show y 开心 at ct with dissolve
    narrator "袁艳摇了摇头。然后笑着拿出了勺子，半蹲在我的身旁。"
    #y "来，我喂你吃。"
    w "……"
    narrator "袁艳满满一勺子地将不可名状朝我嘴边递了过来。"
    narrator "同时递过来的还有水果刀，抵在我的颈部的位置。"
    narrator "其威胁的意思非常明显。"
    show y 开心 at ct with dissolve
    y "啊，张嘴。"
    w "……"
    narrator "对不起母亲…"
    narrator "对不起…我远在家乡的母亲。"
    w "啊…"
    w "…"
    narrator "舌头接触到‘那个’的一瞬间。"
    narrator "一股酸味爆炸般在嘴里扩散开来。"
    narrator "眼泪瞬间止不住地流了出来。"
    show y 恐怖颜艺 at ct with dissolve
    y "哎呀，你怎么哭了？"
    w "唔…唔…"
    show y 开心 at ct with dissolve
    y "这么好吃吗？没事，还有很多。"
    narrator "袁艳的笑容此刻宛如真正的恶魔。"
    narrator "……"
    narrator "躺在地上，眼角没有任何神采。"
    narrator "就好像被人给侵犯了一样，屈辱的眼泪不停地从眼睛里头流出来。"
    narrator "什么生啊、死啊、诅咒啊仿佛在这个时候跟我没了关系。"
    narrator "而犯人袁艳则是一脸逍遥自在地在一旁吃着香喷喷的外卖。"
    show y 正常04 at ct with dissolve
    y "别装委屈了。"
    show y 正常05 at ct with dissolve
    y "要说为什么会变成这样还不是你自己做？"
    w "……"
    show y 正常02 at ct with dissolve
    y "赶紧起来，吃点东西，下午我们还有事情要做。"
    w "我觉得整个猫生已经…呕…"
    narrator "突然有点想吐。"
    show y 恼火02 at ct with dissolve
    y "你给我滚到厕所再吐啊！！！"
    narrator "……"
    
    #【场景：医院门口】
    
    scene yy_前台 with dissolve:
        zoom .667
    
    narrator "转眼间，便到了下午。"
    narrator "说句实话，我居然会跟袁艳这个不共戴天的仇人一起出现在医院这里。"
    narrator "我是觉得有些不可思议的。"
    narrator "至于我们为什么会一起出现在这里呢？"
    narrator "这个还是有点点原因的。"
    show y 正常04 at ct with dissolve
    y "你要在外边等着吗？这破医院好像不让宠物进去。"
    w "……"
    w "谁是宠物了，你搞清楚一点啊！"
    w "我是猫啊！"
    show y 正常05 at ct with dissolve
    y "好吧好吧。"
    show y 正常04 at ct with dissolve
    y "不过这个地方好像有规定神圣的猫与狗不得入内，不知道你怎么看呢？"
    w "……"
    w "这样啊，那就没办法了呢。"
    narrator "谁让我是神圣的猫呢。"
    narrator "虽然觉得有什么不对，但是仔细想想又好像没什么不对。"
    w "不过你一个人没问题吗？"
    show y 正常01 at ct with dissolve
    y "难道多了你就能有什么作用吗？"
    narrator "袁艳带着笑容，向我反问道。"
    w "肯定会有…啊。"
    show y 笑容01 at ct with dissolve
    y "呵呵呵…"
    narrator "袁艳无奈地走进了医院。"
    narrator "看着身影消失在拐角处的袁艳，我不屑地啐了一口。"
    narrator "有什么了不起的。"
    w "你不让我去，我还非要去看看。"
    narrator "……"

    #【场景：病房】
    scene bf_黄昏 with dissolve:
        zoom .667
    
    narrator "废了我九牛二虎之力，才勉强从爬到了袁艳所在位置的楼层。"
    narrator "稍微感应一下就知道袁艳在哪个房间了。"
    narrator "话说这个大小姐的病房也太好进了吧。"
    narrator "从窗户下探头，总算是看清了房间里头的景象。"

    
    #【CG：商讨者】（暂定，可要可不要）

    
    narrator "袁艳带着笑容坐在林琴病床的那一边。"
    narrator "林琴则是带着莫名的疑惑同袁艳对视着。"
    narrator "两个人彼此注视着彼此，好像久别的情人一般。"
    narrator "看得我不由得打了一个哈欠。"
    show y 笑容01 at lt with dissolve
    y "刚刚多谢啦。"
    show y 笑容02 at lt with dissolve
    y "不是你的开口的话我估计就要被保安给赶出去了。"
    show l 普通02 at rt with dissolve
    l "用不着谢。"
    show l 普通01 at rt with dissolve
    l "上次玩忽职守的家伙已经被我辞了。"
    show y 正常05 at lt with dissolve
    y "……"
    show y 正常04 at lt with dissolve
    y "这也太严厉了吧——不过…好像是因为我的原因？"
    show l 普通03 at rt with dissolve
    l "不，跟你没关系。"
    show l 普通01 at rt with dissolve
    l "不如说我应该感谢你才对。"
    show l 普通02 at rt with dissolve
    l "如果换做图谋不轨的家伙，我的处境可能就有些危险了。"
    show l 普通01 at rt with dissolve
    l "这点我还是有自知之明的。"
    show y 正常01 at lt with dissolve
    y "……"
    show y 正常04 at lt with dissolve
    y "先声明一点啊！"
    show l 普通02 at rt with dissolve
    l "嗯？"
    show y 笑容01 at lt with dissolve
    y "我确实有点图谋不轨就是了。"
    w "……"
    narrator "我说你一本正经地在胡说八道什么鬼啊。"
    narrator "躲在窗户下的我心里抓狂了起来。"
    show l 普通02 at rt with dissolve
    l "看得出来。"
    narrator "林琴有史以来第一次有点笑意地看着袁艳。"
    show y 正常04 at lt with dissolve
    y "为什么你要躺在病床上呢？你得了什么病吗？"
    show l 普通01 at rt with dissolve
    l "你很想知道吗？"
    show y 正常05 at lt with dissolve
    y "嗯，很想。"
    show l 慌张02 at rt with dissolve
    l "我不是很想说，解释起来稍微有点儿头疼啊。"
    show y 正常02 at lt with dissolve
    y "只是稍微有点儿吗？"
    narrator "林琴点了点头。"
    show y 正常01 at lt with dissolve
    y "那有什么不可以说的呢？我的时间有很多。"
    show y 正常02 at lt with dissolve
    y "今天下午就陪着你好咯。"
    show l 普通02 at rt with dissolve
    l "呵呵…你不是说你时间没几天了吗？"
    show y 正常01 at lt with dissolve
    y "我要是说那是个玩笑你会信嘛？"
    show l 普通02 at rt with dissolve
    l "嗯，会信。"
    show l 不满02 at rt with dissolve
    l "不过我会让那个玩笑变成真的就是了。"
    show y 嘲讽01 at lt with dissolve
    y "哇，那听起来真可怕。"
    w "……"
    narrator "她们好像在进行什么恐怖的对话。"
    narrator "但是两个人却不约而同地带着和善的笑容。"
    show y 正常04 at lt with dissolve
    y "这个跟你要找的那个人是有关系的吗？"
    narrator "袁艳的话题一转，连我都有些措爪不及。"
    show l 惊异 at rt with dissolve
    l "额。"
    show l 普通02 at rt with dissolve
    l "真搞不懂你是真的知道还是猜的。"
    show l 普通01 at rt with dissolve
    l "你说的没错，确实有关系。"
    show y 正常05 at lt with dissolve
    y "那就有参考价值了。"
    show l 普通01 at rt with dissolve
    l "是吗？"
    show y 正常04 at lt with dissolve
    y "说给一个快要死掉的人听跟说给空气听应该没有什么差别吧。"
    show l 普通02 at rt with dissolve
    l "……"
    show l 普通03 at rt with dissolve
    l "你说的话总是没办法让人反驳呢。"
    show l 普通01 at rt with dissolve
    l "这让我很不舒服。"
    show l 普通02 at rt with dissolve
    l "甚至想在这里把你给弄坏掉。"
    show y 开心 at lt with dissolve
    y "讨厌啦，你在这种时候还开玩笑。"
    w "……"
    narrator "算我拜托你们两个了，你们两对话别那么瘆人行不行。"
    narrator "作为神圣的猫我鸡皮疙瘩都起了一身。"
    narrator "不过看到袁艳这么奋力地套取情报，我姑且还是稍微的放下了心来。"
    narrator "这家伙至少还是能分的清楚什么是正事什么是开玩笑的。"
    show l 普通02 at rt with dissolve
    l "不过可以给我一点点时间整理一下吗？"
    show y 正常04 at lt with dissolve
    y "……"
    show y 开心 at lt with dissolve
    y "可是我没有那么多时间呢。"
    narrator "对啊，我们哪里来的时间等你整理好啊。"
    show l 普通02 at rt with dissolve
    l "抱歉，你在我病房的话我还是有点不太想说。"
    show l 普通01 at rt with dissolve
    l "今天晚上我给你打电话吧。"
    show y 正常05 at lt with dissolve
    y "……"
    w "……"
    narrator "我和袁艳像是突然想起了什么一样，不约而同地愣了愣。"
    show y 正常04 at lt with dissolve
    y "这…这样啊。"
    show y 正常06 at lt with dissolve
    y "既然这样的话那就没办法了。"
    show y 正常04 at lt with dissolve
    y "我也没有别的事情。"
    show y 正常05 at lt with dissolve
    y "就是想问问，你什么时候开始谈恋爱呢？"
    show l 慌张01 at rt with dissolve
    l "额…"
    narrator "林琴陷入了沉默。"
    show y 嘲讽01 at lt with dissolve
    y "你别不说话呀，搞得我好像是在强迫你一样。"
    narrator "你本来就是在强迫她。"
    show y 开心 at lt with dissolve
    y "虽然我本来就是在强迫你啦。"
    show y 笑容01 at lt with dissolve
    y "不过你要是不这样做的话，我这边是很会很难受的。"
    show y 正常05 at lt with dissolve
    y "就是我现在也不太清楚难受是什么意思。"
    show l 普通02 at rt with dissolve
    l "这点事不用你来操心了。"
    show l 普通01 at rt with dissolve
    l "我自己会想办法的。"
    narrator "林琴像是有些不满一样别过头去。"
    narrator "但是就算是我也能看得出来。"
    narrator "这分明是不知道怎么回答，有些不好意思的时候才会有的表情啊。"
    show y 正常05 at lt with dissolve
    y "emmmm，既然如此，那我就等你晚上的电话咯。"
    show l 普通01 at rt with dissolve
    l "噢。"
    hide y with dissolve
    narrator "然后袁艳就离开了病房。"
    hide l with dissolve
    narrator "差不多我也该离开了。"
    w "……"
    narrator "我看着三层楼距离的地面，心里一时有点儿慌。"
    narrator "刚刚我是怎么爬上来的来着？"
    narrator "一时间我没了方寸。"
    narrator "不会吧，英明一世的我就这样被困在这种地方？"
    narrator "想到这里我又把头探进了病房，看了看坐在房间里头莫名发愣的林琴。"
    show l 普通02 at ct with dissolve
    l "……"
    w "……"
    show l 普通01 at ct with dissolve
    l "……"
    narrator "我觉得这是一个机会。"
    narrator "踮起我的四个爪子，为什么不趁着这个机会从正门溜出去呢？"
    narrator "我是谁，我可是神圣的猫啊。"
    narrator "让我从窗户跳出去未免也太没面子了吧。"
    narrator "于是，我偷偷摸摸的就从窗户外边地摸了进来。"
    narrator "所以说为什么要用偷偷摸摸这个词语啊。"
    narrator "我可是光明正大地进去的啊。"
    narrator "不过林琴这个丫头却还在发呆。"
    show l 普通01 at ct with dissolve
    l "……"
    w "……"
    narrator "嘛，她发呆也是好事对我来说。"
    narrator "然后——"
    show l 不满01 at ct with dissolve
    l "！！！"
    show l 不满02 at ct with dissolve
    l "啊啊啊啊啊啊！！！"
    narrator "突然间这个女孩就失控了。"
    narrator "就像是一头脱缰的野马…额，这个形容词好像有点不太对。"
    narrator "但是事实就是这样子。"
    narrator "就在我的面前她突然间就发起了疯。"
    narrator "开始撕扯东西、开始乱扔东西、开始…"
    w "现在的女孩子都喜欢乱发狂的吗？"
    show l 惊异 at ct with dissolve
    l "欸？"
    w "……"
    w "！！"
    narrator "林琴的手停在半空中。"
    narrator "我也因为林琴的疑惑声而僵住了身子。"
    narrator "一人一猫就在这个突然变得安静得有些恐怖的病房里头对视了起来。"
    narrator "这样的事情之前好像也发生过来着。"
    show l 惊异 at ct with dissolve
    l "……"
    w "喵…喵~"
    narrator "还没有等这个女孩有什么动作。"
    narrator "我就连忙叫了两声之后直接奔着门口跑了过去。"
    
    #【场景：医院门口】
    scene yy_前台 with dissolve:
        zoom .667
    
    doc "呀！！！有猫！"
    littlegirl "哇，有猫咪耶。"
    w "……"
    narrator "沿途遇到了不少的人类。"
    narrator "她们似乎对我的存在表现出非常惊奇的模样。"
    narrator "这让我感到非常的满足。"
    narrator "毕竟像我这样神圣的猫出现在这个世界上。"
    narrator "本身就是一件不可思议的事情。"
    narrator "会赞叹也是应该的。"
    narrator "虽然有很多不识货的家伙们想把我赶出去。"
    narrator "但是…有一句话刚刚好是那么说的嘛。"
    narrator "有光明的地方就会有黑暗存在，这本身就是不值得惊奇的事情嘛。"
    narrator "……"
    show y 恼火02 at ct with dissolve
    y "所以呢？"
    show y 恼火01 at ct with dissolve
    y "你跑到哪里去了？"
    show y 恼火02 at ct with dissolve
    y "难不成这个地方还有你的老相好？"
    w "……"
    w "话说你跟那个丫头说了些什么呢？"
    show y 恼火01 at ct with dissolve
    y "也没说什么"
    show y 恼火02 at ct with dissolve
    y "就是说了几句家常话，然后晚上在电话里头聊聊。"
    w "…"
    w "你们像是谈得很开心。"
    show y 正常02 at ct with dissolve
    y "各种意义上算是吧。"
    narrator "她无奈的笑容里头透出对现实的无奈。"
    narrator "看她的样子，我觉得问什么都是多余的。"
    show y 正常03 at ct with dissolve
    narrator "袁艳摇摇头，叹了口气，意思是再说“算了，我们去找下一位吧！”"

    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667
    
    show y 正常04 at ct with dissolve
    y "虽然我也没有把事情想得有多么的乐观啦。"
    show y 正常02 at ct with dissolve
    y "但是你这也太过分了吧。"
    show y 正常02 with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show c 斜视01 at rt with dissolve
    c "嗯？"
    show c 斜视02 at rt with dissolve
    c "欸？"
    show y 嘲笑 at lt with dissolve
    y "你倒是说句话啊。"
    show c 张嘴02 at rt with dissolve
    c "我..要说什么呢？"
    show y 嘲讽02 at lt with dissolve
    y "随便什么都好，你倒是说句话啊。"
    show c 侧视01 at rt with dissolve
    c "噢，可以帮我把剩下零食都吃掉吗？"
    show c 侧视02 at rt with dissolve
    c "这个是今天上午一个大姐姐给我的，我一个人吃不完。"
    narrator "程祎琳指着长椅旁边的一大袋零食，对着袁艳认真地说道。"
    show y 开心 at lt with dissolve
    y "啊啊啊啊啊，谢谢！"
    narrator "袁艳非常感谢地接过了程祎琳递过来的零食。"
    narrator "瞬间就倒戈了。"
    narrator "明明之前还在抱怨程祎琳怎么一点行动都没有。"
    narrator "在目睹了全过程的我看来。"
    narrator "毫不犹豫地在心底把袁艳给鄙视了好几百遍。"
    show y 开心 at lt with dissolve
    y "嘎嘣脆，烤肉味。"
    narrator "袁艳幸福地坐在长椅的一旁，丝毫没有客气的意思。"
    narrator "撕开一包薯片就吃了起来。"
    w "……"
    w "喵…"
    w "喵~喵！"
    narrator "为了提醒她想起自己的目的。"
    narrator "我不得不开始出卖自己的色相了。"
    narrator "公然在河边拼了命浪叫起来。"
    show y 恼火05 at lt with dissolve
    y "这只猫在这里嚎啥呢？"
    narrator "袁艳抓着一把薯片看着我。"
    narrator "还吃，你还给我吃。"
    narrator "我死死盯住了袁艳。"
    narrator "然后袁艳就愣住了。"
    show y 恼火02 at lt with dissolve
    y "…"
    narrator "然后她好像突然想起了什么一样看了看我。"
    narrator "又看了看手里的薯片。"
    narrator "又看了看我。"
    show y 正常04 at lt with dissolve
    y "我记起来了。"
    narrator "说着然后又塞了一把薯片到嘴里。"
    show y 正常05 at lt with dissolve
    y "我说程祎琳，你不是说要谈恋爱的吗？"
    show y 正常04 at lt with dissolve
    y "怎么还在这里吃零食？"
    show c 侧视02 at rt with dissolve
    c "嗯？"
    show c 侧视02 at rt with dissolve
    c "说的…也是呢。"
    show y 正常04 at lt with dissolve
    y "嗯。"
    show c 侧视02 at rt with dissolve
    c "但是…但是…"
    show y 正常02 at lt with dissolve
    y "但是什么？"
    show c 斜视02 at rt with dissolve
    c "但是所有的超市我都去找过了。"
    show c 斜视01 at rt with dissolve
    c "没有买到谈恋爱。"
    show y 正常06 at lt with dissolve
    y "……"
    w "……"
    show y 恼火04 at lt with dissolve
    y "你当谈恋爱是零食吗？"
    show c 惊讶02 at rt with dissolve
    c "欸…我…我开个玩笑嘛。"
    show y 正常02 at lt with dissolve
    y "真的假的，你好像真的把超市都跑遍了吧。"
    show c 侧视01 at rt with dissolve
    c "这个…嗯。"
    show y 正常04 at lt with dissolve
    y "哈…"
    show c 注视01 at rt with dissolve
    c "不过请放心！我超努力的！"
    show y 嘲讽02 at lt with dissolve
    y "呵呵呵…是吗？那还真是值得期待啊。"
    w "……"
    narrator "你这期待的语气怎么充满了绝望的味道啊。"
    show y 正常04 at lt with dissolve
    y "话说起来，你一点也不像吃货呢。"
    show c 侧视01 at rt with dissolve
    c "嗯？"
    narrator "程祎琳表现得很疑惑，似乎是并不理解袁艳嘴里说的话。"
    show y 正常05 at lt with dissolve
    y "我是说，你好像并不是什么都吃呀。"
    show c 侧视02 at rt with dissolve
    c "噢…"
    narrator "她点了点头。"
    narrator "也不知道她是理解了点头还是顺着心情随意点了点头。"
    show y 正常01 at lt with dissolve
    y "要不跟我讲讲你都喜欢吃些什么东西吧？"
    show c 斜视01 at rt with dissolve
    c "……"
    show c 斜视02 at rt with dissolve
    c "嗯…"
    show c 斜视01 at rt with dissolve
    c "好。"
    show c 侧视02 at rt with dissolve
    c "今天晚上…想到你家里去玩…"
    show c 侧视01 at rt with dissolve
    c "可以吗？"
    show y 正常04 at lt with dissolve
    y "额。"
    show y 笑容01 at lt with dissolve
    y "欢迎啊！当然欢迎啊。"
    show c 侧视01 at rt with dissolve
    c "唔嘿嘿嘿，那我回去准备一下。"
    show c 斜视01 at rt with dissolve
    c "晚上就去找你。"
    show y 嘲讽01 at lt with dissolve
    y "好…好的。"
    hide c with dissolve
    pause .5
    show y 笑容01 at ct with dissolve
    y "……"
    w "……"
    w "所以，你就让她这样走了？"
    narrator "我和袁艳一起注视着程祎琳一蹦一跳的背影。"
    show y 正常02 at ct with dissolve
    y "不然呢？"
    show y 正常01 at ct with dissolve
    y "我还能怎么办。"
    w "你到底是为了啥的啊。"
    show y 正常02 at ct with dissolve
    y "当然是为了让她们顺利谈恋爱啊。"
    w "话说真正的重点不是谈恋爱啊。"
    w "谈恋爱只是用来减轻你诅咒反噬所带来的疼痛啊。"
    show y 恼火05 at ct with dissolve
    y "我知道我知道的。"
    narrator "袁艳稍微有点儿不耐烦。"
    show y 正常04 at ct with dissolve
    y "你不就是想说让我好好判断一下究竟哪个家伙快崩溃了不是吗？"
    w "嗯…那你现在有什么结论吗？"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "嘛，说不太准，她们两个应该不是的才对。"
    show y 正常06 at ct with dissolve
    y "你看她们表现并不是那种快崩溃的人会有的。"
    w "喔，那也就是说你觉得是剩下的那个丫头了吗？"
    show y 正常04 at ct with dissolve
    y "有这个可能，但是还不能肯定。"
    w "你要不要去找找她？"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "额，我觉得就不用去找她了。"
    w "反正两个都见过了，你在多见一个也没关系吧。"
    #show y 
    y "不用啦。"
    w "不会吧，你就这么怕她？"
    narrator "我有些不满地嘟囔道。"
    show y 正常05 at ct with dissolve
    y "根本就不需要我们去找她。"
    show y 正常04 at ct with dissolve
    y "她已经找到我们了。"
    narrator "袁艳朝着某处看了过去。"
    narrator "我也顺着她的眼神跟了过去。"
    
    
    #【CG：隐藏的守望者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_swz = True
    scene cg_隐藏的守望者 with Dissolve(2)

    pause 1.0
    
    narrator "夏静静静地依着河边的栅栏，看着城市那边的天空。"
    narrator "好像在思考着什么又好像不是。"
    narrator "微风将她的长发轻轻地吹起，远远看起来仿佛她就是画里头的人物一样。"
    narrator "可惜我不是很会欣赏这样的东西。"
    narrator "虽然我不会欣赏。"
    narrator "但是我也能很明显看得出来。"
    narrator "这个女孩子分明就是在看着我们。"
    narrator "而且她还带着很愉快的笑容。"
    
    #【CG：结束】
    scene black with Dissolve(.7)
    
    scene river_白天 with dissolve:
        zoom .667
    
    show y 正常04 at ct with dissolve
    y "……"
    w "……"
    w "你作为她唯一的交易对象。"
    w "难道不应该上去打个招呼吗？"
    show y 恼火02 at ct with dissolve
    y "要你多嘴，死猫。"
    w "我这是在提醒你。"
    w "省得你在这里神神叨叨的。"
    show y 恼火01 at ct with dissolve
    y "一直在废话的是你好不好。"
    narrator "袁艳白了我一眼之后，头也不回的就朝着夏静走了过去。"
    narrator "我也只能悻悻地跟着她的脚步。"
    show y 恼火01 with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show x 假笑01 at rt with dissolve
    x "下午好，袁艳。"
    narrator "夏静虽然是在同袁艳打着招呼。"
    narrator "但是不知道为什么，她更多的时候却是在盯着我看。"
    show y 笑容01 at lt with dissolve
    y "嗯，下午好呀。"
    show y 正常04 at lt with dissolve
    y "……"
    show y 笑容01 at lt with dissolve
    y "你好像对我家的死猫很感兴趣。"
    show y 开心 at lt with dissolve
    y "要带回去炖汤补补身子吗？"
    w "……"
    narrator "我差点没亮出爪子朝着丫头直接撕过去。"
    narrator "这个丫头的嘴巴真的是有一股子狠劲。"
    narrator "连我这样高素质的猫都能被她气成这样。"
    narrator "换做别的猫估计能被她气个半死。"
    show x 怜悯01 at rt with dissolve
    x "不是很喜欢喝猫汤呢，不过要是你手艺不错的话。"
    show x 怜悯02 at rt with dissolve
    x "下次去你家你帮我做一份尝尝吧。"
    show y 开心 at lt with dissolve
    y "这主意听起来不错。"
    narrator "你们别跟唠家常一样讨论怎么吃我的事情啊。"
    show y 笑容01 at lt with dissolve
    y "话说你在这你做什么呢？"
    show x 假笑02 at rt with dissolve
    x "嗯，是呢。"
    show x 假笑01 at rt with dissolve
    x "当然是收集你想要的情报呀。"
    show y 正常04 at lt with dissolve
    y "站在这里就可以吗？"
    narrator "夏静眯了眯眼睛笑着，好像在说‘没错就是这样’。"
    show y 正常05 at lt with dissolve
    y "真是搞不懂你们啊。"
    show y 正常04 at lt with dissolve
    y "尤其是搞不懂你。"
    show x 假笑02 at rt with dissolve
    x "所以，你找我有什么事情呢？"
    show y 正常04 at lt with dissolve
    y "这样问不太好。"
    show x 普通02 at rt with dissolve
    x "噢？"
    show y 正常04 at lt with dissolve
    y "换个问法吧。"
    show y 正常05 at lt with dissolve
    y "你在这里得到了什么情报呢？"
    show y 笑容01 at lt with dissolve
    y "可以跟我分享一下吗？"
    show x 假笑01 at rt with dissolve
    x "呵呵呵，原来如此。"
    show x 假笑02 at rt with dissolve
    x "反问我吗？"
    show y 恼火04 at lt with dissolve
    y "不可以吗？我们可是进行了交易不是吗？"
    show x 假笑01 at rt with dissolve
    x "的确是这样子呢。"
    show x 假笑02 at rt with dissolve
    x "不过就这样告诉你有点稍微的…不太甘心呢。"
    show x 假笑02 at rt with dissolve
    x "今天晚上你来找我吧。"
    show y 正常05 at lt with dissolve
    y "……"
    w "噗…"
    show x 考虑01 at rt with dissolve
    x "怎么了？"
    show x 考虑02 at rt with dissolve
    x "你看上去很为难啊。"
    show y 正常05 at lt with dissolve
    y "不…不没事没事，晚上来找你吗？"
    show y 正常04 at lt with dissolve
    y "什么时候呢？在什么地方呢？"
    show x 假笑02 at rt with dissolve
    x "这个嘛，虽然想说只要你出了门就可以找到我。"
    show x 假笑03 at rt with dissolve
    x "不过还是在这里见面吧。"
    show y 正常04 at lt with dissolve
    y "…"
    show y 正常05 at lt with dissolve
    y "好！没问题，我一定到。"
    show x 假笑01 at rt with dissolve
    x "那我就在这里等着你啦。"
    hide x with dissolve
    narrator "说完，夏静便松开了抓住栏杆的手，离开了这个地方。"
    show y 正常05 at lt with dissolve
    y "……"
    w "……"
    w "噗…哈哈哈哈哈！"
    w "哈哈哈哈！"
    show y 恼火02 at ct with dissolve
    y "笑什么笑，笑死你啊！"
    w "都凑到晚上了。"
    w "今天晚上真的是热闹啊。"
    show y 恼火04 at ct with dissolve
    y "我能怎么办，我也很绝望啊。"
    w "哈哈哈。"
    w "哈哈哈…嗝。"
    narrator "袁艳毫不留情地照着我的屁股就是一脚。"
    narrator "疼得我直接炸了毛。"
    w "你干什么你！"
    show y 嘲讽02 at ct with dissolve
    y "啊，抱歉。"
    show y 嘲讽03 at ct with dissolve
    y "我不小心脚滑了一下。"
    w "谁信啊！！！！"
    narrator "我大声叫了出来。"
    narrator "好在周围根本就没有人。"
    narrator "于是，在彼此瞪着彼此的时间里，我们一起回去了。"


    #【场景：客厅】（晚上）
    scene kt_夜晚 with dissolve:
        zoom .667
    
    narrator "时间一点一点地过去，客厅逐渐披上了一层夕阳的外衣。"
    w "我说，就快到晚上了。"
    w "你想好该怎么办了没有？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "你能不能别站着说话不腰疼。"
    w "我现在是蹲着的好不好。 "
    show y 恼火05 at ct with dissolve
    y "哼。"
    narrator "我实在是搞不懂这个丫头。"
    narrator "她总是会说一些跟实际情况不符的事情。"
    narrator "这让我不由得有些担忧。"
    narrator "等最后那几天她的抉择不会掉链子跟实际情况也不符吧。"
    narrator "不管怎样应该也不会吧。"
    show y 正常04 at ct with dissolve
    y "…"
    show y 恼火05 at ct with dissolve
    y "我怎么总觉得你好像是在想什么不好的事情。"
    w "哈？为什么这么说？"
    show y 正常05 at ct with dissolve
    y "直觉吧。"
    w "你这直觉也太烂了吧。"
    w "我可是什么都没想的啊。"
    show y 恼火04 at ct with dissolve
    y "嘁。"
    show y 恼火05 at ct with dissolve
    y "看你得瑟的。"
    narrator "然后客厅就安静了下来。"
    show y 正常04 at ct with dissolve
    y "……"
    w "……"
    show y 正常05 at ct with dissolve
    y "突然不知道该怎么办了。"
    w "不会吧？这么惨？"
    show y 正常05 at ct with dissolve
    y "晚点那个林大小姐会给我打电话。"
    w "打电话？"
    show y 正常04 at ct with dissolve
    y "我不知道什么时候那个程丫头什么时候到我这里来。"
    show y 正常03 at ct with dissolve
    y "另外还有那个夏静让我去找她。"
    show y 正常04 at ct with dissolve
    y "这不是造孽么？"
    w "啥意思？"
    show y 嘲讽01 at ct with dissolve
    y "就是能凑一桌麻将了。"
    w "麻将是啥？"
    show y 嘲笑 at ct with dissolve
    y "……"
    narrator "我感觉我们之间的文化代沟可能有一点点大。"
    narrator "看着袁艳那副表情，我猜她的想法应该跟我一样。"
    narrator "客厅再一次安静下来。"
    narrator "人跟猫彼此对视，彼此都找不到好的语言来打破这份寂静。"
    w "我说丫头啊…"
    show y 正常04 at ct with dissolve
    y "干啥？"
    w "我们要不吃点什么东西？"
    show y 正常04 at ct with dissolve
    y "喔！"
    narrator "袁艳像是很惊艳地看着我。"
    show y 笑容01 at ct with dissolve
    y "不错嘛，头一回看你想到个好的主意。"
    show y 开心 at ct with dissolve
    y "嗯…嗯嗯嗯，对对对。"
    w "……"
    w "你知道我厉害就好了。"
    narrator "虽然不知道发生了什么。"
    narrator "但是看到因为我一句话而突然变得很忙碌的袁艳。"
    narrator "这种感觉是怎么回事呢…"
    narrator "成就感瞬间就爆棚了。"
    narrator "想不到啊想不到啊。"
    narrator "不对…"
    narrator "我是这么神圣的猫，怎么能因为这点小事就激动了呢。"
    w "冷静冷静…"
    show y 正常04 at ct with dissolve
    y "你在嘀咕啥？"
    w "没…没事。"
    show y 正常05 at ct with dissolve
    y "…"
    show y 正常04 at ct with dissolve
    y "你有没有想吃的？"
    w "我也没有那么饿，就不吃了啦。"
    narrator "想到袁艳之前给我做的那些东西。"
    narrator "反胃感一阵阵地传了上来。"
    show y 正常02 at ct with dissolve
    y "上午的时候我路过宠物店的时候顺便买了点猫薄荷回来。"
    w "……"
    show y 正常01 at ct with dissolve
    y "你跑过来干啥？"
    w "还能干啥？赶紧开饭啊！"
    show y 正常02 at ct with dissolve
    y "你把猫薄荷当饭吃啊。"
    w "管那么多干什么，吃啊。"
    show y 恼火05 at ct with dissolve
    y "你着急啥啊？"
    show y 恼火04 at ct with dissolve
    y "我外卖还没到，等会先。"
    w "等不及了啦！！！"
    w "我要！我要嘛！！！"
    narrator "这个时候的我已经完全失去了对自己所有的控制。"
    narrator "什么东西都被我一股脑抛在了脑后。"
    narrator "现在整个脑壳里头就只有猫薄荷这样的东西。"
    narrator "啊，好想尝一尝。"
    show y 恼火02 at ct with dissolve
    y "额，你好恶心啊！"
    w "我不管我不管啦。"
    w "我就想吃嘛！"
    narrator "袁艳倒吸了一口凉气，浑身发抖。"
    show y 嘲讽01 at ct with dissolve
    y "行行行，你赶紧收起你这幅模样。"
    show y 嘲笑 at ct with dissolve
    y "冷死个人了。"
    w "……"
    narrator "我看着嫌弃似的袁艳拿出了一袋子在我看来就是‘奇迹’的东西。"
    narrator "在她撕开包装袋的一瞬间，我就扑了过去。"
    w "喵！！！"
    show y 无措 at ct with dissolve
    y "哎呀！"
    show y 无措 at ct with dissolve
    y "……"
    show y 无措 at ct with dissolve
    y "就没见过这么野的猫！"
    narrator "可是这个时候的我已经没有管那么多了。"
    narrator "抱着一袋子猫薄荷不断地享受着属于自己的幸福时光。"
    w "啊…喵~~"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "之后的事情我就稍微有点不太在意了。"
    narrator "话说袁艳到底在干什么来着…"
    narrator "……"
    narrator "回过神的时候，耳边回响起来的是一阵阵奇怪的铃声。"
    narrator "好像在什么地方听到过。"
    narrator "还有敲门声。"
    narrator "映入我眼睛里头的，则是一脸沉思地坐在座位边上端着一杯冒着热气的水的袁艳。"
    w "你在干啥？"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳朝着我看了一眼，然后有些颤抖抬起杯子。"
    narrator "抿了一口杯子里头的水。"
    show y 恼火05 at ct with dissolve
    y "我说…死猫啊。"
    show y 正常04 at ct with dissolve
    y "你听说过选择综合症吗？"
    w "那是啥？"
    show y 正常04 at ct with dissolve
    y "这个世界上就是有些人在关键的时候啊，没办法做出选择。"
    show y 正常02 at ct with dissolve
    y "然后就会错失许许多多的机会。"
    w " ……"
    w "说的好，但是这跟你现在有什么关系吗？"
    narrator "袁艳又朝着我看了一眼。"
    narrator "莫名其妙的这人，我不由得这么想到。"
    show y 正常04 at ct with dissolve
    y "我说，要不这次你帮我选择好了。"
    w "选择啥？"
    show y 正常05 at ct with dissolve
    y "先去干啥会比较好呢？"
    w "……"
    narrator "如果没记错的话，今天晚上袁艳应该有三个活动。"
    narrator "理论上来讲，是有规避凑一块的情况发生的。"
    narrator "但是实际上事情还是凑到一块去了。"
    w "我说了你就一定会那样做吗？"
    show y 正常05 at ct with dissolve
    y "这回我听你的。"
    w "……"
    narrator "我看了看桌上一直在响着的被袁艳称之为手机的盒子。"
    narrator "又瞧了瞧门外响起的敲门声。"
    narrator "好像还有一个叫做夏静的丫头约了她。"
    narrator "要我说的话…"


    menu:
        "当然是"
        #【最关键选项】
        "林琴":
            jump c1_c4_l
        
        "夏静":
            jump c1_c4_x
            
        "程祎琳":
            jump c1_c4_c


label c1_c4_l:

    $c1_c4_l_select = True

    narrator "当然是林琴咯，她发起疯来确实让人觉得有点恐怖啊。"
    narrator "要问我谁优先的话那肯定是林琴的事情要优先。"
    narrator "我看着袁艳，郑重地说。"
    w "我觉得最好是林琴。"
    narrator "虽然那个叫程祎琳的那个女孩子就在门外，但是我还是要这么说。"
    
    jump c1_5
    

label c1_c4_x:

    $c1_c4_x_select = True

    narrator "夏静，一定是夏静！"
    narrator "这个女孩子连我都觉得有点恐怖。"
    narrator "总感觉她什么都能够看穿。"
    narrator "这不得不让人不在意啊。"
    w "还用说嘛，你先去见夏静啊。"
    narrator "虽然那个叫程祎琳的那个女孩子就在门外，但是我还是要这么说。"
    
    jump c1_5
    

label c1_c4_c:
    
    $c1_c4_c_select = True

    narrator "我说你过分了啊。"
    narrator "程祎琳就在门外你就不能先见见门外的那个丫头？"
    w "当然先见门外那个啊。"
    w "程祎琳就在门外你还要去见谁啊。"
    
    jump c1_5
    

label c1_5:
    $_dismiss_pause = False

    show y 正常04 at ct
    y "你说得很有道理。"
    show y 正常05 at ct with dissolve
    y "我决定按你说的办。"
    narrator "然后袁艳就拿起手机，接通了电话。"
    narrator "我还没听到她开口说话，她就起身离开了座位。"
    narrator "然后走到了门边，打开了门。"
    show y 正常05 with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show c 侧视01 at rt with dissolve
    c "唔？"
    show y 正常04 at lt with dissolve
    y "进来吧。"
    narrator "然后袁艳自己就又回到了位置上。"
    show y 正常05 at lt with dissolve
    y "记得把门关上。"
    show c 侧视02 at rt with dissolve
    c "好~~~"
    show y 正常05 at lt with dissolve
    y "喂喂，嗯嗯，是我，我是袁艳。"
    narrator "手机那一头传来了声音。"

    #"电话（人物暗色）"
    show y 正常05 d at lt
    show c 侧视02 d at rt

    show l 普通08 at ct with dissolve
    l "…"
    show l 普通07 at ct with dissolve
    l "你那边好像有点儿吵。"
    narrator "袁艳看了一眼刚刚关门之后来到客厅的程祎琳。"
    narrator "又看了一眼正在舔爪子的我。"
    show y 正常04 at lt with dissolve
    y "没事…我能听到你说话的声音。"
    show l 普通08 at ct with dissolve
    l "是吗。"
    show l 普通09 at ct with dissolve
    l "嘛，无所谓了。"
    show c 张嘴02 at rt with dissolve
    c "唔喵唔喵~"
    w "喵~喵！"
    show c 张嘴02 d at rt with dissolve
    show l 普通07 at ct with dissolve
    l "我身体并没有什么问题，我之所以住医院是老头强行给安排的。"
    show y 正常05 at lt with dissolve
    y "老头…老头的意思难不成是你的长辈？"
    show l 普通09 at ct with dissolve
    l "……"
    narrator "电话那边并没有肯定也没有否认。"
    show c 惊讶01 at rt with dissolve
    c "喔，小猫。"
    w "喵…"
    narrator "这丫头怎么逗起我来了。"
    narrator "我得回敬她，让她知道一下到底是谁逗谁。"
    show c 惊讶01 d at rt with dissolve
    show l 普通07 at ct with dissolve
    l "你们那边还挺吵的嘛。"
    show y 正常01 at lt with dissolve
    y "……"
    narrator "袁艳看了一眼乖巧坐在位置上的程祎琳，又一次起身。"
    narrator "然后不一会儿就从冰箱里头翻了一大袋的…像是零食一样的东西。"
    narrator "轻轻地放在了桌上。"
    narrator "程祎琳则是立马眼睛一亮。"
    show c 张嘴01 at rt with dissolve
    c "啊，谢谢！"
    w "嘁。"
    narrator "我却不屑地发出了声音。"
    show c 张嘴02 d at rt with dissolve
    show y 正常02 at lt with dissolve
    y "也有你的。"
    narrator "袁艳随手就丢了一个‘团团’过来。"
    narrator "你以为我 是什么啊！！！"
    w "喵！"
    narrator "在接过这个东西的一瞬间。"
    narrator "我所有的心情瞬间化作了的惊喜。"
    narrator "紧紧抓住手中的幸福象征，绝对不允许任何人抢走它。"
    show y 正常04 at lt with dissolve
    y "……"
    show y 正常05 at lt with dissolve
    y "我们继续吧。"
    show l 普通08 at ct with dissolve
    l "差不多就是长辈的意思吧，比我二三十来岁的人。"
    show y 正常02 at lt with dissolve
    y "也就你能这样子称呼长辈了。"
    show l 普通07 at ct with dissolve
    l "总而言之，我是被刻意安排在医院里头的。"
    show l 普通09 at ct with dissolve
    l "并不是我本身希望住在这里。"
    show y 正常02 at lt with dissolve
    y "……"
    show y 正常04 at lt with dissolve
    y "那你长辈住医院的原因总是有的吧。"
    show l 普通07 at ct with dissolve
    l "你问题还真多。"
    show y 正常05 at lt with dissolve
    y "你以为我很想问啊。"
    show l 普通09 at ct with dissolve
    l "那不问不就行了吗？"
    show y 正常06 at lt with dissolve
    y "不行的，不了解你我怎么帮你呢。"
    show l 普通08 at ct with dissolve
    l "从来没有听说过这样的了解方法。"
    show y 正常03 at lt with dissolve
    y "我也从来没有听说过没病住重症科的大小姐。"
    show l 普通08 at ct with dissolve
    l "……"
    show y 正常04 at lt with dissolve
    y "在怎么说都觉得让人很在意啊。"
    show y 正常05 at lt with dissolve
    y "再说我都要死的人了，这点信息透露一下不行嘛？"
    show l 不满08 at ct with dissolve
    l "嘁。"
    narrator "电话的那头传来林琴有些不爽的声音。"
    show l 普通09 at ct with dissolve
    l "主要是跟我在一起的人容易受点伤。"
    show y 正常04 at lt with dissolve
    y "容易受伤？"
    show l 普通08 at ct with dissolve
    l "最后一个跟我在一块的那个侍从听说最近才出院。"
    show l 普通07 at ct with dissolve
    l "听说还要来报复我来着。"
    show l 普通09 at ct with dissolve
    l "不过后来就没怎么听说过她的消息了。"
    show y 嘲讽01 at lt with dissolve
    y "你别一本正经地说这么恐怖的事情好不好。"
    show l 普通08 at ct with dissolve
    l "恐怖？不是很懂你在说什么。"
    show l 普通07 at ct with dissolve
    l "不过我说的是事实就是了。"
    show y 正常02 at lt with dissolve
    y "……"
    show y 正常02 at lt with dissolve
    y "你说跟你在一起的人容易受伤能具体说说吗？"
    show l 普通07 at ct with dissolve
    l "额。"
    narrator "电话里头，林琴陷入了沉默。"
    narrator "但是很快她的声音又重新响起。"
    show l 慌张08 at ct with dissolve
    l "姑且就说一下吧。"
    show l 慌张07 at ct with dissolve
    l "怎么说呢…"
    show l 慌张09 at ct with dissolve
    l "就是我有个有点不太好的习惯。"
    show y 正常02 at lt with dissolve
    y "啥？你咋支支吾吾的。"
    show l 慌张07 at ct with dissolve
    l "就是…额，用医生的话来说，这个叫狂躁抑郁症。"
    show y 正常05 at lt with dissolve
    y "抑郁症我听说过，狂暴症我也听说过。"
    show y 正常04 at lt with dissolve
    y "但是这个狂暴抑郁症是个什么玩意啊？"
    show l 普通09 at ct with dissolve
    l "我也不清楚。"
    show l 普通07 at ct with dissolve
    l "换医生的说法就是平常的时候我很平常。"
    show y 正常04 at lt with dissolve
    y "然后发病的时候就突然发疯？喜欢乱砸东西？"
    show l 惊异03 at ct with dissolve
    l "……"
    show l 惊异03 at ct with dissolve
    l "怎么说的你好像知道一样。"
    show y 嘲讽03 at lt with dissolve
    y "我…"
    show y 嘲讽03 at lt with dissolve
    y "我猜的。"
    show l 普通08 at ct with dissolve
    l "猜倒是猜得很准。"
    show l 普通07 at ct with dissolve
    l "不过我必须纠正的事情就是我没病！"
    show y 嘲讽02 at lt with dissolve
    y "是是是，你说了算。"
    show l 普通07 at ct with dissolve
    l "医生说我这个症状是心理症状。"
    show l 普通08 at ct with dissolve
    l "这点我很赞同。"
    show l 普通07 at ct with dissolve
    l "但是这个症状并不是我的。"
    show y 无措 at lt with dissolve
    y "等…等一下！"
    show l 普通07 at ct with dissolve
    l "怎么了？"
    show y 无措 at lt with dissolve
    y "这..这么快就到核心的地方吗？"
    show l 普通08 at ct with dissolve
    l "啊？都这时候了你还在说什么。"
    show y 正常05 at lt with dissolve
    y "没…没事，你继续你继续。"
    show l 普通07 at ct with dissolve
    l "我是觉得这个习惯好像根本不是我自己的一样。"
    show y 正常02 at lt with dissolve
    y "额…"
    show l 普通08 at ct with dissolve
    l "怎么？你好像有什么问题想问的。"
    show y 正常01 at lt with dissolve
    y "你的意思是你在发病的时候并不是你自己控制你自己？"
    show l 慌张08 at ct with dissolve
    l "……"
    show y 笑容01 at lt with dissolve
    y "不会猜中了吧？"
    narrator "袁艳的样子看起来非常地惊讶。"
    show l 慌张07 at ct with dissolve
    l "这怎么说都有些不太可能。"
    show l 慌张08 at ct with dissolve
    l "我只是感觉不像是我自己在控制自己一样。"
    show l 慌张07 at ct with dissolve
    l "换句话来说就是没有真实感吧。"
    show l 慌张09 at ct with dissolve
    l "但是实际上还是我本人。"
    show y 正常04 at lt with dissolve
    y "欸？真的假的？"
    show l 普通07 at ct with dissolve
    l "我没必要跟你一样故弄玄虚，你明白我的意思吧。"
    show y 正常05 at lt with dissolve
    y "哇，不是吧，居然扯到我身上来了，先申明啊，我可从来没有故弄玄虚过啊。"
    show l 不满08 at ct with dissolve
    l "哼，这谁知道呢。"
    show y 正常02 at lt with dissolve
    y "……"
    narrator "房间再一次陷入了安静。"
    narrator "我抬起了头。"
    narrator "袁艳在那儿拿着手机，虽然没有说话。"
    narrator "但是皱着的眉头让我知道可能情况似乎…很严峻？"
    w "……"
    narrator "在享受一下就去帮她，就这么愉快地决定了。"
    show l 普通09 at ct with dissolve
    l "今晚就到此结束吧。"
    y "噢，好。"
    hide l with dissolve
    pause 1.0
    narrator "许久之后，袁艳便放下了手中的电话。"
    show y 正常02 at lt with dissolve
    y "唉。"
    narrator "袁艳半垂着眼睛又看了我。"
    show y 正常03 at lt with dissolve
    y "唉。"
    narrator "连续地叹了两口气。"
    narrator "我则是抬起头疑惑地看着袁艳。"
    show y 正常04 at lt with dissolve
    y "喂，阿琳啊。"
    show c 侧视01 at rt with dissolve
    c "……"
    narrator "程祎琳似乎对这个简称并不是很感冒。"
    show y 正常04 at lt with dissolve
    y "……"
    show y 正常02 at lt with dissolve
    y "程祎琳？"
    narrator "程祎琳咬着牛奶的吸管，从一堆零食里头抬头瞪大眼睛看着袁艳。"
    show y 正常05 at lt with dissolve
    y "我想出去一会儿，给你买点吃的可以吗？"
    show y 正常04 at lt with dissolve
    y "你就在这里等我。"
    show c 侧视02 at rt with dissolve
    c "唔…"
    show c 斜视01 at rt with dissolve
    c "好吧。"
    w "……"
    narrator "老实说只是这样看我是真的完全都搞不懂她们之间的对话。"
    narrator "不过袁艳去冰箱里头又拿出一袋子水果放在桌上的时候我就明白了。"
    narrator "这是一场交易。"
    narrator "而且是一场很简单易懂的交易。"
    show c 张嘴01 at rt with dissolve
    c "哇，谢谢！"
    narrator "程祎琳很开心地接过去。"
    show c 惊讶01 at rt with dissolve
    c "路上小心。"
    show y 正常02 at lt with dissolve
    y "……"
    hide c with dissolve
    narrator "袁艳则是无奈地扶了扶额头，叹了口气。"
    scene room_夜晚 with dissolve:
        zoom .667
    narrator "然后去房间准备了一下。"
    narrator "看样子是打算离开这里去见夏静那个丫头了。"
    narrator "舔了舔薄荷，然后又看着沉浸在自己世界里头的程祎琳。"
    narrator "心一横。"
    narrator "是的，我打算跟上袁艳，跟她一起去见那个丫头。"
    show y 正常02 at ct with dissolve
    y "你跟过来干啥？"
    narrator "门口的袁艳看着我。"
    w "呜喵唔喵！"
    show y 正常01 at ct with dissolve
    y "叼着薄荷你想说啥。"
    w "唔喵…"
    narrator "跟过去是对的，但是也没说一定不能带自己想带的东西啊。"
    show y 正常04 at ct with dissolve
    y "唉，算了算了，跟过来吧。"
    narrator "然后我们就一起暂时离开了家。"
    
    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    #门外背景
    scene door_夜晚 with dissolve:
        zoom .667
    
    
    narrator "到了门外，我把猫薄荷放在了地上。"
    w "你把那丫头一个人留在家里没问题吗？"
    show y 正常05 at ct with dissolve
    y "她啊，估计没啥问题吧，反正门我都锁了。"
    w "……"
    narrator "我刚想抬头去看袁艳，但是却发现她理都不理我早就走远了。"
    narrator "无奈我只能连忙叼起薄荷跟了上去。"
    show y 正常05 with dissolve:
        linear .3 xpos 0.0 xanchor 0.0
    show x 假笑01 at rt with dissolve
    x "哈喽~"
    narrator "就在我们刚走没有多久。"
    narrator "夏静就出现在我们的面前。"
    narrator "准确地说应该是袁艳的面前，伸出手似乎想要吓袁艳一跳。"
    show y 正常02 at lt with dissolve
    y "……"
    narrator "袁艳迟疑了一秒钟，然后非常夸张地往后一跳。"
    show y 无措 at lt with dissolve
    y "哇！！！吓死人啦！！！"
    w "……"
    show x 惊讶01 at rt with dissolve
    x "……"
    narrator "我不由得用爪子挡住眼睛，这个场面尴尬得有点刺眼。"
    show x 怜悯02 at rt with dissolve
    x "你看上去很惊讶呢。"
    show y 无措 at lt with dissolve
    y "嗯…嗯，相当惊讶啊，你为什么会出现在这里呢？"
    show x 普通02 at rt with dissolve
    x "因为我知道程祎琳那丫头在你家里。"
    show y 笑容01 at lt with dissolve
    y "喔噢，原来如此。"
    show x 普通01 at rt with dissolve
    x "对了，我这里有一点东西想要送给你。"
    show y 无措 at lt with dissolve
    y "哈？送给我？"
    show x 假笑02 at rt with dissolve
    x "嗯。"
    narrator "夏静在我的注视下递了明显就是零食的一个袋子给了袁艳。"
    narrator "袁艳则是一脸狐疑地接过了袋子。"
    narrator "有点儿搞不懂夏静在干什么的样子。"
    show y 正常04 at lt with dissolve
    y "你想干啥？"
    show y 正常05 at lt with dissolve
    y "这个时候请我吃零食有什么意义吗？"
    show x 普通01 at rt with dissolve
    x "并没有什么意义。"
    show y 正常04 at lt with dissolve
    y "……"
    show x 怜悯02 at rt with dissolve
    x "但是我也没有说这个是给你吃的呀。"
    show y 正常05 at lt with dissolve
    y "额…"
    show x 假笑01 at rt with dissolve
    x "把这个送给程祎琳当礼物吧，就当是你请她的。"
    show x 假笑02 at rt with dissolve
    x "我要说的就只有这么多。"
    narrator "她没有多说别的什么东西就背对着我们离开了。"
    show y 正常02 at lt with dissolve
    y "……"

    w "她把你叫过来到底是干什么的？"
    narrator "袁艳看了看手中的零食却长长地叹了一口气。"
    show y 正常04 at lt with dissolve
    y "不知道。"
    show y 嘲讽02 at lt with dissolve
    y "就是总觉得不会是什么好事。"
    w "我跟你的感觉也差不多。"
    narrator "我和袁艳相互对视了一眼。"
    show y 正常01 at lt with dissolve
    y "唉，回去吧。"
    w "哦…"
    narrator "一路上没有多余的话语。"

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
    
    show c 张嘴02 at rt with dissolve
    c "唔…"
    show c 张嘴01 at rt with dissolve
    c "……"
    w "喵~"
    show y 正常02 at lt with dissolve
    y "你就一直坐在这里吃吗。"
    show c 斜视01 at rt with dissolve
    c "嗯。"
    narrator "程祎琳咬吸管然后看着袁艳点头。"
    narrator "袁艳无奈地把夏静送的一袋零食放在了桌上。"
    narrator "程祎琳则是很惊喜地打开了袋子。"
    narrator "但是在打开袋子的一瞬间，她的表情就像是泄气的皮球一样变化了起来。"
    show y 正常01 at lt with dissolve
    y "……"
    show c 侧视01 at rt with dissolve
    c "唔……"
    show y 正常04 at lt with dissolve
    y "你看上去不是很开心啊，不喜欢吃吗？"
    show y 正常05 at lt with dissolve
    y "里面都是一些薯片啊、还有盐焗包装食品。"
    show y 正常04 at lt with dissolve
    y "虽然不是很推荐，但是就吃这个方面来说我觉得还是很不错的。"
    show y 正常06 at lt with dissolve
    y "尤其是搭配汽水来吃是最好吃的。"
    narrator "不是很懂这个丫头在一本正经地在说些什么，感觉很厉害的样子。"
    narrator "不过程祎琳并不是很给面子。"
    narrator "只见她摇了摇头。"
    show y 正常04 at lt with dissolve
    y "你也没跟我说你不喜欢吃些什么，所以一不小心买错了。"
    show y 正常05 at lt with dissolve
    y "没想到你不是很喜欢吃薯片。"
    show c 恶心01 at rt with dissolve
    c "也不是这样…"
    show y 正常05 at lt with dissolve
    y "啊？"
    narrator "程祎琳像是想到了什么一样从袋子里头拿出了一袋薯片。"
    show c 侧视01 at rt with dissolve
    c "我很喜欢吃薯片！"
    show y 正常04 at lt with dissolve
    y "额…"
    show c 侧视02 at rt with dissolve
    c "就是…就是。"
    narrator "说道这里程祎琳扭扭捏捏了起来。"
    show y 正常05 at lt with dissolve
    y "就是什么？"
    show c 斜视03 at rt with dissolve
    c "就是有些口味有点点吃不下去。"
    narrator "程祎琳拿着薯片看了两眼有点儿念念不舍地放回了原位。"
    narrator "袁艳则是有些无语地拿起了刚刚被程祎琳放下的薯片。"
    narrator "我一跃而起调到了袁艳身旁的桌子上。"
    narrator "仔细看看的话，总觉得这包薯片有点点熟悉。"
    
    
    #【CG：暴食者】（）（之前的cg）
    
    narrator "回忆突然在我的脑海里头一闪而过。"
    narrator "于是我看向了袁艳，袁艳这时也像是想到了什么一样看着我。"
    narrator "确认过眼神以后我明白了。"
    narrator "我们两个应该是想到一块去了。"
    show y 正常04 at lt with dissolve
    y "你不太喜欢吃烤肉味道东西呢。"
    show c 侧视02 at rt with dissolve
    c "也不能这么说…"
    show y 正常05 at lt with dissolve
    y "……"
    show y 正常04 at lt with dissolve
    y "那到底要怎么说啊?"
    show c 斜视02 at rt with dissolve
    c "因为我是个素食主义者啦。"
    show c 侧视01 at rt with dissolve
    c "所以不是很喜欢有肉脂的零食。"
    show y 正常02 at lt with dissolve
    y "素食主义者？"
    show y 正常01 at lt with dissolve
    y "这还真没看出来。"
    show c 斜视02 at rt with dissolve
    c "是真的。"
    show c 斜视01 at rt with dissolve
    c "不能吃带肉脂的东西，一点点都不行。"
    show y 正常04 at lt with dissolve
    y "……"
    narrator "关于这个，我和袁艳当然是相信的。"
    
    
    #【CG：暴食者】
    
    #【场景：房间】
    #scene room_夜晚 with dissolve:
    #    zoom .667
    
    show y 正常05 at lt with dissolve
    y "好吧。"
    show y 正常04 at lt with dissolve
    y "不能吃就算了"
    show y 笑容01 at lt with dissolve
    y "反正我能吃就行。"
    w "……"
    narrator "你能不能稍微掩饰一下你这副丑恶嘴脸。"
    show y 笑容02 at lt with dissolve
    y "话说起来，你到底是过来干啥的啊。"
    show y 笑容01 at lt with dissolve
    y "白天我只是问问你喜欢吃些什么啊。"
    show c 张嘴02 at rt with dissolve
    c "唔…"
    narrator "程祎琳吃得差不多了以后摸了摸肚子。"
    narrator "然后咬着酸奶的吸管说着。"
    show c 张嘴01 at rt with dissolve
    c "我只是想过来玩而已啊。"
    show c 侧视01 at rt with dissolve
    c "而且你这边的零食都很好吃。"
    show y 正常02 at lt with dissolve
    y "……"
    narrator "袁艳扶了扶额头，无奈地叹了口气。"
    narrator "……"

    
    #【场景：黑屏】
    #【场景：客厅】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    scene kt_夜晚 with dissolve:
        zoom .667
    
    
    w "这丫头终于走了。"
    narrator "我看着桌面上一扫而空的零食。"
    narrator "不由得有些感叹了起来。"
    show y 正常01 at ct with dissolve
    y "是啊…除了夏静给我的东西都吃完了。"
    w "别介意别介意，这都是必要的支出。"
    show y 正常02 at ct with dissolve
    y "唉。"
    show y 正常05 at ct with dissolve
    y "死猫。"
    show y 正常04 at ct with dissolve
    y "我怎么觉得这几天过去，我整个人都老了好几十岁呢。"
    w "那只是你的错觉啦，错觉啦。"
    show y 正常04 at ct with dissolve
    y "是么。"
    show y 正常01 at ct with dissolve
    y "时间不早了，睡觉吧，事情明天再想。"
    w "……"
    w "你还有心情睡觉啊。"
    show y 正常02 at ct with dissolve
    y "因为最近比较累，只有做梦的时候会轻松点。"
    w "……"

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
    
    narrator "对话结束之后，我便同袁艳回到了房间。"
    show y 正常02 at ct with dissolve
    y "喏，自己裹在毛毯里睡。"
    w "……"
    w "又睡毛毯啊？就不能让我跟你一起睡床上？"
    show y 恼火01 at ct with dissolve
    y "你想得倒美。"
    show y 恼火02 at ct with dissolve
    y "也不看你身上有多脏，叫你洗澡又不肯去洗澡。"
    w "洗澡…就是你前几天在厕所…"
    show y 恼火02 at ct with dissolve
    y "怎么了吗？"
    w "别瞎说了，会死猫的好不好。"
    show y 恼火05 at ct with dissolve
    y "那你就别想上床睡觉了。"
    w "……"
    w "不上就不上，搞得我好像很羡慕似的。"
    show y 正常02 at ct with dissolve
    y "……"
    narrator "…………"
    
    jump c2