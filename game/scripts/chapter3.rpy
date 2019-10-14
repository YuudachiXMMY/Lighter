default c3_select = False
default c3_c1_l_select = False
default c3_c1_c_select = False
default c3_c1_x_select = False
default c3_2_l_select = False
default c3_3_l_select = False
default c3_2_c_select = False
default c3_2_x_select = False
default c3_4 = False
default c3_end1_select = False
default c3_end2_select = False

label c3:

    $c3_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve
    
    narrator "【距离诅咒发作还剩两天】"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0
    
    #场景：黑屏
    scene black with dissolve

    narrator "我要死掉了…绝对要死掉了。"
    narrator "身上传来的剧烈的疼痛感，仿佛整个骨头都要散架了一样。"
    w "唔猫…."
    narrator "欸？我还能听到自己的声音？"

    #场景：医院走廊
    
    scene yy_走廊 with dissolve:
        zoom .667

    narrator "挣扎着睁开了眼睛。"
    w "……."
    narrator "稍微有点熟悉的场景出现在我的面前。"
    narrator "跟林琴的房间有点相像，但是又有点不一样的地方。"
    narrator "应该是病房。"
    narrator "我才床上坐了起来。"
    narrator "感觉身体有点紧绷，还有点微疼。"
    narrator "我这是怎么了。"
    narrator "最后还记得的事情就是疼得要死…."
    narrator "啊，这还真是不好的回忆。"
    narrator "病房的外边传来了很吵闹但是却很熟悉的声音。"
    w "……"
    narrator "干什么这么吵啊？"
    show l 普通07 at ct with dissolve
    l "她到底怎么了，你说清楚点。"
    "男人的声音" "小姐…这个女孩真的只是疲劳过度了而已。"
    "男人的声音" "为什么会出现这样的症状我们也不清楚。"
    "男人的声音" "我们已经成立专家组专门研究这个症状了。"
    "男人的声音" "夏教授也在这里，她可以证明我们说的说正确的。"
    narrator "林琴看一眼夏静，夏静则是点头。"
    show l 普通08 at ct with dissolve
    l "我没让你解释那么多，你就说有没有解决方案吧。"
    "男人的声音" "这个…专家们还在评估。"
    show l 普通07 at ct with dissolve
    l "……"
    # TODO
    show l normal_9_8:
        linear .3 xpos 1.0 xanchor 1.0
    l "唉，算了你走吧。"
    "男人的声音" "好…好的。"
    narrator "疑惑着我的听着门外的有些忐忑的脚步声，渐渐的走远了。"
    show l 普通07 at rt with dissolve
    l "到底是怎么样？"
    show x 无奈01 at lt with dissolve
    x "什么怎么样？"
    show l 注视08 at rt with dissolve
    l "当然是里面那家伙。"
    show x 考虑01 at lt with dissolve
    x "我怎么知道，医生不是说了她只是疲劳过度了吗？"
    show l 惊异03 at rt with dissolve
    l "跟死了一样还能算疲劳过度？"
    show x 闭眼 at lt with dissolve
    x "但是她的体温是正常的，心跳也是正常的，所有的数据显示都是正常的。"
    show x 普通01 at lt with dissolve
    x "除了相信这个答案还能有什么别的解释吗？"
    narrator "夏静的平静的语气里头似乎带了一丝不易察觉的微妙腔调。"
    show l 普通08 at rt with dissolve
    l "那个什么鬼专家的评审会你不是也参加了么？"
    show l 不满07 at rt with dissolve
    l "你就得出这么个结论？"
    show x 普通03 at lt with dissolve
    x "我已经尽力了。"
    show x 怜悯01 at lt with dissolve
    x "那个评议会开大半个晚上，还不如直接给她一剂镇静剂管用。"
    show l 普通07 at rt with dissolve
    l "……."
    show c 恶心01 at ct with dissolve
    c "还没有尽力，还有办法的。"
    narrator "一直没有说话的女孩子突然发出了声音。"
    show l 普通08 at rt with dissolve
    l "……"
    show x 考虑01 at lt with dissolve
    x "……"
    show x 考虑02 at lt with dissolve
    x "倒不如说你手上的伤是怎么回事？"
    show c 惊讶01 at ct with dissolve
    c "欸？"
    show c 惊讶02 at ct with dissolve
    c "没…没事。"
    show c 侧视01 at ct with dissolve
    c "不小心弄伤的。"
    show c 斜视01 at ct with dissolve
    c "医生说没有伤到骨头所以没关系的，不过可能以后会留疤。"
    show l 普通09 at rt with dissolve
    l "意外的很严重…."
    show c 侧视01 at ct with dissolve
    c "没问题的啦，只是小伤而已。"
    show c 斜视01 at ct with dissolve
    c "我比较担心艳仔现在的情况。"
    show c 侧视01 at ct with dissolve
    c "我觉得一定会有办法的……"
    show x 反驳02 at lt with dissolve
    x "那你说说办法是什么？"
    show x 反驳01 at lt with dissolve
    x "这个地方已经是整个地区最厉害的医院了。"
    show x 反驳03 at lt with dissolve
    x "那几个最厉害的医生教授开会讨论一晚上病情。"
    show x 反驳02 at lt with dissolve
    x "现在还在讨论，没有结果。"
    show x 考虑02 at lt with dissolve
    x "我觉得没有办法了。"
    show x 考虑01 at lt with dissolve
    x "只能等她自己恢复过来了。"
    show l 普通08 at rt with dissolve
    l "就那样也能恢复过来？"
    hide l with dissolve
    hide c with dissolve
    hide x with dissolve
    narrator "……."
    w "……."
    narrator "她们三个丫头在吵什么东西。"
    narrator "不对，我突然想起了一件事——那个丫头怎么样了？"
    narrator "那个和我同甘共苦但是却不幸先走一步了的名叫做袁艳的丫头。"
    w "我大概会怀念她的…."
    narrator "当然….是开玩笑的。"
    narrator "这家伙要真挂了我该怎么办啊？"
    narrator "不过等一下…袁艳去哪里了？"
    narrator "不会还在家里吧。"
    narrator "我发动了力量感应了一下。"
    w "……."
    narrator "怎么好像就在附近？"
    narrator "我能感受到她的气息。"
    narrator "不会吧，袁艳难不成在外头跟那三个丫头努力磋商？"
    narrator "不愧是袁艳，真的敬业啊。"
    w "怎么可能呢！！！！"
    narrator "我自己吐槽起了自己。"
    narrator "不由得低下了头。"
    narrator "然后就看到了缠满绷带的自己——咦咦咦？"
    narrator "这都是什么鬼东西啊！！！"
    narrator "绑得特别紧，几乎没办法动弹，动作太大还特别疼。"
    narrator "这是哪门子的捆绑游戏啊。"
    narrator "我咧开嘴撕咬着身上的绷带——这味道…"
    w "唔噜噜…."
    narrator "然而…不断观察周围的我却愣住了。"
    narrator "在我的旁边，另外的一张床上，有一个女孩坐在那里——她就坐在那里，面无表情，手里还端着一杯水。"
    w "……."
    w "袁艳？你….原来在的啊。"
    w "啊哈哈…."
    narrator "我怪不好意思的松开了自己的嘴，然后看着袁艳说道。"
    narrator "没有回应。"
    narrator "这家伙怎么了？"
    narrator "我稍微朝着她那边爬了爬…仔细的观察起了袁艳。"

    # TODO 1
    #[CG：少女的躯壳]
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_yot = True
    scene cg_少女的躯壳 with Dissolve(2):
        zoom .667
    
    pause 1.0
        
    w "不是吧…."
    narrator "…."
    narrator "这才第几天啊。"
    narrator "袁艳低着头，眼睛里没有任何身神采。"
    narrator "身体的生命气息还存在，但是灵魂的气息已经消失了。"
    narrator "我睁大了眼睛注视着袁艳。"
    narrator "想不到诅咒降临得这么快，真的是快出了我的想象。"
    narrator "我不由得抹了抹眼睛。"
    narrator "事已至此，我已经没有退路可以走了。"

    #[CG：结束]
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    scene bf_白天 with dissolve:
        zoom .667

    w "不是，应该是我们没有退路可以走了。"
    w "袁艳…想不到这种关键时候你居然倒了。"
    narrator "我摇了摇头。"
    w "所以说最后还不是得靠我嘛。"
    narrator "然后我跳下了床，先把袁艳叫醒吧，这种状态越久越不安全啊。"
    w "哎哟…."
    narrator "爬…爬不起来了…好痛…"
    
    scene yy_走廊 with dissolve:
        zoom .667

    show l 惊异03 at ct with vpunch
    l "里面有声音？"
    show x 考虑01 at rt with dissolve
    x "嗯？"
    show c 惊讶01 at lt with dissolve
    c "嗯？"
    w "……."

    scene bf_白天 with dissolve:
        zoom .667
    
    narrator "我刚从床上掉到地上，门外的三个女孩就急冲冲的冲进了病房。"
    narrator "速度快得我无法想象。"
    narrator "但是，在看到袁艳的瞬间三个人眼里一闪而过的失望色彩我看的清清楚楚。"
    narrator "拜托…你们倒是先看看病猫啊！"
    narrator "我才是受伤的那只好吗？床上那个根本就是没睡好加诅咒的暂时灵魂离体啊！"
    show c 惊讶02 at ct with dissolve
    c "啊…猫掉到地上了。"
    narrator "唯独只有程祎琳指着我说道。"
    narrator "我这个时候真想大声叫一声…."
    narrator "程祎琳走过来把我抱了起来，轻轻的重新放回了床上。"
    narrator "她手上缠了好几圈跟我身上一样的纱布…她受伤了吗？"
    narrator "也就是说在那双纤细的双手上缠绕着的纱布下有着跟我身体一样的痛感吗——我坐在床上碰了碰被纱布缠起来的地方。"
    w "唔…."
    narrator "好痛…."
    show c 侧视01 at ct with dissolve
    c "诶呵呵…."
    narrator "程祎琳笑嘻嘻的用双手撑着脑袋趴在床上看着我。"
    show l 慌张07 at rt with dissolve
    l "唉…."
    narrator "林琴则是叹了一口气，像是在看没出息的孩子一样。"
    show l 不满09 at rt with dissolve
    l "程祎琳啊，你别忘了这可是袁艳的猫。"
    show c 斜视01 at ct with dissolve
    c "嗯，知道。"
    show x 惊讶03 at lt with dissolve
    x "我看你一点自觉都没有，记得别把猫吃了哦。"
    show l 惊异03 at rt with dissolve
    l "……."
    narrator "林琴无语的看了看夏静，那表情好像在说，‘你说的什么鬼啊，哪里会有人想要吃猫的啊。’"
    show c 侧视01 at ct with dissolve
    c "嗯，不会的。"
    show l 慌张07 at rt with dissolve
    l "……."
    narrator "林琴更无语的看了看程祎琳，那表情好像在说，‘还真打算吃啊喂！’"
    narrator "最无语的是我。"
    narrator "你们在我面前啊，能不能不要这么明目张胆的讨论一些危险的事情啊。"
    narrator "好歹顾及一下我的感受啊。"
    show l 注视08 at rt with dissolve
    l "不过这丫头还是一点反应都没有呢。"
    narrator "林琴走了过去，把袁艳手里的一杯水抽了出来放在桌上。"
    show x 假笑01 at lt with dissolve
    x "累得魂都不在了吧。"
    narrator "夏静也靠近了袁艳的身边，把她慢慢的往床上推倒。"
    narrator "就像是在搬运人偶一样，帮她鞋子脱好了放到了床上。"
    w "……"
    narrator "我在后面看着，她们是闹的哪一出啊。"
    narrator "拜托你们快点离开这里吧，我要把袁艳那丫头给叫醒啊。"
    narrator "但是事实上…这三个家伙就像赖在这里了一样根本就不打算离开。"
    narrator "既然这样，那我也无能为力了。"
    narrator "袁艳加油…."
    narrator "只能有些同情的看了一眼面无表情的袁艳，然后在程祎琳的注视下蜷成一团打了一个哈欠。"
    narrator "老实说我还有点累，要不先睡一下？"
    narrator "好主意….反正袁艳也活过来了，也没有那么担心了。"
    narrator "心里放轻松的时候，整个猫都变得慵懒了起来。"
    narrator "………"
    narrator "然后就是一阵奇怪的凉风吹了过来。"
    w "喵？"
    narrator "我疑惑的抬了抬头看着周围。"
    narrator "那三个女孩百无聊赖的在那里有一句没一句的搭着话。"
    narrator "时不时还回过头来看看袁艳。"
    narrator "场景没有什么奇怪的才对….但是我就是觉得哪里违和。"
    narrator "我有种奇怪的感觉…这附近还有什么多余的存在。"
    narrator "不会是我暴露了吧。"
    narrator "我咽了口唾沫，不是吧….我没有跟人类说话啊。"
    narrator "惊疑的我不停的朝着周围张望。"
    hide x
    hide l
    hide c
    show x 普通02 at lt with dissolve
    x "嗯？"
    narrator "夏静似乎也感觉到了什么东西，朝着房间的某一处看了过去。"
    narrator "那种眼神就像是看到了什么不该看到的东西一样。"
    show x 普通01 at lt with dissolve
    x "今天…怎么只有一个。"
    narrator "她似乎很疑惑。"
    narrator "听她这么说我反而更加疑惑了。"
    w "…."
    show l 普通07 at rt with dissolve
    l "你在看什么鬼？"
    show x 普通02 at lt with dissolve
    x "像你这样的女人是看不到的，因为脑子太空了。"
    show l 普通08 at rt with dissolve
    l "哦呵？你是想打架吗？"
    show x 普通03 at lt with dissolve
    x "抱歉，没空。"
    narrator "夏静耸了耸肩，但是眼睛并没有看着林琴。"
    show l 普通07 at rt with dissolve
    l "你到底在看什么？"
    show x 考虑01 at lt with dissolve
    x "我也不太清楚，只是能看到而已。"
    show l 注视07 at rt with dissolve
    l "看到什么？"
    show x 考虑02 at lt with dissolve
    x "这个房子里头有鬼。"
    show l 惊异03 at rt with dissolve
    l "啥？"
    show c 张嘴01 at ct with dissolve
    c "欸？"
    narrator "林琴听到后一脸懵，反倒是程祎琳突然一惊，好像听到了什么不得了的事情一样。"
    narrator "毛都竖了起来。"
    narrator "反应这么大干什么？"
    show c 张嘴02 at ct with dissolve
    c "夏…小静，你刚刚…刚刚说什么？"
    show x 考虑01 at lt with dissolve
    x "我说这个房间有鬼。"
    show c 惊讶01 at ct with dissolve
    c "嘶….额…."
    narrator "程祎琳像是听呆了一样。"
    hide c with dissolve
    show l 惊异03 at rt with dissolve
    l "我说你没毛病吧，大白天的。"
    show x 假笑01 at lt with dissolve
    x "……."
    show x 闭眼 at lt with dissolve
    x "所以我才说你这样脑袋空空的女人无知。"
    show l 普通07 at rt with dissolve
    l "哦呵…看来你是真的想跟我打一架呢。"
    show x 嘲笑02 at lt with dissolve
    x "啊呀呀呀…看来这位大小姐是真的不知道天高地厚呢。"
    show x 嘲笑01 at lt with dissolve
    x "跟我打架真的没关系吗？我跆拳道已经黑带毕业了噢。"
    show l 普通09 at rt with dissolve
    l "哦呵呵呵…真不知道是谁目中无人呢，你在上届散打冠军面前是不是太放肆了点？"
    show c 惊讶02 at ct with dissolve
    c "欸…原来这里有鬼的吗？"
    w "……"
    narrator "这三个丫头是真的厉害，各种意义上的厉害我都不知道该怎么评价她们。"
    narrator "反倒是夏静所说的‘鬼’我很感兴趣。"
    narrator "我记得这个世界人的说法‘鬼’其实就是灵魂而已…."
    narrator "灵魂….鬼…"
    narrator "嗯…."
    narrator "鬼？灵魂？"
    narrator "emmmmm…."
    narrator "我好像明白了什么…."
    narrator "……."
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    
    w "……."
    narrator "她果然在这里。"
    narrator "我看着病房床的那边，一个半透明化的女孩子站在那里，哭得一把鼻涕一把眼泪的。"
    w "我说…袁艳。"
    w "额…."
    show y 无措 at ct with dissolve:
        alpha .85
    y "欸？"
    show y 无措 at ct with vpunch:
        alpha .85
    y "哇！！！！"
    narrator "这个女孩突然就扑了过来，一阵凉风吹了过来。"
    narrator "啊…刚刚的风原来是这么回事啊。"
    narrator "袁艳的双手从我的身体里头穿了过去，我无奈的摇了摇头。"
    w "这里你是碰不到我的啦。"
    w "还有你哭什么啊？"
    show y 不爽02 at ct with dissolve:
        alpha .85
    y "别胡说.我没哭！"
    show y 不爽01 at ct with dissolve:
        alpha .85
    y "死猫！"
    w "……"
    narrator "这个丫头的嘴还是这么犟。"
    w "我好歹也是猫精灵…"
    show y 不爽02 at ct with dissolve:
        alpha .85
    y "怎么这个时候才来…"
    w "……"
    narrator "看着弱弱的袁艳，我反而觉得不好意思了起来。"
    w "不…不好意思，我来晚了。"
    narrator "……"

    scene bf_白天 with dissolve:
        zoom .667

    show c 张嘴02 at ct with dissolve
    c "猫睡着了？"
    w "欸？"
    narrator "房间里头程祎琳的声音响了起来。"
    show x 考虑02 at rt with dissolve
    x "嗯？那个矮一点的鬼出现了。"
    show l 普通07 at lt with dissolve
    l "哈？你在说什么鬼？"
    show c 张嘴01 at ct with dissolve
    c "咿！！！！！"
    narrator "程祎琳吓得不轻。"
    show c 惊讶01 at ct with dissolve
    c "在…在哪里？"
    show x 考虑02 at rt with dissolve
    x "……."
    show l 普通07:
        linear .3 xpos .25 xanchor .25
    show c 惊讶01:
        linear .3 xpos .75 xanchor .75
    show x 考虑01:
        linear .3 xpos 1.25 xanchor 1.25
    show y 正常04 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    narrator "夏静指着我和袁艳在的地面，然后若无其事的说道。"
    show x 考虑01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "就在那里一动不动。"
    w "……"
    y "……."
    w "！！！！！？"
    show y 无措 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "？？？？"
    narrator "我和袁艳彼此对视了两秒钟，然后瞬间意识到了事情的严重性。"
    show y 无措 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "哇哇哇哇哇啊！！！我就知道她能看得见我们！"
    w "不会吧不会吧不会吧！！！！"
    narrator "我们两个同时抓狂了起来。"
    show x 惊异 with dissolve:
        xpos 1.25 xanchor 1.25
    x "啊，那两个鬼在到处晃。"
    show c 张嘴01 with dissolve:
        xpos .75 xanchor .75
    c "咿！！！！！！"
    narrator "程祎琳再一次被吓得不行了。"
    w "…."
    w "不过等一下…."
    show y 恼火04 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "啊？"
    w "这事之前好像也发生过吧。"
    w "我说我们惊讶个啥？"
    show y 恼火05 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "……"
    show y 恼火04 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "好像确实是这样，世界上就是有能看到灵魂的人存在。"
    show y 恼火06 with dissolve:
        alpha .85 xpos -.25 xanchor -.25
    y "再一次认识到这个事实总是有点吃惊呐。"
    w "第一次听到的时候我也很吃惊就是了。"
    show x 惊异 with dissolve:
        xpos 1.25 xanchor 1.25
    x "啊，那两个又停下来不动了。"
    show c 张嘴01 with dissolve:
        xpos .75 xanchor .75
    c "唔咿？？？！？！？"
    w "……"
    narrator "我无语的看着另外那三人其中的两个。"
    w "不过你是怎么回事啊？"
    narrator "我看着袁艳，想问问她昨天晚上到底发生了什么。"
    hide x
    hide c
    hide l
    show y 正常05 at ct with dissolve:
        alpha .85
    y "不是跟你说了吗？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我两天都没睡了吧。"
    w "所以呢？"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "你到底懂不懂一个两天没睡的人会怎么样啊？"
    w "会特别想睡觉？"
    show y 恼火02 at ct with dissolve:
        alpha .85
    y "那不是废话吗！"
    w "……"
    show y 恼火01 at ct with dissolve:
        alpha .85
    y "我是说…"
    show y 恼火02 at ct with dissolve:
        alpha .85
    y "三天不睡就会死人的你懂吗。"
    show y 恼火05 at ct with dissolve:
        alpha .85
    y "你懂我的意思了吗？"
    w "好像懂了…又好像什么都没听懂。"
    show y 恼火06 at ct with dissolve:
        alpha .85
    y "……"
    show y 恼火04 at ct with dissolve:
        alpha .85
    y "啊，算了，跟你解释实在是太费脑子了。"
    show y 恼火03 at ct with dissolve:
        alpha .85
    y "你就这样保持不懂的节奏就行了。"
    show y 恼火06 at ct with dissolve:
        alpha .85
    y "其实我也没期待你能懂什么的。"
    w "额…."
    w "虽然我听不太懂你在说什么，但是总觉得你说得很过分啊喂！"
    show y 嘲讽04 at ct with dissolve:
        alpha .85
    y "额呵呵呵…."
    show y 嘲讽05 at ct with dissolve:
        alpha .85
    y "所以你能解释一下我现在的情况吗？"
    narrator "袁艳看了看周身，似乎现在的灵魂状态令她十分的疑惑。"
    narrator "疑惑是很正常的。"
    w "哼哼，这你就不知道了吧。"
    show y 恼火05 at ct with dissolve:
        alpha .85
    y "我是不知道，你呢？"
    w "那还用说吗？"
    narrator "我当然不知道…."
    narrator "虽然我自己知道答案，但是这个时候说出来会不会有点不太好。"
    narrator "看着袁艳有点将信将疑的表情…这个时候示弱的话一定会被她看不起的。"
    w "我当然是知道的啦！"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "你知道些什么啊，倒是说来听听？"
    w "咳咳，是这样子的…"
    w "因为…你看诅咒发作不是只剩下几天了吗…."
    show y 正常04 at ct with dissolve:
        alpha .85
    y "所以呢？"
    w "是这样子的…."
    narrator "能够明显感觉到大脑在颤抖，这就是思考的力量吗？"
    w "其实这是诅咒即将降临的预告…"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "啊？"
    narrator "袁艳歪了歪脑袋表示自己完全不懂。"
    w "你的身体已经开始有预告了，诅咒开始侵犯你的身体了。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "…."
    show y 正常02 at ct with dissolve:
        alpha .85
    y "虽然你说得很有道理…."
    show y 正常01 at ct with dissolve:
        alpha .85
    y "但是能别说得这么恶心吗？"
    narrator "袁艳嫌弃的裹了裹自己的衣服…衣服原来也有灵魂的吗？"
    narrator "嘛….这倒不是重点。"
    narrator "重点是…."
    w "我说你注意的点是不是有点偏差？？？"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "说吧，你继续。"
    w "……."
    narrator "说是让我继续，可是继续什么啊…都是我编的啊。"
    w "咳咳，总之就是说这个情况就是诅咒提前降临的原因啦。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "这样吗…"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "我还以是因为我之前灵魂离开身体的次数太多了。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我的身体守不住灵魂了呢。"
    w "还有这种解释的吗？"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "你那么惊讶干什么？"
    w "额…不是，我是说怎么可能呢？诶嘿嘿…."
    narrator "原来还有这种解释…我怎么就没想到呢。"
    narrator "我苦恼的挠了挠脑袋，不过已经解释了，那只有一条路走到黑了。"
    narrator "做好决定之后，我坚定的看着袁艳。"
    w "当然…这些都是小事。"
    w "重要的是我们的时间不多了。"
    w "再有一个日落的时间我们可能就结束了。"
    w "差不多该做决定了。"
    narrator "我朝着三个还在吵闹的三个女孩看了过去。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "说的是啊。"
    narrator "袁艳的声音在房间里头长长的回荡着…虽然只有我听得见。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "点火的话…会发生什么呢？"
    narrator "袁艳看着我，仿佛知晓了这是最后的时刻一般说道。"
    w "……"
    w "这个点一次的话你就知道了。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "这样吗？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "现在我还有办法回到身体里头去吗？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "我还想再跟她们说两句话看看。"
    w "我试试…."
    narrator "于是便发动了力量。"

    #场景：黑屏
    scene black with dissolve

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    w "……"
    narrator "回来的感觉有点跟往常不太一样。"
    show l 普通08 at lt with dissolve
    l "想不到医院还有这样的虫子，整天就知道理论。"
    show x 反驳02 at rt with dissolve
    x "那还真是对不起了，这家医院许多实验成果都建立在虫子的理论上呢。"
    show c 侧视02 at ct with dissolve
    c "唔…唔…."
    narrator "这三个丫头怎么聚在一起就开始闹，还有…."
    narrator "这个程祎琳怎么一直抱着我…."
    narrator "身体并没有挣脱她怀抱的力气。"
    w "……"
    narrator "算了。"
    narrator "我看了看袁艳之前所在的方向。"
    narrator "不出所料，那里什么都没有。"
    narrator "但是我却知道。"
    narrator "她就在那里。"
    narrator "没有把她带回来，说明事情非常的严重了。"
    show c 侧视01 at ct with dissolve
    c "啊.猫醒了。"
    show x 考虑02 at rt with dissolve
    x "嗯？咦？消失了？"
    w "……"
    narrator "这个对话刚好在这一时刻响起，吓得我瞬间冷汗都出来了。"
    narrator "不过好在夏静似乎跟林琴吵架已经到了关键时刻。"
    narrator "并不是很注意她所看到的东西和程祎琳嘴里说的话之间的联系。"
    narrator "程祎琳….完全就不用担心就是了。"
    narrator "她温柔的摸了摸我的头，我则是眯着眼睛瞟了她一眼。"
    narrator "没有什么情况…."
    narrator "好，继续过去。"
    
    #场景：黑屏
    scene black with dissolve

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    show c 张嘴02 at rt with dissolve
    c "啊…它又睡了？"
    w "……."
    hide c window dissolve
    show y 正常02 at ct with dissolve:
        alpha .85
    y "……."
    show y 正常03 at ct with dissolve:
        alpha .85
    y "你好像很舒服呢。"
    narrator "袁艳酸酸的说道。"
    w "别胡说，我只是动不了了而已。"
    narrator "我这么反驳道。"
    show y 恼火02 at ct with dissolve:
        alpha .85
    y "哼，关系还真好呢。"
    show y 恼火01 at ct with dissolve:
        alpha .85
    y "你干脆跟那傻丫头回家过日子吧。"
    w "我说你突然生什么气啊。"
    narrator "……."
    hide y with dissolve
    show x 惊讶03 at rt with vpunch
    x "啊…又出现了。"
    narrator "夏静朝着我的方向注视着，发出了有些疑惑的声音。"
    show l 惊异03 at lt with dissolve
    l "哈？从刚开始你就在说什么鬼？"
    show x 惊讶01 at rt with dissolve
    x "我怎么知道是什么鬼，山海经你不知道自己去查吗？"
    show l 普通09 at lt with dissolve
    l "我可没有那个心情，也没有时间。"
    show x 考虑02 at rt with dissolve
    x "难怪到现在都还是个无知的家伙呢。"
    narrator "……."
    narrator "看到她们俩又莫名其妙的吵上之后，我突然又放松了起来。"
    narrator "这几个丫头真是…让人莫名其妙的家伙啊。"
    hide x with dissolve
    hide l with dissolve
    show y 正常05 at ct with dissolve:
        alpha .85
    y "这几个家伙…真是让人莫名其妙的家伙啊。"
    narrator "袁艳准确的复述出了我内心的想法。"
    narrator "我看了一眼袁艳。"
    w "不然的话就不会出现在这里了。"
    w "正是因为如此…你的选择才非常重要啊。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "真的….额，我有几个问题想问你。"
    w "都到这时候还有什么想问的？你问呗，反正你问了我也不见得能回答就是了。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "嘛…就是…就是说…."
    show y 正常04 at ct with dissolve:
        alpha .85
    y "选对了我们就能活下来吗？"
    w "那不是废话吗。"
    w "就是三选一的选择题噢！"
    narrator "我郑重的说道。"
    w "选错了就会死去。"
    w "但是选对了就能活下去。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "活下去你打算去干什么呢？"
    w "哈？当然是….没想过。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "嘛，现在还有时间，要不先想想再说？"
    narrator "袁艳笑眯眯的这么跟我说道。"
    w "……."
    w "我说你又在打什么主意啊。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我能打什么主意啊。"
    w "你就不能快点选一个吗？"
    w "都观察这么久了，总有答案吧。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "……."
    w "喂，说话啊。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "……"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "你催命啊。"
    w "嗯。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "就不能为了让我维持一下平常心，好好配合我一下？"
    show y 恼火04 at ct with dissolve:
        alpha .85
    y "死猫，你到底有没有点大局观啊！"
    w "大局观是什么东西？"
    show y 嘲讽04 at ct with dissolve:
        alpha .85
    y "是我不好，不该一直跟你讲人才能听懂的话。"
    narrator "袁艳跟我好好的道起了歉。"
    narrator "但是这个道歉一点歉意都没有。"
    w "好吧好吧…说起来你要是选对了那我还有一大堆事情要做呢。"
    w "你以为我很闲啊。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "是吗？那说来听听，你都忙些啥。"
    narrator "看着像是打算跟我长聊而坐在地上的袁艳…的灵魂。"
    w "嘛，就是一些善后工作，之后就要踏上旅程了。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "你要走了吗？"
    w "那是肯定的，我不可能只待在这里，实在是太危险了。"
    w "而且只要跟人类说话我就死定了。"
    w "不管我在族内的地位有多么高，私下跟人类传达信息仍旧是禁止的。"
    w "所以我必须离开人类的世界。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "那你不是跟我说话了吗？"
    w "额…."
    narrator "要不要跟这个丫头说实话呢….看着她的眼神。"
    narrator "我想了一下，还是说了吧。"
    w "你不一样，你已经不是普通的人类了。"
    w "你见过有哪个人类能用这种状态存活吗？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "我是没见到啦，也不想见到。"
    w "总之，你已经不是人了。"
    show y 不爽01 at ct with dissolve:
        alpha .85
    y "你才不是人啊！"
    w "我本来就不是人。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "……."
    show y 正常04 at ct with dissolve:
        alpha .85
    y "很微妙的在这方面你居然是对的，简直了。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "不过虽然是这样，但是你咒我不是人很过分耶！"
    w "我虽然诅咒了你，但是这个诅咒可没你想象得那么简单的。 "
    show y 正常04 at ct with dissolve:
        alpha .85
    y "哈？"
    w "你在被诅咒的瞬间起就已经不是人类了噢。"
    narrator "袁艳神色严峻，似乎在等着我的解释。"
    w "否则我跟你说话的时候，我就已经死了。"
    w "我还存在就是最好的证明。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "喂喂，你这么说很没说服力啊，如果我不是人的话，那我是什么啊？"
    w "点灯使呗。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "啥玩意？"
    w "点灯使！！！"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "我耳朵有点不太好使，你能在讲一遍吗？"
    w "就是点灯使，之后要跟我永远在一起的点灯使。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "……"
    narrator "袁艳似乎还是很吃惊….嘛，只要活下来她迟早还是会知道的，只要活下来。"
    w "就是一个很麻烦的东西啦。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "打住，我讨厌麻烦，你别说了。"
    w "……."
    w "这种时候麻烦你不要怕麻烦啊！！！"
    narrator "我夸张的叫着。"
    narrator "………"
    w "现在解释也没啥用就是了。"
    w "不过之后我是说如果我们选对了，然后活下来的话…."
    show y 正常02 at ct with dissolve:
        alpha .85
    y "话？"
    w "要跟我一起去旅行吗？"
    w "到很远很远的地方去。"
    show y 无措 at ct with dissolve:
        alpha .85
    y "哇！！是很远的地方吗？"
    w "嗯，是相当相当远的地方。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "……."
    narrator "袁艳眼睛直勾勾的看着我，我好像已经得到了答案——她不会去的吧。"
    narrator "仿佛已经听到了声音一样。"
    narrator "她的话，肯定会那样做吧。"
    narrator "不知道为什么自己已经接受这个答案了。"
    w "不去的话可能会有一点点惩罚，但也不是什么大事。"
    narrator "其实，我也没有很多期待啦，她要是跟我一起踏上旅程的话。"
    narrator "倒也不是很讨厌。"
    narrator "毕竟我一只猫的话可能会有点无聊，带个宠物在路上倒也不错。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我不太理解你在说啥。"
    show y 笑容01 at ct with dissolve:
        alpha .85
    y "不过….如果是带着一只宠物去旅旅行的话。"
    show y 笑容02 at ct with dissolve:
        alpha .85
    y "我倒是挺有兴趣的。"
    w "……."
    narrator "好像跟我想到一块去了。"
    narrator "这个袁艳跟我有时候莫名其妙的会很有默契，这种感觉，还挺不错的。"
    narrator "不过…."
    w "喂！！你说的宠物是谁啊？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "不就是你吗？"
    w "我看起来像宠物吗！！！"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "你不就是的吗？"
    w "我都跟你说了多少次了！"
    w "我是猫精灵啊！！精灵啊！！"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "对对对，就是一点出息都没有的精灵。"
    w "你是几个意思啊！"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "……."
    w "……"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "不过你要去干什么啊？"
    w "当然是有事啊，你以为我像你整天那么闲啊。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "这句话我可就不能当作没听见了。"
    show y 不爽02 at ct with dissolve:
        alpha .85
    y "你倒是说说我哪里闲了？"
    w "……"
    narrator "这个东西还要我说么。"
    narrator "看了你这几天的生活我都不想说什么了。"
    w "不是我想说你，我是连对你叹气都觉得无语。"
    w "好了好了，你差不多该做出选择了吧。	"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "好像是的呢…."
    narrator "我背对着身后病房里头的三个女孩子，然后正视着袁艳说道。"
    w "说吧。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "欸…."
    show y 正常04 at ct with dissolve:
        alpha .85
    y "现在一定要做出选择吗？"
    w "不然你还想拖到什么时候去啊？"
    w "我们只剩两天了啊。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "明天和后天吗？"
    w "……."
    show y 正常01 at ct with dissolve:
        alpha .85
    y "这不是还有两天的时间吗？"
    w "我说你到底在纠结个什么鬼啊。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "总觉得….总觉得还差点什么，再给我一点时间可以吗？"
    w "就算你这么说…."
    w "给你时间是没问题啦，但是这样子的你还能做什么呢？"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "……."
    narrator "袁艳皱着眉头，似乎在苦恼着。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "还能让我回去吗？不用多久，只要能够回去一会儿。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "在跟她们说上几句话我可能就能够做出判断了。"
    w "……."
    narrator "我看着袁艳。"
    w "你确定？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我有必须需要确定的事情。"
    w "有件事我必须提前告诉你。"
    narrator "袁艳看了看我，没有说话，看来是打算等我直接说了。"
    w "诅咒的征兆已经降临了，虽然跟真正的诅咒不一样。"
    w "但是也是一般人所无法承受得了的东西。"
    w "现在你的状态是最安全的。"
    w "这样你也打算回去吗？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "啊？你在说什么鬼？"
    w "总之就是说你无论如何也想要回去咯？"
    show y 恼火04 at ct with dissolve:
        alpha .85
    y "废话那么多干什么，你就说能不能回去吧。"
    w "回去啊….可以的吧，我会试试。"
    show y 恼火05 at ct with dissolve:
        alpha .85
    y "……."
    w "会发生什么我可管不了的哦。"
    show y 恼火03 at ct with dissolve:
        alpha .85
    y "行了行了，别废话了，什么时候能把我送回去。"
    w "我试试就是了呗。"
    narrator "之前回去并没能成功的把她的灵魂带回去。"
    narrator "也就是说平常的方法行不通了吗？"
    narrator "针对性的试试看好了。"

    #场景：黑屏
    scene black with dissolve

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    narrator "抱着这样的想法，我又回到了自己的身体。"
    w "……"
    narrator "又回来了呢，我朝着袁艳看看。"
    narrator "她没有醒，看样子这一次应该是失败了。"
    show c 侧视01 at ct with dissolve
    c "唔，乖乖。"
    narrator "似乎是看到我睁眼了，程祎琳的手轻轻的抚摸上了我的脑袋。"
    narrator "被摸得眼睛眯了起来。"
    narrator "然而我这个时候根本就没精力理会这个丫头。"
    narrator "于是，我又闭上了眼睛。"
    
    #场景：黑屏
    scene black with Dissolve(.7)
    narrator "现在必须得想办法把袁艳重新带回这个世界。"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    show y 正常05 at ct with dissolve:
        alpha .85
    y "…."
    show y 正常04 at ct with dissolve:
        alpha .85
    y "失败了吗？"
    w "失败了。"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "不会再也回不去了吧。"
    w "失误而已，在多试几次就可以了。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "噢噢噢，是吗？那就拜托你了。"
    w "哼，你就放心的在这里看着我吧。"
    narrator "我故作镇定的说道，但其实我自己的也不知道该怎么办。"
    narrator "只要多尝试几次应该就有办法了吧。"
    narrator "大概是这样子….大概…."
    narrator "第五次失败…"
    narrator "……."
    narrator "第十次失败…."
    narrator "袁艳坐在一旁的地上，双手撑着自己的下巴。"
    show y 嘲笑 at ct with dissolve:
        alpha .85
    y "我说…你到底行不行啊。"
    w "下一次一定可以的。"
    show y 嘲讽01 at ct with dissolve:
        alpha .85
    y "这都快二十来次了，你不累我看着都累，先歇会吧。"
    w "不用你管。"
    narrator "其实我自己也是知道的，这么尝试下去也不是个办法。"
    narrator "必须得另辟蹊径，不然现在就是白白的浪费时间。"
    narrator "但是….我看了看袁艳，她还在那里不以为然。"
    narrator "这家伙还真是能那么轻松的坐在那里呢——倒是来体谅体谅一下我这边啊。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "我可不是不体谅你这边。"
    narrator "袁艳就像是猜透了我的心思一样说道。"
    w "我说…我们两个在某个时候还真是莫名其妙的有默契呢。		"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "默契什么的我倒是不知道，，如果实在不行的话就别勉强了。"
    narrator "虽然我也是这么想的，但是总觉得咽不下这口气呢。"
    w "不过你回去是打算干什么啊？"
    narrator "休息中的我漫不经心的问道。"
    narrator "袁艳看了看我，叹了一口气又停下了动作。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "死猫，其实现在回不回去都没所谓，只要我做出正确的选择然后你来点火就行了吧？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "再说我现在回去我也不知道怎么面对这三个家伙。"
    narrator "我顿了顿，点了点头，虽然还有些细节不对，但是这个时候我也没有必要纠正她，毕竟确确实实是由我来主导。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "话说我这个状态有什么优势吗？比如观察更多的东西什么的。"
    narrator "优势？能有什么优势？死得比别人更快一点？还是能看到自己肉体是怎么消亡的？"
    narrator "仔细想想好像还真的有。"
    w "被你这么一说好像还真的有。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "是什么是什么？"
    w "比较多就是了。"
    w "比如说能比别人死得更快一点。"
    w "能看到自己的死亡之类的。"
    w "或者是偷窥别人隐私之类的。"
    w "或者说是到处飞之类的，或者你感兴趣的话也可以跟别的灵魂交流之类的。"
    narrator "袁艳无语的表情已经说明了这些情报对她来说一点作用都没有。"
    narrator "只见她叹了一口气。"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "这些都什么玩意啊，要是能知道她们以前发生了什么就好了。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "可是咱们又不会穿越时空。"
    w "这倒是。"
    narrator "就算用我的力量也不可能让时光倒流，而且就算能回去你也体会不到她们的感受啊。"
    w "……"
    narrator "但是我仔细回想了一下。"
    narrator "好像也不完全是没有办法。"
    w "那个…袁艳呀…你的意思是只要体会她们的感觉就可以了吗？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "嗯？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "啥意思？"
    w "我是说你只要体会到她们以前经历了什么就可以了吗？"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "唔，差不多就是那样吧。"
    w "额…那个我可能有个办法。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "瞧把你能的，你有什么办法？"
    w "只要让你们的灵魂同步就可以了啊！"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "那是什么鬼？"
    w "总而言之就是能让你体会一下她们之前经历过的事情，不知道你愿不愿意…."
    w "你看，你现在不是也刚好回不去了吗。"
    w "暂时变成别人活着不是也挺好的吗？"
    show y 正常05 at ct with dissolve:
        alpha .85
    y "……"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "你够了。"
    narrator "虽然她嘴上这么说，但是实际上她还是陷入了思考。"
    show y 正常02 at ct with dissolve:
        alpha .85
    y "好吧好吧，反正也没有什么别的办法了。"
    w "……"
    show y 正常03 at ct with dissolve:
        alpha .85
    y "……"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "那么要怎么做？"
    w "额…"
    narrator "我仔细回想了一下。"
    w "不过我的力量有限，你最多只能选择一个女孩子了。"
    w "而且还得在特定的时间。"
    show y 正常01 at ct with dissolve:
        alpha .85
    y "额…现在就做判断？"
    w "这个你就当做是预选吧，就算错了也没关系的。"
    w "然后在从剩下的两个人之中选择一个。"
    w "有一半可能是对的。"
    show y 恼火02 at ct with dissolve:
        alpha .85
    y "那你为什么不早点跟我说这种事情啊！"
    w "……"
    w "之前我还以为不用这种办法就能选出来的。"
    w "咳咳咳，好了好了，那么你打算选择谁呢？"
    show y 恼火03 at ct with dissolve:
        alpha .85
    y "……."
    narrator "袁艳的眼睛在三个皱着眉头的女孩身上扫了一眼，她选择了——"

    menu:
        "林琴":
            jump c3_c1_l
        "夏静":
            jump c3_c1_x
        "程祎琳":
            jump c3_c1_c

label c3_c1_l:

    $c3_c1_l_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve
    
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我觉得林琴的可能性比较大，就她了。"
    nvl_narrator "{color=#e5e5e5}我看着一脸认真袁艳。{/color}"
    w "你认真的？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "嗯，很真，我要怎么做？"
    w "等天色暗下来再说吧。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "……"

    #$narrator = nvl_narrator

    $renpy.music.set_volume(1.5, delay=0.2, channel="voice")
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/程依琳.wav" loop fadein 2.0 fadeout 2.0

    nvl clear

    window hide

    #【场景：病房】
    scene bf_白天 with dissolve:
        zoom .667

    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}事实上从现在算起到晚上并没有发生什么特别的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}倒是我和灵魂状态下的袁艳有一句没一句的搭话一直到了晚上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}其实到头来我也不知道和她聊了些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看着她的眼神，我觉得她跟我想的也差不了多少。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}看着袁艳一脸恍惚的模样，我觉得她可能跟我想得一样，完全不知道在聊些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看了看已经渐渐暗下的天空，三个女孩中其中的两个已经离开病房。{/color}"
    nvl_narrator "{color=#e5e5e5}只有林琴还留在这里，她似乎并不打算离开。{/color}"
    nvl_narrator "{color=#e5e5e5}而且她留在这里好像是那三个女孩商量好的一样。{/color}"
    nvl clear

    window hide dissolve

    show l 普通08 at ct with dissolve
    l "……"
    
    hide l with dissolve
    window hide
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}林琴则是看着躺在床上的‘袁艳’看了许久。{/color}"
    nvl_narrator "{color=#e5e5e5}我则是和袁艳对视一眼，完全不知道她在想什么。{/color}"
    nvl clear

    window hide dissolve
    show y 嘲讽02 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/36.mp3"
    y "她倒是自在，死猫什么时候可以开始？"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}我看看窗外已经完全暗下来的景象。{/color}"
    nvl_narrator "{color=#e5e5e5}心里默默计算着时间。{/color}"
    nvl clear

    w "在稍微等一会儿吧，得等她睡下才行。"
    nvl_narrator "{color=#e5e5e5}说完我也没有理会袁艳嘴里的不满。{/color}"
    nvl_narrator "{color=#e5e5e5}因为我知道现在还不是时候。{/color}"
    nvl_narrator "{color=#e5e5e5}想要灵魂同步，这种状态下肯定是不行的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}在这期间我和袁艳再一次有一句没一句的搭话起来。{/color}"
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是事实上，林琴她睡觉倒是睡得特别的早。{/color}"
    nvl_narrator "{color=#e5e5e5}我和袁艳也没聊多久的天，虽然大多数都是聊的这几天发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}再然后就是找她讨要报酬一直在讨价还价。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这家伙也太小气了。{/color}"
    nvl_narrator "{color=#e5e5e5}枉费我那么大的力气找人就她，结果她居然表示最多十盒不能再多了。{/color}"
    nvl_narrator "{color=#e5e5e5}这人简直过分得可以。{/color}"
    nvl clear

    w "准备好没？"
    nvl_narrator "{color=#e5e5e5}虽然说是要让袁艳体验一下林琴以前发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}但是像是灵魂同步这样恐怖的事情能不能做到我心里也没有底。{/color}"
    nvl_narrator "{color=#e5e5e5}只是印象中突然出现的方法，刚好在近期想起来的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}万一方法是错的话，那我脸就丢大了。{/color}"
    nvl_narrator "{color=#e5e5e5}丢脸还是小事，可能小命都会丢掉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我一脸谨慎的看着袁艳，结果她一副完全都不放在心上的样子。{/color}"
    nvl_narrator "{color=#e5e5e5}明明自己都变成灵魂状态了，转眼间就适应也有点太过分了吧。{/color}"
    nvl clear

    window hide dissolve
    show y 恼火02 at ct with Dissolve(.7)
    voice "voice/dlc_voice/c/18.mp3"
    y "你看这都快一点了，我很早就开始问你什么时候开始了吧。"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}袁艳甚至还有点点不满的看着我。{/color}"
    nvl clear

    window hide dissolve

    w "好吧好吧，你躺到床上去。"

    show y 正常03 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/47.mp3"
    y "知道了。"

    hide y dissolve
    
    w "……."
    nvl_narrator "{color=#e5e5e5}看着袁艳熟练的动作，我有些无语。{/color}"
    nvl_narrator "{color=#e5e5e5}忘记跟她说明了。{/color}"
    nvl clear

    w "不是躺倒你自己的床上去啦，是躺倒她的床上。"
    nvl_narrator "{color=#e5e5e5}我指着林琴的床，示意袁艳上错床了。{/color}"
    nvl_narrator "{color=#e5e5e5}袁艳皱了皱眉毛，并没有说什么，出奇的配合。{/color}"
    nvl_narrator "{color=#e5e5e5}然后走到睡在林琴的床边，微微的犹豫一下，看我一眼。{/color}"
    nvl clear

    window hide dissolve
    show y 正常02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/27.mp3"
    y "怎么做？"

    hide y with dissolve

    w "躺下。"
    w "可能会有点点烫，但是放心。"
    w "不会有生命危险的。"
    nvl clear
    
    nvl_narrator "{color=#e5e5e5}袁艳再次皱眉，但是她并没有多说话。{/color}"
    nvl_narrator "{color=#e5e5e5}仅仅的爬上床，她的眼神里多是疑惑。应该是对自己为什么能爬上床感到疑惑吧。{/color}"
    nvl_narrator "{color=#e5e5e5}不过我也没有和她解释的意思，只要她想就可以了。{/color}"
    nvl clear

    window hide dissolve
    show y 正常04 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/22.mp3"
    y "接下来呢？"

    hide y dissolve
    window hide

    w "躺倒她的身体里面去就可以了。"

    window hide dissolve
    show y 正常05 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/13.mp3"
    y "你疯了吧？"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}说着袁艳又坐起来了，指着身后已经熟睡的林琴惊呼道。{/color}"
    nvl clear
    
    w "大惊小怪，你尽管躺就是了，剩下的交给我。"
    nvl_narrator "{color=#e5e5e5}袁艳看着我又一次皱了皱眉，最终她还是叹了口气，像是放弃了什么一样。{/color}"
    nvl_narrator "{color=#e5e5e5}她看一眼身后的林琴。{/color}"
    nvl_narrator "{color=#e5e5e5}躺了下去。{/color}"
    nvl clear

    window hide dissolve
    show y 不爽02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/21.mp3"
    y "哇！！烫死个人了。"
    
    hide y dissolve
    window hide
    
    w "你稍微忍一下不行吗？"
    nvl clear

    window hide dissolve
    show y 不爽01 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/9.mp3"
    y "烫的又不是你，你当然这么说啊！"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}就在这个时候，林琴的身体蜷缩了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}像是置身于冰窟一般。{/color}"
    nvl_narrator "{color=#e5e5e5}当然，林琴并没有因此醒过来，反而是裹裹被子接着睡了过去。{/color}"
    nvl clear

    w "忍一下哈。"
    nvl_narrator "{color=#e5e5e5}我闭上眼睛，将蕴藏在体内的力量引发了出来。{/color}"
    nvl clear

    w "咳咳…"
    w "……."
    nvl_narrator "{color=#e5e5e5}没想到这个方法真的能有效。{/color}"
    nvl_narrator "{color=#e5e5e5}疲惫瞬间涌入了我的身体。{/color}"
    nvl clear

    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with dissolve
    window show

    nvl_narrator "{color=#e5e5e5}啊.算了，先睡一会吧。{/color}"
    nvl_narrator "{color=#e5e5e5}恍惚之中，我似乎有听到谁的声音。{/color}"
    nvl_narrator "{color=#e5e5e5}是在对话，还是在叫我？{/color}"
    nvl_narrator "{color=#e5e5e5}不管了。{/color}"
    nvl_narrator "{color=#e5e5e5}这是我最后的一丝念想。	{/color}"
    nvl clear

    jump l_indi_1

label c3_c1_c:

    $c3_c1_c_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve
    
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我觉得程祎琳的可能性比较大，就她了。"
    nvl_narrator "{color=#e5e5e5}我看着一脸认真袁艳。{/color}"
    w "你认真的？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "嗯，很真，我要怎么做？"
    w "等天色暗下来再说吧。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y_nvl "……"

    #$narrator = nvl_narrator

    $renpy.music.set_volume(1.5, delay=0.2, channel="voice")
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/程依琳.wav" loop fadein 2.0 fadeout 2.0

    nvl clear

    window hide

    #【场景：病房】
    scene bf_白天 with dissolve:
        zoom .667

    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}事实上从现在算起到晚上并没有发生什么特别的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}倒是我和灵魂状态下的袁艳有一句没一句的搭话一直到了晚上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}其实到头来我也不知道和她聊了些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看着她的眼神，我觉得她跟我想的也差不了多少。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}看着袁艳一脸恍惚的模样，我觉得她可能跟我想得一样，完全不知道在聊些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看了看已经渐渐暗下的天空，三个女孩中其中的两个已经离开病房。{/color}"
    nvl_narrator "{color=#e5e5e5}只有程祎琳还留在这里，她似乎并不打算离开。{/color}"
    nvl_narrator "{color=#e5e5e5}而且她留在这里好像是那三个女孩商量好的一样。{/color}"
    nvl clear

    window hide dissolve
    show c 斜视01 at ct with Dissolve(.7)
    
    c "……"

    hide c with dissolve
    window hide
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}程祎琳则是看着躺在床上的‘袁艳’看了许久。{/color}"
    nvl_narrator "{color=#e5e5e5}我则是和袁艳对视一眼，完全不知道她在想什么。{/color}"
    nvl clear

    window hide dissolve
    show y 嘲讽02 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/36.mp3"
    y "她倒是自在，死猫什么时候可以开始？"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}我看看窗外已经完全暗下来的景象。{/color}"
    nvl_narrator "{color=#e5e5e5}心里默默计算着时间。{/color}"
    nvl clear

    w "在稍微等一会儿吧，得等她睡下才行。"
    nvl_narrator "{color=#e5e5e5}说完我也没有理会袁艳嘴里的不满。{/color}"
    nvl_narrator "{color=#e5e5e5}因为我知道现在还不是时候。{/color}"
    nvl_narrator "{color=#e5e5e5}想要灵魂同步，这种状态下肯定是不行的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}在这期间我和袁艳再一次有一句没一句的搭话起来。{/color}"
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是事实上，程祎琳她睡觉倒是睡得特别的早。{/color}"
    nvl_narrator "{color=#e5e5e5}我和袁艳也没聊多久的天，虽然大多数都是聊的这几天发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}再然后就是找她讨要报酬一直在讨价还价。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这家伙也太小气了。{/color}"
    nvl_narrator "{color=#e5e5e5}枉费我那么大的力气找人就她，结果她居然表示最多十盒不能再多了。{/color}"
    nvl_narrator "{color=#e5e5e5}这人简直过分得可以。{/color}"
    nvl clear

    w "准备好没？"
    
    window show dissolve
    nvl_narrator "{color=#e5e5e5}虽然说是要让袁艳体验一下程祎琳以前发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}但是像是灵魂同步这样恐怖的事情能不能做到我心里也没有底。{/color}"
    nvl_narrator "{color=#e5e5e5}只是印象中突然出现的方法，刚好在近期想起来的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}万一方法是错的话，那我脸就丢大了。{/color}"
    nvl_narrator "{color=#e5e5e5}丢脸还是小事，可能小命都会丢掉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我一脸谨慎的看着袁艳，结果她一副完全都不放在心上的样子。{/color}"
    nvl_narrator "{color=#e5e5e5}明明自己都变成灵魂状态了，转眼间就适应也有点太过分了吧。{/color}"
    nvl clear

    window hide dissolve
    show y 恼火02 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/18.mp3"
    y "你看这都快一点了，我很早就开始问你什么时候开始了吧。"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}袁艳甚至还有点点不满的看着我。{/color}"
    nvl clear

    window hide

    w "好吧好吧，你躺到床上去。"

    show y 正常03 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/47.mp3"
    y "知道了。"

    hide y dissolve
    
    w "……."
    nvl_narrator "{color=#e5e5e5}看着袁艳熟练的动作，我有些无语。{/color}"
    nvl_narrator "{color=#e5e5e5}忘记跟她说明了。{/color}"
    nvl clear

    w "不是躺倒你自己的床上去啦，是躺倒她的床上。"
    nvl_narrator "{color=#e5e5e5}我指着程祎琳的床，示意袁艳上错床了。{/color}"
    nvl_narrator "{color=#e5e5e5}袁艳皱了皱眉毛，并没有说什么，出奇的配合。{/color}"
    nvl_narrator "{color=#e5e5e5}然后走到睡在程祎琳的床边，微微的犹豫一下，看我一眼。{/color}"
    nvl clear

    window hide dissolve
    show y 正常02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/27.mp3"
    y "怎么做？"

    hide y dissolve

    w "躺下。"
    w "可能会有点点烫，但是放心。"
    w "不会有生命危险的。"
    
    nvl_narrator "{color=#e5e5e5}袁艳再次皱眉，但是她并没有多说话。{/color}"
    nvl_narrator "{color=#e5e5e5}仅仅的爬上床，她的眼神里多是疑惑。应该是对自己为什么能爬上床感到疑惑吧。{/color}"
    nvl_narrator "{color=#e5e5e5}不过我也没有和她解释的意思，只要她想就可以了。{/color}"
    nvl clear

    window hide dissolve
    show y 正常04 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/22.mp3"
    y "接下来呢？"

    hide y dissolve

    w "躺倒她的身体里面去就可以了。"

    window hide dissolve
    show y 正常05 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/13.mp3"
    y "你疯了吧？"

    hide y dissolve
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}说着袁艳又坐起来了，指着身后已经熟睡的程祎琳惊呼道。{/color}"
    nvl clear
    
    w "大惊小怪，你尽管躺就是了，剩下的交给我。"
    nvl_narrator "{color=#e5e5e5}袁艳看着我又一次皱了皱眉，最终她还是叹了口气，像是放弃了什么一样。{/color}"
    nvl_narrator "{color=#e5e5e5}她看一眼身后的程祎琳。{/color}"
    nvl_narrator "{color=#e5e5e5}躺了下去。{/color}"
    nvl clear

    window hide dissolve
    show y 不爽02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/21.mp3"
    y "哇！！烫死个人了。"
    
    hide y dissolve
    window hide
    
    w "你稍微忍一下不行吗？"

    window hide dissolve
    show y 不爽01 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/9.mp3"
    y "烫的又不是你，你当然这么说啊！"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}就在这个时候，程祎琳的身体蜷缩了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}像是置身于冰窟一般。{/color}"
    nvl_narrator "{color=#e5e5e5}当然，程祎琳并没有因此醒过来，反而是裹裹被子接着睡了过去。{/color}"
    nvl clear

    w "忍一下哈。"
    nvl_narrator "{color=#e5e5e5}我闭上眼睛，将蕴藏在体内的力量引发了出来。{/color}"
    nvl clear

    w "咳咳…"
    w "……."
    nvl_narrator "{color=#e5e5e5}没想到这个方法真的能有效。{/color}"
    nvl_narrator "{color=#e5e5e5}疲惫瞬间涌入了我的身体。{/color}"
    nvl clear

    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with dissolve
    window show

    nvl_narrator "{color=#e5e5e5}啊.算了，先睡一会吧。{/color}"
    nvl_narrator "{color=#e5e5e5}恍惚之中，我似乎有听到谁的声音。{/color}"
    nvl_narrator "{color=#e5e5e5}是在对话，还是在叫我？{/color}"
    nvl_narrator "{color=#e5e5e5}不管了。{/color}"
    nvl_narrator "{color=#e5e5e5}这是我最后的一丝念想。	{/color}"
    nvl clear

    jump c_indi_1

label c3_c1_x:

    $c3_c1_x_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve
    
    show y 正常04 at ct with dissolve:
        alpha .85
    y "我觉得夏静的可能性比较大，就她了。"
    nvl_narrator "{color=#e5e5e5}我看着一脸认真袁艳。{/color}"
    w "你认真的？"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "嗯，很真，我要怎么做？"
    w "等天色暗下来再说吧。"
    show y 正常04 at ct with dissolve:
        alpha .85
    y "……"

    #$narrator = nvl_narrator

    $renpy.music.set_volume(1.5, delay=0.2, channel="voice")
    $renpy.music.set_volume(1.0, delay=0.2, channel="music")
    play music "music/程依琳.wav" loop fadein 2.0 fadeout 2.0

    nvl clear

    window hide

    #【场景：病房】
    scene bf_白天 with dissolve:
        zoom .667

    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}事实上从现在算起到晚上并没有发生什么特别的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}倒是我和灵魂状态下的袁艳有一句没一句的搭话一直到了晚上。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}其实到头来我也不知道和她聊了些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看着她的眼神，我觉得她跟我想的也差不了多少。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}看着袁艳一脸恍惚的模样，我觉得她可能跟我想得一样，完全不知道在聊些什么。{/color}"
    nvl_narrator "{color=#e5e5e5}看了看已经渐渐暗下的天空，三个女孩中其中的两个已经离开病房。{/color}"
    nvl_narrator "{color=#e5e5e5}只有夏静还留在这里，她似乎并不打算离开。{/color}"
    nvl_narrator "{color=#e5e5e5}而且她留在这里好像是那三个女孩商量好的一样。{/color}"
    nvl clear

    window hide dissolve

    show x 注视01 at ct with dissolve
    x "……"

    hide x with dissolve
    window hide
    window show Dissolve(.7)
    
    nvl_narrator "{color=#e5e5e5}夏静则是看着躺在床上的‘袁艳’看了许久。{/color}"
    nvl_narrator "{color=#e5e5e5}我则是和袁艳对视一眼，完全不知道她在想什么。{/color}"
    nvl clear

    window hide dissolve
    show y 嘲讽02 at ct with Dissolve(.7)
    pause .7

    voice "voice/dlc_voice/c/36.mp3"
    y "她倒是自在，死猫什么时候可以开始？"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}我看看窗外已经完全暗下来的景象。{/color}"
    nvl_narrator "{color=#e5e5e5}心里默默计算着时间。{/color}"
    nvl clear

    w "在稍微等一会儿吧，得等她睡下才行。"
    nvl_narrator "{color=#e5e5e5}说完我也没有理会袁艳嘴里的不满。{/color}"
    nvl_narrator "{color=#e5e5e5}因为我知道现在还不是时候。{/color}"
    nvl_narrator "{color=#e5e5e5}想要灵魂同步，这种状态下肯定是不行的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}在这期间我和袁艳再一次有一句没一句的搭话起来。{/color}"
    nvl_narrator "{color=#e5e5e5}…….{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}但是事实上，夏静她睡觉倒是睡得特别的早。{/color}"
    nvl_narrator "{color=#e5e5e5}我和袁艳也没聊多久的天，虽然大多数都是聊的这几天发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}再然后就是找她讨要报酬一直在讨价还价。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}这家伙也太小气了。{/color}"
    nvl_narrator "{color=#e5e5e5}枉费我那么大的力气找人就她，结果她居然表示最多十盒不能再多了。{/color}"
    nvl_narrator "{color=#e5e5e5}这人简直过分得可以。{/color}"
    nvl clear

    w "准备好没？"
    nvl_narrator "{color=#e5e5e5}虽然说是要让袁艳体验一下夏静以前发生的事情。{/color}"
    nvl_narrator "{color=#e5e5e5}但是像是灵魂同步这样恐怖的事情能不能做到我心里也没有底。{/color}"
    nvl_narrator "{color=#e5e5e5}只是印象中突然出现的方法，刚好在近期想起来的。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}万一方法是错的话，那我脸就丢大了。{/color}"
    nvl_narrator "{color=#e5e5e5}丢脸还是小事，可能小命都会丢掉。{/color}"
    nvl clear

    nvl_narrator "{color=#e5e5e5}我一脸谨慎的看着袁艳，结果她一副完全都不放在心上的样子。{/color}"
    nvl_narrator "{color=#e5e5e5}明明自己都变成灵魂状态了，转眼间就适应也有点太过分了吧。{/color}"
    nvl clear

    window hide dissolve
    show y 恼火02 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/18.mp3"
    y "你看这都快一点了，我很早就开始问你什么时候开始了吧。"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}袁艳甚至还有点点不满的看着我。{/color}"
    nvl clear

    window hide dissolve

    w "好吧好吧，你躺到床上去。"

    show y 正常03 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/47.mp3"
    y "知道了。"

    hide y dissolve
    window hide
    
    w "……."
    nvl_narrator "{color=#e5e5e5}看着袁艳熟练的动作，我有些无语。{/color}"
    nvl_narrator "{color=#e5e5e5}忘记跟她说明了。{/color}"
    nvl clear

    w "不是躺倒你自己的床上去啦，是躺倒她的床上。"
    nvl_narrator "{color=#e5e5e5}我指着夏静的床，示意袁艳上错床了。{/color}"
    nvl_narrator "{color=#e5e5e5}袁艳皱了皱眉毛，并没有说什么，出奇的配合。{/color}"
    nvl_narrator "{color=#e5e5e5}然后走到睡在夏静的床边，微微的犹豫一下，看我一眼。{/color}"
    nvl clear

    window hide dissolve
    show y 正常02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/27.mp3"
    y "怎么做？"

    hide y dissolve

    w "躺下。"
    w "可能会有点点烫，但是放心。"
    w "不会有生命危险的。"
    
    nvl_narrator "{color=#e5e5e5}袁艳再次皱眉，但是她并没有多说话。{/color}"
    nvl_narrator "{color=#e5e5e5}仅仅的爬上床，她的眼神里多是疑惑。应该是对自己为什么能爬上床感到疑惑吧。{/color}"
    nvl_narrator "{color=#e5e5e5}不过我也没有和她解释的意思，只要她想就可以了。{/color}"
    nvl clear

    window hide dissolve
    show y 正常04 at ct with Dissolve(.7)

    voice "voice/dlc_voice/c/22.mp3"
    y "接下来呢？"

    hide y dissolve
    window hide

    w "躺倒她的身体里面去就可以了。"

    window hide dissolve
    show y 正常05 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/13.mp3"
    y "你疯了吧？"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}说着袁艳又坐起来了，指着身后已经熟睡的夏静惊呼道。{/color}"
    nvl clear
    
    w "大惊小怪，你尽管躺就是了，剩下的交给我。"
    nvl_narrator "{color=#e5e5e5}袁艳看着我又一次皱了皱眉，最终她还是叹了口气，像是放弃了什么一样。{/color}"
    nvl_narrator "{color=#e5e5e5}她看一眼身后的夏静。{/color}"
    nvl_narrator "{color=#e5e5e5}躺了下去。{/color}"
    nvl clear

    window hide dissolve
    show y 不爽02 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/21.mp3"
    y "哇！！烫死个人了。"
    
    hide y dissolve
    
    w "你稍微忍一下不行吗？"

    show y 不爽01 at ct with Dissolve(.7)
    
    voice "voice/dlc_voice/c/9.mp3"
    y "烫的又不是你，你当然这么说啊！"

    hide y dissolve
    window hide
    window show Dissolve(.7)

    nvl_narrator "{color=#e5e5e5}就在这个时候，夏静的身体蜷缩了起来。{/color}"
    nvl_narrator "{color=#e5e5e5}像是置身于冰窟一般。{/color}"
    nvl_narrator "{color=#e5e5e5}当然，夏静并没有因此醒过来，反而是裹裹被子接着睡了过去。{/color}"
    nvl clear

    w "忍一下哈。"
    nvl_narrator "{color=#e5e5e5}我闭上眼睛，将蕴藏在体内的力量引发了出来。{/color}"
    nvl clear

    w "咳咳…"
    w "……."
    nvl_narrator "{color=#e5e5e5}没想到这个方法真的能有效。{/color}"
    nvl_narrator "{color=#e5e5e5}疲惫瞬间涌入了我的身体。{/color}"
    nvl clear

    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with dissolve
    window show

    nvl_narrator "{color=#e5e5e5}啊.算了，先睡一会吧。{/color}"
    nvl_narrator "{color=#e5e5e5}恍惚之中，我似乎有听到谁的声音。{/color}"
    nvl_narrator "{color=#e5e5e5}是在对话，还是在叫我？{/color}"
    nvl_narrator "{color=#e5e5e5}不管了。{/color}"
    nvl_narrator "{color=#e5e5e5}这是我最后的一丝念想。	{/color}"
    nvl clear

    jump x_indi_1

label c3_2_l:

    $c3_2_l_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    #(个人线-主线转换线)"
    scene black with dissolve
    narrator "【距离诅咒发作还剩一天】"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
        
    show y 正常03 at ct with dissolve
    y "咳咳咳…"
    show y 正常01 at ct with dissolve
    y "喂…死猫该醒了。"
    show y 恼火01 at ct with dissolve
    y "还睡你妹啊。"
    w " 唔…唔喵…喵？"
    w "哇，你放开手啊！耳朵要掉啦要掉啦！"
    narrator "我还在做春秋大梦的时候，不知何时袁艳已经醒过来了。"
    narrator "其实一点也不痛，也没人她也没揪住我的耳朵。"
    narrator "我只是习惯性的就开口了，看来这几天受她不少照顾。"
    narrator "喉咙已经生成了肌肉记忆了，只要她叫我起床，我就会这样叫嚷。"
    narrator "这以后要是嫁出去不知道要给伴侣家添多少麻烦。"
    narrator "这么快的吗？"
    w "你回来得这么快的吗？"
    narrator "袁艳则是一脸很吃惊的表情看着我。"
    show y 正常02 at ct with dissolve
    y "你逗我呢？你看着都什么时候了。"
    show y 正常03 at ct with dissolve
    y "都第二天了好不好？？"
    narrator "袁艳指着窗外渐渐亮起来的天空。"
    narrator "我似乎明白了一件事情。"
    w "嗯。"
    w "我们好像完蛋了呢，嘿嘿。"
    show y 不爽02 at ct with dissolve
    y "笑你个大头鬼啦。"
    show y 不爽01 at ct with dissolve
    y "我跟你说的不是这个事情。"
    w "那是啥？"
    show y 正常04 at ct with dissolve
    y "而是她啦，林琴的。"
    w "她怎么么？"
    w "难不成她就是我们要找的那个崩坏的女孩？"
    narrator "我露出惊喜的表情，期待着袁艳的回答。"
    narrator "不料袁艳却白我一眼。"
    show y 正常05 at ct with dissolve
    y "很难说，你知道我干啥去了不。"
    w "你干啥去了？不是让你去看她的过去么？"
    show y 正常04 at ct with dissolve
    y "不，没那么简单。"
    show y 正常02 at ct with dissolve
    y "我的意识直接变成了她。"
    w "啥？"
    show y 正常01 at ct with dissolve
    y "就是我直接变成了林琴。"
    narrator "袁艳伸了伸大拇指，指着躺在床上还在安静睡觉的林琴。"
    narrator "其实仔细看的话不难看到，林琴额头上那碗大的汗珠。"
    w "怎么样了？"
    show y 正常03 at ct with dissolve
    y "怎么说…就是我看到的都是记忆片段。"
    w "额，听不懂但是很厉害的样子。"
    w "所以呢？你得出什么结论没有？"
    show y 正常04 at ct with dissolve
    y "能不能麻烦你再送我回去一趟？"
    w "……"
    w "这才是你的目的吧。"
    show y 正常04 at ct with dissolve
    y "是啊"
    w "喂，我们哪里还有时间给你这样子玩啊。"
    w "再说我已经没剩多少力量了啊。"
    show y 正常05 at ct with dissolve
    y "可是我总觉得故事到那里还没有完结。"
    show y 俏皮 at ct with dissolve
    y "就一次…就一次可以不？"
    narrator "我有些瞠目结舌的看着袁艳，我也是第一次被这样提要求。"
    narrator "搞得好像还能有下一次一样。"
    narrator "我不免在心里狠狠的吐槽了袁艳这个家伙一顿。"
    narrator "这家伙绝对是生下来克我的。"
    show y 正常04 at ct with dissolve
    y "如果这家伙不是，我们接下来点燃正确的几率就大多了好不啦。"
    narrator "但是听她这么一说好像也确实有道理。"
    narrator "话说一开始我就是被这么忽悠的吧。"
    narrator "也没有道理事情做一半就没做完吧。"
    narrator "只是可怜我那用一点就少一点的力量啊，这样就算是点燃对了，我想要恢复也要很长时间了。"
    narrator "唉。"
    narrator "算了算了。"
    w "好吧好吧，你准备一下。"
    narrator "我无奈的叹了一口气。"
    narrator "真的下血本啊。"
    w "我们没剩多少时间了。"
    w "该回来的时候你可得记着要回来啊。"
    show y 正常05 at ct with dissolve
    y "额…"
    w "准备好。"
    show y 正常04 at ct with dissolve
    y "其实…"
    narrator "就在我将她的灵魂送往过去的那一瞬间。"
    show y 正常02 at ct with dissolve
    y "其实…"
    show y 正常01 at ct with dissolve
    y "我好像在林琴的过去看到了我们两个。"
    #"(袁艳立绘消失)"
    hide y with dissolve
    narrator "……"
    narrator "短短的几句话却让我足足愣了好几秒。"
    narrator "许久，才终于爆发出来。"
    w "啥？？？"

    scene black with dissolve

    jump c3_3_l

label c3_3_l:

    $c3_3_l_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    #"(林琴视角：林琴第一人称)"
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    
    show l 普通02 at ct with dissolve
    l "……."
    show l normal_3_1 at ct with dissolve
    l "呵呵。"
    narrator "坐在病床上再一次无聊的看着天花板。"
    narrator "不想看周围的场景，因为周边只是被我大闹之后的狼藉。"
    
    #场景：黑暗
    scene black with dissolve

    #show l 普通02 at ct with dissolve
    l "唉…."
    narrator "能够清楚的感受到身体各处的疼痛。"
    narrator "只有在这个时候我才能感觉到些许的平静。"
    narrator "甚至我已经把强行拔掉注射器这件事情当成茶余饭后一根烟的消遣一样了。"
    narrator "有时候经常自己都没办法理解的行为，却依旧做出来了。"

    #场景：街道
    scene street_白天 with dissolve:
        zoom .667
    
    narrator "就比如现在。"
    narrator "我偷偷的跑到了街道上。"
    narrator "街上的人都朝我投来视线，就像是在看什么明星。"
    narrator "毕竟经常在是新闻头条出没的大小姐。"
    narrator "只是我心里却没有任何感觉。"
    show l 普通04 at ct with dissolve
    l "呵呵呵…."
    narrator "我漫无目的的在街道上走着。"
    narrator "下意识的在人群中寻找着。"
    narrator "想要捕捉一个熟悉的身影。"
    narrator "但是我很清楚，你不会出现在这样的街道上的。"
    narrator "莫名的悲伤再度向我袭来。"
    narrator "完了…我的身体又要失控了吗？"
    narrator "在这样的大街上？"
    narrator "我可以想象明天的头条新闻上会是怎么写的…"
    narrator "林氏集团继承人突然在大街上发疯？"
    narrator "毫无疑问，这对于林氏集团的股市是一次沉重的打击。"
    narrator "这对于我来说并没有损失什么。"
    show l 注视04 at ct with dissolve
    l "额…"
    #(难受的哼声)
    narrator "但是那样的，我毫无疑问是践踏了她的心意。"
    narrator "我是知道的。"
    narrator "如果没有她的话，我不可能能把林氏集团抢回来。"
    narrator "因此我必须守护好这块我们一起开创的净土。"
    narrator "……."
    narrator "所以，我为什么非要出来不可啊？"
    narrator "老老实实呆在家里不好吗？"
    narrator "我不由得开始埋怨自己。"
    show l 普通04 at ct with dissolve
    l "回去了。"
    #(难受的声音)
    "保镖" "好的。"
    narrator "我竭力克制着内心的躁动。"
    narrator "朝着车的方向走着。"
    narrator "千万不要在这种地方出事啊…."
    #show ？？ y at ct with dissolve
    "？？" "哈喽？？？"
    
    # TODO 18
    #[CG：两人的相遇]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_l_yzgirl = True
    scene cg_两人的相遇 with Dissolve(2):
        zoom .667
        ###1
    
    pause 1.0

    narrator "………"
    narrator "………"
    narrator "突然一个声音出现在我的前方…"
    narrator "那是我们第一次真正意义上的相遇。"

    #场景：黑屏
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve

    narrator "突然一切就消失了，我伫立在黑暗中。"
    narrator "有谁在黑暗的另一端。"
    "女孩" "嘿嘿…"

    # TODO 19
    ##CG:下沉]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xc = True
    scene cg_下沉 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0
    
    narrator "女孩的声音回荡在这个黑暗空间里。"
    narrator "有点熟悉，更多的是陌生。"
    narrator "微微的荧光环绕在的周身。"
    narrator "她的嘴唇微微张合，述说着什么。"
    narrator "像是说给我听的，可是我又是谁？"

    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    
    narrator "再一次回到这里的袁艳，伫立在我的面前。"
    w "……"
    show y 正常05 at ct with dissolve
    y "……"
    w "所以说到底怎么了？"
    show y 正常04 at ct with dissolve
    y "这个不好跟你解释…"
    narrator "袁艳看了看躺在床上的林琴。"
    narrator "叹了一口气。"
    w "…."
    narrator "所以说到底怎么啦。"
    narrator "林琴到底是不是那个崩坏女孩啊。"
    show y 正常03 at ct with dissolve
    y "我可能见到了很奇怪的东西"
    w "什么东西？"
    show y 正常01 at ct with dissolve
    y "你现在还能把我送回去不？"
    narrator "她指一下自己的身体。"
    narrator "我马上就明白她的意思。"
    w "……"
    w "之前不是试过了吗？基本上不太可能了啊。"
    show y 正常02 at ct with dissolve
    y "好吧。"
    narrator "……."
    w "那你现在能做判断了不？"
    narrator "我看了看袁艳，她应该是明白我的意思。"
    narrator "袁艳则是又看看床上的林琴，依旧在犹豫。"
    narrator "还没有下定决心。"
    show y normal_3_2 at ct with dissolve
    y "我好像做了一个很长的梦。"
    narrator "忽然间，袁艳这么说道。"
    w "哈？"
    narrator "我有点不太理解她现在说这个是有啥意义。"
    w "做个梦跟我们现在的情况有关系嘛？"
    show y 正常01 at ct with dissolve
    y "怎么说呢…我就感觉特别疼，特别难受，还有个谁让我带话。"
    w "谁让你带话？"
    narrator "我歪了歪脑袋，有点不太明白袁艳这家伙说的话。"
    narrator "袁艳再一次看床上的林琴一眼，叹了一口气。"
    show y 正常05 at ct with dissolve
    y "该怎么说呢…这种感觉并不是很好。"
    show y 正常04 at ct with dissolve
    y "有人托我给这丫头带个话。"
    w "说啥了？"
    show y 正常02 at ct with dissolve
    y "虽然不知道有啥用，但是大概就几句道别的话之类的？"
    w "道别？跟谁道别？"
    w "算了算了，别管那么多，你到底弄清楚没？"
    w "这个丫头到底是不是我们要找的那个啊？"
    show y 正常01 at ct with dissolve
    y "……"
    narrator "这个时候反倒是她沉默了一下。"
    show y 正常05 at ct with dissolve
    y "问一下。"
    w "都到这种时候，你还有啥问题啊？"
    show y 正常05 at ct with dissolve
    y "说到底崩坏到底是个什么东西？"
    show y 正常04 at ct with dissolve
    y "我觉得她这丫头挺好的呀。"
    w "那你就把事情想得太简单了。"
    narrator "太草率了！"
    w "所谓的崩坏可比你想的要严重的多。"
    w "这样的人是介于灵魂状态和现实状态为一体的存在。"
    w "换句话来说，就是这样的人在现实世界中不论生死都能影响现实世界。"
    w "严重的会使得灾难具象化。"
    show y 正常04 at ct with dissolve
    y "麻烦你解释得通俗点，能让我听懂的那种。"
    w "……"
    w "简单来说崩坏的人可以引发灾难。"
    w "大到你们常见的洪水，地震，小到你走路被天上掉下来的东西砸死这样的。"
    show y 正常04 at ct with dissolve
    y "…."
    show y 正常05 at ct with dissolve
    y "那不是很刺激？？"
    w "刺激个鬼啦！"
    w "这种无法无天的存在很容易导致城市毁灭的好不啦！"
    show y 无措 at ct with dissolve
    y "我都想变成崩坏的那只了！"
    w "你这么羡慕个啥？"
    show y 俏皮 at ct with dissolve
    y "你想想，完全没人能管我耶？"
    w "是没人能管你了。"
    narrator "我不由得摊了摊爪子。"
    w "包括你自己也管不了你自己。"
    show y 正常04 at ct with dissolve
    y "啊？"
    show y 正常05 at ct with dissolve
    y "不可控的？"
    w "嗯。"
    show y 正常03 at ct with dissolve
    y "那还是不要了。"
    w "明白了？"
    show y 正常02 at ct with dissolve
    y "明白了！"
    w "那这个叫林琴的丫头是不是那个崩坏的女孩啊？"
    show y 正常01 at ct with dissolve
    y "这个啊…."
    narrator "看她犹豫的样子，我多半就能理解了。"
    narrator "她没有办法做出判断。"
    narrator "但是花了这么大的代价，总得问出有用的信息才行啊。"
    show y 正常04 at ct with dissolve
    y "虽然还是没办法判断，不过我有个有用的信息可以拿出来用用。"
    w "嗯？"
    narrator "和我想到一块去了。"
    show y 正常05 at ct with dissolve
    y "这个丫头身体里面应该还有另外一个灵魂。"
    w "……"
    narrator "听到这个消息，我不由得沉默了起来。"
    narrator "另一个灵魂？干扰现世？好像完全符合崩坏的条件啊。"
    show y 正常04 at ct with dissolve
    y "其实我们也不急不是，不是还有一天嘛。"
    narrator "袁艳尴尬的笑着。"

    #场景：黑屏
    scene black with dissolve

    w "……"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    narrator "我长长叹了一口气。"
    w "哪里还有一天啊。"
    show y 正常01 at ct with dissolve
    y "啊？"
    w "现在的你已经是必须要做出决定的时候了。"
    w "今天黄昏时刻，我们点火若不成功。"
    w "…."
    w "最好的情况就是咱们两个灰飞烟灭，再也回不去。"
    show y 正常02 at ct with dissolve
    y "那.最坏的呢？"
    narrator "女孩瞪大眼睛，就像是我刚刚说的话毫无震撼力度一样。"
    w "……"
    narrator "至始至终，这个丫头都是这样。"
    narrator "把心大的性格发挥到了极致，这已经不是心大了吧。"
    narrator "我都不知道拿什么个性来形容她。"
    narrator "这丫头难不成就是那个要崩溃的女孩吗？"
    narrator "我被我的想法吓了一跳，但是我马上摇了摇猫头。"
    narrator "不可能的，在我边上我都不知道。"
    narrator "那我这神圣的猫不是白当了。"
    narrator "不过她的性格真的是有点厉害了，适应能力也有点强得让我无法理解了。"
    narrator "人类都是这样的吗？"
    narrator "要都是还会有什么崩坏的人嘛？"
    narrator "说到底这个世界上真的有袁艳这种人吗？"
    w "我说…你真的是个人吗？"
    show y 正常04 at ct with dissolve
    y "问的什么话…"
    show y 不爽02 at ct with dissolve
    y "我不是人是什么？鬼吗？"
    narrator "我点了点头。"
    show y 正常05 at ct with dissolve
    y "……"
    w "不扯了不扯了，你现在能做判断不？"
    w "我觉得她很有可能就是有问题的女生。"
    w "毕竟两个灵魂，这也太可疑了。"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳没有说话，我就当她是默认了。"
    w "……"
    narrator "既然如此，也就没有必要继续等待下去了。"
    narrator "看了袁艳一眼，我便闭上了眼睛，准备开始引出最后的力量，吟唱赞歌。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/2333.wav" loop fadein 2.0 fadeout 2.0

    # TODO 20
    #[CG:引导者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz1 = True
    scene cg_引导者1 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    #show y 无措 at ct with dissolve
    y "哇，你在干嘛呢？"
    w "…."
    #show y 无措 at ct with dissolve
    y "哇？她是谁啊？？？"
    narrator "我闭着眼睛。"
    w "我在有事你没看见吗？"
    w "忙着呢，别打扰我！"
    #show y 无措 at ct with dissolve
    y "……"
    #show y 无措 at ct with dissolve
    y "不是，你谁啊？"

    # TODO 21
    #[CG:引导者](睁眼)"
    nvl clear
    nvl hide
    window hide dissolve
    #scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz2 = True
    scene cg_引导者2 with Dissolve(1):
        zoom .667
    
    pause 1.0

    w "…."
    narrator "被她烦的不行了，睁开眼睛瞅了她一眼。"
    w "是我怎么了？"
    #show y 正常04 at ct with dissolve
    y "你还是个美少女啊，没看出来啊。"
    w "……"
    #show y 开心 at ct with dissolve
    y "啧啧啧…还挺漂亮的。"
    #show y 笑容01 at ct with dissolve
    y "你要是早点变成这样，我就不会对你那么凶了。"
    w "……"
    w "快闭嘴啊！我在控制力量，能不能别让我分神。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0

    nvl clear
    nvl hide
    window hide dissolve

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    
    narrator "好说歹说，终于算是让这个妮子闭嘴了。"
    narrator "没了她说话分神，我引导力量的速度也快了许多。"
    narrator "不一会儿，就完成了力量的引导，在我的人体印象的胸口，点燃了一簇蓝色的火焰。"
    w "…."
    show y 正常04 at ct with dissolve
    y "……"
    narrator "在火焰下，我和袁艳彼此对视一眼。"
    w "我做了啊…"
    show y 正常05 at ct with dissolve
    y "做啥？"
    w "点燃她啊。"
    narrator "我看着床上的林琴，然后又看了看袁艳。"
    narrator "怎么好像还要征得她同意一样。"
    narrator "顿时有点郁闷了起来。"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳明显的犹豫了一下。"
    show y 正常04 at ct with dissolve
    y "你点呗。"
    w "那我动手了啊。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "你动手啊！磨磨唧唧的。"
    w "……"
    narrator "我一怔，就准备开始书写大结局的故事了。"
    narrator "只要我把接下来的灵魂之火放到这个女孩的身体里面，一切就完成了。"
    narrator "总觉得事情没那么顺利…"
    narrator "林琴翻了个身。"
    narrator "然后我控制着灵火直接放到了她的身体里面。"
    narrator "看着灵火漂浮在她的胸口。"
    narrator "我有些愣神…会不会有点太简单了？"
    narrator "按道理来说，这个时候不应该出现一点点变故吗？"
    w "……"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "接下来呢？"
    w "等着就行了。"
    narrator "接下来只需要等灵魂之火灼烧殆尽这个灵魂即可。"
    narrator "保佑啊，这个丫头是那个女孩，一定要是啊…."

    #场景：黑屏]"
    scene black with Dissolve(.7)

    narrator "时间一点一点的过去了。"

    #场景：病房
    scene bf_白天 with Dissolve(.7):
        zoom .667

    w "……"
    show y 正常02 at ct with dissolve
    y " ……"

    #场景：黑屏
    scene black with dissolve

    narrator "没什么变化。"
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    show y 正常04 at ct with dissolve
    y "怎么没啥动静啊？"
    w "再等等…"
    narrator "头一回要这么久的时间。"
    show y 正常05 at ct with dissolve
    y "我去看看林琴的情况。"
    w "你是灵魂状态，你别靠太近啊。"
    show y 正常04 at ct with dissolve
    y "靠太近怎么了？"
    w "灵魂靠近这个火太近的话，就有可能会把你烧得灰飞烟灭啊。"
    w "别怪我没提醒你，你别到时候还没被诅咒干掉就被灵火烧死了。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "为啥？"
    w "这火对普通灵魂有绝对的杀伤力。"
    show y 正常05 at ct with dissolve
    y "那我还是不靠近了。"
    narrator "说罢，她退后了好几步。"
    show y 正常05 at ct with dissolve
    y "那它对人会咋样呢？如果她不是崩坏的灵魂的话…"
    w "…."
    l "…."
    l "emmm…."
    l "唔…唔…"
    narrator "难受的呻吟声在病房里幽幽的响起，我和袁艳对视一眼，马上就安静了下来。"
    narrator "看来，该来的还是来了。"
    narrator "但是，总感觉不太对。"
    narrator "这不像是在清除崩坏的症状啊…"
    narrator "别吧…我不由得捂住了眼睛，不敢看。"
    w "袁…袁艳。"
    show y 正常02 at ct with dissolve
    y "干啥？"
    w "你帮我看看…"
    w "她是不是浑身冒黑烟之类的？有没有？"
    w "……"
    show y 正常01 at ct with dissolve
    y "没有啊，她就一直在叫而已啊，像做噩梦一样。"
    narrator "听到袁艳的话，我的顿时就愣住了。"
    w "完了…."
    show y 正常01 at ct with dissolve
    y "怎么了？"
    narrator "这不是清除掉崩坏时应该有的现象…"
    narrator "换而言之，也就是林琴这个女孩并不是那个崩坏的女孩."
    narrator "判断错了。"
    w "我们….错了啊…"
    narrator "知道真相的我差点都要哭出来了。"
    narrator "这么多天的努力，结果居然弄错了。"
    narrator "真的是命啊…"
    w "呜喵…唔喵…."
    narrator "还是没忍住，哭出来了。"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "干啥呢干啥呢，奔丧呢你？"
    w "我们…我们，我们…完了啊！"
    show y 正常05 at ct with dissolve
    y "完什么完，你还没回答我呢。"
    w "啊？"
    narrator "回答什么，都这时候还回答什么啊？"
    show y 正常05 at ct with dissolve
    y "灵魂之火对普通人有啥伤害吗？"
    narrator "袁艳指了指躺在床上翻来覆去非常痛苦的林琴。"
    w "灵魂之火对人体能有什么伤害啊？"
    w "大姐…你省省心吧…我们选错了，要死了啊，你还有心情担心她？"
    narrator "我心情哽咽，知道自己马上要死的感觉真的一点都不好。"
    show y 正常04 at ct with dissolve
    y "那为啥这丫头这么难受啊？"
    w "……."
    narrator "我还在难受着呢，突然面前一阵风吹了过来。"
    narrator "她就像是一阵风一样冲到了我的面前。"
    show y 正常04 at ct with dissolve
    y "到底是怎么回事啦？"
    w "…."
    w "虽然她有躯体可以保护自己的灵魂，但是灵魂之火仍然是能够灼烧其灵魂的。"
    show y 正常05 at ct with dissolve
    y "嗯？"
    w "她肯定是要失去一些东西的，强行失去怎么可能不难受啊。"
    w "如果没有错的话，灼烧的肯定是她觉得比较重要的事情。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "能不能说点我能懂的？"
    show y 正常04 at ct with dissolve
    y "比如她失去了啥，或者怎么灭了这火？"
    w "你疯啦？"
    show y 恼火04 at ct with dissolve
    y "讲重点。"
    narrator "袁艳很无语的看着我，难不成她真打算灭掉这火？"
    w "……"
    narrator "一旦点燃这个火，想要在灭掉是不可能的…几乎不可能的。"
    narrator "除非……"
    w "这玩意肯定要烧掉啥东西才能灭掉。"
    w "啊….反正咱们也死定了.你能不能表现得在悲伤一点啊？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "死猫，既然不是她，她这么难受不是显得我们俩有点缺德嘛？"
    w "都快死的人了…呜呜呜…."
    narrator "我几乎要放生大哭了起来。"
    show y 正常05 at ct with dissolve
    y "…."
    narrator "袁艳则是非常无语的看着我。"
    show y 恼火04 at ct with dissolve
    y "别奔丧了。"
    w "……"
    w "我们快完了好不好！！"
    show y 正常05 at ct with dissolve
    y "不是你真有那么悲伤？"
    w "…."
    w "那不是废话嘛？"
    narrator "看着有些玩味的袁艳，我有点儿搞不懂她是啥意思了。"
    w "倒是你，快完蛋的人了，你怎么跟过节一样开心啊喂！"
    show y 开心 at ct with dissolve
    y "我有说啥吗？"
    show y 笑容01 at ct with dissolve
    y "反正我们已经没救了不是吗？"
    narrator "袁艳突然在这个时候笑了起来。"
    narrator "完了，这丫头也没救了。"
    narrator "不，应该说这一开始咱们就没救了。"
    narrator "把希望放在她身上的我真的是个大笨蛋啊。"
    narrator "她压根对这种事情就无所谓的。"
    narrator "有点点懊恼。"
    narrator "但是现在已经来不及了啊。"
    narrator "我们真的已经完了。"
    w "你…干啥呢？"
    narrator "我看着袁艳一点一点的靠近少女。"
    narrator "我不是说她这个灵魂状态的不要靠近火吗？"
    narrator "她想干啥？"
    #show l 难受的声音 at ct with dissolve
    l "啊…"
    show y 正常05 at ct with dissolve
    y "她这叫声我听不下去了。"
    show y 正常05 at ct with dissolve
    y "让人担心的丫头。"
    narrator "在我的注视之下，袁艳伸出了手。"
    narrator "将放置在女孩胸口的灵魂之火取了出来。"
    w "喂，你别乱搞啊！！会死的！"
    narrator "我突然紧张了起来。"

    #场景：淡入 黑屏
    
    # TODO 22
    #"淡出[CG:救赎者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz = True
    scene cg_救赎者 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    w "…."
    w "我.的…妈呀…"
    narrator "女孩手捧着灵魂之火，伫立在房间里头。"
    narrator "静谧的房间，传来了滋滋的声音，看不见的火焰在不断的溶解着少女的身体。"
    narrator "就好似飘散的花瓣，散落漂浮在这个空间里面。"
    narrator "你到底要做什么啊？"
    narrator "之前一点点火就已经把你疼了个半死。"
    narrator "现在直接把火捧在手上，你不要命啦？"

    #场景：黑屏
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667
    
    y "死猫…这个火会烧掉琴丫头全部的记忆。"
    narrator "她好像忽然明白了什么一样。"
    w "…."
    narrator "我其实是知道的，灵魂之火会褪去一个人心中全部的执念。"
    narrator "会把一个人变成符合世界所需要的‘正常人’，渐渐的融入世界中，与他人无异。"
    narrator "这就是我们的使命。"
    narrator "很显然，这些记忆就是林琴全部的执念。"
    narrator "如果烧掉，那么这个不合群的少女，就应该很容易融入人类所谓的社会当中去。"
    narrator "这应该是一件好事才对。"
    narrator "我不明白，为什么这丫头会这么痛苦呢？"

    # TODO 23
    #CG:救赎者的笑容]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz_smile = True
    scene cg_救赎者的笑容 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    y "我刚刚看到了…"
    narrator "袁艳，几乎是是从牙缝里面挤出来的几句话。"
    y "这丫头…在哭。"
    y "那些被记住的事情，对她应该特别重要。"
    y "死猫…再帮我一件事…"
    y "我…要回到那具身体里面去。"
    w "……"
    narrator "这是不可能做到的吧。"
    narrator "话说…"
    w "你赶快…放手啊！你会被烧死的啊！"
    w "灵魂一旦被烧， 这个世界上就真的没有你了啊！！"
    y "…."
    y "痛痛痛痛死了！"
    y "诶嘿嘿…你以为是我死了吗？"
    y "其实我没有死哒！"

    # TODO 24
    ##CG:抛出去]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_pcq = True
    scene cg_抛出去 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    narrator "就像是扔掉了一个烫手山芋一样。"
    narrator "袁艳伸出了手，将灵魂之火抛到了空中。"
    narrator "它就飘在半空中，似乎是被谁带走的一样。"
    w "……"
    narrator "我惊讶的说不出话来。"
    w "你….你是怎么做到的？"
    w "灵魂之火不烧掉一个灵魂是不会熄灭的。"
    y "嘿嘿…."
    narrator "你笑个鬼啦，虽然很想吐槽她，但是我还是说不出口。"
    narrator "我知道，肯定是发生了什么。"

    # TODO 25
    ##CG结束]"
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    show y 开心 at ct with dissolve
    y "刚刚我听到了声音。"
    show y 俏皮 at ct with dissolve
    y "林琴那丫头身体里面传出来的。"
    w "声音？"
    show y 笑容01 at ct with dissolve
    y "就是之前说的那个另外一个灵魂。"
    show y 笑容02 at ct with dissolve
    y "她一直守护着林琴。"
    show y 开心 at ct with dissolve
    y "…."
    narrator "她看着半空。"
    show y 正常04 at ct with dissolve
    y "然后，她代替了我。"
    w "……"
    narrator "我也看着半空。"
    narrator "虽然说挺了不起啦，但是也没有用。"
    narrator "我已经能够感觉到诅咒就快要来临了。"
    narrator "我们已经完蛋了。"
    show y 正常05 at ct with dissolve
    y "在此之前，我还有一件事要做来着。"
    w "……"
    w "干嘛？你那么盯着我干嘛？"
    show y 正常02 at ct with dissolve
    y "诶嘿，麻烦你把我送回去。"
    narrator "袁艳指着自己躺在病床上的身体。"
    w "……."
    narrator "这怎么可能做得到啊，之前不是试过很多次了吗？"
    show y 正常03 at ct with dissolve
    y "拜托啦，就一次就一次！"
    w "……"
    narrator "这丫头笑嘻嘻的，搞得好像能成功一样。"
    narrator "这个时候我不应该有点紧张感，应该很难受才是吗？"
    narrator "自从和她在一起之后，我就发现好像什么都不一样了。"
    narrator "不过，诅咒已经压过来了，横竖都逃不过了。"
    narrator "看着笑嘻嘻的袁艳，我就一阵火大，我之后的计划都给搞乱了。"
    narrator "这个人到底是怎么回事啊？"
    narrator "从认识她之后我的节奏一直就被她带着跑，这家伙难道是我命里的克星吗？"

    # TODO 26
    #CG:雨中的猫](忘记原CG叫啥了，回头改一下。)"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_c_yz = True
    scene c_雨中 with Dissolve(2)
    
    pause 1.0

    narrator "突然想起来，好像我的命也是被她救的。"
    narrator "不然的话我早就应该死了才对。"
    narrator "这么想想，感觉好像是我把她给拖下水了。"
    narrator "说到底，责任还是有我一份的呀。"
    narrator "哎…想太多脑袋都炸了"
    narrator "既然这个丫头已经疯了，那我陪她疯一下就好咯。"
    narrator "反正我的命也是她救的。"
    narrator "还给她就是了。"
    narrator "反正她也跑不掉。"

    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    w "哈哈哈哈…"
    narrator "我忍不住笑了起来。"
    show y 正常04 at ct with dissolve
    y "你笑啥？"
    w "算啦算啦，我试试好了。"
    show y 正常05 at ct with dissolve
    y "……"
    narrator "我闭上了双眼，再一次引动力量。"
    narrator "但是实际上我这个时候已经完全没有啥力量了。"
    narrator "反正诅咒已经快到了，早到跟晚到也没啥区别…"
    narrator "就让我借一下所谓诅咒的力量吧。"
    w "……"
    show y 正常04 at ct with dissolve
    y "你在做啥啊？"
    w "……"
    narrator "灵魂开始颤抖…"
    narrator "好疼…"
    narrator "有种撕心裂肺的感觉…."
    narrator "但是说句实话，跟袁艳这丫头相处了一段时间之后，会发现自己的心也变大了。"
    w "…."
    narrator "别吵了，这丫头让我完全专心不起来。"
    show y 正常02 at ct with dissolve
    y "哇，你的脚消失啦！！"
    w "…."
    narrator "吵死啦，一会失败了怎么办！"
    show y 正常01 at ct with dissolve
    y "你肚子不见啦！！！喂！你听到我说话没有？"
    show y 恼火01 at ct with dissolve
    y "喂！你听我说话啊喂！"
    w "……"
    narrator "我在也忍不住了。"
    w "都说让你别吵啦！没看到我在专心做事吗？"
    narrator "……"

    # TODO 27
    #CG：破碎者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_psz = True
    scene cg_破碎者 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    narrator "然我的面前原本应该站在那里的身影，已经消失了。"
    w "……"
    w "咳咳咳…"
    narrator "突然而然的静谧让我原本想要说出的话哽咽在喉咙里。"
    narrator "撕裂的疼痛感然我已经快要睁不开眼睛了。"
    narrator "引用诅咒的力量，我的胆子是真的大。"
    narrator "无数黑色碎片宛如漩涡一般向我席卷而来。"
    narrator "我的身体正在渐渐的被卷走。"
    narrator "我看着病房里渐渐苏醒的袁艳。"
    narrator "鼻子忽然一酸。"
    narrator "我成功了。"
    narrator "我成功把这丫头送回去了。"
    narrator "以我自己提前被诅咒为代价。"
    narrator "我自己也没想到，这里就是旅程的终点…"
    narrator "啊，还有好多事情没有做…"
    narrator "啊，还没来得及多了解一下这个世界。"
    narrator "啊，还没来得及跟那个丫头道歉，把她卷入这件事情里面。"
    w "袁艳！！！你王八蛋！你还欠我猫薄荷没还啊！！！！！"
    narrator "伴随着眼里和吼声，似乎舒服了好多。"
    narrator "我看着袁艳渐渐的从床上爬起。"
    narrator "诅咒提前降临了…"
    narrator "快啊，死丫头…我快撑不住了。"
    narrator "我没了，下一个….就是你了。"

    # TODO 28
    #CG：破碎者结束]"
    nvl clear
    nvl hide
    window hide dissolve

    #场景：黑屏
    scene black with dissolve
    #场景：病房]"
    scene bf_白天 with dissolve:
        zoom .667
    # TODO
    #变色UI
    
    narrator "睁开了双眼。"
    narrator "再一次看到了天花板。"
    narrator "我从床上坐了起来。"
    narrator "看看自己的双手，抵在床上。"
    narrator "我回来了。"
    narrator "我看了看死猫曾在待过的位置。"
    narrator "那里什么也没有。"
    narrator "这只死猫做了啥我不知道，"
    narrator "但是我知道，现在那里肯定在发生着什么。"
    narrator "这个时候的林琴已经平静了下来。"
    narrator "我下床，打着赤脚走向了她的床位。"
    show y 正常02 at lt with dissolve
    y "醒一下醒一下…"
    show l 慌张09 at rt with dissolve
    l "…."
    show l 慌张08 at rt with dissolve
    l "嗯…嗯…"
    narrator "带着泪光，少女逐渐苏醒了过来。"
    narrator "在目光触及我的一瞬间，像是些许无助的孩子。"
    show l 注视07 at rt with dissolve
    l "我…"
    show l 慌张08 at rt with dissolve
    l "我…."
    show y 正常04 at lt with dissolve
    y "我什么？"
    show l 慌张07 at rt with dissolve
    l "我梦见她不见了…"
    narrator "不就是一个梦么，你哭啥啊？"
    narrator "我不由得笑了起来。"
    show l 慌张08 at rt with dissolve
    l "你不是说能让我见到她么？"
    show l 慌张08 at rt with dissolve
    l "她现在在哪？"
    show y 笑容03 at lt with dissolve
    y "呵呵呵…."
    narrator "我看了看原本灵魂之火所在的位置，笑了一下。"
    narrator "我看不见什么。"
    narrator "很可惜，你并不是那个我要找的女孩。"
    narrator "林琴的表情有些紧张，她期待着看着我。"
    narrator "但是我很抱歉，我没有办法回应你的期待。"
    narrator "虽然没办法让你见到她。"
    show y 开心 at lt with dissolve
    y "她…让我给你带一句话。"
    narrator "话刚刚说出口，我的心脏忽然收缩。"
    narrator "或许是哪一个神明意识到了我接下来要说出口的事情。"
    narrator "话到了嘴边却开始受到了无数阻力。"
    narrator "有什么东西在阻止我把话说出口。"
    show l 惊异03 at rt with dissolve
    l "…."
    narrator "少女睁大了眼睛，死死的盯着我，想要听到我嘴里的话。"
    show y 俏皮 at lt with dissolve
    y "…."
    narrator "那家伙已经死掉啦，我没办法把他的人带回来给你。"
    narrator "但是…多少帮他传达一句话给你，还是没有问题的。"
    show y 嘲笑 at lt with dissolve
    y "我是说啦…"
    show y 嘲讽02 at lt with dissolve
    y "咳咳咳…."
    narrator "我感到了一阵阵的拉扯力，这份疼痛感就像是藤蔓一般，缠绕上我的胸口。"
    narrator "并随着我的血管一路攀岩，拉扯着我的喉咙。"
    narrator "简单的话语，到了嘴边…愣是发不出声音。"
    narrator "一个想法闪过了我的脑海，如果我把下面的话说出来。"
    narrator "我将会受到无比苛刻的惩罚。"
    narrator "说的也是，想要传达来自另外一个世界的思念，根本就是一件不可能的事情。"
    narrator "早知道…就不救那只死猫了。"
    narrator "谁知道这只死猫身上会带着那个世界的思念啊…"
    narrator "我真是个笨蛋啊…"
    show y 嘲讽02 at lt with dissolve
    y " 她说啦…你一个人辛苦啦。"
    show y 嘲讽01 at lt with dissolve
    y "她说…和你在一起的时间超开心啦。"
    show y 开心 at lt with dissolve
    y "她说…她真的好喜欢你啦！"
    show l 惊异03 at rt with dissolve
    l "…."
    show y 开心 at lt with dissolve
    y "这真的是一个苦差事，你有啥话让我带给她的吗？"
    narrator "就好像什么枷锁被瞬间打碎了一样。"
    narrator "我说的话变得容易了许多。"
    narrator "然而，少女的眼泪忽然滑落脸颊。"
    #show l 慌张07 at rt with dissolve
    #l "(呜咽声)"
    
    # TODO 29
    #CG:哭泣]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_lxj = True
    scene cg_林小姐 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    narrator "伴随着我的话语，似乎有什么传达到了少女的身边。"
    narrator "或许是这份持续了不知道多少年的思念。"
    narrator "或许是让少女孤独的走在这个世界上的歉意。"
    narrator "少女的哭声就像是让我重新回到了那个静谧的房间。"
    narrator "少女的形影单只让人心疼。"
    narrator "这些年，你辛苦了。"
    narrator "少女再也忍不住，大声哭了起来。"
    narrator "……"

    #场景：黑暗
    scene black with dissolve

    narrator "而我，却坠入了黑暗之中。"

    # TODO 30
    #CG:堕落者]"
    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xc = True
    scene cg_下沉 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0
    
    narrator "我仿佛不断的在下坠。"
    narrator "周围安静得可怕。"
    "？？" "死丫头，你来啦？"
    y "…."
    y "呵呵，我来了。"
    "猫" "真的搞不懂耶，你是个猪吗？"
    "猫" "居然真的把那个世界的话带到现实世界里面去了。"
    "猫" "真不知道该佩服你还是说你好了。"
    y "呵呵…"
    narrator "短暂的沉寂之后，熟悉的声音再一次响起。"

    # TODO 31
    #CG:光晕]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_mf = True
    scene cg_魔法 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0
    

    "猫" "你后悔不？"
    narrator "…."
    y "该说后悔还是不后悔呢？"
    y "……"
    y "希望她们都能过得好一点吧。"
    y "毕竟…她们可是我唯一的朋友啊。"
    narrator "黑暗的那一端，陷入了沉默。"
    y "…."
    y "还有你…死猫。"

    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    # TODO 32
    #CG:结束]"
    narrator "(个人线 完结)"

    jump c3_4

label c3_2_c:

    $c3_2_c_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0

    #个人线-主线转换线)"
    scene black with dissolve
    narrator "【距离诅咒发作还剩一天】"
    #场景：黑屏
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
        
    show y 正常03 at ct with dissolve
    y "咳咳咳…"
    show y 正常01 at ct with dissolve
    y "喂…死猫该醒了。"
    show y 恼火01 at ct with dissolve
    y "还睡你妹啊。"
    w " 唔…唔喵…喵？"
    w "哇，你放开手啊！耳朵要掉啦要掉啦！"
    narrator "我还在做春秋大梦的时候，不知何时袁艳已经醒过来了。"
    narrator "其实一点也不痛，也没人她也没揪住我的耳朵。"
    narrator "我只是习惯性的就开口了，看来这几天受她不少照顾。"
    narrator "喉咙已经生成了肌肉记忆了，只要她叫我起床，我就会这样叫嚷。"
    narrator "这以后要是嫁出去不知道要给伴侣家添多少麻烦。"
    narrator "这么快的吗？"
    w "你回来得这么快的吗？"
    narrator "袁艳则是一脸很吃惊的表情看着我。"
    show y 正常02 at ct with dissolve
    y "你逗我呢？你看着都什么时候了。"
    show y 正常03 at ct with dissolve
    y "都第二天了好不好？？"
    narrator "袁艳指着窗外渐渐亮起来的天空。"
    narrator "我似乎明白了一件事情。"
    w "嗯。"
    w "我们好像完蛋了呢，嘿嘿。"
    show y 不爽02 at ct with dissolve
    y "笑你个大头鬼啦。"
    show y 不爽01 at ct with dissolve
    y "我跟你说的不是这个事情。"
    w "那是啥？"
    show y 正常04 at ct with dissolve
    y "而是她啦，程祎琳的。"
    w "她怎么么？"
    w "难不成她就是我们要找的那个崩坏的女孩？"
    narrator "我露出惊喜的表情，期待着袁艳的回答。"
    narrator "不料袁艳却白我一眼。"
    show y 正常05 at ct with dissolve
    y "很难说，你知道我干啥去了不。"
    w "你干啥去了？不是让你去看她的过去么？"
    show y 正常04 at ct with dissolve
    y "不，没那么简单。"
    show y 正常02 at ct with dissolve
    y "我直接在意识里面见到程祎琳了。"
    w "啥？"
    show y 正常01 at ct with dissolve
    y "一时半会也说不清。"
    show y 正常01 at ct with dissolve
    y "总之就是我好像陷入了一场奇怪的灾难里面。"
    w "额，虽然听不懂但是很厉害的样子。"
    w "那你得到了什么结论没有？"
    show y 正常04 at ct with dissolve
    y "能不能麻烦你再送我回去一趟？"
    w "……"
    w "这才是你的目的吧。"
    show y 正常04 at ct with dissolve
    y "是啊"
    w "喂，我们哪里还有时间给你这样子玩啊。"
    w "再说我已经没剩多少力量了啊。"
    show y 正常05 at ct with dissolve
    y "可是我总觉得故事到那里还没有完结。"
    show y 俏皮 at ct with dissolve
    y "就一次…就一次可以不？"
    narrator "我有些瞠目结舌的看着袁艳，我也是第一次被这样提要求。"
    narrator "搞得好像还能有下一次一样。"
    narrator "我不免在心里狠狠的吐槽了袁艳这个家伙一顿。"
    narrator "这家伙绝对是生下来克我的。"
    show y 正常04 at ct with dissolve
    y "如果这家伙不是，我们接下来点燃正确的几率就大多了好不啦。"
    narrator "但是听她这么一说好像也确实有道理。"
    narrator "话说一开始我就是被这么忽悠的吧。"
    narrator "也没有道理事情做一半就没做完吧。"
    narrator "只是可怜我那用一点就少一点的力量啊，这样就算是点燃对了，我想要恢复也要很长时间了。"
    narrator "唉。"
    narrator "算了算了。"
    w "好吧好吧，你准备一下。"
    narrator "我无奈的叹了一口气。"
    narrator "真的下血本啊。"
    w "我们没剩多少时间了。"
    w "该回来的时候你可得记着要回来啊。"
    show y 正常05 at ct with dissolve
    y "额…"
    w "准备好。"
    show y 正常04 at ct with dissolve
    y "其实…"
    narrator "就在我将她的灵魂送往过去的那一瞬间。"
    show y 正常02 at ct with dissolve
    y "其实…"
    show y 正常01 at ct with dissolve
    y "我好像在程祎琳的过去看到了我们两个。"
    hide y with dissolve
    #袁艳立绘消失)"
    narrator "……"
    narrator "短短的几句话却让我足足愣了好几秒。"
    narrator "许久，才终于爆发出来。"
    w "啥？？？"
    narrator "……"
    w "啥？？？"
    
    #场景：黑屏" ""
    scene black with dissolve

    narrator "好黑…好难受…肚子好饿。"
    narrator "好痛苦的感觉。"
    
    #场景：街道" ""
    scene street_白天 with dissolve:
        zoom .667
    
    narrator "我在大街上，是一直熟悉的街道。"
    #show c 呼气 at ct with dissolve
    c "……"
    narrator "阳光照在我的身上，好暖和，但是好饿；"
    narrator "微风吹过我的身体，好舒服，但是好饿；"
    narrator "人群经过我的身边，好热闹，但是好饿；"
    narrator "时间真的是一个好东西。"
    narrator "很多与自己无关的事情都会被抛之脑后。"
    narrator "然而我一件也忘不了。"
    narrator "闭上眼睛还能听到他们曾经的声音。"
    narrator "即便紧紧捂住耳朵也无法阻隔他们的声音。"
    narrator "那场灾难里，有一个幸存者。"
    narrator "那就是我。"
    narrator "那就是事实。"
    narrator "后来，我找了很多当时的信息，甚至还去询问过对我们实施救援的人。"
    narrator "那个完全黑暗的隧道里，曾接连发生了好几次塌方。"
    narrator "许多救援人员都牺牲在二三次灾害中。"
    narrator "然而就是这样，一个发着高烧、浑身是伤的女孩却凭借着自己完全的毅力活了下来。"
    narrator "成为了那场灾难中唯一的幸存者。"
    narrator "这简直就像是在说一个笑话。"
    narrator "连我自己都不会相信我是凭借着自己的毅力活下来的。"
    narrator "他们是这么说的。"
    narrator "这是一个奇迹，居然还有人能在那样恶劣的环境下生存下来。"
    narrator "原本是赞叹奇迹的事情，但事情总不可能顺利。"
    narrator "我想要再次融入社会生活十分的困难。"
    narrator "‘为什么她能活下来？’"
    narrator "尽管明面上没有发生任何变化，但是大家都对我为什么能活下来非常疑惑。"
    narrator "一次灾祸之后总是会伴随着第二次灾祸。"
    narrator "‘她是吃着同学的血肉存活至今的’"
    narrator "不和谐的声音伴随着舆论席卷起了二次灾难。"
    narrator "只不过这一次是针对我一个人而来。"
    narrator "宛如浪潮一般，一轮接着一轮。"
    narrator "谁解释都没有用。"
    narrator "这些舆论比起当初压在我身上的石头，过而犹不及。"
    narrator "他们都想要知道在那个废墟之下究竟发生了什么事情。"
    show c cs_3_1 at ct with dissolve
    c "我不知道….我没有说谎。"
    narrator "我真的不知道，我也不知道自己为什么能活下来。"
    narrator "关于那时的记忆…"
    
    # TODO 44
    #CG： 黑影](前面的拥抱CG图 涂黑 加 回忆线)"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_c_yb = True
    scene c_拥抱 with dissolve

    pause 1.0

    narrator "有些断断续续，但是我还是能依稀记起在那暗黑的废墟下的记忆。"
    narrator "冷静下来思考的话，一定不止我一个幸存者才对。"
    narrator "因为我记得，在那废墟之下除我还有别人活着。"
    narrator "只是我想不起他是谁。"
    narrator "就是这个人，用双手撑起了我的生命。"
    
    #场景：街道" ""
    scene street_白天 with dissolve:
        zoom .667
    
    narrator "我想要找到他。"
    narrator "我也不知道自己为什么要找到他。"
    narrator "精神上的饥饿感迫使我无法于这正常人交流。"
    narrator "我太过弱小，所以出院之后我就拼命的锻炼自己。"
    narrator "如果当时的我也能像现在一样，是不是就能看清他的样子呢？"
    narrator "如果他真的在的话，好想亲口问他——"
    narrator "我真的把我幸存的同学们杀死了吗？"
    narrator "我真的为了活下来吃了已经死去的朋友们吗？"
    narrator "我真的是一个为了活下来不择手段的女孩子吗？"
    narrator "我真的…是一个危险的孩子吗？"
    show c 恶心02 at ct with dissolve
    c "……."
    narrator "好疼…胸口忽然隐隐作痛。"
    narrator "身体传来阵痛…到底是怎么回事？"
    # TODO 45
    #CG： 黑影](前面的拥抱CG图 涂黑 加 回忆线)"
    narrator "好想知道为什么…"
    narrator "为什么我非得承受这份委屈不可…"
    narrator "我明明什么都不知道。"
    narrator "凭什么压力都在我一个人的身上。"
    narrator "就因为我活下来了吗？"
    narrator "好难受…这是个什么样的世界啊？"
    show c 恶心02 at ct with dissolve
    #尖叫声)
    c "啊啊啊啊啊啊啊！！！！！！"
    
    #场景：黑屏" ""
    scene black with dissolve

    narrator "突然一切就消失了，我伫立在黑暗中。"
    narrator "有谁在黑暗的另一端。"

    # TODO 46
    #CG:下沉]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xc = True
    scene cg_下沉 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0

    narrator "少年的声音回荡在这个空间里。"
    narrator "像是说给我听的，可是我又是谁？"
    narrator "他又是谁，他的声音有重逢一般的喜悦。"
    narrator "又有说不清道不明的后悔，那是欣喜与歉意的声音。"
    narrator "……"
    narrator "话说我不是信使啊，为啥要我带话？"
    narrator "还有让我带话给谁啊？"
    narrator "想到这里，一切戛然而止。"
    narrator "无形的漩涡将我带走。"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667
    
    narrator "再一次回到这里的袁艳，伫立在我的面前。"
    w "……"
    show y 正常05 at ct with dissolve
    y "……"
    w "所以说到底怎么了？"
    show y 正常04 at ct with dissolve
    y "这个不好跟你解释…"
    narrator "袁艳看了看躺在床上的程祎琳。"
    narrator "叹了一口气。"
    w "…."
    narrator "所以说到底怎么啦。"
    narrator "程祎琳到底是不是那个崩坏女孩啊。"
    show y 正常03 at ct with dissolve
    y "我可能见到了很奇怪的东西"
    w "什么东西？"
    show y 正常01 at ct with dissolve
    y "你现在还能把我送回去不？"
    narrator "她指一下自己的身体。"
    narrator "我马上就明白她的意思。"
    w "……"
    w "之前不是试过了吗？基本上不太可能了啊。"
    show y 正常02 at ct with dissolve
    y "好吧。"
    narrator "……."
    w "那你现在能做判断了不？"
    narrator "我看了看袁艳，她应该是明白我的意思。"
    narrator "袁艳则是又看看床上的程祎琳，依旧在犹豫。"
    narrator "还没有下定决心。"
    show y normal_3_2 at ct with dissolve
    y "我好像做了一个很长的梦。"
    narrator "忽然间，袁艳这么说道。"
    w "哈？"
    narrator "我有点不太理解她现在说这个是有啥意义。"
    w "做个梦跟我们现在的情况有关系嘛？"
    show y 正常01 at ct with dissolve
    y "怎么说呢…我就感觉特别疼，特别难受，还有个谁让我带话。"
    w "谁让你带话？"
    narrator "我歪了歪脑袋，有点不太明白袁艳这家伙说的话。"
    narrator "袁艳再一次看床上的程祎琳一眼，叹了一口气。"
    show y 正常05 at ct with dissolve
    y "该怎么说呢…这种感觉并不是很好。"
    show y 正常04 at ct with dissolve
    y "有人托我给这丫头带个话。"
    w "说啥了？"
    show y 正常02 at ct with dissolve
    y "虽然不知道有啥用，不过应该是谁很想她之类的？"
    w "想她？咋没人想想我们？"
    w "算了算了，别管那么多，你到底弄清楚没？"
    w "这个丫头到底是不是我们要找的那个啊？"
    show y 正常01 at ct with dissolve
    y "……"
    narrator "这个时候反倒是她沉默了一下。"
    show y 正常05 at ct with dissolve
    y "问一下。"
    w "都到这种时候，你还有啥问题啊？"
    show y 正常05 at ct with dissolve
    y "说到底崩坏到底是个什么东西？"
    show y 正常04 at ct with dissolve
    y "我觉得她这丫头挺好的呀。"
    w "那你就把事情想得太简单了。"
    narrator "太草率了！"
    w "所谓的崩坏可比你想的要严重的多。"
    w "这样的人是介于灵魂状态和现实状态为一体的存在。"
    w "换句话来说，就是这样的人在现实世界中不论生死都能影响现实世界。"
    w "严重的会使得灾难具象化。"
    show y 正常04 at ct with dissolve
    y "麻烦你解释得通俗点，能让我听懂的那种。"
    w "……"
    w "简单来说崩坏的人可以引发灾难。"
    w "大到你们常见的洪水，地震，小到你走路被天上掉下来的东西砸死这样的。"
    show y 正常04 at ct with dissolve
    y "…."
    show y 正常05 at ct with dissolve
    y "那不是很刺激？？"
    w "刺激个鬼啦！"
    w "这种无法无天的存在很容易导致城市毁灭的好不啦！"
    show y 无措 at ct with dissolve
    y "我都想变成崩坏的那只了！"
    w "你这么羡慕个啥？"
    show y 俏皮 at ct with dissolve
    y "你想想，完全没人能管我耶？"
    w "是没人能管你了。"
    narrator "我不由得摊了摊爪子。"
    w "包括你自己也管不了你自己。"
    show y 正常04 at ct with dissolve
    y "啊？"
    show y 正常05 at ct with dissolve
    y "不可控的？"
    w "嗯。"
    show y 正常03 at ct with dissolve
    y "那还是不要了。"
    w "明白了？"
    show y 正常02 at ct with dissolve
    y "明白了！"
    w "那这个叫程祎琳的丫头是不是那个崩坏的女孩啊？"
    show y 正常01 at ct with dissolve
    y "这个啊…."
    narrator "看她犹豫的样子，我多半就能理解了。"
    narrator "她没有办法做出判断。"
    narrator "但是花了这么大的代价，总得问出有用的信息才行啊。"
    show y 正常04 at ct with dissolve
    y "虽然还是没办法判断，不过我有个有用的信息可以拿出来用用。"
    w "嗯？"
    narrator "和我想到一块去了。"
    show y 正常05 at ct with dissolve
    y "这个丫头身体里面应该还有另外一个灵魂。"
    w "……"
    narrator "听到这个消息，我不由得沉默了起来。"
    narrator "另一个灵魂？干扰现世？好像完全符合崩坏的条件啊。"
    show y 正常04 at ct with dissolve
    y "其实我们也不急不是，不是还有一天嘛。"
    narrator "袁艳尴尬的笑着。"
    
    #场景：黑屏" ""
    scene black with dissolve

    w "……"

    #场景：病房" ""
    scene bf_白天 with dissolve:
        zoom .667

    narrator "我长长叹了一口气。"
    w "哪里还有一天啊。"
    show y 正常01 at ct with dissolve
    y "啊？"
    w "现在的你已经是必须要做出决定的时候了。"
    w "今天黄昏时刻，我们点火若不成功。"
    w "…."
    w "最好的情况就是咱们两个灰飞烟灭，再也回不去。"
    show y 正常02 at ct with dissolve
    y "那.最坏的呢？"
    narrator "女孩瞪大眼睛，就像是我刚刚说的话毫无震撼力度一样。"
    w "……"
    narrator "至始至终，这个丫头都是这样。"
    narrator "把心大的性格发挥到了极致，这已经不是心大了吧。"
    narrator "我都不知道拿什么个性来形容她。"
    narrator "这丫头难不成就是那个要崩溃的女孩吗？"
    narrator "我被我的想法吓了一跳，但是我马上摇了摇猫头。"
    narrator "不可能的，在我边上我都不知道。"
    narrator "那我这神圣的猫不是白当了。"
    narrator "不过她的性格真的是有点厉害了，适应能力也有点强得让我无法理解了。"
    narrator "人类都是这样的吗？"
    narrator "要都是还会有什么崩坏的人嘛？"
    narrator "说到底这个世界上真的有袁艳这种人吗？"
    w "我说…你真的是个人吗？"
    show y 正常04 at ct with dissolve
    y "问的什么话…"
    show y 不爽02 at ct with dissolve
    y "我不是人是什么？鬼吗？"
    narrator "我点了点头。"
    show y 正常05 at ct with dissolve
    y "……"
    w "不扯了不扯了，你现在能做判断不？"
    w "我觉得她很有可能就是有问题的女生。"
    w "毕竟两个灵魂，这也太可疑了。"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳没有说话，我就当她是默认了。"
    w "……"
    narrator "既然如此，也就没有必要继续等待下去了。"
    narrator "看了袁艳一眼，我便闭上了眼睛，准备开始引出最后的力量，吟唱赞歌。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/2333.wav" loop fadein 2.0 fadeout 2.0

    # TODO 47
    #[CG:引导者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz1 = True
    scene cg_引导者1 with Dissolve(2):
        zoom .667
    
    pause 1.0

    #show y 无措 at ct with dissolve
    y "哇，你在干嘛呢？"
    w "…."
    #show y 无措 at ct with dissolve
    y "哇？她是谁啊？？？"
    narrator "我闭着眼睛。"
    w "我在有事你没看见吗？"
    w "忙着呢，别打扰我！"
    #show y 无措 at ct with dissolve
    y "……"
    #show y 无措 at ct with dissolve
    y "不是，你谁啊？"
    
    # TODO 48
    #CG:引导者](睁眼)"
    nvl clear
    nvl hide
    window hide dissolve
    #scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz2 = True
    scene cg_引导者2 with Dissolve(1):
        zoom .667
    
    pause 1.0

    w "…."
    narrator "被她烦的不行了，睁开眼睛瞅了她一眼。"
    w "是我怎么了？"
    #show y 正常04 at ct with dissolve
    y "你还是个美少女啊，没看出来啊。"
    w "……"
    #show y 开心 at ct with dissolve
    y "啧啧啧…还挺漂亮的。"
    #show y 笑容01 at ct with dissolve
    y "你要是早点变成这样，我就不会对你那么凶了。"
    w "……"
    w "快闭嘴啊！我在控制力量，能不能别让我分神。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0
    
    #场景：病房" ""
    scene bf_白天 with dissolve:
        zoom .667
    
    narrator "好说歹说，终于算是让这个妮子闭嘴了。"
    narrator "没了她说话分神，我引导力量的速度也快了许多。"
    narrator "不一会儿，就完成了力量的引导，在我的人体印象的胸口，点燃了一簇蓝色的火焰。"
    w "…."
    #show y 正常04 at ct with dissolve
    y "……"
    narrator "在火焰下，我和袁艳彼此对视一眼。"
    w "我做了啊…"
    #show y 正常05 at ct with dissolve
    y "做啥？"
    w "点燃她啊。"
    narrator "我看着床上的程祎琳，然后又看了看袁艳。"
    narrator "怎么好像还要征得她同意一样。"
    narrator "顿时有点郁闷了起来。"
    #show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳明显的犹豫了一下。"
    #show y 正常04 at ct with dissolve
    y "你点呗。"
    w "那我动手了啊。"
    #show y 正常04 at ct with dissolve
    y "……"
    #show y 正常05 at ct with dissolve
    y "你动手啊！磨磨唧唧的。"
    w "……"
    narrator "我一怔，就准备开始书写大结局的故事了。"
    narrator "只要我把接下来的灵魂之火放到这个女孩的身体里面，一切就完成了。"
    narrator "总觉得事情没那么顺利…"
    narrator "程祎琳翻了个身。"
    narrator "然后我控制着灵火直接放到了她的身体里面。"
    narrator "看着灵火漂浮在她的胸口。"
    narrator "我有些愣神…会不会有点太简单了？"
    narrator "按道理来说，这个时候不应该出现一点点变故吗？"
    w "……"
    #show y 正常02 at ct with dissolve
    y "……"
    #show y 正常03 at ct with dissolve
    y "接下来呢？"
    w "等着就行了。"
    narrator "接下来只需要等灵魂之火灼烧殆尽这个灵魂即可。"
    narrator "保佑啊，这个丫头是那个女孩，一定要是啊…."

    nvl clear
    nvl hide
    window hide dissolve

    #场景：黑屏"
    scene black with Dissolve(.7)
    narrator "时间一点一点的过去了。"
    
    #场景：病房" ""
    scene bf_白天 with dissolve:
        zoom .667
    w "……"
    show y 正常02 at ct with dissolve
    y " ……"

    #场景：黑屏"
    scene black with dissolve
    narrator "没什么变化。"

    #场景：病房"
    scene bf_白天 with dissolve:
        zoom .667
    show y 正常04 at ct with dissolve
    y "怎么没啥动静啊？"
    w "再等等…"
    narrator "头一回要这么久的时间。"
    show y 正常05 at ct with dissolve
    y "我去看看程祎琳的情况。"
    w "你是灵魂状态，你别靠太近啊。"
    show y 正常04 at ct with dissolve
    y "靠太近怎么了？"
    w "灵魂靠近这个火太近的话，就有可能会把你烧得灰飞烟灭啊。"
    w "别怪我没提醒你，你别到时候还没被诅咒干掉就被灵火烧死了。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "为啥？"
    w "这火对普通灵魂有绝对的杀伤力。"
    show y 正常05 at ct with dissolve
    y "那我还是不靠近了。"
    narrator "说罢，她退后了好几步。"
    show y 正常05 at ct with dissolve
    y "那它对人会咋样呢？如果她不是崩坏的灵魂的话…"
    w "…."
    c "…."
    c "emmm…."
    c "唔…唔…"
    narrator "难受的呻吟声在病房里幽幽的响起，我和袁艳对视一眼，马上就安静了下来。"
    narrator "看来，该来的还是来了。"
    narrator "但是，总感觉不太对。"
    narrator "这不像是在清除崩坏的症状啊…"
    narrator "别吧…我不由得捂住了眼睛，不敢看。"
    w "袁…袁艳。"
    show y 正常02 at ct with dissolve
    y "干啥？"
    w "你帮我看看…"
    w "她是不是浑身冒黑烟之类的？有没有？"
    w "……"
    show y 正常01 at ct with dissolve
    y "没有啊，她就一直在叫而已啊，像做噩梦一样。"
    narrator "听到袁艳的话，我的顿时就愣住了。"
    w "完了…."
    show y 正常01 at ct with dissolve
    y "怎么了？"
    narrator "这不是清除掉崩坏时应该有的现象…"
    narrator "换而言之，也就是程祎琳这个女孩并不是那个崩坏的女孩."
    narrator "判断错了。"
    w "我们….错了啊…"
    narrator "知道真相的我差点都要哭出来了。"
    narrator "这么多天的努力，结果居然弄错了。"
    narrator "真的是命啊…"
    w "呜喵…唔喵…."
    narrator "还是没忍住，哭出来了。"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "干啥呢干啥呢，奔丧呢你？"
    w "我们…我们，我们…完了啊！"
    show y 正常05 at ct with dissolve
    y "完什么完，你还没回答我呢。"
    w "啊？"
    narrator "回答什么，都这时候还回答什么啊？"
    show y 正常05 at ct with dissolve
    y "灵魂之火对普通人有啥伤害吗？"
    narrator "袁艳指了指躺在床上翻来覆去非常痛苦的程祎琳。"
    w "灵魂之火对人体能有什么伤害啊？"
    w "大姐…你省省心吧…我们选错了，要死了啊，你还有心情担心她？"
    narrator "我心情哽咽，知道自己马上要死的感觉真的一点都不好。"
    show y 正常04 at ct with dissolve
    y "那为啥这丫头这么难受啊？"
    w "……."
    narrator "我还在难受着呢，突然面前一阵风吹了过来。"
    narrator "她就像是一阵风一样冲到了我的面前。"
    show y 正常04 at ct with dissolve
    y "到底是怎么回事啦？"
    w "…."
    w "虽然她有躯体可以保护自己的灵魂，但是灵魂之火仍然是能够灼烧其灵魂的。"
    show y 正常05 at ct with dissolve
    y "嗯？"
    w "她肯定是要失去一些东西的，强行失去怎么可能不难受啊。"
    w "如果没有错的话，灼烧的肯定是她觉得比较重要的事情。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "能不能说点我能懂的？"
    show y 正常04 at ct with dissolve
    y "比如她失去了啥，或者怎么灭了这火？"
    w "你疯啦？"
    show y 恼火04 at ct with dissolve
    y "讲重点。"
    narrator "袁艳很无语的看着我，难不成她真打算灭掉这火？"
    w "……"
    narrator "一旦点燃这个火，想要在灭掉是不可能的…几乎不可能的。"
    narrator "除非……"
    w "这玩意肯定要烧掉啥东西才能灭掉。"
    w "啊….反正咱们也死定了.你能不能表现得在悲伤一点啊？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "死猫，既然不是她，她这么难受不是显得我们俩有点缺德嘛？"
    w "都快死的人了…呜呜呜…."
    narrator "我几乎要放生大哭了起来。"
    show y 正常05 at ct with dissolve
    y "…."
    narrator "袁艳则是非常无语的看着我。"
    show y 恼火04 at ct with dissolve
    y "别奔丧了。"
    w "……"
    w "我们快完了好不好！！"
    show y 正常05 at ct with dissolve
    y "不是你真有那么悲伤？"
    w "…."
    w "那不是废话嘛？"
    narrator "看着有些玩味的袁艳，我有点儿搞不懂她是啥意思了。"
    w "倒是你，快完蛋的人了，你怎么跟过节一样开心啊喂！"
    show y 开心 at ct with dissolve
    y "我有说啥吗？"
    show y 笑容01 at ct with dissolve
    y "反正我们已经没救了不是吗？"
    narrator "袁艳突然在这个时候笑了起来。"
    narrator "完了，这丫头也没救了。"
    narrator "不，应该说这一开始咱们就没救了。"
    narrator "把希望放在她身上的我真的是个大笨蛋啊。"
    narrator "她压根对这种事情就无所谓的。"
    narrator "有点点懊恼。"
    narrator "但是现在已经来不及了啊。"
    narrator "我们真的已经完了。"
    w "你…干啥呢？"
    narrator "我看着袁艳一点一点的靠近少女。"
    narrator "我不是说她这个灵魂状态的不要靠近火吗？"
    narrator "她想干啥？"
    #show c 难受的声音 at ct with dissolve
    c "啊…"
    show y 正常05 at ct with dissolve
    y "她这叫声我听不下去了。"
    show y 正常05 at ct with dissolve
    y "让人担心的丫头。"
    narrator "在我的注视之下，袁艳伸出了手。"
    narrator "将放置在女孩胸口的灵魂之火取了出来。"
    w "喂，你别乱搞啊！！会死的！"
    narrator "我突然紧张了起来。"
    
    # TODO 49
    #淡出[CG:救赎者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz = True
    scene cg_救赎者 with Dissolve(2):
        zoom .667
    
    pause 1.0

    w "…."
    w "我.的…妈呀…"
    narrator "女孩手捧着灵魂之火，伫立在房间里头。"
    narrator "静谧的房间，传来了滋滋的声音，看不见的火焰在不断的溶解着少女的身体。"
    narrator "就好似飘散的花瓣，散落漂浮在这个空间里面。"
    narrator "你到底要做什么啊？"
    narrator "之前一点点火就已经把你疼了个半死。"
    narrator "现在直接把火捧在手上，你不要命啦？"
    
    #场景：黑屏" ""
    scene black with dissolve
    #场景：病房" ""
    scene bf_白天 with dissolve:
        zoom .667
    
    y "死猫…这个火会烧掉琴丫头全部的记忆。"
    narrator "她好像忽然明白了什么一样。"
    w "…."
    narrator "我其实是知道的，灵魂之火会褪去一个人心中全部的执念。"
    narrator "会把一个人变成符合世界所需要的‘正常人’，渐渐的融入世界中，与他人无异。"
    narrator "这就是我们的使命。"
    narrator "很显然，这些记忆就是程祎琳全部的执念。"
    narrator "如果烧掉，那么这个不合群的少女，就应该很容易融入人类所谓的社会当中去。"
    narrator "这应该是一件好事才对。"
    narrator "我不明白，为什么这丫头会这么痛苦呢？"

    # TODO 50
    #CG:救赎者的笑容]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz_smile = True
    scene cg_救赎者的笑容 with Dissolve(2):
        zoom .667
    
    pause 1.0

    y "我刚刚看到了…"
    narrator "袁艳，几乎是是从牙缝里面挤出来的几句话。"
    y "这丫头…在哭。"
    y "那些被记住的事情，对她应该特别重要。"
    y "死猫…再帮我一件事…"
    y "我…要回到那具身体里面去。"
    w "……"
    narrator "这是不可能做到的吧。"
    narrator "话说…"
    w "你赶快…放手啊！你会被烧死的啊！"
    w "灵魂一旦被烧， 这个世界上就真的没有你了啊！！"
    y "…."
    y "痛痛痛痛死了！"
    y "诶嘿嘿…你以为是我死了吗？"
    y "其实我没有死哒！"

    # TODO 51
    #CG:抛出去]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_pcq = True
    scene cg_抛出去 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "就像是扔掉了一个烫手山芋一样。"
    narrator "袁艳伸出了手，将灵魂之火抛到了空中。"
    narrator "它就飘在半空中，似乎是被谁带走的一样。"
    w "……"
    narrator "我惊讶的说不出话来。"
    w "你….你是怎么做到的？"
    w "灵魂之火不烧掉一个灵魂是不会熄灭的。"
    y "嘿嘿…."
    narrator "你笑个鬼啦，虽然很想吐槽她，但是我还是说不出口。"
    narrator "我知道，肯定是发生了什么。"

    # TODO 25
    ##CG结束]"
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    show y 开心 at ct with dissolve
    y "刚刚我听到了声音。"
    show y 俏皮 at ct with dissolve
    y "程祎琳那丫头身体里面传出来的。"
    w "声音？"
    show y 笑容01 at ct with dissolve
    y "就是之前说的那个另外一个灵魂。"
    show y 笑容02 at ct with dissolve
    y "她一直守护着程祎琳。"
    show y 开心 at ct with dissolve
    y "…."
    narrator "她看着半空。"
    show y 正常04 at ct with dissolve
    y "然后，她代替了我。"
    w "……"
    narrator "我也看着半空。"
    narrator "虽然说挺了不起啦，但是也没有用。"
    narrator "我已经能够感觉到诅咒就快要来临了。"
    narrator "我们已经完蛋了。"
    show y 正常05 at ct with dissolve
    y "在此之前，我还有一件事要做来着。"
    w "……"
    w "干嘛？你那么盯着我干嘛？"
    show y 正常02 at ct with dissolve
    y "诶嘿，麻烦你把我送回去。"
    narrator "袁艳指着自己躺在病床上的身体。"
    w "……."
    narrator "这怎么可能做得到啊，之前不是试过很多次了吗？"
    show y 正常03 at ct with dissolve
    y "拜托啦，就一次就一次！"
    w "……"
    narrator "这丫头笑嘻嘻的，搞得好像能成功一样。"
    narrator "这个时候我不应该有点紧张感，应该很难受才是吗？"
    narrator "自从和她在一起之后，我就发现好像什么都不一样了。"
    narrator "不过，诅咒已经压过来了，横竖都逃不过了。"
    narrator "看着笑嘻嘻的袁艳，我就一阵火大，我之后的计划都给搞乱了。"
    narrator "这个人到底是怎么回事啊？"
    narrator "从认识她之后我的节奏一直就被她带着跑，这家伙难道是我命里的克星吗？"

    # TODO 53
    #CG:雨中的猫](忘记原CG叫啥了，回头改一下。)"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_c_yz = True
    scene c_雨中 with Dissolve(2)
    
    pause 1.0

    narrator "突然想起来，好像我的命也是被她救的。"
    narrator "不然的话我早就应该死了才对。"
    narrator "这么想想，感觉好像是我把她给拖下水了。"
    narrator "说到底，责任还是有我一份的呀。"
    narrator "哎…想太多脑袋都炸了"
    narrator "既然这个丫头已经疯了，那我陪她疯一下就好咯。"
    narrator "反正我的命也是她救的。"
    narrator "还给她就是了。"
    narrator "反正她也跑不掉。"

    
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    w "哈哈哈哈…"
    narrator "我忍不住笑了起来。"
    show y 正常04 at ct with dissolve
    y "你笑啥？"
    w "算啦算啦，我试试好了。"
    show y 正常05 at ct with dissolve
    y "……"
    narrator "我闭上了双眼，再一次引动力量。"
    narrator "但是实际上我这个时候已经完全没有啥力量了。"
    narrator "反正诅咒已经快到了，早到跟晚到也没啥区别…"
    narrator "就让我借一下所谓诅咒的力量吧。"
    w "……"
    show y 正常04 at ct with dissolve
    y "你在做啥啊？"
    w "……"
    narrator "灵魂开始颤抖…"
    narrator "好疼…"
    narrator "有种撕心裂肺的感觉…."
    narrator "但是说句实话，跟袁艳这丫头相处了一段时间之后，会发现自己的心也变大了。"
    w "…."
    narrator "别吵了，这丫头让我完全专心不起来。"
    show y 正常02 at ct with dissolve
    y "哇，你的脚消失啦！！"
    w "…."
    narrator "吵死啦，一会失败了怎么办！"
    show y 正常01 at ct with dissolve
    y "你肚子不见啦！！！喂！你听到我说话没有？"
    show y 恼火01 at ct with dissolve
    y "喂！你听我说话啊喂！"
    w "……"
    narrator "我在也忍不住了。"
    w "都说让你别吵啦！没看到我在专心做事吗？"
    narrator "……"

    # TODO 54
    #CG：破碎者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_psz = True
    scene cg_破碎者 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "然我的面前原本应该站在那里的身影，已经消失了。"
    w "……"
    w "咳咳咳…"
    narrator "突然而然的静谧让我原本想要说出的话哽咽在喉咙里。"
    narrator "撕裂的疼痛感然我已经快要睁不开眼睛了。"
    narrator "引用诅咒的力量，我的胆子是真的大。"
    narrator "无数黑色碎片宛如漩涡一般向我席卷而来。"
    narrator "我的身体正在渐渐的被卷走。"
    narrator "我看着病房里渐渐苏醒的袁艳。"
    narrator "鼻子忽然一酸。"
    narrator "我成功了。"
    narrator "我成功把这丫头送回去了。"
    narrator "以我自己提前被诅咒为代价。"
    narrator "我自己也没想到，这里就是旅程的终点…"
    narrator "啊，还有好多事情没有做…"
    narrator "啊，还没来得及多了解一下这个世界。"
    narrator "啊，还没来得及跟那个丫头道歉，把她卷入这件事情里面。"
    w "袁艳！！！你王八蛋！你还欠我猫薄荷没还啊！！！！！"
    narrator "伴随着眼里和吼声，似乎舒服了好多。"
    narrator "我看着袁艳渐渐的从床上爬起。"
    narrator "诅咒提前降临了…"
    narrator "快啊，死丫头…我快撑不住了。"
    narrator "我没了，下一个….就是你了。"

    # TODO 55
    #CG：破碎者结束]"
    nvl clear
    nvl hide
    window hide dissolve

    #场景：黑屏
    scene black with dissolve
    #场景：病房]"
    scene bf_白天 with dissolve:
        zoom .667

    #变色UI"

    narrator "睁开了双眼。"
    narrator "再一次看到了天花板。"
    narrator "我从床上坐了起来。"
    narrator "看看自己的双手，抵在床上。"
    narrator "我回来了。"
    narrator "我看了看死猫曾在待过的位置。"
    narrator "那里什么也没有。"
    narrator "这只死猫做了啥我不知道，"
    narrator "但是我知道，现在那里肯定在发生着什么。"
    narrator "这个时候的程祎琳已经平静了下来。"
    narrator "我下床，打着赤脚走向了她的床位。"
    show y 正常02 at lt with dissolve
    y "醒一下醒一下…"
    show c 注视03 at rt with dissolve
    c "…."
    show c 注视02 at rt with dissolve
    c "嗯…嗯…"
    narrator "带着泪光，少女逐渐苏醒了过来。"
    narrator "在目光触及我的一瞬间，像是些许无助的孩子。"
    show c 张嘴01 at rt with dissolve
    c "我…"
    show c 张嘴02 at rt with dissolve
    c "我记起来了…."
    show c 张嘴01 at rt with dissolve
    c "我都记起来了…."
    show c 张嘴01 at rt with dissolve
    c "我记起来我在找谁了，我知道了。"
    narrator "记起来不是一件开心的事情么？"
    narrator "那你哭啥啊？"
    narrator "我不由得笑了起来。"
    show c 惊讶02 at rt with dissolve
    c "那他现在在哪？"
    show y 笑容01 at lt with dissolve
    y "……"
    narrator "我看了看原本灵魂之火所在的位置，淡淡的笑了笑。"
    narrator "程祎琳的表情有些紧张，她期待着看着我。"
    narrator "但是我很抱歉，我没有办法回应她的期待。"
    show y 开心 at lt with dissolve
    y "他…让我给你带一句话。"
    narrator "话刚刚说出口，我的心脏忽然收缩。"
    narrator "或许是哪一个神明意识到了我接下来要说出口的事情。"
    narrator "话到了嘴边却开始受到了无数阻力。"
    narrator "有什么东西在阻止我把话说出口。"
    show c 斜视02 at rt with dissolve
    c "…."
    narrator "少女睁大了眼睛，死死的盯着我，想要听到我嘴里的话。"
    show y 俏皮 at lt with dissolve
    y "…."
    narrator "那家伙已经死掉啦，我没办法把他的人带回来给你。"
    narrator "但是…多少帮他传达一句话给你，还是没有问题的。"
    show y 嘲讽02 at lt with dissolve
    y "我是说啦…"
    show y 嘲讽06 at lt with dissolve
    y "咳咳咳…."
    narrator "我感到了一阵阵的拉扯力，这份疼痛感就像是藤蔓一般，缠绕上我的胸口。"
    narrator "并随着我的血管一路攀岩，拉扯着我的喉咙。"
    narrator "简单的话语，到了嘴边…愣是发不出声音。"
    narrator "一个想法闪过了我的脑海，如果我把下面的话说出来。"
    narrator "我将会受到无比苛刻的惩罚。"
    narrator "说的也是，想要传达来自另外一个世界的思念，根本就是一件不可能的事情。"
    narrator "早知道…就不救那只死猫了。"
    narrator "谁知道这只死猫身上会带着那个世界的思念啊…"
    narrator "我真是个笨蛋啊…"
    show y 嘲讽02 at lt with dissolve
    y "他说他好喜欢你。"
    show y 嘲讽01 at lt with dissolve
    y "他说…他好喜欢喜欢你。"
    show y angry_3_2 at lt with dissolve
    y "他说….他真的好喜欢你！"
    show c 侧视02 at rt with dissolve
    c "…."
    show y 开心 at lt with dissolve
    y "这真的是一个苦差事，你有啥话让我带给他的吗？"
    narrator "就好像什么枷锁被瞬间打碎了一样。"
    narrator "我说的话变得容易了许多。"
    narrator "然而，少女的眼泪忽然滑落脸颊。"
    show c 恶心01 at rt with dissolve
    c "(呜咽声)"

    # TODO 56
    #CG:哭泣]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_cylcry = True
    scene cg_哭泣程依琳 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "伴随着我的话语，似乎有什么传达到了少女的身边。"
    narrator "或许是这份持续了不知道多少年的思念。"
    narrator "或许是让少女孤独的走在这个世界上的歉意。"
    narrator "少女的哭声就像是让我重新回到了那个灾祸的现场。"
    narrator "这些年，你辛苦了。"
    narrator "少女再也忍不住，大声哭了起来，就像是一个孩子。"
    narrator "……"

    #场景：黑暗" ""
    scene black with dissolve

    narrator "而我，却坠入了黑暗之中。"
    
    #(淡出)"
    # TODO 57
    #CG:堕落者]"
    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xc = True
    scene cg_下沉 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0
    
    
    narrator "我仿佛不断的在下坠。"
    narrator "周围安静得可怕。"
    #show ？？ 猫 at ct with dissolve
    "？？" "死丫头，你来啦？"
    y "…."
    y "呵呵，我来了。"
    "猫" "真的搞不懂耶，你是个猪吗？"
    "猫" "居然真的把那个世界的话带到现实世界里面去了。"
    "猫" "真不知道该佩服你还是说你好了。"
    y "呵呵…"
    narrator "短暂的沉寂之后，熟悉的声音再一次响起。"
    
    # TODO 58
    #CG:光晕]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_mf = True
    scene cg_魔法 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0
    
    "猫" "你后悔不？"
    narrator "…."
    y "该说后悔还是不后悔呢？"
    y "……"
    y "希望她们都能过得好一点吧。"
    y "毕竟…她们可是我唯一的朋友啊。"
    narrator "黑暗的那一端，陷入了沉默。"
    y "…."
    y "还有你…死猫。"

    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    narrator "(个人线 完结)"

    jump c3_4

label c3_2_x:

    $c3_2_x_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0

    #个人线-主线转换线)"
    scene black with dissolve
    narrator "【距离诅咒发作还剩一天】"
    #场景：黑屏
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    show y 正常03 at ct with dissolve
    y "咳咳咳…"
    show y 正常01 at ct with dissolve
    y "喂…死猫该醒了。"
    show y 恼火01 at ct with dissolve
    y "还睡你妹啊。"
    w " 唔…唔喵…喵？"
    w "哇，你放开手啊！耳朵要掉啦要掉啦！"
    narrator "我还在做春秋大梦的时候，不知何时袁艳已经醒过来了。"
    narrator "其实一点也不痛，也没人她也没揪住我的耳朵。"
    narrator "我只是习惯性的就开口了，看来这几天受她不少照顾。"
    narrator "喉咙已经生成了肌肉记忆了，只要她叫我起床，我就会这样叫嚷。"
    narrator "这以后要是嫁出去不知道要给伴侣家添多少麻烦。"
    narrator "这么快的吗？"
    w "你回来得这么快的吗？"
    narrator "袁艳则是一脸很吃惊的表情看着我。"
    show y 正常02 at ct with dissolve
    y "你逗我呢？你看着都什么时候了。"
    show y 正常03 at ct with dissolve
    y "都第二天了好不好？？"
    narrator "袁艳指着窗外渐渐亮起来的天空。"
    narrator "我似乎明白了一件事情。"
    w "嗯。"
    w "我们好像完蛋了呢，嘿嘿。"
    show y 不爽02 at ct with dissolve
    y "笑你个大头鬼啦。"
    show y 不爽01 at ct with dissolve
    y "我跟你说的不是这个事情。"
    w "那是啥？"
    show y 正常04 at ct with dissolve
    y "而是她啦，夏静的。"
    w "她怎么么？"
    w "难不成她就是我们要找的那个崩坏的女孩？"
    narrator "我露出惊喜的表情，期待着袁艳的回答。"
    narrator "不料袁艳却白我一眼。"
    show y 正常05 at ct with dissolve
    y "很难说，你知道我干啥去了不。"
    w "你干啥去了？不是让你去看她的过去么？"
    show y 正常04 at ct with dissolve
    y "不，没那么简单。"
    show y 正常02 at ct with dissolve
    y "我的意识直接变成了她。"
    w "啥？"
    show y 正常01 at ct with dissolve
    y "就是我直接变成了夏静。"
    narrator "袁艳伸了伸大拇指，指着躺在床上还在安静睡觉的夏静。"
    narrator "其实仔细看的话不难看到，夏静额头上那碗大的汗珠。"
    w "怎么样了？"
    show y 正常03 at ct with dissolve
    y "怎么说…就是我看到的都是记忆片段。"
    w "额，听不懂但是很厉害的样子。"
    w "所以呢？你得出什么结论没有？"
    show y 正常04 at ct with dissolve
    y "能不能麻烦你再送我回去一趟？"
    w "……"
    w "这才是你的目的吧。"
    show y 正常04 at ct with dissolve
    y "是啊"
    w "喂，我们哪里还有时间给你这样子玩啊。"
    w "再说我已经没剩多少力量了啊。"
    show y 正常05 at ct with dissolve
    y "可是我总觉得故事到那里还没有完结。"
    show y 俏皮 at ct with dissolve
    y "就一次…就一次可以不？"
    narrator "我有些瞠目结舌的看着袁艳，我也是第一次被这样提要求。"
    narrator "搞得好像还能有下一次一样。"
    narrator "我不免在心里狠狠的吐槽了袁艳这个家伙一顿。"
    narrator "这家伙绝对是生下来克我的。"
    show y 正常04 at ct with dissolve
    y "如果这家伙不是，我们接下来点燃正确的几率就大多了好不啦。"
    narrator "但是听她这么一说好像也确实有道理。"
    narrator "话说一开始我就是被这么忽悠的吧。"
    narrator "也没有道理事情做一半就没做完吧。"
    narrator "只是可怜我那用一点就少一点的力量啊，这样就算是点燃对了，我想要恢复也要很长时间了。"
    narrator "唉。"
    narrator "算了算了。"
    w "好吧好吧，你准备一下。"
    narrator "我无奈的叹了一口气。"
    narrator "真的下血本啊。"
    w "我们没剩多少时间了。"
    w "该回来的时候你可得记着要回来啊。"
    show y 正常05 at ct with dissolve
    y "额…"
    w "准备好。"
    show y 正常04 at ct with dissolve
    y "其实…"
    narrator "就在我将她的灵魂送往过去的那一瞬间。"
    show y 正常02 at ct with dissolve
    y "其实…"
    show y 正常01 at ct with dissolve
    y "我好像在夏静的过去看到你了"
    #"(袁艳立绘消失)"
    hide y with dissolve
    narrator "……"
    narrator "短短的几句话却让我足足愣了好几秒。"
    narrator "许久，才终于爆发出来。"
    w "啥？？？"

    #场景：黑屏
    scene black with dissolve

    narrator "‘恭喜夏静小姐荣获**医荣誉奖’"
    narrator "‘恭喜夏静同学荣获奥林***国家级二等奖’"
    narrator "…."
    narrator "耳边回荡着麦克风的声音。"
    narrator "前方是一片漆黑，我看不见终点。"
    narrator "后边也是一片漆黑，甚至忘记了来时的方向。"
    narrator "我漫无目的的在黑暗中摸索着。"
    narrator "真是毫无乐趣可言的人生。"
    narrator "尽管如此…."

    # TODO 81
    #CG:平凡的天才]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_x_genius = True
    scene x_沉迷学习 with dissolve:
        zoom .667
    
    pause 1.0
    
    narrator "我还是竭尽全力的在努力。"
    narrator "看完了一本又一本的书，写着没有尽头的习题，钻研好像是天书一样的论文。"
    narrator "天才‘夏静’的称号无疑是沉重的。"
    narrator "世界上没有不需要付诸代价就能获得的东西。"
    narrator "埋在书海里面，如痴如醉的学习。"
    narrator "如痴如醉…"
    narrator "我想办法榨取书本中的没一点知识，如果不这样做的话，我感觉自己就要窒息一般。"
    narrator "脖子和手腕有点疼，眼睛有点酸。"
    narrator "然而这跟停下学习之后的窒息感比起来完全不值一提。"

    # TODO 82
    #CG:平凡的天才(睁眼)]"
    
    narrator "好累啊…"
    narrator "好累啊…."
    narrator "真的…好累啊。"
    narrator "天才的称呼真的很重要吗？"
    narrator "只是为了那种不值一提的殊荣，我才这样拼命努力吗？"
    narrator "如果是这样，我不要了好不好？"
    narrator "为了这个称号，我奉献了几乎我所有的时间。"
    narrator "有时候连饭都顾不上。"
    narrator "几次住院都是因为疲劳过度。"
    narrator "我肯定是哪里出了问题吧。"

    #场景：黑暗
    scene black with dissolve

    narrator "为什么我会对天才这个称呼这么执着呢？"
    narrator "为什么只有我非努力不可呢？"
    narrator "我想不起来了，我好像忘记了什么重要的事情？"
    narrator "那是让我变成如今这模样的原因，也是我一直努力的理由。"
    narrator "为什么…我会忘记了呢？"
    narrator "身体传来阵痛…到底是怎么回事？"
    x "好…疼…"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    narrator "好疼…"
    
    #场景：开心的日子
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_x_happyday = True
    scene x_阅读开心 with dissolve:
        zoom .667
    pause 1.0
    

    narrator "好疼好疼好疼…."

    #场景：手术后的少女
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_x_gc = True
    scene x_观察 with dissolve:
        zoom .667

    pause 1.0
    
    narrator "好疼好疼好疼好疼好疼好疼"
    narrator "好疼好疼好疼好疼好疼好疼！"

    # TODO 83
    #CG：变故]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_x_bg = True
    scene x_离世 with dissolve:
        zoom .667
    pause 1.0
    
    narrator "好疼好疼好疼！！！！！！！！！！！！"
    
    #场景：黑屏
    scene black with dissolve

    narrator "突然一切就消失了，我伫立在黑暗中。"
    narrator "有谁在黑暗的另一端。"
    narrator "男孩的声音回荡在这个空间里。"
    narrator "像是说给我听的，可是我又是谁？"
    narrator "他又是谁？为什么声音里充满了后悔？"
    narrator "话说我不是信使啊，为啥要我带话？"
    narrator "还有让我带话给谁啊？"
    narrator "想到这里，一切戛然而止。"
    narrator "无形的漩涡将我带走。"

    #场景：病房
    scene bf_室内 with dissolve:
        zoom .667

    narrator "再一次回到这里的袁艳，伫立在我的面前。"
    w "……"
    show y 正常05 at ct with dissolve
    y "……"
    w "所以说到底怎么了？"
    show y 正常04 at ct with dissolve
    y "这个不好跟你解释…"
    narrator "袁艳看了看躺在床上的夏静。"
    narrator "叹了一口气。"
    w "…."
    narrator "所以说到底怎么啦。"
    narrator "夏静到底是不是那个崩坏女孩啊。"
    show y 正常03 at ct with dissolve
    y "我可能见到了很奇怪的东西"
    w "什么东西？"
    show y 正常01 at ct with dissolve
    y "你现在还能把我送回去不？"
    narrator "她指一下自己的身体。"
    narrator "我马上就明白她的意思。"
    w "……"
    w "之前不是试过了吗？基本上不太可能了啊。"
    show y 正常02 at ct with dissolve
    y "好吧。"
    narrator "……."
    w "那你现在能做判断了不？"
    narrator "我看了看袁艳，她应该是明白我的意思。"
    narrator "袁艳则是又看看床上的夏静，依旧在犹豫。"
    narrator "还没有下定决心。"
    show y normal_3_2 at ct with dissolve
    y "我好像做了一个很长的梦。"
    narrator "忽然间，袁艳这么说道。"
    w "哈？"
    narrator "我有点不太理解她现在说这个是有啥意义。"
    w "做个梦跟我们现在的情况有关系嘛？"
    show y 正常01 at ct with dissolve
    y "怎么说呢…我就感觉特别疼，特别难受，还有个谁让我带话。"
    w "谁让你带话？"
    narrator "我歪了歪脑袋，有点不太明白袁艳这家伙说的话。"
    narrator "袁艳再一次看床上的夏静一眼，叹了一口气。"
    show y 正常05 at ct with dissolve
    y "该怎么说呢…这种感觉并不是很好。"
    show y 正常04 at ct with dissolve
    y "有人托我给这丫头带个话。"
    w "说啥了？"
    show y 正常02 at ct with dissolve
    y "虽然不知道有啥用，但是大概就几句道别的话之类的？"
    w "道别？跟谁道别？"
    w "算了算了，别管那么多，你到底弄清楚没？"
    w "这个丫头到底是不是我们要找的那个啊？"
    show y 正常01 at ct with dissolve
    y "……"
    narrator "这个时候反倒是她沉默了一下。"
    show y 正常05 at ct with dissolve
    y "问一下。"
    w "都到这种时候，你还有啥问题啊？"
    show y 正常05 at ct with dissolve
    y "说到底崩坏到底是个什么东西？"
    show y 正常04 at ct with dissolve
    y "我觉得她这丫头挺好的呀。"
    w "那你就把事情想得太简单了。"
    narrator "太草率了！"
    w "所谓的崩坏可比你想的要严重的多。"
    w "这样的人是介于灵魂状态和现实状态为一体的存在。"
    w "换句话来说，就是这样的人在现实世界中不论生死都能影响现实世界。"
    w "严重的会使得灾难具象化。"
    show y 正常04 at ct with dissolve
    y "麻烦你解释得通俗点，能让我听懂的那种。"
    w "……"
    w "简单来说崩坏的人可以引发灾难。"
    w "大到你们常见的洪水，地震，小到你走路被天上掉下来的东西砸死这样的。"
    show y 正常04 at ct with dissolve
    y "…."
    show y 正常05 at ct with dissolve
    y "那不是很刺激？？"
    w "刺激个鬼啦！"
    w "这种无法无天的存在很容易导致城市毁灭的好不啦！"
    show y 无措 at ct with dissolve
    y "我都想变成崩坏的那只了！"
    w "你这么羡慕个啥？"
    show y 俏皮 at ct with dissolve
    y "你想想，完全没人能管我耶？"
    w "是没人能管你了。"
    narrator "我不由得摊了摊爪子。"
    w "包括你自己也管不了你自己。"
    show y 正常04 at ct with dissolve
    y "啊？"
    show y 正常05 at ct with dissolve
    y "不可控的？"
    w "嗯。"
    show y 正常03 at ct with dissolve
    y "那还是不要了。"
    w "明白了？"
    show y 正常02 at ct with dissolve
    y "明白了！"
    w "那这个叫夏静的丫头是不是那个崩坏的女孩啊？"
    show y 正常01 at ct with dissolve
    y "这个啊…."
    narrator "看她犹豫的样子，我多半就能理解了。"
    narrator "她没有办法做出判断。"
    narrator "但是花了这么大的代价，总得问出有用的信息才行啊。"
    show y 正常04 at ct with dissolve
    y "虽然还是没办法判断，不过我有个有用的信息可以拿出来用用。"
    w "嗯？"
    narrator "和我想到一块去了。"
    show y 正常05 at ct with dissolve
    y "这个丫头身体里面应该还有另外一个灵魂。"
    w "……"
    narrator "听到这个消息，我不由得沉默了起来。"
    narrator "另一个灵魂？干扰现世？好像完全符合崩坏的条件啊。"
    show y 正常04 at ct with dissolve
    y "其实我们也不急不是，不是还有一天嘛。"
    narrator "袁艳尴尬的笑着。"

    #场景：黑屏
    scene black with dissolve

    w "……"
    
    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    narrator "我长长叹了一口气。"
    w "哪里还有一天啊。"
    show y 正常01 at ct with dissolve
    y "啊？"
    w "现在的你已经是必须要做出决定的时候了。"
    w "今天黄昏时刻，我们点火若不成功。"
    w "…."
    w "最好的情况就是咱们两个灰飞烟灭，再也回不去。"
    show y 正常02 at ct with dissolve
    y "那.最坏的呢？"
    narrator "女孩瞪大眼睛，就像是我刚刚说的话毫无震撼力度一样。"
    w "……"
    narrator "至始至终，这个丫头都是这样。"
    narrator "把心大的性格发挥到了极致，这已经不是心大了吧。"
    narrator "我都不知道拿什么个性来形容她。"
    narrator "这丫头难不成就是那个要崩溃的女孩吗？"
    narrator "我被我的想法吓了一跳，但是我马上摇了摇猫头。"
    narrator "不可能的，在我边上我都不知道。"
    narrator "那我这神圣的猫不是白当了。"
    narrator "不过她的性格真的是有点厉害了，适应能力也有点强得让我无法理解了。"
    narrator "人类都是这样的吗？"
    narrator "要都是还会有什么崩坏的人嘛？"
    narrator "说到底这个世界上真的有袁艳这种人吗？"
    w "我说…你真的是个人吗？"
    show y 正常04 at ct with dissolve
    y "问的什么话…"
    show y 不爽02 at ct with dissolve
    y "我不是人是什么？鬼吗？"
    narrator "我点了点头。"
    show y 正常05 at ct with dissolve
    y "……"
    w "不扯了不扯了，你现在能做判断不？"
    w "我觉得她很有可能就是有问题的女生。"
    w "毕竟两个灵魂，这也太可疑了。"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳没有说话，我就当她是默认了。"
    w "……"
    narrator "既然如此，也就没有必要继续等待下去了。"
    narrator "看了袁艳一眼，我便闭上了眼睛，准备开始引出最后的力量，吟唱赞歌。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/2333.wav" loop fadein 2.0 fadeout 2.0

    # TODO 84
    #CG:引导者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz1 = True
    scene cg_引导者1 with Dissolve(2):
        zoom .667
    
    pause 1.0

    #show y 无措 at ct with dissolve
    y "哇，你在干嘛呢？"
    w "…."
    #show y 无措 at ct with dissolve
    y "哇？她是谁啊？？？"
    narrator "我闭着眼睛。"
    w "我在有事你没看见吗？"
    w "忙着呢，别打扰我！"
    #show y 无措 at ct with dissolve
    y "……"
    #show y 无措 at ct with dissolve
    y "不是，你谁啊？"

    # TODO 85
    #CG:引导者](睁眼)"
    nvl clear
    nvl hide
    window hide dissolve
    #scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_ydz2 = True
    scene cg_引导者2 with Dissolve(1):
        zoom .667
    
    pause 1.0

    w "…."
    narrator "被她烦的不行了，睁开眼睛瞅了她一眼。"
    w "是我怎么了？"
    #show y 正常04 at ct with dissolve
    y "你还是个美少女啊，没看出来啊。"
    w "……"
    #show y 开心 at ct with dissolve
    y "啧啧啧…还挺漂亮的。"
    #show y 笑容01 at ct with dissolve
    y "你要是早点变成这样，我就不会对你那么凶了。"
    w "……"
    w "快闭嘴啊！我在控制力量，能不能别让我分神。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    narrator "好说歹说，终于算是让这个妮子闭嘴了。"
    narrator "没了她说话分神，我引导力量的速度也快了许多。"
    narrator "不一会儿，就完成了力量的引导，在我的人体印象的胸口，点燃了一簇蓝色的火焰。"
    w "…."
    show y 正常04 at ct with dissolve
    y "……"
    narrator "在火焰下，我和袁艳彼此对视一眼。"
    w "我做了啊…"
    show y 正常05 at ct with dissolve
    y "做啥？"
    w "点燃她啊。"
    narrator "我看着床上的夏静，然后又看了看袁艳。"
    narrator "怎么好像还要征得她同意一样。"
    narrator "顿时有点郁闷了起来。"
    show y 正常04 at ct with dissolve
    y "……"
    narrator "袁艳明显的犹豫了一下。"
    show y 正常04 at ct with dissolve
    y "你点呗。"
    w "那我动手了啊。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "你动手啊！磨磨唧唧的。"
    w "……"
    narrator "我一怔，就准备开始书写大结局的故事了。"
    narrator "只要我把接下来的灵魂之火放到这个女孩的身体里面，一切就完成了。"
    narrator "总觉得事情没那么顺利…"
    narrator "夏静翻了个身。"
    narrator "然后我控制着灵火直接放到了她的身体里面。"
    narrator "看着灵火漂浮在她的胸口。"
    narrator "我有些愣神…会不会有点太简单了？"
    narrator "按道理来说，这个时候不应该出现一点点变故吗？"
    w "……"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "接下来呢？"
    w "等着就行了。"
    narrator "接下来只需要等灵魂之火灼烧殆尽这个灵魂即可。"
    narrator "保佑啊，这个丫头是那个女孩，一定要是啊…."
    
    #场景：黑屏"
    scene black with dissolve
    
    narrator "时间一点一点的过去了。"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    w "……"
    #show y 正常02 at ct with dissolve
    y " ……"
    
    #场景：黑屏
    scene black with dissolve
    narrator "没什么变化。"

    #场景：病房
    scene bf_白天 with dissolve:
        zoom .667

    show y 正常04 at ct with dissolve
    y "怎么没啥动静啊？"
    w "再等等…"
    narrator "头一回要这么久的时间。"
    show y 正常05 at ct with dissolve
    y "我去看看夏静的情况。"
    w "你是灵魂状态，你别靠太近啊。"
    show y 正常04 at ct with dissolve
    y "靠太近怎么了？"
    w "灵魂靠近这个火太近的话，就有可能会把你烧得灰飞烟灭啊。"
    w "别怪我没提醒你，你别到时候还没被诅咒干掉就被灵火烧死了。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常04 at ct with dissolve
    y "为啥？"
    w "这火对普通灵魂有绝对的杀伤力。"
    show y 正常05 at ct with dissolve
    y "那我还是不靠近了。"
    narrator "说罢，她退后了好几步。"
    show y 正常05 at ct with dissolve
    y "那它对人会咋样呢？如果她不是崩坏的灵魂的话…"
    w "…."
    x "…."
    x "emmm…."
    x "唔…唔…"
    narrator "难受的呻吟声在病房里幽幽的响起，我和袁艳对视一眼，马上就安静了下来。"
    narrator "看来，该来的还是来了。"
    narrator "但是，总感觉不太对。"
    narrator "这不像是在清除崩坏的症状啊…"
    narrator "别吧…我不由得捂住了眼睛，不敢看。"
    w "袁…袁艳。"
    show y 正常02 at ct with dissolve
    y "干啥？"
    w "你帮我看看…"
    w "她是不是浑身冒黑烟之类的？有没有？"
    w "……"
    show y 正常01 at ct with dissolve
    y "没有啊，她就一直在叫而已啊，像做噩梦一样。"
    narrator "听到袁艳的话，我的顿时就愣住了。"
    w "完了…."
    show y 正常01 at ct with dissolve
    y "怎么了？"
    narrator "这不是清除掉崩坏时应该有的现象…"
    narrator "换而言之，也就是夏静这个女孩并不是那个崩坏的女孩."
    narrator "判断错了。"
    w "我们….错了啊…"
    narrator "知道真相的我差点都要哭出来了。"
    narrator "这么多天的努力，结果居然弄错了。"
    narrator "真的是命啊…"
    w "呜喵…唔喵…."
    narrator "还是没忍住，哭出来了。"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "干啥呢干啥呢，奔丧呢你？"
    w "我们…我们，我们…完了啊！"
    show y 正常05 at ct with dissolve
    y "完什么完，你还没回答我呢。"
    w "啊？"
    narrator "回答什么，都这时候还回答什么啊？"
    show y 正常05 at ct with dissolve
    y "灵魂之火对普通人有啥伤害吗？"
    narrator "袁艳指了指躺在床上翻来覆去非常痛苦的夏静。"
    w "灵魂之火对人体能有什么伤害啊？"
    w "大姐…你省省心吧…我们选错了，要死了啊，你还有心情担心她？"
    narrator "我心情哽咽，知道自己马上要死的感觉真的一点都不好。"
    show y 正常04 at ct with dissolve
    y "那为啥这丫头这么难受啊？"
    w "……."
    narrator "我还在难受着呢，突然面前一阵风吹了过来。"
    narrator "她就像是一阵风一样冲到了我的面前。"
    show y 正常04 at ct with dissolve
    y "到底是怎么回事啦？"
    w "…."
    w "虽然她有躯体可以保护自己的灵魂，但是灵魂之火仍然是能够灼烧其灵魂的。"
    show y 正常05 at ct with dissolve
    y "嗯？"
    w "她肯定是要失去一些东西的，强行失去怎么可能不难受啊。"
    w "如果没有错的话，灼烧的肯定是她觉得比较重要的事情。"
    show y 正常05 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "能不能说点我能懂的？"
    show y 正常04 at ct with dissolve
    y "比如她失去了啥，或者怎么灭了这火？"
    w "你疯啦？"
    show y 恼火04 at ct with dissolve
    y "讲重点。"
    narrator "袁艳很无语的看着我，难不成她真打算灭掉这火？"
    w "……"
    narrator "一旦点燃这个火，想要在灭掉是不可能的…几乎不可能的。"
    narrator "除非……"
    w "这玩意肯定要烧掉啥东西才能灭掉。"
    w "啊….反正咱们也死定了.你能不能表现得在悲伤一点啊？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常05 at ct with dissolve
    y "死猫，既然不是她，她这么难受不是显得我们俩有点缺德嘛？"
    w "都快死的人了…呜呜呜…."
    narrator "我几乎要放生大哭了起来。"
    show y 正常05 at ct with dissolve
    y "…."
    narrator "袁艳则是非常无语的看着我。"
    show y 恼火04 at ct with dissolve
    y "别奔丧了。"
    w "……"
    w "我们快完了好不好！！"
    show y 正常05 at ct with dissolve
    y "不是你真有那么悲伤？"
    w "…."
    w "那不是废话嘛？"
    narrator "看着有些玩味的袁艳，我有点儿搞不懂她是啥意思了。"
    w "倒是你，快完蛋的人了，你怎么跟过节一样开心啊喂！"
    show y 开心 at ct with dissolve
    y "我有说啥吗？"
    show y 笑容01 at ct with dissolve
    y "反正我们已经没救了不是吗？"
    narrator "袁艳突然在这个时候笑了起来。"
    narrator "完了，这丫头也没救了。"
    narrator "不，应该说这一开始咱们就没救了。"
    narrator "把希望放在她身上的我真的是个大笨蛋啊。"
    narrator "她压根对这种事情就无所谓的。"
    narrator "有点点懊恼。"
    narrator "但是现在已经来不及了啊。"
    narrator "我们真的已经完了。"
    w "你…干啥呢？"
    narrator "我看着袁艳一点一点的靠近少女。"
    narrator "我不是说她这个灵魂状态的不要靠近火吗？"
    narrator "她想干啥？"
    #show x 难受的声音 at ct with dissolve
    show y 笑容01 at ct with vpunch
    x "啊…"
    show y 正常05 at ct with dissolve
    y "她这叫声我听不下去了。"
    show y 正常05 at ct with dissolve
    y "让人担心的丫头。"
    narrator "在我的注视之下，袁艳伸出了手。"
    narrator "将放置在女孩胸口的灵魂之火取了出来。"
    w "喂，你别乱搞啊！！会死的！"
    narrator "我突然紧张了起来。"

    #场景：淡入 黑屏
    # TODO 86
    #CG:救赎者]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz = True
    scene cg_救赎者 with Dissolve(2):
        zoom .667
    
    pause 1.0

    w "…."
    w "我.的…妈呀…"
    narrator "女孩手捧着灵魂之火，伫立在房间里头。"
    narrator "静谧的房间，传来了滋滋的声音，看不见的火焰在不断的溶解着少女的身体。"
    narrator "就好似飘散的花瓣，散落漂浮在这个空间里面。"
    narrator "你到底要做什么啊？"
    narrator "之前一点点火就已经把你疼了个半死。"
    narrator "现在直接把火捧在手上，你不要命啦？"
    
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    y "死猫…这个火会烧掉琴丫头全部的记忆。"
    narrator "她好像忽然明白了什么一样。"
    w "…."
    narrator "我其实是知道的，灵魂之火会褪去一个人心中全部的执念。"
    narrator "会把一个人变成符合世界所需要的‘正常人’，渐渐的融入世界中，与他人无异。"
    narrator "这就是我们的使命。"
    narrator "很显然，这些记忆就是夏静全部的执念。"
    narrator "如果烧掉，那么这个不合群的少女，就应该很容易融入人类所谓的社会当中去。"
    narrator "这应该是一件好事才对。"
    narrator "我不明白，为什么这丫头会这么痛苦呢？"

    # TODO 87
    #CG:救赎者的笑容]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jsz_smile = True
    scene cg_救赎者的笑容 with Dissolve(2):
        zoom .667
    
    pause 1.0

    y "我刚刚看到了…"
    narrator "袁艳，几乎是是从牙缝里面挤出来的几句话。"
    y "这丫头…在哭。"
    y "那些被记住的事情，对她应该特别重要。"
    y "死猫…再帮我一件事…"
    y "我…要回到那具身体里面去。"
    w "……"
    narrator "这是不可能做到的吧。"
    narrator "话说…"
    w "你赶快…放手啊！你会被烧死的啊！"
    w "灵魂一旦被烧， 这个世界上就真的没有你了啊！！"
    y "…."
    y "痛痛痛痛死了！"
    y "诶嘿嘿…你以为是我死了吗？"
    y "其实我没有死哒！"

    # TODO 88
    #CG:抛出去]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_pcq = True
    scene cg_抛出去 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "就像是扔掉了一个烫手山芋一样。"
    narrator "袁艳伸出了手，将灵魂之火抛到了空中。"
    narrator "它就飘在半空中，似乎是被谁带走的一样。"
    w "……"
    narrator "我惊讶的说不出话来。"
    w "你….你是怎么做到的？"
    w "灵魂之火不烧掉一个灵魂是不会熄灭的。"
    y "嘿嘿…."
    narrator "你笑个鬼啦，虽然很想吐槽她，但是我还是说不出口。"
    narrator "我知道，肯定是发生了什么。"

    # TODO 25
    ##CG结束]"
    nvl clear
    nvl hide
    window hide dissolve
    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    show y 开心 at ct with dissolve
    y "刚刚我听到了声音。"
    show y 俏皮 at ct with dissolve
    y "夏静那丫头身体里面传出来的。"
    w "声音？"
    show y 笑容01 at ct with dissolve
    y "就是之前说的那个另外一个灵魂。"
    show y 笑容02 at ct with dissolve
    y "她一直守护着夏静。"
    show y 开心 at ct with dissolve
    y "…."
    narrator "她看着半空。"
    show y 正常04 at ct with dissolve
    y "然后，她代替了我。"
    w "……"
    narrator "我也看着半空。"
    narrator "虽然说挺了不起啦，但是也没有用。"
    narrator "我已经能够感觉到诅咒就快要来临了。"
    narrator "我们已经完蛋了。"
    show y 正常05 at ct with dissolve
    y "在此之前，我还有一件事要做来着。"
    w "……"
    w "干嘛？你那么盯着我干嘛？"
    show y 正常02 at ct with dissolve
    y "诶嘿，麻烦你把我送回去。"
    narrator "袁艳指着自己躺在病床上的身体。"
    w "……."
    narrator "这怎么可能做得到啊，之前不是试过很多次了吗？"
    show y 正常03 at ct with dissolve
    y "拜托啦，就一次就一次！"
    w "……"
    narrator "这丫头笑嘻嘻的，搞得好像能成功一样。"
    narrator "这个时候我不应该有点紧张感，应该很难受才是吗？"
    narrator "自从和她在一起之后，我就发现好像什么都不一样了。"
    narrator "不过，诅咒已经压过来了，横竖都逃不过了。"
    narrator "看着笑嘻嘻的袁艳，我就一阵火大，我之后的计划都给搞乱了。"
    narrator "这个人到底是怎么回事啊？"
    narrator "从认识她之后我的节奏一直就被她带着跑，这家伙难道是我命里的克星吗？"

    # TODO 90
    #CG:雨中的猫](忘记原CG叫啥了，回头改一下。)"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_c_yz = True
    scene c_雨中 with Dissolve(2)
    
    pause 1.0

    narrator "突然想起来，好像我的命也是被她救的。"
    narrator "不然的话我早就应该死了才对。"
    narrator "这么想想，感觉好像是我把她给拖下水了。"
    narrator "说到底，责任还是有我一份的呀。"
    narrator "哎…想太多脑袋都炸了"
    narrator "既然这个丫头已经疯了，那我陪她疯一下就好咯。"
    narrator "反正我的命也是她救的。"
    narrator "还给她就是了。"
    narrator "反正她也跑不掉。"

    nvl clear
    nvl hide
    window hide dissolve

    #场景：病房
    scene bf_白天 with Dissolve(1.0):
        zoom .667

    w "哈哈哈哈…"
    narrator "我忍不住笑了起来。"
    show y 正常04 at ct with dissolve
    y "你笑啥？"
    w "算啦算啦，我试试好了。"
    show y 正常05 at ct with dissolve
    y "……"
    narrator "我闭上了双眼，再一次引动力量。"
    narrator "但是实际上我这个时候已经完全没有啥力量了。"
    narrator "反正诅咒已经快到了，早到跟晚到也没啥区别…"
    narrator "就让我借一下所谓诅咒的力量吧。"
    w "……"
    show y 正常04 at ct with dissolve
    y "你在做啥啊？"
    w "……"
    narrator "灵魂开始颤抖…"
    narrator "好疼…"
    narrator "有种撕心裂肺的感觉…."
    narrator "但是说句实话，跟袁艳这丫头相处了一段时间之后，会发现自己的心也变大了。"
    w "…."
    narrator "别吵了，这丫头让我完全专心不起来。"
    show y 正常02 at ct with dissolve
    y "哇，你的脚消失啦！！"
    w "…."
    narrator "吵死啦，一会失败了怎么办！"
    show y 正常01 at ct with dissolve
    y "你肚子不见啦！！！喂！你听到我说话没有？"
    show y 恼火01 at ct with dissolve
    y "喂！你听我说话啊喂！"
    w "……"
    narrator "我在也忍不住了。"
    w "都说让你别吵啦！没看到我在专心做事吗？"
    narrator "……"

    # TODO 91
    #CG：破碎者]"
    
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_psz = True
    scene cg_破碎者 with Dissolve(2):
        zoom .667
    
    pause 1.0
    narrator "然我的面前原本应该站在那里的身影，已经消失了。"
    w "……"
    w "咳咳咳…"
    narrator "突然而然的静谧让我原本想要说出的话哽咽在喉咙里。"
    narrator "撕裂的疼痛感然我已经快要睁不开眼睛了。"
    narrator "引用诅咒的力量，我的胆子是真的大。"
    narrator "无数黑色碎片宛如漩涡一般向我席卷而来。"
    narrator "我的身体正在渐渐的被卷走。"
    narrator "我看着病房里渐渐苏醒的袁艳。"
    narrator "鼻子忽然一酸。"
    narrator "我成功了。"
    narrator "我成功把这丫头送回去了。"
    narrator "以我自己提前被诅咒为代价。"
    narrator "我自己也没想到，这里就是旅程的终点…"
    narrator "啊，还有好多事情没有做…"
    narrator "啊，还没来得及多了解一下这个世界。"
    narrator "啊，还没来得及跟那个丫头道歉，把她卷入这件事情里面。"
    w "袁艳！！！你王八蛋！你还欠我猫薄荷没还啊！！！！！"
    narrator "伴随着眼里和吼声，似乎舒服了好多。"
    narrator "我看着袁艳渐渐的从床上爬起。"
    narrator "诅咒提前降临了…"
    narrator "快啊，死丫头…我快撑不住了。"
    narrator "我没了，下一个….就是你了。"

    # TODO 28
    #CG：破碎者结束]"
    nvl clear
    nvl hide
    window hide dissolve

    #场景：黑屏
    scene black with dissolve
    #场景：病房]"
    scene bf_白天 with dissolve:
        zoom .667
    # TODO
    #变色UI

    narrator "睁开了双眼。"
    narrator "再一次看到了天花板。"
    narrator "我从床上坐了起来。"
    narrator "看看自己的双手，抵在床上。"
    narrator "我回来了。"
    narrator "我看了看死猫曾在待过的位置。"
    narrator "那里什么也没有。"
    narrator "这只死猫做了啥我不知道，"
    narrator "但是我知道，现在那里肯定在发生着什么。"
    narrator "这个时候的夏静已经平静了下来。"
    narrator "我下床，打着赤脚走向了她的床位。"
    show y 正常02 at lt with dissolve
    y "醒一下醒一下…"
    show x 怜悯03 at rt with dissolve
    x "…."
    show x 怜悯02 at rt with dissolve
    x "嗯…嗯…"
    narrator "带着泪光，少女逐渐苏醒了过来。"
    narrator "冷静，非常冷静的眼神。"
    show x 闭眼 at rt with dissolve
    x "我记起来了…."
    show y 正常04 at lt with dissolve
    y "记起来什么了？"
    show x 反驳02 at rt with dissolve
    x "我忘掉的东西，我想起来了。"
    narrator "记起来不是一件开心的事情么？"
    narrator "那你哭啥啊？"
    narrator "我不由得笑了起来。"
    show x 反驳01 at rt with dissolve
    x "那他现在在哪？"
    show y 笑容01 at lt with dissolve
    y "……"
    narrator "我看了看原本灵魂之火所在的位置，淡淡的笑了笑。"
    narrator "夏静的表情有些紧张，她期待着看着我。"
    narrator "但是我很抱歉，我没有办法回应她的期待。"
    show y 笑容02 at lt with dissolve
    y "他…让我给你带一句话。"
    narrator "话刚刚说出口，我的心脏忽然收缩。"
    narrator "或许是哪一个神明意识到了我接下来要说出口的事情。"
    narrator "话到了嘴边却开始受到了无数阻力。"
    narrator "有什么东西在阻止我把话说出口。"
    narrator "少女睁大了眼睛，死死的盯着我，想要听到我嘴里的话。"
    show y 俏皮 at lt with dissolve
    y "…."
    narrator "那家伙已经死掉啦，我没办法把他的人带回来给你。"
    narrator "但是…多少帮他传达一句话给你，还是没有问题的。"
    show y 嘲笑 at lt with dissolve
    y "我是说啦…"
    show y 嘲讽02 at lt with dissolve
    y "咳咳咳…."
    narrator "我感到了一阵阵的拉扯力，这份疼痛感就像是藤蔓一般，缠绕上我的胸口。"
    narrator "并随着我的血管一路攀岩，拉扯着我的喉咙。"
    narrator "简单的话语，到了嘴边…愣是发不出声音。"
    narrator "一个想法闪过了我的脑海，如果我把下面的话说出来。"
    narrator "我将会受到无比苛刻的惩罚。"
    narrator "说的也是，想要传达来自另外一个世界的思念，根本就是一件不可能的事情。"
    narrator "早知道…就不救那只死猫了。"
    narrator "谁知道这只死猫身上会带着那个世界的思念啊…"
    narrator "我真是个笨蛋啊…"
    show y 嘲讽02 at lt with dissolve
    y "他说你好厉害！"
    show y 嘲讽01 at lt with dissolve
    y "他觉得你特别特别的厉害。"
    show y 开心 at lt with dissolve
    y "然后他说和你在一起玩很开心。"
    show x 注视02 at rt with dissolve
    x "…."
    show y 开心 at lt with dissolve
    y "这真的是一个苦差事，你有啥话让我带给他的吗？"
    narrator "就好像什么枷锁被瞬间打碎了一样。"
    narrator "我说的话变得容易了许多。"
    narrator "然而，少女的眼泪忽然滑落脸颊。"
    #show x 呜咽声 at rt with dissolve
    x "(呜咽声)"
    
    # TODO 93
    #CG:哭泣]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xjcry = True
    scene cg_夏泣 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "伴随着我的话语，似乎有什么传达到了少女的身边。"
    narrator "或许是这份持续了不知道多少年的思念。"
    narrator "或许是让少女孤独的走在这个世界上的歉意。"
    narrator "少女的哭声就像是让我重新回到了那个灾祸的现场。"
    narrator "这些年，你辛苦了。"
    narrator "少女再也忍不住，大声哭了起来，就像是一个孩子。"
    narrator "……"
    
    #场景：黑暗
    scene black with dissolve

    narrator "而我，却坠入了黑暗之中。"

    #"(淡出)"
    # TODO 94
    #CG:堕落者]"
    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xc = True
    scene cg_下沉 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0

    narrator "我仿佛不断的在下坠。"
    narrator "周围安静得可怕。"
    #show ？？ 猫 at ct with dissolve
    "？？" "死丫头，你来啦？"
    y "…."
    y "呵呵，我来了。"
    "猫" "真的搞不懂耶，你是个猪吗？"
    "猫" "居然真的把那个世界的话带到现实世界里面去了。"
    "猫" "真不知道该佩服你还是说你好了。"
    y "呵呵…"
    narrator "短暂的沉寂之后，熟悉的声音再一次响起。"

    # TODO 95
    #CG:光晕]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_mf = True
    scene cg_魔法 with Dissolve(2):
        zoom 0.67  xpos 0 ypos 0
        linear .7 xpos -6 ypos -0
        linear .7 xpos -0 ypos -0
        linear .7 xpos -6 ypos -6
        linear .7 xpos -0 ypos -4
        linear .7 xpos -0 ypos -0
        repeat
    
    pause 1.0

    "猫" "你后悔不？"
    narrator "…."
    y "该说后悔还是不后悔呢？"
    y "……"
    y "希望她们都能过得好一点吧。"
    y "毕竟…她们可是我唯一的朋友啊。"
    narrator "黑暗的那一端，陷入了沉默。"
    y "…."
    y "还有你…死猫。"

    # TODO 96
    ##CG:结束]
    nvl clear
    nvl hide
    window hide Dissolve(.7)
    scene black with Dissolve(.7)
    narrator "(个人线 完结)"

    jump c3_4
    
label c3_4:
    
    $c3_4 = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    #主线
    
    #场景：黑屏
    scene black with dissolve

    narrator "似乎摆脱了那几个女孩。"
    narrator "我不由得扶了扶脑袋。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/ai.wav" loop fadein 2.0 fadeout 2.0

    #场景：房门口
    scene door_白天 with dissolve:
         zoom .667
    narrator "真的是，自从到这个城市来之后总是会遇到一些莫名其妙的事情。"
    narrator "还是回家好好休息吧。"
    narrator "我叹了一口气。"
    narrator "打开房门。"
    
    #场景：客厅
    scene kt_白天 with dissolve:
        zoom .667

    #"(音效：开门声)"
    narrator "坐在沙发上，我总算是松了一口气。"
    narrator "也就只有这里是我的安全屋了。"
    narrator "但是总觉得忘记了什么事情。"
    
    #"(浴室水声)"
    w "……."
    narrator "什么情况，我不由得朝着浴室那边看过去。"
    narrator "那边好像传来了奇怪的声音。"
    narrator "难道是有人在用浴室吗？"
    narrator "但是我是独居啊。"
    narrator "除了房东应该没有别人会有钥匙了吧。"
    narrator "难道房东跑到我的房间里面来洗澡？"
    narrator "我摇了摇头…"
    narrator "难不成进了贼？"
    narrator "我摇了摇头…"
    narrator "贼偷东西的时候还会顺便洗个澡吗，那这贼的心理素质是要有多强啊。"
    narrator "更何况我家里就放了点吃的，也没啥值钱的东西啊。"
    narrator "难不成….是那家伙来了？？"
    narrator "我不由得扶了扶脑袋。"
    narrator "为了印证我的想法，我决定冒个险。"
    narrator "小心翼翼的我朝着浴室走过去。"
    narrator "不过可惜的是，浴室的门是反锁的，我打不开，只能依稀的看到一个身影在里面洗澡。"
    narrator "真的是在洗澡啊喂！"
    #"(音效：咚咚咚 敲门声)"
    w "！！！"
    narrator "突如其来的敲门声把我吓了一跳。"
    narrator "浴室里面传来响声。"
    
    #show ？？？ c 配音 at ct with dissolve
    "？？？" "谁啊！！！"
    w "……"
    narrator "果然是她！！！！"
    
    #show ？？ l 配音 at ct with dissolve
    "？？" "喂，死丫头开门啊，薯片我给你买来了。"
    
    #show ？？？ c 配音 at ct with dissolve
    "？？？" "来啦！"
    w "……"
    narrator "我的天，怎么另外一个也来了？"
    narrator "顿时我头大了两圈。"
    narrator "我怎么把她们给忘了啊。"
    narrator "不行，我得躲起来。"
    narrator "想到这里，我连忙赶到了房间。"
    
    #场景：房间

    w "…."
    narrator "然而在关上门的一瞬间，"
    narrator "我遇见了她。"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/2333.wav" loop fadein 2.0 fadeout 2.0

    # TODO 97
    #CG:窗边的夏静]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xn1 = True
    scene cg_夏女1 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "少女站在窗户边上，看着窗户外边的景色。"
    narrator "但是就我看来窗外没啥好看的，她的背影很好看。"
    narrator "就以我职业的水准来看，这个女孩必然是个美少女。"

    # TODO 98
    #CG:夏静回头]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xn2 = True
    scene cg_夏女2 with Dissolve(2):
        zoom .667
    
    pause 1.0

    narrator "然后她回过头来，显然是意识到了我的存在。"
    narrator "她朝着我流出了笑容。"

    # TODO 99
    #CG 结束]"

    #场景：房间
    w "……"
    #show ？？ x 配音 at ct with dissolve
    "？？" " 哟，回来啦？"
    narrator "想不到…她们竟然会追到这里。"
    narrator "失策，真的是太失策了。"
    #show ？？ x at ct with dissolve
    "？？" "[persistent.playername]老师欢迎回家。"
    w "……"
    #show 我 无配音 at ct with dissolve
    w "你们…赢了。"
    #show ？？ x at ct with dissolve
    "？？" "哈哈哈哈~！"
    narrator "面前笑呵呵的女孩叫做夏静，是我的责任编辑同时是Yuki编辑社内的主编。"
    narrator "洗澡的那个叫做程祎琳，是我的责编。"
    narrator "门外的那个叫做林琴，也是我的责编之一。"

    #场景：黑屏
    scene black with Dissolve(.7)
    #场景：客厅
    # TODO 100
    
    #CG:全员CG]"
    #show 随便画个白衬衫 裹着浴巾的程祎琳吃着薯片在沙发上看着手上的白稿子，林琴穿着单袖[随便画个白衬衫]坐在程祎琳旁边伸手拿程祎琳的零食吃同时也看着稿子，夏静则是戴着眼镜非常认真的憋着笑看手中的稿子
    #"随便画个白衬衫"

    $renpy.music.set_volume(0.1, delay=0.2, channel="music")
    play music "music/日常1.wav" loop fadein 2.0 fadeout 2.0

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jh1 = True
    scene cg_聚会1 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    x "噗…."
    x "不行我忍不住了！哈哈哈哈！"
    narrator "有什么好笑的嘛。"
    w "……"
    x "天才夏静，哈哈哈！！！"
    c "喂喂，我喜欢吃薯片的好不好，你别搞得好像我不喜欢吃薯片啊！"
    l "怎么说呢，我这个精分的性格怪怪的，话说起来这是得了什么病啊？"
    narrator "三个人对着我拿给她们的原稿指指点点。"
    narrator "叽叽喳喳的。"
    narrator "更可恶的是程祎琳洗完澡连衣服都懒得换，直接穿着浴巾在我房间里面。"
    narrator "能不能尊重我点，我好歹也是个男生啊。"
    x "想不到你还能想出这样的故事来啊！"
    narrator "在审阅了原稿的最后一部分之后，夏静用非常怜悯的眼神看着我。"
    w "我怎么了啊？"
    x "[persistent.playername]老师还真是有点意思啊。"
    c "对吧对吧，我就说[persistent.playername]老师是个不错的东西吧。"
    w "我才不是东西啊！！！"
    l "不过话说起来，从lighter发布以来咱们都没有跟人说女主的设定呀。"
    l "你看故事里面林琴是大小姐。"
    c "程祎琳就是个神经病！！哈哈哈…"
    narrator "程祎琳对自己的角色表示非常的喜欢。"
    x "……."
    l "而且你也太舔夏静了吧，凭啥她就是天才啊。"
    x "但是你有钱啊！"
    w "……"
    narrator "不就一个设定嘛，这么纠结干啥。"
    w "反正你们现实里面也没有。"

    nvl clear
    nvl hide
    window hide dissolve
    #场景：客厅
    scene kt_白天 with dissolve:
        zoom .667

    x "……"
    l "……"
    x "同意~"
    l "同意！"
    c "哈哈哈！"
    c "但是女主袁艳一点设定都没有，还有那只猫，话说这只猫不会是我们家的那只为原型吧。"
    x "没有设定才对啊，不然这个女孩怎么死啊。"
    w "……"
    narrator "这个问题早在Lighter企划之前就已经想过了。"

    # TODO 101
    #CG:全员CG]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_jh2 = True
    scene cg_聚会2 with Dissolve(2):
        zoom .667
    
    pause 1.0

    x "喂喂，[persistent.playername]老师，我文件包落在房间了。"
    x "你帮我去拿一下。"
    w "…."
    w "你自己去不行嘛？"
    x "你去嘛！"
    w "行吧。"
    narrator "她们三个叽叽喳喳的在客厅闹着剧本。"
    narrator "什么袁艳和猫的关系啊。"
    narrator "什么游戏剧情太平淡啊。"
    narrator "什么三个女孩子怎么样啊。"
    narrator "最后那个崩坏的女孩啊这类的。"
    narrator "我不由得叹了一口气，有点点微微苦涩，回到了自己的房间。"

    nvl clear
    nvl hide
    window hide dissolve
    #场景：房间
    scene room_白天 with dissolve:
        zoom .667

    narrator "我看着房间墙面上的海报，想起街道上四处可见的lihgter海报图。"
    narrator "转眼之间，lighter问世已经很长时间了啊。"
    narrator "这一路走来是心酸的，不易的。"
    narrator "但是其中也有不少的欢声笑语。"
    narrator "当初随口说的YY三个编辑现在居然成为了一个故事。"
    narrator "我当初是怎么想的？"
    narrator "也许是我本来就想写这个故事吧，用她们的名字不过是一个象征。"
    w "唉…."
    narrator "Lihgter是个很好的故事，但是我依然觉得她很陌生。"
    narrator "陌生的原因就像是突然出现在我脑海的记忆一样。"
    narrator "突兀、疑惑、但又坦然。"
    narrator "于是我写下了lighter故事。"
    w "好累啊。"
    narrator "那个叫做袁艳的奇异少女真的存在于这个世界上吗？"
    narrator "我不知道，但是我抛开三个编辑。"
    narrator "去了许多的城市，就是为了寻找和这段记忆有关的城市。"
    narrator "随着满大街的宣传海报，我知道许多人已经知道了这个故事。"
    narrator "然而我却仍然没有获得关于这个女孩的任何消息。"
    narrator "她就像故事里的少女一般被诅咒吞噬，从此在世界上消失。"
    narrator "这个世界在没有人记得她。"
    narrator "我甚至还想过我只不过是替代她在这个世界上运作的齿轮。"
    narrator "疑惑、焦虑，被负面情绪包围的我。"
    narrator "真的还能就这样继续寻找下去吗？"
    narrator "拿起夏静的包，我朝着门看了过去，是时候做出决断了——"
    menu:
        "我一定会找到她的":
            jump c3_end1
        "推开门，梦已经破碎":
            jump c3_end2
    
label c3_end1:

    $c3_end1_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    #"选择一、我一定会找到她的"

    #场景：房间
    scene room_白天 with dissolve:
        zoom .667

    narrator "有人说过，梦想都是虚幻的，但是人还是会努力的追求。"
    
    # TODO 102
    #CG:袁艳和猫笑着看着我]"
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_girlcat = True
    scene cg_少女与猫 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    narrator "我坚信记忆中那个叫做袁艳的少女一定会在世界的某处存在着。"
    narrator "我有许多事情想要询问她；"
    narrator "我还有许多事情想要告诉她；"
    narrator "也许没有人记得她，但是我记得，我清楚的认识到她不是我幻想出来的人物。"
    narrator "我坚信着她存在，所以我会竭尽全力的寻找到她。"
    narrator "有人会说我分不清现实与幻想太傻。"
    narrator "但是那又怎么样，追逐梦想的道路总是穷途末路。"
    narrator "请你看我越是穷途末路，越是势如破竹。"
    narrator "我坚信着她存在，所以我会竭尽全力的寻找到她。"
    narrator "纵使如此，我依然想要找到你"
    narrator "(故事·完)"

    return
    
label c3_end2:

    $c3_end2_select = True

    $_dismiss_pause = False

    nvl clear
    nvl hide
    window hide dissolve

    #"选项二、推开门，梦已经破碎"
    
    #场景：房间
    scene room_白天 with dissolve:
        zoom .667

    narrator "有人说，要清楚的看清现实。"
    narrator "我推开了房间的门。"
    
    #CG:全员笑容的CG
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_end2 = True
    scene cg_end2 with Dissolve(2):
        zoom .667
    
    pause 1.0
    
    narrator "Lighter写的再怎么用心，那最终不过也就是故事。"
    narrator "我在这个世界上活着，总有一天就应该分清楚梦想与现实的关系。"
    narrator "记忆中那个奇异的女孩曾是我的梦想。"
    narrator "我为她曾去过不同的城市寻找，竭尽全力的努力过。"
    narrator "但是纵然满大街都已经是她的故事，我却依然得不到关于她的任何消息。"
    narrator "这就是一场梦，所以我该醒了。"
    x "来来！你看看你写得什么东西啊！今晚准备通宵吧，公司决定下下周就要把最后章节发出去了！"
    c "对对对！今晚你别想睡觉了！我要让你的身体感受到神仙般的愉悦！"
    l "你们说话怎么怪怪的，让人改稿就改稿吧。"
    narrator "他们会的声音就像是那清晨的闹钟一般。"
    narrator "喧闹，刺耳却无比的真实。"
    narrator "那么我就应该醒过来了，从此以后不再寻找故事中的女孩。"
    narrator "推开门的那一刻，我就明白天亮了，梦就应该碎了。"
    narrator "梦想终将败于现实"
    narrator "(故事·完)"

    return