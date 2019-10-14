define y_nvl = Character("袁艳",kind=nvl)
define l_nvl = Character("林琴",kind=nvl)
define x_nvl = Character("夏静",kind=nvl)
define c_nvl = Character("程祎琳",kind=nvl)
define w_nvl = Character("我",kind=nvl)
define unknown_nvl = Character("？？？",kind=nvl)

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
label c_indi_1:

    $_dismiss_pause = False

    window hide Dissolve(.7)
    #【场景：车窗】
    $ persistent.cg_c_cc2 = True
    scene c_车窗2 with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}车窗外的风景随着旅行大巴的奔驰而飞逝。{/color}"
    nvl_narrator "{color=#e5e5e5}窗外的每一处景色像是被拉长。{/color}"
    nvl_narrator "{color=#e5e5e5}原本已经司空见惯了的风景，今天却有种别样的美感{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}如果只是看风景的话，那么我此刻的心情又是怎么回事呢？{/color}"
    nvl_narrator "{color=#e5e5e5}稍微有一点不安，可能是因为昨天逃课被抓到了？{/color}"
    nvl_narrator "{color=#e5e5e5}稍微有一点紧张，可能是不知道教导主任在这趟旅程里会怎么整自己。{/color}"
    nvl_narrator "{color=#e5e5e5}都不是，心里虽然一直在想着别的可能性，但是我却不断的在否定想法。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看着窗外的景色。{/color}"
    nvl_narrator "{color=#e5e5e5}心跳不由得怦怦加速了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}旅行也能让我这样激动的吗？{/color}"
    nvl clear

    window hide Dissolve(.7)
    #音效：嘈杂的说话声
    #【CG:大巴车】
    $ persistent.cg_c_dbc = True
    scene c_大巴车 with dissolve
    window show Dissolve(.7)

    voice "voice/dlc_voice/c/20.mp3"
    c_nvl "{color=#e5e5e5}你家里养了猫呀？完全都不知道这个事情！{/color}"#（开心的声音）
    voice "voice/dlc_voice/c/17.mp3"
    c_nvl "{color=#e5e5e5}下次我可以去你家里玩吗？{/color}"
    nvl_narrator "{color=#e5e5e5}女孩的声音淹没在嘈杂的大巴车，可我还是听得清清楚楚。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她喜欢猫。{/color}"
    nvl_narrator "{color=#e5e5e5}我有去研究过，喜欢猫的女孩子大多数是很善良的女孩子。{/color}"
    nvl_narrator "{color=#e5e5e5}她们或多或少会有一点点敏感。{/color}"
    nvl_narrator "{color=#e5e5e5}她们不会墨守成规，{/color}"
    nvl_narrator "{color=#e5e5e5}但是有时候会非常的懒。{/color}"
    nvl_narrator "{color=#e5e5e5}她们很聪明，可是有时候会很迟钝。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}…..{/color}"
    nvl_narrator "{color=#e5e5e5}收起了笔记本，我长长的叹了一口气。{/color}"
    nvl_narrator "{color=#e5e5e5}类似这样的总结我已经写了很多，但是真正的她又是怎么样的呢？{/color}"
    nvl_narrator "{color=#e5e5e5}思绪中我的目光不由得向她看了过去。{/color}"
    nvl clear

    window hide Dissolve(.7)
    #【场景：车窗】
    $ persistent.cg_c_cc = True
    scene c_车窗 with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}她的名字叫做程祎琳。{/color}"
    nvl_narrator "{color=#e5e5e5}如果第一次看见这个名字很有可能会读错。{/color}"
    nvl_narrator "{color=#e5e5e5}毕竟班上还有许多人叫她程伟林。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}很多人下意识就会把‘祎’这个字的发音读错。{/color}"
    nvl_narrator "{color=#e5e5e5}原本这个字和‘依’是相同的发音，但是却还是有人读成‘伟’字发音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}当然我是绝对不会读错的。{/color}"
    nvl_narrator "{color=#e5e5e5}前提得给我叫出她的名字机会。{/color}"
    nvl_narrator "{color=#e5e5e5}至今我们之间还没有说过话，我可能只是没有找到适宜的——{/color}"
    nvl_narrator "{color=#e5e5e5}能和她拉近距离的契机。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是我觉得总会有办法的，毕竟我们在一个学校里面。{/color}"
    nvl_narrator "{color=#e5e5e5}然后就这样我潜伏一年多了还没有找到合适的机会。{/color}"
    nvl clear

    window hide Dissolve(.7)
    # TODO
    #【CG:妄想1】
    $ persistent.cg_c_wx = True
    scene c_妄想 with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}脑内闪过一丝念想。{/color}"
    nvl_narrator "{color=#e5e5e5}我内心沉淀了起来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}仔细的在脑海里面设想着某一个场景。{/color}"
    nvl_narrator "{color=#e5e5e5}如果事情顺利的话…就能够牵着她的手。{/color}"
    nvl_narrator "{color=#e5e5e5}只要能顺利的和她搭上话的话，那么这一切很快就能成为事实。{/color}"
    nvl clear

    #音效：笑声 男+女）

    w_nvl "{color=#e5e5e5}啊哈哈！！！{/color}"
    nvl_narrator "{color=#e5e5e5}我开始忍不住要笑起来，每次就都是这样。{/color}"
    nvl_narrator "{color=#e5e5e5}还没和人家说一句话，我就已经把happy end都想好了。{/color}"
    nvl clear
    
    window hide Dissolve(.7)
    #【场景：隧道】
    $ persistent.cg_c_sd = True
    scene c_隧道 with dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}就在我这么想的时候。{/color}"
    nvl_narrator "{color=#e5e5e5}突然眼睛一黑，吓我一跳。{/color}"
    nvl_narrator "{color=#e5e5e5}原来是进入隧道了吗？{/color}"
    nvl_narrator "{color=#e5e5e5}我松一口气，我还以为是因为自己的胡思乱想导致老天都看不下去要来整我呢。{/color}"
    nvl clear
    
    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with hpunch
    window show

    #（画面震动，左右摇摆。）

    #（急刹车的音效）
    #音效+撞击音效）

    #【场景：隧道02】
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve

    window show dissolve

    nvl_narrator "{color=#e5e5e5}在思考着发生什么时候，大巴车剧烈的晃动。{/color}"
    nvl_narrator "{color=#e5e5e5}突然就像是做自由转体运动一样，我们所有人的身子都侧了过来。{/color}"
    nvl_narrator "{color=#e5e5e5}没有绑安全带的学生像是被弹射出去了一样一头撞在了车窗的玻璃上。{/color}"
    nvl_narrator "{color=#e5e5e5}刹那间尖叫声和惨叫声像是应景一般的响起。{/color}"
    nvl_narrator "{color=#e5e5e5}我也没有以外的一头撞向了旁边的玻璃。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}在陷入昏睡的时候，我最后一丝想法竟然是这车的玻璃什么材质做的，太硬了吧。{/color}"
    nvl clear

    window hide Dissolve(1)
    #【场景：黑屏】
    #（灰色场景过场）
    #【场景：隧道】（灰色）
    $ persistent.cg_c_sd = True
    scene c_隧道 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}啊？我们这是要去哪里？{/color}"
    nvl clear

    window hide dissolve
    #【场景：大巴车】（灰色）
    $ persistent.cg_c_dbc = True
    scene c_大巴车 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}她怎么也在？{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道2】（灰色）
    $ persistent.cg_c_sd = True
    scene c_隧道 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}发….发生了什么？{/color}"
    nvl clear

    window hide dissolve
    #【场景：承重者】
    $ persistent.cg_c_czz = True
    scene c_承重者 with dissolve
    pause 2
    scene black with Dissolve(2)
    window show dissolve

    nvl_narrator "{color=#e5e5e5}咦？？她没事吧？{/color}"
    nvl clear

    window hide dissolve
    #（色调回归）
    #【场景：侧躺】
    $ persistent.cg_c_ct = True
    scene c_侧躺 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我从昏迷中惊醒。{/color}"
    nvl_narrator "{color=#e5e5e5}最后一幕着实把我吓坏了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}还好这只是一个梦。{/color}"
    nvl_narrator "{color=#e5e5e5}还好….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}就在我松了一口气，以为自己还在教室上课的时候。{/color}"
    nvl_narrator "{color=#e5e5e5}梦中的场景就像是告诉我什么才叫做现实一样展现在我的面前。{/color}"
    nvl clear

    window hide dissolve
    #【场景：灾难现场】
    $ persistent.cg_c_znxc = True
    scene c_灾难现场 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我看着远处的大巴。{/color}"
    w_nvl "{color=#e5e5e5}额…发…发…{/color}"
    nvl_narrator "{color=#e5e5e5}我却说不出话来，身体到处都有着疼痛感，看样子我可能是被甩出了公交车。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}脸上湿哒哒的，我摸了摸似乎还有着未干的血迹。{/color}"
    #音效：水滴声）
    nvl_narrator "{color=#e5e5e5}隧道里面静悄悄的，水滴的声音就好像是死神敲打着乐器一样追上来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}没有风却总有一丝凉意像是蛇一样缠绕过来，让我不禁打了一个寒颤。{/color}"
    nvl_narrator "{color=#e5e5e5}我曾经无数次梦想过这样的场景，{/color}"
    nvl_narrator "{color=#e5e5e5}自己作为某个灾难的幸存者存活下来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}现在我存活下来了，我却只感觉到周身钻心的疼痛。{/color}"
    nvl_narrator "{color=#e5e5e5}有点难受的起身。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}额…额…啊….{/color}"
    nvl_narrator "{color=#e5e5e5}骨头像是要碎掉一样让我不由得呻吟了出来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}饶是如此，我依旧还是站起来。{/color}"
    nvl_narrator "{color=#e5e5e5}我努力告诫自己冷静下来。{/color}"
    nvl_narrator "{color=#e5e5e5}冷静…我要冷静才行。{/color}"
    nvl clear

    window hide dissolve
    #【场景：承重者】（灰色）
    $ persistent.cg_c_czz = True
    scene c_承重者 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}一闪而过的记忆突然出现在我的脑海里面。{/color}"
    nvl_narrator "{color=#e5e5e5}我好像看到了什么。{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道02】
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}对，这个时候得去确定一下隧道里还有没有别人。{/color}"
    nvl_narrator "{color=#e5e5e5}……{/color}"
    nvl clear

    window hide dissolve
    #【场景：黑屏】
    scene black with dissolve

    #【场景：灾难现场】
    $ persistent.cg_c_znxc = True
    scene c_灾难现场 with dissolve

    window show dissolve

    nvl_narrator "{color=#e5e5e5}大量的石块压在了大巴上将大巴的一部分压得扁平了过去。{/color}"
    nvl_narrator "{color=#e5e5e5}微弱的隧道荧光下，我所能看到的视野里面一片狼藉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我仿佛置身于恐怖袭击的现场。{/color}"
    nvl_narrator "{color=#e5e5e5}但是感觉却大不相同。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}喂..有..有人…活着…{/color}"
    nvl_narrator "{color=#e5e5e5}说不出话来。{/color}"
    nvl_narrator "{color=#e5e5e5}我的喉咙像是被什么堵住了一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}本来想着往前面走一步。{/color}"
    nvl_narrator "{color=#e5e5e5}然而这件事情却并没有想象中那么轻松。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}啊….{/color}"
    nvl_narrator "{color=#e5e5e5}我痛苦的呻吟了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}腿上的疼痛瞬间席卷了我的全身，让我不由得靠在墙壁上坐了下来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我喘着气，然后颤抖着把双手轻轻的搭在膝盖的地方——这里是最疼的地方。{/color}"
    nvl_narrator "{color=#e5e5e5}难不成——是断了吗？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}手感觉得到有些发烫，这让我的手触感越发的真实，膝盖变得有点儿肿大。{/color}"
    nvl_narrator "{color=#e5e5e5}我不是很明白这是什么感觉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}在这里我没办法确认时间，周围一切的信息都指向了黑暗。{/color}"
    nvl_narrator "{color=#e5e5e5}而黑暗也像是明白我的意思一样，向我回馈水滴落的声音。{/color}"
    nvl_narrator "{color=#e5e5e5}在这个漆黑的隧道里面，我只感觉到莫名的悲哀。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}有人可以来救救我吗？{/color}"
    nvl_narrator "{color=#e5e5e5}切身处境的我最终想到的是竟然这个。{/color}"
    nvl_narrator "{color=#e5e5e5}有点羞愧，但是也只能如此。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}外边的世界里面肯定已经乱成了一锅粥吧。{/color}"
    nvl_narrator "{color=#e5e5e5}然后会拼了命往这边救援，然后我很快就能获救之类的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}剧本如果是这么写的话，那我就有不得不去做的事情了。{/color}"
    nvl_narrator "{color=#e5e5e5}想到这里，我不由得驱散脑海中想要求救的想法。{/color}"
    nvl clear

    window hide dissolve
    #【场景：承重者】（灰白）
    $ persistent.cg_c_czz = True
    scene c_承重者 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}这一幕的场景再一次划过我的脑海。{/color}"
    nvl_narrator "{color=#e5e5e5}我想起来了，她也出事了。{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道2】
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}现在她怎么样了？{/color}"
    nvl_narrator "{color=#e5e5e5}我不由得突然担心了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}就像是电视剧里面男主人公突然担心起女主人公一样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}只要我这样担心着她应该就不会有事吧。{/color}"
    nvl_narrator "{color=#e5e5e5}我美好的想到。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}隧道里面静悄悄的，没有人走动的声音。{/color}"
    nvl_narrator "{color=#e5e5e5}好像就只有我一个活人一样。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}其实也并没有证据证明我活着。{/color}"
    nvl_narrator "{color=#e5e5e5}如果是的话，隧道不可能这么安静的才对。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}原本只是无聊的幻想，此刻我才真正的陷入了恐惧。{/color}"
    nvl_narrator "{color=#e5e5e5}为什么这种事我还在想着这样的事情啊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}隧道里面只有远处被砸成七零八落的大巴还能看出点轮廓，其余的地方没有别的任何事物。{/color}"
    nvl_narrator "{color=#e5e5e5}怎么想都让人觉得奇怪。{/color}"
    nvl_narrator "{color=#e5e5e5}隧道只有我旅行的大巴车吗？{/color}"
    nvl_narrator "{color=#e5e5e5}应该没可能才对。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}想到这里，腿上的疼痛感变得异常清晰起来。{/color}"
    nvl_narrator "{color=#e5e5e5}我的牙齿不由得上下打颤。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}有…有人在吗！！{/color}"
    nvl_narrator "{color=#e5e5e5}喉咙依旧发不出声音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}好像我突然失声了一般，明明感觉自己说了出来，但事实上却听不到任何声音{/color}"
    nvl_narrator "{color=#e5e5e5}真是糟透了。{/color}"
    nvl_narrator "{color=#e5e5e5}我心情开始烦躁起来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我也知道我此刻是自己在吓自己。{/color}"
    nvl_narrator "{color=#e5e5e5}但是无论如何我都没办法停止脑海里面那絮乱的思绪。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}不知道过了多久，我的意识都变得模糊起来——就在这个时候…{/color}"
    nvl_narrator "{color=#e5e5e5}我却不由自主的站了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}此时的膝盖上的疼痛仿佛被减轻了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}有点儿疲惫；{/color}"
    nvl_narrator "{color=#e5e5e5}好想睡觉啊；{/color}"
    nvl_narrator "{color=#e5e5e5}依旧听不到任何声音，听不到我自己的声音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我安慰着自己没有事的，另一方面不断的在这个地方搜索着。{/color}"
    nvl_narrator "{color=#e5e5e5}且不管当下的情况，至少趁现在自己还有有意识的时候，想办法反抗或者打破这一个场景。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}也不知道家里的老妈怎么样了。{/color}"
    nvl_narrator "{color=#e5e5e5}肯定急的不行才是，不过我现在还活着。{/color}"
    nvl_narrator "{color=#e5e5e5}而且我肯定能活着回去。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}强大的自信心陡然升起，这种自信心真的有时候出现得没有道理。{/color}"
    nvl_narrator "{color=#e5e5e5}毕竟现在就只有我一个人在嘛，我死了谁告诉外边这里面发生了什么。{/color}"
    nvl_narrator "{color=#e5e5e5}因为周边一个人也没有的样子，所以就算是想哭也没有意义。{/color}"
    nvl_narrator "{color=#e5e5e5}所以我必须先想办法活下去，然后在哭——呸，男孩子怎么能随便哭。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然而就在我这么决定之后没多久。{/color}"
    nvl_narrator "{color=#e5e5e5}仿佛像是上天故意的一样。{/color}"
    nvl_narrator "{color=#e5e5e5}我在隧道里面一瘸一拐的走了没有多远的距离，第一个幸存者就出现在了我的面前。{/color}"
    nvl clear

    window hide dissolve
    #【CG：承重者】
    $ persistent.cg_c_czz = True
    scene c_承重者 with dissolve
    window hide dissolve

    nvl_narrator "{color=#e5e5e5}即便是身处黑暗之中。{/color}"
    nvl_narrator "{color=#e5e5e5}她的身影我还是立马就认出来了。{/color}"
    nvl_narrator "{color=#e5e5e5}我连忙一瘸一拐的扑了过去过去。{/color}"
    nvl_narrator "{color=#e5e5e5}想要确认她的情况。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl_narrator "{color=#e5e5e5}虽然很微弱，但是她还在呼吸，胸口微微的在起伏就是证明。{/color}"
    nvl_narrator "{color=#e5e5e5}她还活着，程祎琳还活着。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我心里有点雀跃，这是我醒过来之后遇见的第一个幸存者。{/color}"
    nvl_narrator "{color=#e5e5e5}但是其实我心里还是非常惭愧的。{/color}"
    nvl_narrator "{color=#e5e5e5}我还以为她已经死了。{/color}"
    nvl_narrator "{color=#e5e5e5}幸好没有。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"
    nvl_narrator "{color=#e5e5e5}庆幸是一方面。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我俯下身子。{/color}"
    nvl_narrator "{color=#e5e5e5}想要叫醒她。{/color}"
    nvl_narrator "{color=#e5e5e5}手掌感受得到她的温度。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}此刻的我是什么样的心情呢？我自己也说不清楚。{/color}"
    nvl_narrator "{color=#e5e5e5}只是觉得眼下并不是思考那些事情的时候。{/color}"
    nvl clear

    # TODO
    voice "voice/dlc_voice/c/40.mp3"
    c_nvl "{color=#e5e5e5}……..{/color}"
    #c_nvl "{color=#e5e5e5}（呼吸声）{/color}"

    nvl_narrator "{color=#e5e5e5}她身体的温度似乎有点儿高。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我这么想着把手放到她的额头上——好烫。{/color}"
    nvl_narrator "{color=#e5e5e5}发烧了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}松了一口气的我，不由得看向压在她身上的碎石块，还有许多的碎玻璃渣。{/color}"
    nvl_narrator "{color=#e5e5e5}没怎么多想，我就开始把石头从她的身体上挪开。{/color}"
    nvl_narrator "{color=#e5e5e5}好在这些石头并不是很重，花了一点时间我才清理掉这些石头。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她身上的伤看起来有点儿严重。{/color}"
    nvl_narrator "{color=#e5e5e5}地面上挪开石头之后是一滩一滩的血迹。{/color}"
    nvl_narrator "{color=#e5e5e5}脚踝处一道道触目惊心的割伤看的我心疼。{/color}"
    nvl clear

    #音效：石块掉落）

    nvl_narrator "{color=#e5e5e5}拼着咬牙的劲头，我把她架起来送到隧道边缘处刚好可以坐人的地方。{/color}"
    nvl_narrator "{color=#e5e5e5}原来女孩子的身体是可以这么轻的吗？{/color}"
    nvl_narrator "{color=#e5e5e5}我几乎都感觉不到她身体重量，软绵绵的。{/color}"
    nvl_narrator "{color=#e5e5e5}她迷迷糊糊就跟着我走了。{/color}"
    nvl clear

    window hide dissolve
    #【场景：过道】
    $ persistent.cg_c_ydcq = True
    scene c_营地初期 with dissolve
    window show dissolve

    # TODO
    voice "voice/dlc_voice/c/23.mp3"
    c_nvl "{color=#e5e5e5}哈…哈…（呼气）{/color}"

    nvl_narrator "{color=#e5e5e5}她缓缓的睁开了眼睛。{/color}"
    nvl clear
    voice "voice/dlc_voice/c/39.mp3"
    c_nvl "{color=#e5e5e5}好…好黑啊。{/color}"
    nvl_narrator "{color=#e5e5e5}这是当然的，毕竟这里是隧道。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}额…额….{/color}"
    nvl_narrator "{color=#e5e5e5}还是发不出声音。{/color}"
    nvl clear
    # TODO
    voice "voice/dlc_voice/c/1.mp3"
    c_nvl "{color=#e5e5e5}有谁在吗？{/color}"
    nvl_narrator "{color=#e5e5e5}虚弱的声音从她的嘴里发出来。{/color}"
    nvl_narrator "{color=#e5e5e5}然而我却没有办法回答她。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    voice "voice/dlc_voice/c/28.mp3"
    c_nvl "{color=#e5e5e5}有人…在吗？我的眼睛好疼…{/color}"
    voice "voice/dlc_voice/c/32.mp3"
    c_nvl "{color=#e5e5e5}看不见了。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/1.mp3"
    c_nvl "{color=#e5e5e5}应该有谁在的吧…{/color}"
    # TODO
    voice "voice/dlc_voice/c/3.mp3"
    c_nvl "{color=#e5e5e5}如果你在的话，可以握住我的手吗？{/color}"

    nvl_narrator "{color=#e5e5e5}她伸出手来想要寻找着什么。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}尽管我说不出话来，然而却能清楚的听见她的说的每一个字。{/color}"
    nvl_narrator "{color=#e5e5e5}而直到这个时候我才发现。{/color}"
    nvl_narrator "{color=#e5e5e5}她的眼睛似乎出了一点点问题。{/color}"
    nvl_narrator "{color=#e5e5e5}丝丝血迹顺着她的眼睑流了下来。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}想到这里，我不由得心一疼。{/color}"
    nvl_narrator "{color=#e5e5e5}伸出手握住了她滚烫的手。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}人…总是要握紧什么才能知道自己是存在于这里的。{/color}"
    nvl_narrator "{color=#e5e5e5}而我握紧了她的手。{/color}"
    nvl_narrator "{color=#e5e5e5}若有若无，纤细却依旧能够感受到她。{/color}"
    nvl clear

    c_nvl "{color=#e5e5e5}……{/color}"
    nvl_narrator "{color=#e5e5e5}她很明显的愣了一下。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/37.mp3"
    c_nvl "{color=#e5e5e5}诶..嘿嘿嘿。{/color}"
    nvl_narrator "{color=#e5e5e5}傻傻的朝着我的方向笑了一下。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/25.mp3"
    c_nvl "{color=#e5e5e5}你的手好冷啊。{/color}"
    nvl_narrator "{color=#e5e5e5}然后就像是突然松了一口气一样，闭上了眼睛。{/color}"
    nvl_narrator "{color=#e5e5e5}比之前稍微安稳一点的睡了过去。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这种程度就放心了吗？{/color}"
    nvl_narrator "{color=#e5e5e5}问题很大啊。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}放心吧….{/color}"
    w_nvl "{color=#e5e5e5}我一定会救你出去的。{/color}"
    nvl_narrator "{color=#e5e5e5}虽然嘴上这么说，但是却一句话也发不出来声音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}先去找点吃的，毕竟这种时期。{/color}"
    nvl_narrator "{color=#e5e5e5}运气好的事情是这一次大家是去郊游，所以带了不少的食物才对。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}虽然我只带了几个面包和两瓶水。{/color}"

    nvl_narrator "{color=#e5e5e5}但是其他的同学应该带了不少的零食。{/color}"

    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear

    window hide dissolve
    #【场景：灾难现场】
    $ persistent.cg_c_znxc = True
    scene c_灾难现场 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}隧道的地面大部分都塌陷了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我一瘸一拐的越过了裂缝，朝着巴士走了过去。{/color}"
    nvl_narrator "{color=#e5e5e5}沿途我才发现这里场景是多么的恐怖。{/color}"
    nvl_narrator "{color=#e5e5e5}真是糟糕透了。{/color}"
    nvl clear

    window hide dissolve
    #【场景：过道】
    $ persistent.cg_c_gd = True
    scene c_过道 with dissolve

    pause 3.0

    #【场景：车的尸首】
    $ persistent.cg_c_cdss = True
    scene c_车的尸首 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我所熟悉的那些同学们此刻都鸦雀无声的躺在废墟当中。{/color}"

    nvl_narrator "{color=#e5e5e5}她们有的被石头砸成了两截，有的被深埋在废墟中。{/color}"

    nvl_narrator "{color=#e5e5e5}有的趴在地上一动不动，但是关节全部扭曲以一个诡异的姿势躺在那儿。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}好在光线昏暗，让我的压力减轻了不少。{/color}"

    nvl_narrator "{color=#e5e5e5}她们都很安静。{/color}"

    nvl_narrator "{color=#e5e5e5}但是空气中弥漫的那股腥味还是让我有点不寒而栗，恶心想吐。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}这真是糟糕透了。{/color}"

    nvl_narrator "{color=#e5e5e5}我心里不断念叨着，然后一面前进，这里简直就是地狱。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我强忍着不适爬到了大巴车的侧身，准备从窗户里面跃进去。{/color}"

    nvl_narrator "{color=#e5e5e5}大部分学生的零食都是随身携带的，我必须去搜集这些。{/color}"

    nvl_narrator "{color=#e5e5e5}这是我看了许多灾难片之后得出的结论。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}大巴车散发出来的汽油味很好的缓解了空气中的腥味。{/color}"

    nvl_narrator "{color=#e5e5e5}这让我好受了不少。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我以为外边的场景就是真正的恐怖了。{/color}"

    nvl_narrator "{color=#e5e5e5}谁知道在进入大巴车以后我才发现。{/color}"

    nvl_narrator "{color=#e5e5e5}这里面才是真正的惨无人寰。{/color}"
    nvl clear

    window hide dissolve
    #【场景：车内】
    $ persistent.cg_c_cn = True
    scene c_车内 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}被甩出车内的我究竟有多幸运。{/color}"

    nvl_narrator "{color=#e5e5e5}有部分巨大的石头把大巴车的一节整个给压扁了。{/color}"

    nvl_narrator "{color=#e5e5e5}然后里面当然还有没有来得及逃开的学生。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}三个五个全部被压在了石头下，其中还有几个伤势并不重的女孩。{/color}"

    nvl_narrator "{color=#e5e5e5}如果不是被这个大石头砸中的话，想必她们几个应该也会成为这场灾难的幸存者吧。{/color}"
    nvl clear

    window hide dissolve
    #【场景：食物】
    $ persistent.cg_c_sw = True
    scene c_食物 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}司机那边更加的惨，但是想到了什么我开始在他的残肢里摸索着。{/color}"

    #音效：拉扯肌肉，肌肉碎裂音
    
    nvl_narrator "{color=#e5e5e5}并没有花太多时间我就找到了我想要的东西——手机。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我捂住鼻子，阵阵的恶心开始刺激着我的大脑。{/color}"

    nvl_narrator "{color=#e5e5e5}我只想拿着食物赶紧走人。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我的运气不错，车上确实还有不少食物。{/color}"

    nvl_narrator "{color=#e5e5e5}我尽可能的多拿一些，因为我实在是不想在回这个地方了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}当然那是不可能的。{/color}"

    nvl_narrator "{color=#e5e5e5}不过我还是选择多拿一些。{/color}"

    nvl_narrator "{color=#e5e5e5}于是我就拿了性价比比较高的几个，面包和饼干还有水。{/color}"

    nvl_narrator "{color=#e5e5e5}还顺便把车上的小医疗箱带走了，和车上的车帘给拉扯着带走了。{/color}"

    nvl_narrator "{color=#e5e5e5}在这个地方，上面的红十字显得格外的刺眼。{/color}"
    nvl clear

    window hide dissolve
    #【场景：营地】
    $ persistent.cg_c_yd = True
    scene c_营地 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}没多久我便回到了程祎琳的旁边。{/color}"

    nvl_narrator "{color=#e5e5e5}她还在睡觉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看了看时间，已经是晚上九点多了。{/color}"

    nvl_narrator "{color=#e5e5e5}我看一下日期，稍稍愣住了。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}这已经是我们出行旅行的第二天晚上。{/color}"

    nvl_narrator "{color=#e5e5e5}也就是说我昏迷了接近一天的时间。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}真是糟糕啊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}更何况程祎琳还在发烧。{/color}"

    nvl_narrator "{color=#e5e5e5}发烧并不是什么恐怖的事情。{/color}"

    nvl_narrator "{color=#e5e5e5}但是在这种环境下发烧麻烦就大了。{/color}"

    nvl_narrator "{color=#e5e5e5}治疗发烧的方法有很多种。{/color}"

    nvl_narrator "{color=#e5e5e5}只不过现在我手里一种也没有。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}唯一能做的就只有用酒精帮程祎琳的身体降温。{/color}"

    nvl_narrator "{color=#e5e5e5}缓解病情，除此之外我什么也做不了。{/color}"

    nvl_narrator "{color=#e5e5e5}但是不出意外的话，救援应该很快就能到才对。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}额…额….{/color}"

    nvl_narrator "{color=#e5e5e5}我这么安慰着自己。{/color}"
    nvl clear

    window hide dissolve
    #【CG：灾难现场】
    $ persistent.cg_c_znxc = True
    scene c_灾难现场 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}然而事实是很残酷的。{/color}"

    nvl_narrator "{color=#e5e5e5}我们在这个地方等了很久。{/color}"

    nvl_narrator "{color=#e5e5e5}没有救援。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}期间地面又引发了一次震动，刚好是大巴车的那一块地面直接陷下去了，地面裂缝出来一个十几米高度的大洞。{/color}"

    nvl_narrator "{color=#e5e5e5}大巴车也坠落了下去。{/color}"

    nvl_narrator "{color=#e5e5e5}司机的手机也没有电了。{/color}"

    nvl_narrator "{color=#e5e5e5}最后一次显示的时间是我们已经在这里待过了五天，{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是实际上我并没有任何时间概念，我觉得程祎琳应该也是这样子想的。{/color}"

    nvl_narrator "{color=#e5e5e5}我和程祎琳的情况都开始有些变化了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}程祎琳还好，每天我都会用酒精帮她降温。{/color}"

    nvl_narrator "{color=#e5e5e5}只能用从大巴上扯下来的车帘当做被子给程祎琳盖上。{/color}"

    nvl_narrator "{color=#e5e5e5}只是她每次喝水的时候会喃喃的说着水好冷。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我当然知道发烧是最好还是别喝冷水。{/color}"

    nvl_narrator "{color=#e5e5e5}所以我就把水捂在肚子上，哪怕稍微提高一点温度也好。{/color}"

    nvl_narrator "{color=#e5e5e5}心疼的同时却也无可奈何，只能尽我所能。{/color}"
    nvl clear

    window hide dissolve
    #【CG：饭】
    $ persistent.cg_c_f = True
    scene c_饭 with dissolve
    window show dissolve

    w_nvl "{color=#e5e5e5}吃…吃饭了{/color}"

    nvl_narrator "{color=#e5e5e5}尽管还是发不出声音。{/color}"

    nvl_narrator "{color=#e5e5e5}但是每当我给她递食物的时候她还是能够理解。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她的食量不是很大，一般一个或者半个面包加上一小撮水她就会去接着休息。{/color}"

    nvl_narrator "{color=#e5e5e5}但是这是不行的。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}这种时候我往往会强迫她在吃一些，尽管是没有什么营养的零食。{/color}"

    nvl_narrator "{color=#e5e5e5}但是总比饿着肚子要好。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/10.mp3"
    c_nvl "{color=#e5e5e5}我…我吃饱了。{/color}"

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}我把零食往她手上蹭了蹭，意思就是让她在吃一点。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/26.mp3"
    c_nvl "{color=#e5e5e5}不想吃，谢谢你了。{/color}"

    nvl_narrator "{color=#e5e5e5}她摇着头，惨白的脸上浮现出有些微弱的笑容。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}有时间的时候我们还能够稳定的维持一日三餐的时间。{/color}"

    nvl_narrator "{color=#e5e5e5}但是自从司机大叔的手机没电以后，我就对时间失去了把控。{/color}"

    nvl_narrator "{color=#e5e5e5}因此我们吃饭的时间开始变得不稳定。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}程祎琳肯定是察觉到了什么才突然会自顾自的缩减食量了吧。{/color}"

    nvl_narrator "{color=#e5e5e5}我没有办法向她说明情况。{/color}"

    nvl_narrator "{color=#e5e5e5}因为我的声带似乎出了点问题，只能发出呜呜的声音。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}饶是这样这也已经是我这几天努力的成果了。{/color}"

    nvl_narrator "{color=#e5e5e5}但是这并不重要，我看了看已经开始化脓的膝盖，这里已经感觉不到疼痛了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这也不重要。{/color}"

    nvl_narrator "{color=#e5e5e5}重要的事情是有两件。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}第一件事就是连续好多天没有洗澡了，我身上的味道有点点奇怪。{/color}"

    nvl_narrator "{color=#e5e5e5}第二件事情就是我们的食物没剩多少，我基本上都是隔很长时间才会吃一点。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}总的来说就是我们现在的处境变得更加糟糕了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}我心里埋怨了很多次为什么救援还不来。{/color}"
    nvl clear


    nvl_narrator "{color=#e5e5e5}有过一瞬间很自私的想法。{/color}"

    nvl_narrator "{color=#e5e5e5}如果只有我自己的话，省吃俭用应该能撑一两个月吧…{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}当然我马上甩了甩头把这种想法抛弃到了一边去。{/color}"

    nvl_narrator "{color=#e5e5e5}但是这个想法就像是只恶鬼一样随着时间的流逝缠得我越来越深。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}每每饿的不行的时候，我就会这么想。{/color}"

    nvl_narrator "{color=#e5e5e5}但事实确实如此，如果真的只有我一个人来吃的话。{/color}"

    nvl_narrator "{color=#e5e5e5}根本就不用担心会挨饿的。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}我没法否认这个事情，可是我却因为这个事情而感到愧疚。{/color}"

    nvl_narrator "{color=#e5e5e5}甚至不敢看面前的女孩。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/37.mp3"
    c_nvl "{color=#e5e5e5}嘿嘿…{/color}"

    nvl_narrator "{color=#e5e5e5}突然她笑了一下。{/color}"

    nvl_narrator "{color=#e5e5e5}是想到了什么开心的事情吗？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}啊，好想和她说话啊。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}额..额额…{/color}"

    nvl_narrator "{color=#e5e5e5}然而我却发不出声音。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/5.mp3"
    c_nvl "{color=#e5e5e5}这几天我做了一个梦。{/color}"
    voice "voice/dlc_voice/c/31.mp3"
    c_nvl "{color=#e5e5e5}我梦到我死了。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    voice "voice/dlc_voice/c/46.mp3"
    c_nvl "{color=#e5e5e5}爸爸和妈妈…还有杨静，都围在我的旁边哭。{/color}"
    voice "voice/dlc_voice/c/35.mp3"
    c_nvl "{color=#e5e5e5}我看得见但是没有办法跟她们说话。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}说完她一只手扶住了额头，失声痛哭了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}我看着面前的女孩…只看感觉手指有些发冷。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这种感觉比饥饿还要难受。{/color}"

    nvl_narrator "{color=#e5e5e5}但是现在的我能给她什么呢？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看着漆黑的隧道，热泪盈眶。{/color}"

    nvl_narrator "{color=#e5e5e5}我现在只是扳着手指混时间，兴许下一秒救援应该就会来的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}毕竟出了这么大的事情。{/color}"

    nvl_narrator "{color=#e5e5e5}但是出了这么大的事情，为什么还没有救援到来呢？{/color}"

    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear

    window hide dissolve
    #【CG:拥抱】
    $ persistent.cg_c_yb = True
    scene c_拥抱 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}从来没有发现，原来我喜欢的女孩哭鼻子的时候声音这么小。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}别…别哭了。{/color}"
    nvl_narrator "{color=#e5e5e5}事实上我根本就没有看见过这个女孩哭鼻子啦。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她在我的怀里啜泣着。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/44.mp3"
    c_nvl "{color=#e5e5e5}好冷…{/color}"
    voice "voice/dlc_voice/c/7.mp3"
    c_nvl "{color=#e5e5e5}好疼….{/color}"
    nvl clear
    voice "voice/dlc_voice/c/4.mp3"
    c_nvl "{color=#e5e5e5}这里到底是哪里啊！{/color}"
    nvl clear
    voice "voice/dlc_voice/c/24.mp3"
    c_nvl "{color=#e5e5e5}为什么我什么都看不见….{/color}"
    nvl clear

    voice "voice/dlc_voice/c/6.mp3"
    c_nvl "{color=#e5e5e5}呜呜呜….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}许久之后我才回过神来，这是在平常不可能做到的事情。{/color}"

    nvl_narrator "{color=#e5e5e5}然而在这里却非常的简单。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}或许是这几天无声的交流，让她开始有一点信任我了。{/color}"

    nvl_narrator "{color=#e5e5e5}直到今天才毫无保留的对我露出无比怯弱的模样。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然而我却想到了一件有点儿没法面对的事情。{/color}"

    nvl_narrator "{color=#e5e5e5}她的身体可能已经到极限了。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"

    nvl_narrator "{color=#e5e5e5}很快这个事实就被验证了，没过多久她便睡了过去，紧紧地握住了我的手。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她又笑了起来。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/15.mp3"
    c_nvl "{color=#e5e5e5}你的手，好冰啊。{/color}"
    nvl clear

    window hide dissolve
    #【CG:吃饭】
    $ persistent.cg_c_f = True
    scene c_饭 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}渐渐的她的双手在捏不住饼干。{/color}"

    nvl_narrator "{color=#e5e5e5}渐渐的她的嘴唇在发不出声音。{/color}"

    nvl_narrator "{color=#e5e5e5}就算是像我这么笨的也明白会发生什么事情。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}我…一定会让你活着出去的。{/color}"

    nvl_narrator "{color=#e5e5e5}看着明明在休息却越来越虚弱的女孩，我信誓旦旦的开口说道。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}尽管我知道我已经发不出什么声音。{/color}"

    nvl_narrator "{color=#e5e5e5}不知道是不是巧合。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/12.mp3"
    c_nvl "{color=#e5e5e5}嘿…嘿嘿{/color}"

    nvl_narrator "{color=#e5e5e5}她发出应答的声音，虽然很微弱。{/color}"

    nvl_narrator "{color=#e5e5e5}但是就仿佛就是在回应我的决心一般。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}……..果然……{/color}"

    nvl_narrator "{color=#e5e5e5}果然我没有喜欢错人啊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}坚强的让人心疼。{/color}"
    nvl_narrator "{color=#e5e5e5}坚强的让我心疼。{/color}"
    nvl clear

    window hide dissolve
    #【场景：过道】
    $ persistent.cg_c_gd = True
    scene c_过道 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我吃了半块面包，喝了一口水，就算是把饭吃完了。{/color}"

    nvl_narrator "{color=#e5e5e5}接下来我撕开了自己的裤子，把膝盖上下死死的给绑住。{/color}"
    nvl clear

    #【场景：过道】

    nvl_narrator "{color=#e5e5e5}这些天我发现了一个问题，隧道的两端似乎是被石头崩塌给埋住了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}从大巴坠落的方向来看。{/color}"

    nvl_narrator "{color=#e5e5e5}来的方向要比出隧道近得多。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}也许外卖发生了比里面更惨的事情；{/color}"
    nvl_narrator "{color=#e5e5e5}也许根本就不存在什么救援；{/color}"
    nvl_narrator "{color=#e5e5e5}如果没有人来救我们的话——{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}那就让我来救你吧。 {/color}"
    nvl_narrator "{color=#e5e5e5}哪怕只有一点点希望，我也会玩命帮你抓住的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}你是这么的坚强，我怎么舍得让你就这样死去…{/color}"
    nvl_narrator "{color=#e5e5e5}我喜欢你啊…我好喜欢你。{/color}"
    nvl clear

    window hide dissolve
    scene black with dissolve
    pause 1
    #【场景：洞口】（震动）
    $ persistent.cg_c_dk = True
    scene c_洞口 with vpunch
    window show dissolve

    nvl_narrator "{color=#e5e5e5}啊，这还真是惨了。{/color}"

    nvl_narrator "{color=#e5e5e5}不知不觉我拖着几乎已经残废掉的腿，一点一点的靠近了隧道的入口处。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我没有犹豫。{/color}"

    nvl_narrator "{color=#e5e5e5}捡着石头然后往隧道的裂缝里面扔。{/color}"

    nvl_narrator "{color=#e5e5e5}可能我是个傻子吧。{/color}"

    nvl_narrator "{color=#e5e5e5}妄想着靠自己的一双手挖通这个隧道。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"

    nvl_narrator "{color=#e5e5e5}我先从最小的石子捡起，趴在石碓上把上面可以拿走的石头都扔进裂缝里。{/color}"

    nvl_narrator "{color=#e5e5e5}不知疲倦的重复着这一个动作。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}每扔半个小时我就会休息一会，然后拖着推爬回程祎琳那里。{/color}"

    nvl_narrator "{color=#e5e5e5}小心的给她喂一些吃的。{/color}"

    nvl_narrator "{color=#e5e5e5}然后我自己撕一块面包就当是充饥，然后我便会重新回到被堵住的入口。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这简直就是不可能完成的任务啊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看着面前的石堆。{/color}"

    nvl_narrator "{color=#e5e5e5}真是糟糕透啦！{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}一面抱怨着，一面还是不忘捡着石头往身后的裂缝里面扔。{/color}"

    nvl_narrator "{color=#e5e5e5}但是这样的速度，不知道要做到什么时候去。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}果然我很奇怪吧。{/color}"

    nvl_narrator "{color=#e5e5e5}再说靠一个人的力气怎么可能打得通被堵住的隧道。{/color}"

    nvl_narrator "{color=#e5e5e5}这种想一下就知道不可能的事情我却正在做。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"

    w_nvl "{color=#e5e5e5}但是…{/color}"

    nvl_narrator "{color=#e5e5e5}但是在看到她哭泣的模样之后。{/color}"
    nvl clear

    window hide dissolve
    # TODO
    #【CG:哭泣】（灰白）
    $ persistent.cg_c_yb = True
    scene c_拥抱 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我怎么放弃得了啊。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"

    nvl_narrator "{color=#e5e5e5}眼泪渐渐模糊了我的视野。{/color}"

    nvl_narrator "{color=#e5e5e5}怎么可能放弃的了啊，我喜欢她啊！{/color}"

    nvl_narrator "{color=#e5e5e5}我好喜欢她…{/color}"
    nvl clear

    window hide dissolve
    #【场景：旅行】（灰白）
    # TODO
    $ persistent.cg_c_sd = True
    scene c_隧道 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}如果知道会变成今天这样的话，早知道在车上的时候就应该和她搭话了。{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道】
    $ persistent.cg_c_dbc = True
    scene c_大巴车 with dissolve
    window show dissolve

    w_nvl "{color=#e5e5e5}呼…呼…（喘气声）{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}其实那个时候肯定算不上好的搭话时间段吧。{/color}"

    nvl_narrator "{color=#e5e5e5}毕竟那个时候她正在跟旁边的那谁聊猫的事情。{/color}"

    nvl_narrator "{color=#e5e5e5}她很喜欢猫。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}可恶啊，要不是家里不让养猫，我早就买一只猫养着了。{/color}"

    nvl_narrator "{color=#e5e5e5}早知道会发生今天这种事情的话，就算被打死我也要偷偷养一只。{/color}"
    nvl clear

    window hide dissolve
    #【场景：侧脸】（灰色）
    $ persistent.cg_c_mmdys = True
    scene c_迷茫的眼神 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}突然闪过了另外一个画面。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我想起来了。{/color}"

    nvl_narrator "{color=#e5e5e5}那是我和她第一次见面时候的表情。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}高中刚入学的时候，我晚了两天入学。{/color}"

    nvl_narrator "{color=#e5e5e5}别人已经排好座位，相互熟悉的时候，我却还在火车上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}陌生的环境，陌生的班级。{/color}"

    nvl_narrator "{color=#e5e5e5}自我介绍得环节我显得有点紧张。{/color}"

    nvl_narrator "{color=#e5e5e5}我紧张的时候整个人的眼睛乱瞟，然后我一生难忘的场景就在这样的情况下出现了。{/color}"

    nvl_narrator "{color=#e5e5e5}我想这应该是我这辈子看过最美的侧目吧。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她看着窗外，完全没有听我自我介绍的意思（一看就知道不是什么爱学习的学生）{/color}"

    nvl_narrator "{color=#e5e5e5}事实上后面也证明了她就是一个完全不爱学习的女孩。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}白色的衬衫穿在她的身上感觉很合适，要我说的话…{/color}"

    nvl_narrator "{color=#e5e5e5}我很在意她。{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道】
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    w_nvl "{color=#e5e5e5} 啊哈…{/color}"

    nvl_narrator "{color=#e5e5e5}呼着气，肚子又饿了，我已经不知道做了多久。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}石堆像是没怎么减少一样。{/color}"

    nvl_narrator "{color=#e5e5e5}拖着有些不适的腿，再一次回到了她所在的地方。{/color}"
    nvl clear

    window hide dissolve
    $ persistent.cg_c_yd = True
    scene c_营地 with dissolve
    window show dissolve

    voice "voice/dlc_voice/c/19.mp3"
    c_nvl "{color=#e5e5e5}……{/color}"
    voice "voice/dlc_voice/c/41.mp3"
    c_nvl "{color=#e5e5e5}回…回来了吗？{/color}"

    nvl_narrator "{color=#e5e5e5}她好像知道我离开了。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}额…{/color}"

    nvl_narrator "{color=#e5e5e5}我支支吾吾两声，示意我在。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/33.mp3"
    c_nvl "{color=#e5e5e5}是去找吃的吗？{/color}"

    nvl_narrator "{color=#e5e5e5}不是的…虽然我想要说，但是不知道为何却说不出口。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/38.mp3"
    c_nvl "{color=#e5e5e5}这样吗….{/color}"
    voice "voice/dlc_voice/c/16.mp3"
    c_nvl "{color=#e5e5e5}没找到啊……{/color}"

    nvl_narrator "{color=#e5e5e5}她好像擅自的理解了什么。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}女孩微微的笑了笑，躺下的时候整个人变得更加的虚弱了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}仿佛刚刚那几句话就已经用尽她全部的力气一般。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}喂…{/color}"

    nvl_narrator "{color=#e5e5e5}不是你想的那样啊。{/color}"

    nvl_narrator "{color=#e5e5e5}但是我却并没有办法反驳她。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看了看食物袋，里面所剩的零食和水没有多少了。{/color}"

    nvl_narrator "{color=#e5e5e5}叹了口气，确实我也有在路上搜罗食物就是。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}就这样好像过了好几天的样子。{/color}"

    nvl_narrator "{color=#e5e5e5}我的时间概念已经开始变得很模糊了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}累了就回来睡。{/color}"

    nvl_narrator "{color=#e5e5e5}姑且我就是靠着自己睡的次数计算天数。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}程祎琳则是每次会在我回来的时候会和我说上一句‘回来了？’这样的话。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}不知怎么的，我竟然会感觉这样还挺幸福的。{/color}"

    nvl_narrator "{color=#e5e5e5}而这份幸福环绕在我身边我却怎么也握不住。{/color}"

    nvl_narrator "{color=#e5e5e5}因为它随时都有可能会消失。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}该放弃吗？我靠在墙壁，吃着程祎琳吃剩下的面包屑。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}会有这种想法的我真是幼稚。{/color}"

    nvl_narrator "{color=#e5e5e5}我扶了扶脑袋。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}而就在这个时候，程祎琳翻过身来。{/color}"

    nvl_narrator "{color=#e5e5e5}我以为她会像往常一样问候一声‘回来了’之类的…{/color}"

    nvl_narrator "{color=#e5e5e5}虽然说嘴上说是像往常一样，其实这个过程也没有进行多少次。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是今天好像和往常不太一样。{/color}"

    nvl_narrator "{color=#e5e5e5}她只是虚弱的笑了笑。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/45.mp3"
    c_nvl "{color=#e5e5e5}诶嘿嘿…{/color}"
    voice "voice/dlc_voice/c/48.mp3"
    c_nvl "{color=#e5e5e5}那个…{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}看她一脸为难的模样，难不成是想上厕所了吗？{/color}"
    nvl clear

    voice "voice/dlc_voice/c/23.mp3"
    c_nvl "{color=#e5e5e5}……{/color}"
    voice "voice/dlc_voice/c/11.mp3"
    c_nvl "{color=#e5e5e5}稍微有点点疼….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她在说什么？{/color}"

    nvl_narrator "{color=#e5e5e5}嘴上说疼干嘛笑起来了。{/color}"

    nvl_narrator "{color=#e5e5e5}这时候开玩笑很奇怪吧。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/8.mp3"
    c_nvl "{color=#e5e5e5}好想睡觉…可以睡觉吗？{/color}"

    w_nvl "{color=#e5e5e5}……{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}可以啊…当然可以，事实上你一整天都在睡啊。{/color}"

    voice "voice/dlc_voice/c/30.mp3"
    c_nvl "{color=#e5e5e5}已经可以了吧。{/color}"

    w_nvl "{color=#e5e5e5}…..{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}嗯？{/color}"

    nvl_narrator "{color=#e5e5e5}什么可以了？{/color}"
    nvl clear

    voice "voice/dlc_voice/c/2.mp3"
    c_nvl "{color=#e5e5e5}已经不用在努力了吧。{/color}"

    nvl_narrator "{color=#e5e5e5}你在说什么啊？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她蹒跚的爬了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}颤颤巍巍的在黑暗中摸索着。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}为了防止她摔倒，我伸出了手托住了她的身体。{/color}"

    nvl_narrator "{color=#e5e5e5}然而在下一个瞬间。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她就失去了重心倒了下去。{/color}"
    nvl clear

    window hide dissolve
    #【场景：隧道】
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}慌张之中，我连忙把她从地上扶了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}但是无奈腿根本就使不上力气。{/color}"
    nvl clear

    window hide dissolve
    $ persistent.cg_c_wcbq = True
    scene c_卧床不起 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}只能勉强把她扶到了原来的位置上。{/color}"

    nvl_narrator "{color=#e5e5e5}让她躺了下来，车帘再一次盖在她的身上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我的手抚上了她的额头。{/color}"

    nvl_narrator "{color=#e5e5e5}好烫，我连忙从医疗箱里面拿出了所剩不多的酒精，打湿碎布，然后放到她的额头上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}不知不觉的时候她已经病得这么严重了吗？{/color}"

    nvl_narrator "{color=#e5e5e5}她伸出已经脏兮兮的手，抓住了我衣服的一角。{/color}"

    nvl_narrator "{color=#e5e5e5}她努力的睁着眼睛，似乎想要看清我一样。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/29.mp3"
    c_nvl "{color=#e5e5e5}还是看不见，哈啊…{/color}"
    voice "voice/dlc_voice/c/43.mp3"
    c_nvl "{color=#e5e5e5}你要活下去啊….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她的话语就像在告别一般。{/color}"

    nvl_narrator "{color=#e5e5e5}抓住我衣角的手渐渐失去了力气。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我慌张的抓住了她的手，她却笑了起来。{/color}"

    nvl_narrator "{color=#e5e5e5}苍白脸庞下的笑容，让我浑身都了鸡皮疙瘩。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这种时候还在笑什么的，你是傻子吗？{/color}"

    nvl_narrator "{color=#e5e5e5}……{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}等我….{/color}"

    nvl_narrator "{color=#e5e5e5}我竭尽全力，突破了声带的限制，轻轻放下紧握住的手。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}嘶哑的声音终究还是发出来。{/color}"

    nvl_narrator "{color=#e5e5e5}少女短暂的惊愕并没有停留多久时间。{/color}"

    nvl_narrator "{color=#e5e5e5}随着眼角一丝泪水的滑落，她缓缓的闭上了眼睛。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}…….{/color}"

    #【场景：隧道】（奔跑）
    window hide dissolve
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我早该发现了，她一直在默默的忍受痛楚。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}她的伤势比我只重不轻，为什么我早没有意识到呢？{/color}"

    nvl_narrator "{color=#e5e5e5}一厢情愿的以为她只是普通的发烧而已。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}有人在吗？{/color}"

    nvl_narrator "{color=#e5e5e5}我拼命的在隧道里面制造响声。{/color}"
    nvl clear

    voice "voice/dlc_voice/c/42.mp3"
    nvl_narrator "{color=#e5e5e5}有谁在吗？？？{/color}"

    nvl_narrator "{color=#e5e5e5}我朝着隧道入口处的地方一瘸一拐的跑了过去。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}那里有着被我挖出来的一个深洞。{/color}"

    nvl_narrator "{color=#e5e5e5}怎么可能会让你就这样死在这里。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}之前的我都在做什么啊！{/color}"

    nvl_narrator "{color=#e5e5e5}明明有那么的多时间。{/color}"

    nvl_narrator "{color=#e5e5e5}为什么才挖到这里啊！{/color}"
    nvl clear

    window hide dissolve
    $ persistent.cg_c_sd2 = True
    scene c_隧道2 with dissolve
    window show dissolve

    w_nvl "{color=#e5e5e5}啊…{/color}"

    nvl_narrator "{color=#e5e5e5}我就像是不要命了一样，双手在石堆里面疯狂的盘着石头，期间还有不少碎石从我的头顶砸下。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}稍微不小心的话，我可能就会被落下来的石头给砸伤。{/color}"

    nvl_narrator "{color=#e5e5e5}但是这都已经无所谓了。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}拜托了请让我救救她吧。{/color}"

    nvl_narrator "{color=#e5e5e5}很快我就精疲力竭了，可是即便如此我也努力的扒着斜坡上碎石。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我想要救她。{/color}"

    nvl_narrator "{color=#e5e5e5}只要救她就好，我死了也没关系。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}救救她吧！{/color}"

    nvl_narrator "{color=#e5e5e5}不是我也没关系，谁来救救她吧！！{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}神啊，如果你在的话就救救她吧。{/color}"

    nvl_narrator "{color=#e5e5e5}我什么都给你，求求您救救她吧。{/color}"

    nvl_narrator "{color=#e5e5e5}眼眶里面热热的。{/color}"
    nvl clear

    window hide dissolve
    #【场景：落石】
    $ persistent.cg_c_ls = True
    scene c_落石 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}就在我大意的时候，头顶上一块巨大的，尖锐的三角形一样的石块迎着斜坡砸了下来。{/color}"

    nvl_narrator "{color=#e5e5e5}慌乱之中我只是头朝着边上撇了一下，然而这块石头却直接朝着我的肚子扎了过来。{/color}"
    #音效：肌肉破碎 ）
    nvl clear

    nvl_narrator "{color=#e5e5e5}无数次想过餐桌上鸡鸭鱼被开肠破肚的感觉。{/color}"

    nvl_narrator "{color=#e5e5e5}想不到居然是这样子的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}好痛好痛好痛！{/color}"
    nvl_narrator "{color=#e5e5e5}好痛好痛好痛好痛好痛好痛！{/color}"
    nvl_narrator "{color=#e5e5e5}好痛好痛好痛好痛好痛好痛好痛好痛！！！{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}呜啊！！！啊啊啊啊啊啊！！！！{/color}"

    nvl_narrator "{color=#e5e5e5}腹部传来撕裂般疼痛，身体以下瞬间就没了知觉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}然而就在这个时候，在我的正上方一束月光照了下来。{/color}"
    nvl clear

    unknown_nvl "{color=#e5e5e5}这里还有幸存者，重伤。{/color}"

    nvl_narrator "{color=#e5e5e5}声音顺着洞口传了下来。{/color}"
    nvl clear

    window hide dissolve
    #【CG:至死之人】
    $ persistent.cg_c_zszr2 = True
    scene c_至死之人2 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}似乎有人影随着绳索跳跃了下来。{/color}"

    nvl_narrator "{color=#e5e5e5}他们似乎再用无线电说着什么话。{/color}"

    nvl_narrator "{color=#e5e5e5}然而这个时候的我已经开始意识陷入模糊。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}他们在说什么来着？总之我这是获救了？{/color}"

    nvl_narrator "{color=#e5e5e5}额不对，还没有她还没有获救。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}救…救…{/color}"

    nvl_narrator "{color=#e5e5e5}我微张着嘴，也不知道有没有发出声音。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}救救她…她…还活着….{/color}"

    nvl_narrator "{color=#e5e5e5}一只有力的手握住了我伸出的手。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}瞬间我的眼泪就流了下来。{/color}"

    nvl_narrator "{color=#e5e5e5}好冷…我好冷…{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}好冷好冷好冷好冷好冷好冷好冷好冷好冷！{/color}"

    nvl_narrator "{color=#e5e5e5}好害怕好害怕好害怕好害怕好害怕好害怕好害怕好害怕！{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……{/color}"

    nvl_narrator "{color=#e5e5e5}我紧紧的握住这双手…我也好想得救…我也好想得救。{/color}"
    nvl clear

    unknown_nvl "{color=#e5e5e5}没事的…一切都会好起来的。{/color}"

    w_nvl "{color=#e5e5e5}…..{/color}"
    nvl clear

    window hide dissolve
    #【场景：迷茫的眼神】
    $ persistent.cg_c_mmdys = True
    scene c_迷茫的眼神 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}一切都会好起来吗？{/color}"

    nvl_narrator "{color=#e5e5e5}对啊，救我们的人已经来了，一切都会好起来的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我之后就能跟她搭话了。{/color}"

    nvl_narrator "{color=#e5e5e5}啊哈哈…..{/color}"
    nvl clear

    window hide dissolve
    #【场景：回归02】
    $ persistent.cg_c_hg = True
    scene c_回归 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}果然还是要表白会比较好吧…{/color}"

    nvl_narrator "{color=#e5e5e5}也不对….这个时候可不是搭话的好机会，还是等下一次吧。{/color}"

    nvl_narrator "{color=#e5e5e5}于是我咧了咧满是鲜血的嘴，用着嘶哑恍惚的声音这么说道。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}……笔…笔…{/color}"

    nvl_narrator "{color=#e5e5e5}她的故事还很长，不能没有眼睛啊。{/color}"
    nvl clear

    window hide dissolve
    #【场景：至死之人2】
    $ persistent.cg_c_mmdys = True
    scene c_迷茫的眼神 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}我突然想到，如果未来过着看不见的生活肯定会很痛苦吧。{/color}"
    nvl_narrator "{color=#e5e5e5}紧握住我手的人连忙为我拿来了纸和笔。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}颤颤巍巍的我写下了一个捐之后就在没有了力气。{/color}"

    nvl_narrator "{color=#e5e5e5}能理解吗？如果能理解就好了呢。{/color}"
    nvl clear

    #【场景：至死之人2】（灰色）

    nvl_narrator "{color=#e5e5e5}还有好多事情没有做，明明还有好多事情没有做。{/color}"

    nvl_narrator "{color=#e5e5e5}眼泪止不住的涌出眼眶。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}可是——果然还是觉得好寂寞。{/color}"

    nvl_narrator "{color=#e5e5e5}好寂寞啊…..{/color}"
    nvl clear

    window hide dissolve
    #【场景：星空】
    $ persistent.cg_c_xk = True
    scene c_星空 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}意识正在渐渐的远去。{/color}"

    nvl_narrator "{color=#e5e5e5}恍惚之中，似乎有这样一句话在我的耳边响起——{/color}"
    nvl clear

    window hide dissolve
    scene black with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}“如果她死了，那么我的故事也就结束了；如果我死了，她的故事还长得很。”{/color}"
    nvl clear

    window hide dissolve
    #【场景：黑屏】
    scene black with dissolve

    ##
    #【CG：雨中的女孩】
    $ persistent.cg_c_yz = True
    scene c_雨中 with dissolve
    window show dissolve

    nvl_narrator "{color=#e5e5e5}原本这应该只是一场梦的。{/color}"

    nvl_narrator "{color=#e5e5e5}无数雨点打在我的身上。{/color}"

    nvl_narrator "{color=#e5e5e5}我望着漆黑的天空。{/color}"
    nvl clear

    w_nvl "{color=#e5e5e5}（咦？这是？）{/color}"
    w_nvl "{color=#e5e5e5}喵……{/color}"

    nvl_narrator "{color=#e5e5e5}然而我却没有发出声音{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我仿佛被谁抱在怀里。{/color}"

    nvl_narrator "{color=#e5e5e5}这是…什么情况？{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我看着少女。{/color}"

    nvl_narrator "{color=#e5e5e5}她紧紧的将我抱在怀里。{/color}"

    nvl_narrator "{color=#e5e5e5}然而我却莫名的觉得有些违和。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这份违和渐渐的放大。{/color}"

    nvl_narrator "{color=#e5e5e5}就像是忽然张开的幕布，朝我围了起来。 {/color}"

    nvl_narrator "{color=#e5e5e5}这一定是有什么地方出现了问题。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}就在我这么想着的时候，阵阵的黑暗将我整个包裹起来。{/color}"

    nvl_narrator "{color=#e5e5e5}啊，我记起来了。{/color}"
    nvl_narrator "{color=#e5e5e5}这个女孩不就是我自己吗？{/color}"
    nvl clear
    
    jump c3_2_c