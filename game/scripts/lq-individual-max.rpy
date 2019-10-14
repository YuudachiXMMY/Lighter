define y_nvl = Character("袁艳",kind=nvl)
define l_nvl = Character("林琴",kind=nvl)
define x_nvl = Character("夏静",kind=nvl)
define c_nvl = Character("程祎琳",kind=nvl)
define w_nvl = Character("我",kind=nvl)
define mzsn_nvl = Character("迷之少女",kind=nvl)
define yr_nvl = Character("佣人",kind=nvl)
define jzsn_nvl = Character("镜中少女",kind=nvl)
define znr_nvl = Character("中年人",kind=nvl)
define nr_nvl = Character("女人",kind=nvl)

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

#支线：程祎琳线（当程祎琳好感度最高时进入本支线）
label l_indi_1:

    $_dismiss_pause = False

    #说明：以下部分‘我’均为林琴个人 视角转变：林琴

    nvl clear

    window hide

    #场景：花园
    $ persistent.cg_l_hy = True
    scene hy_1 with Dissolve(1):
        zoom .667
    
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}人没有了价值，不能够再被利用就会被抛弃。{/color}"
    nvl_narrator "{color=#e5e5e5}这是我从小就学会的道理，人和记忆是同一个道理。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}如果某一段记忆没有了价值，就一定会被忘掉。{/color}"
    nvl_narrator "{color=#e5e5e5}关于过去，我没有任何需要记住的东西，我只需要大步往前面走就行了——{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}——原本应该是这样子的。{/color}"
    nvl_narrator "{color=#e5e5e5}可我却唯独没法忘记有关于你的一切。{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    # TODO
    #CG：人群
    $ persistent.cg_l_rq_2 = True
    scene rq_2 with dissolve:
        zoom .667
    pause 1.0
    $ persistent.cg_l_rq_3 = True
    scene rq_3 with dissolve:
        zoom .667
    pause 1.0
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}人群喧闹着，我知道‘他们’都注视着我。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我只是蹲着身子，在爷爷摇头和叹气声中低下了头。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我不想说话，因为争辩没有任何意义。{/color}"
    nvl_narrator "{color=#e5e5e5}我知道有谁在诋毁我。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我却不知道是谁。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}或许是面前人群里面的一个，或许他正在幕后笑着我这个十岁的女孩太好对付了。{/color}"
    nvl_narrator "{color=#e5e5e5}然后一点一点的消磨掉爷爷对我的最后一丝信心。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}只要爷爷放弃我，放弃让我继承这个家业。{/color}"
    nvl_narrator "{color=#e5e5e5}那么现在我面前的这一群人之中就会有人一步登天。{/color}"
    nvl_narrator "{color=#e5e5e5}而这一切仅仅只因为我姓林。{/color}"
    nvl_narrator "{color=#e5e5e5}林氏集团的林。{/color}"
    nvl_narrator "{color=#e5e5e5}也是继承者的林。{/color}"
    nvl clear


    window hide Dissolve(.7)
    #场景：房间
    $ persistent.cg_l_fj_n = True
    scene fj_n with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}这个姓氏自从我出出生起就如同一座大山一样压在我的肩膀上。{/color}"
    nvl_narrator "{color=#e5e5e5}懂事后，我才发现原来父母并没有为我遮风挡雨。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}因为他们并不存在，我的脑海中没有关于他们一点的讯息。{/color}"
    nvl_narrator "{color=#e5e5e5}爷爷说他们死了。{/color}"
    nvl_narrator "{color=#e5e5e5}所以我最亲的是爷爷，但是离得最远的也是爷爷。{/color}"

    window hide Dissolve(.7)
    #场景：客厅
    $ persistent.cg_l_kt_n = True
    scene kt_n with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}印象中的爷爷总是被公事缠身。{/color}"
    nvl_narrator "{color=#e5e5e5}可他对我非常的好。{/color}"
    nvl_narrator "{color=#e5e5e5}因此我度过了一个富足的童年。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}如果不是在某一天夜里做噩梦——{/color}"
    nvl_narrator "{color=#e5e5e5}——我梦见有无数恶狼在追我。{/color}"
    nvl_narrator "{color=#e5e5e5}它们想要把我撕碎，咬碎。{/color}"
    nvl_narrator "{color=#e5e5e5}我拼命的逃跑、拼命的逃跑…{/color}"
    nvl_narrator "{color=#e5e5e5}这应该是极度正常的，至少在说给别人听的时候，别人的想法肯定是这并没有什么。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是，梦里的我在逃跑时的感觉却并不是恐惧。{/color}"
    nvl_narrator "{color=#e5e5e5}我完全没有害怕。{/color}"
    nvl_narrator "{color=#e5e5e5}而是另外一种我前所未有过的感觉。{/color}"
    nvl_narrator "{color=#e5e5e5}后来我把那种感觉称之为兴奋。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我逃跑只是为了让自己在多体验一下这种感觉而已。{/color}"
    nvl_narrator "{color=#e5e5e5}这怎么能称之为噩梦呢？简直就是美梦一般。{/color}"
    nvl_narrator "{color=#e5e5e5}我尽情的享受着，梦却终归有终点。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}醒过来的时候依旧是半夜。{/color}"
    nvl_narrator "{color=#e5e5e5}冷链的月光透过别墅的窗台洒落了进来。{/color}"
    nvl_narrator "{color=#e5e5e5}空荡的房间悄无声息。{/color}"
    nvl_narrator "{color=#e5e5e5}我静静的注视着眼前的一切。{/color}"
    nvl clear


    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}如果说我被饿狼追捕是一场噩梦。{/color}"
    nvl_narrator "{color=#e5e5e5}那么这个房间就是比噩梦还要恐怖的——{/color}"
    nvl_narrator "{color=#e5e5e5}——名为现实的存在。{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    # TODO 4
    #CG：人群
    $ persistent.cg_l_rq_1 = True
    scene rq_1 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}但是我还是找到了新的玩具。{/color}"
    nvl_narrator "{color=#e5e5e5}自那之后我就发现了…{/color}"
    nvl_narrator "{color=#e5e5e5}有人在故意怂恿我去做些奇怪的事情。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}譬如三叔会让我拿着手机偷偷的去拍一些奇怪的‘东西’，然后以我的名义发布出去。{/color}"
    nvl_narrator "{color=#e5e5e5}然后那天爷爷就把我叫到他的房间里面去了，但是我却没有告诉爷爷是谁指使我做的，我告诉他我觉得很有趣所以做了，那是我的真心话。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}再譬如远房小姨会给奇怪的粉末，让我下在佣人的食物里面，我当然照办了。{/color}"
    nvl_narrator "{color=#e5e5e5}看着几个佣人痛不欲生的模样，表面胆怯的我却感到了异常的开心。{/color}"
    nvl_narrator "{color=#e5e5e5}原来世界上还有这么好玩的事情啊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}于是事情就开始一发不可收拾。{/color}"
    nvl_narrator "{color=#e5e5e5}越来越多的人开始怂恿我做越来越奇怪的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}他们就好像梦里面那一匹匹的饿狼追逐着我。{/color}"
    nvl_narrator "{color=#e5e5e5}他们撕咬着我的身躯，我却觉得异常的开心。{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    # TODO 5
    #CG：小女孩的沉思
    $ persistent.cg_l_girlscs = True
    scene cg_小女孩的沉思 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}只不过…这一切终于在今天要迎来结束了。{/color}"
    nvl_narrator "{color=#e5e5e5}——只因为我差点儿失手害死了我至今都记不住名字的谁。{/color}"
    nvl_narrator "{color=#e5e5e5}爷爷失望的目光下，我知道他不会再庇护我了。{/color}"
    nvl_narrator "{color=#e5e5e5}严厉的呵斥已经超出了我的想象。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我从来没有想过那样慈祥的爷爷居然会如此严肃的呵斥我。{/color}"
    nvl_narrator "{color=#e5e5e5}我不知道接下来会迎来的命运。{/color}"
    nvl_narrator "{color=#e5e5e5}我只是蹲下了身子。{/color}"
    nvl_narrator "{color=#e5e5e5}迎接我的结局。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这个时候的我已经想到了等这一次结束了我就去死好了。{/color}"
    nvl_narrator "{color=#e5e5e5}这个年纪的我并不知道死亡的含义到底是什么。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}只是听说，死亡很轻松。{/color}"
    nvl_narrator "{color=#e5e5e5}就好像我那死去的父母一样。{/color}"
    nvl_narrator "{color=#e5e5e5}他们什么也不需要做。{/color}"
    nvl_narrator "{color=#e5e5e5}什么也不需要说。{/color}"
    nvl_narrator "{color=#e5e5e5}那一刻我睁开了双眼，第一次认认真真的注视着这个世界。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}有谁…有谁可以来抱抱我吗？{/color}"
    nvl_narrator "{color=#e5e5e5}我感觉好冷。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这时候有点点温暖从我的背后传来，仿佛愈演愈烈的炙热火光，有人站在了我的身后，用好奇的眼神注视着我。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我一直觉得，我被降生在这个世界上一定是存在意义的，我等了十年，在我最绝望的时候，最能宣告我意义的天使出现了。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 6
    #CG：另一个少女的好奇
    $ persistent.cg_l_girlshq = True
    scene cg_另一个少女的好奇 with dissolve:
        zoom .667
    pause 1.0

    # TODO 7
    #CG：另一个少女的笑容]"
    $ persistent.cg_l_girlssmile = True
    scene cg_另一个少女的笑容 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}那个天使出现在了我的面前，起初她似乎也因为见到我而感到惊愕。{/color}"
    nvl_narrator "{color=#e5e5e5}但是旋即{/color}"
    nvl_narrator "{color=#e5e5e5}她就笑了出来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她暗红色的头发梳的整整齐齐，和我头发的颜色有点像，但她留的是长发。{/color}"
    nvl_narrator "{color=#e5e5e5}粉红色的套裙，月白色丝绸的小衬衣。{/color}"
    nvl_narrator "{color=#e5e5e5}明明个子比我还小，而此时看起来却比我高上了许多。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}压迫感简直让我感觉到了腿软，整个身体摇摇欲坠，随时都有可能会倒下来。{/color}"
    nvl_narrator "{color=#e5e5e5}但她却毫不自觉的伸出了手，扶住了我——让我站稳了。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 8
    #CG：少女的攀谈]"
    $ persistent.cg_l_girlstalk = True
    scene cg_少女的攀谈 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    mzsn_nvl "{color=#e5e5e5}你叫什么名字呀？{/color}"
    nvl_narrator "{color=#e5e5e5}她蹲下身来，笑嘻嘻的和我说话，好像是在询问一个许久不见的朋友一样那般的自然。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我…我？{/color}"
    mzsn_nvl "{color=#e5e5e5}对呀！{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我…我叫…我叫….{/color}"
    nvl_narrator "{color=#e5e5e5}话到了喉咙边上，可是我却怎么也说不出来。{/color}"
    nvl_narrator "{color=#e5e5e5}急的我脸上发热。{/color}"
    nvl_narrator "{color=#e5e5e5}可纵然如此，我却依然没有办法说出我自己的名字。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}咳…我..额…额…啊…{/color}"
    nvl_narrator "{color=#e5e5e5}随着时间的推移；{/color}"
    nvl_narrator "{color=#e5e5e5}渐渐的我甚至连一个清晰的咬字都做不到。{/color}"
    nvl_narrator "{color=#e5e5e5}张着嘴巴，咿呀学语一般只能发出声音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}面前的这个女孩带着善意的笑容，什么也没有说。{/color}"
    nvl_narrator "{color=#e5e5e5}只是轻抚我的背脊。{/color}"
    nvl_narrator "{color=#e5e5e5}像是在安慰我，好像是在跟我说‘别着急别着急，慢慢来慢慢来这样的话语’。{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    # TODO 9
    #CG：痛苦流涕
    $ persistent.cg_l_tklt = True
    scene cg_痛苦流涕 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}我看着面前的小女孩，莫名其妙的就被她的举动给感动了。{/color}"
    #show l 嗷嗷大哭 at ct with dissolve
    #l_nvl "{color=#e5e5e5}"
    nvl_narrator "{color=#e5e5e5}失声痛哭…这是我脑海里面唯一想到的词语。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这一刻我在顾不得周围有多少人。{/color}"
    nvl_narrator "{color=#e5e5e5}只是像是一个傻子一样痛哭流涕。{/color}"
    nvl clear

    """
    window hide Dissolve(.7)
    #场景：花园
    $ persistent.cg_l_hy = True
    scene hy_1 with dissolve:
        zoom .667
    window show Dissolve(.7)
    """
    
    nvl_narrator "{color=#e5e5e5}第一次丝毫没有顾忌的哭了出来。{/color}"
    nvl_narrator "{color=#e5e5e5}却只是因为一个陌生女孩传达给我的善意。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我无视于震撼的人群。{/color}"
    nvl_narrator "{color=#e5e5e5}那个时候的我却还不知道，那是全部故事的开始。{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    pause .5

    #场景：房间
    $ persistent.cg_l_fj_n = True
    scene fj_n with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}醒过来的时候已经是晚上了。{/color}"
    nvl_narrator "{color=#e5e5e5}房间里面的灯依旧亮着，整个房间宛如白昼。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}小女孩的笑容就是我见到的最后一幕。{/color}"
    nvl_narrator "{color=#e5e5e5}然后大量的记忆像是忽然而然的涌入了我的脑海，好似潮水一般。{/color}"
    nvl_narrator "{color=#e5e5e5}瞬间就充斥了脑海。{/color}"
    nvl_narrator "{color=#e5e5e5}而我在记忆中看到的那一天和她相遇的那个日子，我只看到了所有人的惊愕。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}转眼间，记忆中的‘我’开始嗷嗷大哭。{/color}"
    nvl_narrator "{color=#e5e5e5}我知道这段时间里，是她出现了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}可是明明我可以看见所有人，却唯独看不见她。{/color}"
    nvl_narrator "{color=#e5e5e5}记忆中的她仿佛不存在一样。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我心里面却知道她存在的。{/color}"
    nvl_narrator "{color=#e5e5e5}如果非要问为什么的话。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 10
    #CG：镜面倒影]
    $ persistent.cg_l_jmdy = True
    scene cg_镜面倒影 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}因为她现在就在我的面前啊。{/color}"
    nvl_narrator "{color=#e5e5e5}我看着面前的‘她’不由得愣住了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她笑眯眯的看着我。{/color}"
    nvl_narrator "{color=#e5e5e5}我也充满幸福感的注视着她。{/color}"
    nvl clear


    # TODO 11
    #CG结束
    
    #场景：房间
    $ persistent.cg_l_fj_n = True
    scene fj_n with dissolve:
        zoom .667
    window show Dissolve(.7)

    yr_nvl "{color=#e5e5e5}小姐…小姐…三爷还在门外跪着呢…{/color}"
    yr_nvl "{color=#e5e5e5}他求着想见您。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然而就是这样的时候，总是会有不懂得察言观色的人出现。{/color}"
    nvl_narrator "{color=#e5e5e5}我有些不满的看了看面前的佣人。{/color}"
    nvl_narrator "{color=#e5e5e5}可能是眼神太过严厉，把这个新来的佣人人吓了一跳。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我知道了，我会处理的。{/color}"
    l_nvl "{color=#e5e5e5}你可以去做别的事情了。{/color}"
    yr_nvl "{color=#e5e5e5}好…好的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然如如释重负一般，佣人里面转身就离开了我的房间。{/color}"
    nvl_narrator "{color=#e5e5e5}我这才心情好一些。{/color}"
    nvl_narrator "{color=#e5e5e5}然而回过头的时候，她开口说话了。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    # TODO 10
    #CG：镜面倒影]
    $ persistent.cg_l_jmdy = True
    scene cg_镜面倒影 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    jzsn_nvl "{color=#e5e5e5}你吓到她了。{/color}"
    nvl_narrator "{color=#e5e5e5}她皱着眉，似乎有点儿不满我的做法。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}唔…我什么也没做啊。{/color}"
    jzsn_nvl "{color=#e5e5e5}你干嘛要吓她啊，她又没做坏事。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我真的没有吓她啦。{/color}"
    nvl_narrator "{color=#e5e5e5}这倒是我说的实话，我确确实实没有恐吓刚刚的佣人啊。{/color}"
    nvl clear

    jzsn_nvl "{color=#e5e5e5}你就是吓到她了，之后给我好好的跟她赔礼道歉。{/color}"
    jzsn_nvl "{color=#e5e5e5}知道了吗？{/color}"
    nvl_narrator "{color=#e5e5e5}她一如既往的凶悍。{/color}"
    nvl_narrator "{color=#e5e5e5}看着她一副当家作主的模样，我不由得头疼的扶了扶脑袋。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}好…好的，听你的。{/color}"
    nvl_narrator "{color=#e5e5e5}只要是她说的话，不知道怎么回事我一点气也生不起来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}心里只想着怎么去给那个佣人道歉才不会吓着她了。{/color}"
    nvl_narrator "{color=#e5e5e5}不过我觉得不管我怎么道歉都会吓着她吧，但是那也是之后要考虑的事情了。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}那三叔怎么处理他？{/color}"
    nvl_narrator "{color=#e5e5e5}镜子中的她露出了笑容。{/color}"
    nvl_narrator "{color=#e5e5e5}我不由得也笑了起来。{/color}"
    nvl clear

    jzsn_nvl "{color=#e5e5e5}当初就是害你被爷爷处罚的是他。{/color}"
    jzsn_nvl "{color=#e5e5e5}在一旁看笑话的也是她。{/color}"
    jzsn_nvl "{color=#e5e5e5}现在反过来求你的也是她。{/color}"
    jzsn_nvl "{color=#e5e5e5}这个世界上的事情就是这样子好笑呢。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}呵呵…是呢…那要做掉他吗？{/color}"
    jzsn_nvl "{color=#e5e5e5}……{/color}"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}镜子里面的‘她’看着我，只是默默的笑了一下。{/color}"
    nvl_narrator "{color=#e5e5e5}我就明白了她的意思。{/color}"
    nvl_narrator "{color=#e5e5e5}然后我就起身离开了。{/color}"
    nvl clear


    window hide Dissolve(.7)
    #场景：花园
    scene hy_1 with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}一个中年人就这样一脸紧张在门口的阶梯上踱步。{/color}"
    nvl_narrator "{color=#e5e5e5}他从林氏集团里面瓜分了不知道多少财产。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}看他现在的一副油腻的模样，可想而知他的生活是过得有多滋润了。{/color}"
    nvl_narrator "{color=#e5e5e5}然而就是这样一个家伙现在却十分紧张。{/color}"
    nvl_narrator "{color=#e5e5e5}似乎是听到了我的脚步声一样，他浑身打了一个冷战。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}这不是三叔吗？{/color}"
    l_nvl "{color=#e5e5e5}平常都见不到您。{/color}"
    l_nvl "{color=#e5e5e5}怎么今天有空跑到我房子门口晒太阳来了？{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}……{/color}"
    znr_nvl "{color=#e5e5e5}她们都是你的亲人啊，你怎么能这么狠心…{/color}"
    nvl_narrator "{color=#e5e5e5}看他一脸悲愤的模样，我不由得露出了冷笑。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}三叔，您在说什么？我怎么完全就听不懂呢？{/color}"
    znr_nvl "{color=#e5e5e5}多少钱？{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}……{/color}"
    znr_nvl "{color=#e5e5e5}多少钱你才肯放过她们？{/color}"
    nvl_narrator "{color=#e5e5e5}我好笑的耸耸肩，摇下头表示完全听不懂。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}我老婆和我女儿，你到底把她们抓到哪里去了？{/color}"
    znr_nvl "{color=#e5e5e5}你快告诉我！{/color}"
    nvl_narrator "{color=#e5e5e5}他满眼都是愤怒，揪助了我的衣领。{/color}"
    nvl_narrator "{color=#e5e5e5}好像这样子就能威胁到我一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我不由得轻蔑的看着这个即将失去理智的男人。{/color}"
    nvl_narrator "{color=#e5e5e5}真是可笑的家伙。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}呵呵呵…三叔，你弄疼我了。{/color}"
    nvl_narrator "{color=#e5e5e5}我尽量以平静的语气在说话。{/color}"
    nvl_narrator "{color=#e5e5e5}至于胸口埋着的情绪到底是害怕还是兴奋就不得而知了。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}……{/color}"
    nvl_narrator "{color=#e5e5e5}三叔显然意识到了自己的失态，连忙松开手。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}小琴啊，跟三叔说说你三姨还有堂姐都去了哪里可以吗？{/color}"
    nvl_narrator "{color=#e5e5e5}就像是变脸一样，瞬间在脸上堆出笑容。{/color}"
    nvl_narrator "{color=#e5e5e5}仿佛刚刚什么也没发生一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}远远看上去现在就像是叔侄二人在唠嗑家常。{/color}"
    nvl_narrator "{color=#e5e5e5}他真的很会演。{/color}"
    nvl_narrator "{color=#e5e5e5}换做别人恐怕已经被他骗过去了吧。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}三叔，你就别演了吧，我都要打哈欠了。{/color}"
    nvl_narrator "{color=#e5e5e5}三叔沉默一会儿，默默的看了我一眼，就像是老了好几岁一样。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}你难道真的一点都不顾及手足之情么？{/color}"
    znr_nvl "{color=#e5e5e5}不管怎么说你三姨还有你堂姐终究是你的亲人。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}我知道你还在生小时候的气，我承认是我的一手策划的。{/color}"
    znr_nvl "{color=#e5e5e5}你有什么气，冲我来就是了。{/color}"
    znr_nvl "{color=#e5e5e5}放过她们。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}……{/color}"
    l_nvl "{color=#e5e5e5}小时候真的是受三叔照顾颇多。{/color}"
    l_nvl "{color=#e5e5e5}托你的福我玩得很开心。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我微微欠身，算是给小时候的事情道谢。{/color}"
    nvl_narrator "{color=#e5e5e5}三叔看着我，显得很疑惑。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}小琴你的意思是？{/color}"
    l_nvl "{color=#e5e5e5}我只想说两件事情。{/color}"
    l_nvl "{color=#e5e5e5}我也不想做得太过分。{/color}"
    l_nvl "{color=#e5e5e5}毕竟小时候还是很感谢三叔的。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}第一件事情是你手持的股份全部给我，我给你五千万你拿去养老。{/color}"
    znr_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}不够在找我要就是了。{/color}"
    nvl_narrator "{color=#e5e5e5}三叔皱了皱眉毛，最终还是咬了咬嘴唇，一脸决绝的模样。{/color}"
    znr_nvl "{color=#e5e5e5}好。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}第二件事情就是处理掉小姨，这件事情全部交给你来办。{/color}"
    l_nvl "{color=#e5e5e5}我只有一个要求，那就是小姨跪在这里求我。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}三叔望着我，额头上的皱纹似乎又加深了许多。{/color}"
    nvl_narrator "{color=#e5e5e5}原本还容光焕发的中年人此刻竟和逝去了的爷爷最后的身影一般苍老。{/color}"
    nvl_narrator "{color=#e5e5e5}看来他的路也走到头了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我便不再说话，只是望着面前已经有些恍惚的三叔露出冷笑。{/color}"
    znr_nvl "{color=#e5e5e5}小琴…你真的要做得这么绝么？{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}……..{/color}"
    znr_nvl "{color=#e5e5e5}这就是报应吗？{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}三叔，你搞错了，这不是什么报应。{/color}"
    l_nvl "{color=#e5e5e5}我只不过是从地狱里面活着回来了。{/color}"
    l_nvl "{color=#e5e5e5}然后拿回原本就属于我的东西。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}…….{/color}"
    znr_nvl "{color=#e5e5e5}唉…放了你三姨和你堂姐，我就听你的。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我有分寸。{/color}"
    nvl_narrator "{color=#e5e5e5}似乎是看到我同意了，三叔便不再多做停留。{/color}"
    nvl clear

    znr_nvl "{color=#e5e5e5}这林家，真的要变天了。{/color}"
    nvl_narrator "{color=#e5e5e5}感叹一句之后便失魂落魄的离开了我的庄园。{/color}"
    nvl_narrator "{color=#e5e5e5}……{/color}"
    nvl clear


    #场景：房间
    
    window hide Dissolve(.7)
    # TODO 13
    #CG：镜面倒影]"
    $ persistent.cg_l_jzdy = True
    scene cg_镜面倒影 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    
    jzsn_nvl "{color=#e5e5e5}回来啦？{/color}"
    nvl_narrator "{color=#e5e5e5}她的笑容宛如天边的一缕红霞，十分的迷人。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}嗯，都已经搞定了。{/color}"
    l_nvl "{color=#e5e5e5}三叔拿走的股份我都要回来了。{/color}"
    nvl clear

    jzsn_nvl "{color=#e5e5e5}做得真棒，不愧是林琴大小姐！{/color}"
    nvl_narrator "{color=#e5e5e5}她的夸奖无论听多少次，对于我来说都很是受用。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 14
    #CG：林琴幸福的笑容
    $ persistent.cg_l_lssmile = True
    scene cg_林琴幸福的笑容 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}我看着面前的和我相似而去又完全不同的女孩，有些享受似的笑了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}不知不觉中，她已经成为了能够让我感觉到温暖的人。{/color}"
    nvl_narrator "{color=#e5e5e5}在经历了那般过去的我居然有朝一日也能够以这样的方式获取幸福。{/color}"
    nvl clear

    jzsn_nvl "{color=#e5e5e5}你有在听吗？{/color}"
    jzsn_nvl "{color=#e5e5e5}喂喂！{/color}"
    l_nvl "{color=#e5e5e5}嗯嗯！我有在听呢。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}忽然我想起了一件事情，表情不由得开始僵硬了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}我望着镜子里面的少女。{/color}"
    nvl_narrator "{color=#e5e5e5}不由得开口询问道。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}那个…你叫什么名字？{/color}"
    nvl_narrator "{color=#e5e5e5}少女看着我，眨了眨眼睛，微微一笑。{/color}"
    nvl_narrator "{color=#e5e5e5}还没有听到回答便一阵黑暗便向我袭来。{/color}"
    nvl clear


    window hide Dissolve(.7)
    #场景：黑屏
    scene black with dissolve
    pause .5
    #场景：房间
    scene fj_n with dissolve:
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}再次睁开眼睛的时候房间的场景映入我的眼眸。{/color}"
    nvl_narrator "{color=#e5e5e5}还是熟悉的场景。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}只是这次的房间灯光比以往要暗上一些。{/color}"
    nvl_narrator "{color=#e5e5e5}房间还稍微有点乱，像是被谁大闹了一番一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}与此同时大量的记忆就仿佛泉水一般涌入了我的脑海，与之而来的还有莫名其妙的悲伤。{/color}"
    nvl_narrator "{color=#e5e5e5}就仿佛置身于全封闭的窟窿一般，胸口闷的说不出话来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我的手紧扣在胸口，但完全没有办法抵消这份情感。{/color}"
    nvl_narrator "{color=#e5e5e5}好像此刻我正代替着谁承受着这份痛楚一般。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}一面忍受胸口那足以让人窒息的郁结，一面思维去没有发生任何的混乱。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我的理智还在不断地的翻看着记忆。{/color}"
    nvl_narrator "{color=#e5e5e5}开始一点一点的追溯这份郁结的源头。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我有些严肃的从床上站了起来，意外钻心的疼痛传入了我的脑髓。{/color}"
    nvl_narrator "{color=#e5e5e5}阵阵眩晕涌上我的脑海。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我伸出手，却只看见手腕处大量的鲜血在涌出。{/color}"
    nvl_narrator "{color=#e5e5e5}覆盖在鲜血下的是那触目惊心的伤痕。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}渐渐的意识也逐渐离我远去。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    
    window hide Dissolve(.7)
    #场景：黑暗
    # TODO 15
    #CG：镜中少女](周边黑暗)"
    $ persistent.cg_l_jzsn = True
    scene cg_镜中少女 with Dissolve(.7):
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}她笑着看着我。{/color}"
    nvl_narrator "{color=#e5e5e5}而我却没法触碰倒她。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}从什么时候起的呢？我就已经无法触碰到她了。{/color}"
    nvl_narrator "{color=#e5e5e5}明明小时候的我们还能够手牵手一起在花园玩耍的。{/color}"
    nvl_narrator "{color=#e5e5e5}明明小时候我们还能够一起对付那些所谓亲人的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}渐渐地，她就只能出现在镜子中，我变得再也触碰不到她。{/color}"
    nvl_narrator "{color=#e5e5e5}即便如此我却依旧习惯了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}只要有她在的日子我就是幸福的。{/color}"
    nvl_narrator "{color=#e5e5e5}我是这么认为的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是其实只要仔细想想我就明白——我根本就只是在妥协。{/color}"
    nvl_narrator "{color=#e5e5e5}她在不知不觉中已经离我越来越远了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我却还不肯承认这个事实。{/color}"
    nvl_narrator "{color=#e5e5e5}毕竟她还在我的身边不是吗？{/color}"
    nvl_narrator "{color=#e5e5e5}只要她在就好了。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}只要有你在……{/color}"
    nvl_narrator "{color=#e5e5e5}轻轻的呢喃。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}而她的身影却渐渐隐去。{/color}"
    nvl_narrator "{color=#e5e5e5}我朝着逐渐趋于黑暗的区域伸出手。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}黑暗却吞噬了一切。{/color}"
    nvl_narrator "{color=#e5e5e5}我真的朝她伸出手了吗？{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}只要有你在就可以…{/color}"
    nvl_narrator "{color=#e5e5e5}只要她还在这里。{/color}"
    nvl_narrator "{color=#e5e5e5}我就能感觉到我自己还活着。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 16
    #CG：镜中少女消失]"
    $ persistent.cg_l_jzsnxs = True
    scene cg_镜中少女消失 with Dissolve(.7):
        zoom .667
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}然而她却消失了。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}啊….{/color}"
    nvl_narrator "{color=#e5e5e5}撕心裂肺的声音在黑暗中响起。{/color}"
    nvl_narrator "{color=#e5e5e5}几乎撕裂了我的耳膜。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}把我吓了一跳，连忙捂住了耳朵。{/color}"
    nvl_narrator "{color=#e5e5e5}是谁在呼喊？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我仔细感受发现，原来呐喊声是是我自己发出来的。{/color}"
    nvl_narrator "{color=#e5e5e5}伴随着泪水，伴随着婴儿般的哭泣，伴随着这周边无尽的黑暗。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看到了一个彷徨无助的自己。{/color}"
    nvl_narrator "{color=#e5e5e5}人啊，总是要抱紧什么才知道自己是存在的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我紧紧的抱住了你，而你却消失了。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}别丢下我…{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}别只留下我一个人…{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}我不能没有你啊！！{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}哭闹声中，我仿佛听见了谁的呼唤声。.{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}……{/color}"
    nvl clear


    window hide Dissolve(.7)
    #场景：病房
    scene bf_夜晚 with dissolve:
        zoom .667
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}我微微的睁开了眼睛。{/color}"
    nvl clear
    
    nr_nvl "{color=#e5e5e5}你…你醒啦？{/color}"
    nvl_narrator "{color=#e5e5e5}堆着笑容的女人坐在我的旁边。{/color}"
    nvl_narrator "{color=#e5e5e5}亲切的看着我。{/color}"
    nvl clear

    nr_nvl "{color=#e5e5e5}我削个苹果给你吃吧。{/color}"
    nvl_narrator "{color=#e5e5e5}我认得她，她是我的小姨。{/color}"
    nvl_narrator "{color=#e5e5e5}随着记忆的涌入，我记起了她之所以会来这里的原因。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}不用了，小姨。{/color}"
    l_nvl "{color=#e5e5e5}我想静一静，你先走吧。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}关于你股份的事情我们晚点再谈。{/color}"
    nr_nvl "{color=#e5e5e5}啊！好…好的！{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我望着惨白的天花板出神。{/color}"
    nvl_narrator "{color=#e5e5e5}事情就发生在某个夜晚，三叔给我打电话之后，他跟我说小姨的事情他已经帮我办好了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}原本应该是一切都尘埃落定。{/color}"
    nvl_narrator "{color=#e5e5e5}我终于可以和她一起享受生活的时候。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她消失了。{/color}"
    nvl_narrator "{color=#e5e5e5}——多少人曾被自己认为重要的人给救赎过。{/color}"
    nvl_narrator "{color=#e5e5e5}然而再有一天这个曾救赎过你的那个存在忽然就不见了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}你拼命的去找，直到伸手不见五指的夜幕降临。{/color}"
    nvl_narrator "{color=#e5e5e5}最终你无力的瘫坐在黑暗之中笑了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}没有她存在的世界，白天和黑夜有什么区别呢？{/color}"
    nvl_narrator "{color=#e5e5e5}记忆中的我在她消失以后整个人就变了。{/color}"
    nvl_narrator "{color=#e5e5e5}就像是大坝被打开了阀门一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}原本在胸口能够好好抑制的想法全部涌了出来。{/color}"
    nvl_narrator "{color=#e5e5e5}最终变为利刃，开始向无辜的人们倒去。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}是不是只要我变得不再成熟，你就会回到我的身边呢？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我不仅伤害了别人，连自己也不会放过。{/color}"
    nvl_narrator "{color=#e5e5e5}直到今天我住到了医院，我才明白。{/color}"
    nvl_narrator "{color=#e5e5e5}那阵子的我究竟有多疯狂，如果不是有人及时发现我割腕。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}可能我已经死了。{/color}"
    nvl_narrator "{color=#e5e5e5}如果这辈子再也见不到她的话，我想死去也许会比较轻松吧。{/color}"
    nvl_narrator "{color=#e5e5e5}但是我死了，万一她回来谁能去迎接她呢？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}抱着这样的想法。{/color}"
    nvl_narrator "{color=#e5e5e5}我住进了林氏旗下某医院的重症科。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我不是害怕死亡。{/color}"
    nvl_narrator "{color=#e5e5e5}而是怕我在失去理智的时候杀死自己。{/color}"
    nvl_narrator "{color=#e5e5e5}然后在没人替我去迎接那个她。{/color}"
    nvl_narrator "{color=#e5e5e5}即便，我现在都还不明白为什么她会出现。{/color}"
    nvl clear

    # TODO 999
    #刺耳的尖锐的隐蔽音

    nvl_narrator "{color=#e5e5e5}我默默的念出了她的名字。{/color}"
    nvl_narrator "{color=#e5e5e5}仿佛回到了童年一般，只不过，这一次我有要等的人。{/color}"
    nvl clear

    window hide Dissolve(.7)
    #场景：黑屏
    scene black 
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}直到，我遇见了她。{/color}"
    nvl clear


    window hide Dissolve(.7)
    # TODO 17
    #CG：雨中的女孩
    $ persistent.cg_l_yz = True
    scene c_雨中 with dissolve
    window show dissolve
    
    nvl_narrator "{color=#e5e5e5}原本这应该只是一场梦的。{/color}"
    nvl_narrator "{color=#e5e5e5}无数雨点打在我的身上。{/color}"
    nvl_narrator "{color=#e5e5e5}我望着漆黑的天空。{/color}"
    nvl clear

    l_nvl "{color=#e5e5e5}（咦？这是？）{/color}"
    l_nvl "{color=#e5e5e5}喵……{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然而我却没有发出声音{/color}"
    nvl_narrator "{color=#e5e5e5}我仿佛被谁抱在怀里。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这是…什么情况？{/color}"
    nvl_narrator "{color=#e5e5e5}我看着少女。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她紧紧的将我抱在怀里。{/color}"
    nvl_narrator "{color=#e5e5e5}然而我却莫名的觉得有些违和。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这份违和渐渐的放大。{/color}"
    nvl_narrator "{color=#e5e5e5}就像是忽然张开的幕布，朝我围了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}这一定是有什么地方出现了问题。{/color}"
    nvl clear

    scene black with dissolve
    
    nvl_narrator "{color=#e5e5e5}就在我这么想着的时候，阵阵的黑暗将我整个包裹起来。{/color}"
    nvl_narrator "{color=#e5e5e5}……{/color}"

    jump c3_2_l