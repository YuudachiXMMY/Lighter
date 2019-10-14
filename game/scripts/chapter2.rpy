default c2_select = False
default c2_c1_l_select = False
default c2_c1_c_select = False
default c2_c1_x_select = False
default c2_2_select = False
default c2_c2_l_select = False
default c2_c2_c_select = False
default c2_c2_x_select = False
default c2_c2_select = False
default c2_c3_l_select = False
default c2_c3_c_select = False
default c2_c3_x_select = False
default c2_c3_select = False
default l_in_1_select = False
default x_in_1_select = False
default c_in_1_select = False


label c2:

    $_dismiss_pause = False
    
    $c2_select = True

    narrator "【距离诅咒发作还剩四天】"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：街道】
    scene street_夜晚 with dissolve:
        zoom .667

    ####################################################
    
    #（待补充区域）

    ####################################################

    narrator "原本我以为，这应该只是为数不多、应该隶属平静的夜晚。"
    narrator "但是，现实总是不尽猫意。"
    narrator "就比如早晨天还没亮。"
    narrator "‘啪啪’两声响起，把我从梦里拉回了现实。"
    w "你…干什么啊！"
    narrator "我只感觉到我的下颚麻麻的没有感觉，好像被扇了两巴掌。"

    #【CG：黑眼袋的贤者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_blackxz = True
    scene cg_黑眼袋的贤者 with Dissolve(2)
    
    pause 1.0
    
    #none lh
    y "……"
    narrator "睁开眼睛的时候，我只看见袁艳在我的上方。"
    narrator "她脸上的表情看上去非常的怠惰。"
    narrator "眼睛周围黑黑的，就像是没有睡觉一样。"
    #none lh
    y "醒了没。"
    w "醒了。"
    narrator "我喃喃地回答道。"
    #none lh
    y "醒了就赶紧起来，让我去观察她们。"
    w "……"
    w "这时候？"
    w "你没病吧？"
    w "这时候你们人类都在睡觉吧。"
    #none lh
    y "……."

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    #【CG：结束】
    scene street_夜晚 with dissolve:
        zoom .667

    show y 恼火05 at ct with dissolve
    y "我有预感她们肯定已经醒了，毕竟你看已经早上四点了。"
    w "……."
    w "我也有个预感。"
    w "而且我现在就想问你。"
    show y 正常02 at ct with dissolve
    y "问我什么？"
    w "你昨天晚上不会没有睡觉吧。"
    show y 正常01 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "本来是想睡的，但是不知道怎么回事就睡不着了。"
    show y 正常02 at ct with dissolve
    y "纠结着的时候就已经这个时候了。"
    w "总的来说，就是说你昨晚没睡吧。"
    narrator "我打了一个哈欠，很有条理地把没有营养的结论说了出来。"
    narrator "袁艳点了点头，顶着一个巨大的黑眼圈。"
    show y 恼火05 at ct with dissolve
    y "你废话怎么那么多，快点开始观察吧。"
    w "……"
    w "一大清早的，你对我就不能温柔点吗。"
    w "所以…你打算先从那个丫头观察起呢。"

    menu:
        "林琴":
            jump c2_c1_l
        
        "夏静":
            jump c2_c1_x
        
        "程祎琳":
            jump c2_c1_c


#林琴（CV：配音视角部分）
#（视角切换——林琴）
label c2_c1_l:

    $_dismiss_pause = False
    
    $c2_c1_l_select = True
    
    nvl clear
    nvl hide
    window hide dissolve

    #【场景：医院病房】
    scene bf_夜晚 with dissolve:
        zoom .667
        
    narrator "昨晚打完电话就睡着了，回过神的时候天还没亮。"
    narrator "看下时间已经是另一天的凌晨四点了。"
    narrator "本来想在睡一下，不知道怎么回事就是睡不着。"
    narrator "最主要的还是很在意那个叫袁艳的女孩说的话。"
    narrator "我们的相遇是一个偶遇。"
    narrator "我并不认为我自己的伪装很容易被人识破。"
    narrator "但是这个女孩却准确无误地叫出了我的名字。"
    narrator "并且邀请我到她家里做客。"
    narrator "这真的是件有趣的事情。"
    narrator "有趣得我甚至以为是一个陷阱。"
    narrator "不过事到如今敢在这个城市里头对我动手脚的人——应该已经不存在了吧。"
    narrator "并不是抱着一探究竟的心情去她的家里。"
    narrator "而是去观察这个女孩。"
    w "这家伙说的话，如果是真的就好了。"
    narrator "起初我对她想法是无关信任的，直至今日也不一定有多少信任在里头。"
    narrator "但是我还是会依照她的言语来行动。"
    narrator "只因为她说到了一个重点。"
    narrator "她说的我在找人——"
    narrator "——这个是没有错的。"
    narrator "我确实是在找人。"
    narrator "而且在找一个很重要的人。"
    narrator "但是这个人究竟存在还是不存在我都已经不清楚了。"
    narrator "只不过，我现在能活着出现在这个城市。"
    narrator "全部是因为这个人的原因。"
    narrator "所以我想找到她。"
    narrator "至于找到她要干什么，要说些什么。"
    narrator "我不知道，也没有想过。"
    narrator "现在光是要找到她就已经是件需要我倾注全部精力去进行的事情。"
    narrator "根本就没有更多的时间去思考多余的事情。"

    #【CG：窗边的追逐者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_zzz = True
    scene cg_窗边的追逐者 with Dissolve(2)
    
    pause 1.0

    w "希望么…."
    narrator "我看着窗外的已经有了些许人气的医院。"
    narrator "不由得喃喃地说道。"
    w "或许你就是我唯一的希望吧。"
    narrator "就算是假的，我也要去试一试。"
    narrator "因为现在除了每天在人海里头碰运气。"
    narrator "我自己已经没有任何办法和对策去找到那个人了。"
    w "呵呵…."
    narrator "想不到我林琴在最后反而要把希望寄托在别人的身上。"
    narrator "真的是好笑啊。"
    narrator "明明有那么多的人都在说什么最后的希望在我的身上。"
    narrator "但是我只要能够见到她，跟她说上几句话就可以了。"
    narrator "至于别的…都是我所不需要的。"
    
    #【CG：追逐者结束】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    
    scene bf_夜晚 with dissolve:
        zoom .667

    w "不过…."
    narrator "袁艳嘴里所说的那些我也挺感兴趣的。"
    narrator "她说的自己没有时间到底是怎么一回事呢…."
    
    jump c2_2

#程祎琳（视角，CV配音部分）
#（视角切换——程祎琳）
label c2_c1_c:

    $_dismiss_pause = False

    $c2_c1_c_select = True
    
    nvl clear
    nvl hide
    window hide dissolve

    #【场景：河边】
    scene river_夜晚 with dissolve:
        zoom .667
    
    w "唔…."
    narrator "想睡觉，但是又睡不着。"
    narrator "今晚仿佛被什么东西嘱咐了不能睡过去一样"
    narrator "睡过去的话….就完了。"
    narrator "因此，我很痛苦。"
    narrator "不过，肚子还是很饱，在一个刚认识没多久的女孩那里吃零食吃到饱。"
    narrator "莫名的安全感涌了上来。"
    narrator "尽管伴随着痛苦，我却依然感觉非常的安心。"
    w "之后得去谢谢她呢。"
    narrator "她的名字叫做袁艳。"
    narrator "一个养着猫的奇怪女孩。"
    narrator "不过，我很喜欢。"
    w "唔嘿嘿。"
    narrator "我感觉到很开心。"
    narrator "饿了的时候在去她那里吧。"
    narrator "啊，对了。"
    narrator "我记得好像要帮她买什么东西来着…."
    narrator "好像要帮她买恋爱——"
    narrator "——唔姆…这个女孩果然很奇怪呢。"
    narrator "不过只要帮她买到恋爱她就会帮我找人呢。"
    narrator "这个条件真的很赚呀。"
    narrator "毕竟这个世界可没有人愿意帮我找了。"
    w "加油。"
    narrator "虽然有些疲惫…但是我还是踏上了我的旅途。"
    narrator "不过先帮袁艳买恋爱好了。"
    
    jump c2_2

#夏静（CV配音部分）
label c2_c1_x:

    $_dismiss_pause = False

    $c2_c1_x_select = True

    nvl clear
    nvl hide
    window hide dissolve

    #【场景：街道】
    scene street_夜晚 with dissolve:
        zoom .667
        
    narrator "我踩着和往常一样的步子，比以往早了不知道多少个小时来到了街道上。"
    narrator "不管看多少次，这个时间段的街道都好像是另外一个世界一样。"
    w "唉。"
    narrator "最近总是会出现幻觉。"
    narrator "我看着在我身后不远处像是一高一矮的两个影子不由得这么想到。"
    narrator "这两个影子每次出现都会紧紧地跟在我的身后。"
    narrator "就好像在观察我一样。"
    narrator "它们又总是会自顾自的消失，让我百思不得其解——"
    narrator "——恰好的事情是，它们刚好出现在我和那个叫做袁艳的女孩认识的时间段前后。"
    narrator "在那之后，幻觉就像是幽灵一般几乎每天出现在我的面前。"
    narrator "我正在思考，它们是否与袁艳的出现有所联系。"
    narrator "比起这个，我倒是更加在意袁艳嘴里所描述的那些事情。"
    narrator "如果她真的有办法能让我记起那个时候的事情。"
    narrator "就陪着她胡闹又有什么关系呢？"
    narrator "以至于我根本懒得探究那两个影子的事情直接归类为幻觉还比较轻松。"
    w "谈恋爱才能救命…这是哪部奇幻剧里才有的剧情啊。"
    w "呵呵呵，袁艳啊袁艳。"
    narrator "但是说到这里，我却说不下去了。"
    narrator "她真的可笑吗？"
    narrator "她的所作所为看起来是那样的滑稽，但是她是认真的。"
    narrator "与之相比自己只是抱着玩玩的心态去接触她。"
    narrator "最后同她交易的自己那岂不是显得更加的可笑？"
    narrator "总而言之，先去好好打探一下程祎琳的情报吧。"
    narrator "只要方法得当，总是能够从袁艳那个丫头嘴里套出点什么来的。"
    narrator "望着刚从天空那一角冒出一点儿头的太阳。"
    narrator "我不由得这么想到。"
    
    jump c2_2

# TODO
label c2_2:

    $_dismiss_pause = False

    $c2_2_select = True
    
    nvl clear
    nvl hide
    window hide dissolve

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
        
    show y 恼火02 at ct with dissolve
    y "……."
    show y 恼火01 at ct with dissolve
    y "死猫…."
    w "怎么了？"
    show y 恼火03 at ct with dissolve
    y "我怀疑，这三个女人都是神经病吧。"
    w "事到如今你为什么现在才这么觉得？"
    show y 恼火01 at ct with dissolve
    y "你说的对….我早该意识到了。"
    show y 正常04 at ct with dissolve
    y "她们这群人都不用睡觉的吗？"
    show y 恼火01 at ct with dissolve
    y "几点钟啊，几点钟啊？"
    show y 恼火02 at ct with dissolve
    y "四点都不到就开始逛街的逛街，发呆的发呆，吃零食的吃零食。"
    show y 恼火01 at ct with dissolve
    y "胡闹也要有个限度啊！"
    narrator "这丫头又是哪根经搭错了。"
    w "你这是抓的哪门子的狂啊。"
    show y 正常02 at ct with dissolve
    y "……."
    show y 正常01 at ct with dissolve
    y "这个时候她们不应该好好躺在床上睡觉吗？"
    w "呵呵，搞不好她们只是恰巧这个时候醒了而已吧。"
    show y 正常04 at ct with dissolve
    y "恰巧三个人都是这个时候醒了？"
    w "有什么不可以的吗？"
    w "你自己不也没睡吗？还一巴掌把我给弄醒了。"
    show y 正常05 at ct with dissolve
    y "……."
    show y 正常04 at ct with dissolve
    y "我只是偶尔不小心睡不着而已，这是碰巧而已，碰巧你懂吗？"
    w "哦豁，那你能碰巧就不能让别人碰巧了？"
    show y 正常01 at ct with dissolve
    y "可这也太巧了吧，刚好撞到她们仨都醒着？" 
    #【袁艳】（正常03-01）
    show y normal_3_1 at ct with dissolve
    y "而且我也醒着，简直就像是被安排好的一样。"
    w "……."
    narrator "袁艳说完这句话的时候和我对视了起来，我们彼此都因为这句话而愣住了。"
    show y 正常04 at ct with dissolve
    y "好像….好像…还真像那么一回事。"
    show y 无措 at ct with dissolve
    y "哦呵呵呵哦呵呵。"
    w "这可能就是命运吧。"
    w "那么，你对你已经发生的事情有什么看法吗，袁小姐？"
    show y 无措 at ct with dissolve
    y "我…."
    show y 恼火04 at ct with dissolve
    y "我能怎么办啊，我也很绝望啊。"
    show y 恼火03 at ct with dissolve
    y "还有别叫我袁小姐，抽死你哦！"
    narrator "……"
    narrator "回过神的时候，上午的时间都过去了。"
    show y 正常02 at ct with dissolve
    y "肚子饿了，不跟你争了。"
    w "真巧，我也这么想。"
    narrator "然后袁艳又点了外卖，给我吃的也是跟之前相同的食物。"
    narrator "我们非常默契地都没有说话，而是默默地把自己面前的食物给吃完。"
    narrator "剧本本来应该是这样子写的…."
    show y 正常01 at ct with dissolve
    y "从一开始我就觉得不对劲了。"
    w "喵？"
    show y 恼火01 at ct with dissolve
    y "你们三个是跑过来干什么鬼的啊！！"
    narrator "袁艳指着桌前出现的三个女孩，抓狂似地说道。"

    #【CG：聚餐】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_yzhy = True
    scene cg_圆桌会议 with Dissolve(2)

    pause 1.0
    
    #none lh
    x "这应该就是所谓的家庭聚餐才对啊。"
    #none lh
    l "我只是偶然路过而已。"
    #none lh
    y "聚餐才怪啊！我只买我自己的一份啊！"
    #none lh
    y "还有路过的你骗谁啊，你不是住医院的吗？"
    #none lh
    c "家庭…聚餐吗？"
    #none lh
    c "诶嘿嘿…."
    narrator "程祎琳有些开心地低下了头摆弄自己的手指。"
    #none lh
    y "……."
    #none lh
    y "你脸红个屁啊！"
    #none lh              
    y "啊…."
    narrator "我默默看着面前的突发状况。"
    narrator "身边发狂的袁艳。"
    narrator "还是熟悉的配方，熟悉的味道。"
    w "喵…."

    # TODO
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    
    #【CG：结束】
    scene room_夜晚 with dissolve:
        zoom .667

    show l 注视07 at ct with dissolve
    l "本小姐吃你点的外卖是给你面子。"
    show l 慌张07 at ct with dissolve
    l "你就不能学会感恩吗？"
    show l 慌张07:
        linear .3 xpos 1.25 xanchor 1.25
    show y 无措 with dissolve:
        xpos -0.08 xanchor 0.0
    y "这是哪门子的感恩啊。"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "倒是你们是怎样这么凑巧的都到我家来吃饭的啊？"
    show y 愤怒 with dissolve:
        xpos -0.08 xanchor 0.0
    y "喂！那是我的！"
    show c 惊讶01 with dissolve:
        xpos .75 xanchor .75
    c "(吓~~~)啊？"
    #c "(吓~~~)啊？"
    show x 嘲笑01 with dissolve:
        xpos .25 xanchor .25
    x "呵呵呵呵…."
    show x 嘲笑02 with dissolve:
        xpos .25 xanchor .25
    x "这里还真的是热闹啊。"
    show y 不爽01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "热闹个鬼啊！"
    narrator "……"
    narrator "首先我要惊叹的事情是袁艳这个女孩点来的外卖的量还是有不少的。"
    narrator "一份外卖居然让四个人吃了大半个小时。"
    narrator "虽然说多数是在吵闹，但是在这段时间里她们并没有停止抢食作业。"
    narrator "这是有原因的。"
    
    nvl clear
    nvl hide
    window hide dissolve

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
    
    show y 不爽02 at ct with dissolve
    y "这可是我一天份的外卖啊。"
    w "可是你为什么要突然买一整天份的外卖啊？"
    show y 不爽01 at ct with dissolve
    y "昨晚通宵了，所以我下午想睡一觉。"
    show y 恼火02 at ct with dissolve
    y "一觉睡到晚上然后稍微热热外卖就能吃了。"
    w "你算盘打得不错。"
    w "夏静过来了。"
    w "喵~"
    narrator "……."
    show y 恼火02 with dissolve:
        linear .3 xpos -0.08 xanchor 0.0
    show x 注视01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "喔，这里就是你的房间了吗？"
    show y 恼火01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……."
    show y 恼火02 with dissolve:
        linear .3 xpos -0.08 xanchor 0.0
    y "你能不能不要随便进我的房间啊。"
    show x 假笑02 with dissolve:
        xpos 1.25 xanchor 1.25
    x "哈哈哈，有什么关系呢。"
    show x 假笑01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "反正也不是第一次进了。"
    show y 恼火02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "那也别随便进来啊。"
    show x 怜悯02 at rt with dissolve
    x "别那么无情嘛。"
    show x 怜悯01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "我们不是正在生死相托交易着的伙伴吗？"
    show y 恼火01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "谁跟你是生死相托的伙伴啊。"
    show x 假笑01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "哈哈哈…."
    show l 不满08 with dissolve:
        xpos .25 xanchor .25
    l "还真是一点女孩子味道都没有的房间。"
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "身为一个女孩子你真的是太失败了。"
    show y 恼火05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……."
    show y 恼火06 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我是一个女孩子真是对不起了。"
    show y 恼火04 with dissolve:
        xpos -0.08 xanchor 0.0
    #（小声嘀咕）
    y "你自己也差不了多少吧。"
    w "噗~"
    narrator "我差点没有笑出声来。"
    show c 注视01 with dissolve:
        xpos .75 xanchor .75
    c "有…有吃的东西吗？"
    show c 侧视01 with dissolve:
        xpos .75 xanchor .75
    c "刚刚没吃饱…."
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "没有！"
    narrator "她拒绝得无比的果断，没有丝毫犹豫。"
    narrator "反倒是程祎琳显得有些沮丧了。"
    show x 假笑01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "啧啧。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "啧啧。"
    show y 恼火06 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……."
    show y 恼火04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "抽屉里还有包奶糖…."
    show c 张嘴01 at ct with dissolve
    c "啊，谢谢！"
    show y 恼火05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "……."
    narrator "虽然我知道现在的袁艳正处于暴走边缘，但是不知怎的我就是想笑。"
    w "喵~喵！"
    show c 惊讶01 with dissolve:
        xpos .75 xanchor .75
    c "唔？"
    w "欸？"
    narrator "我兴奋的行为似乎被这个丫头注意到了。"
    show c 惊讶02 with dissolve:
        xpos .75 xanchor .75
    c "啊哈哈。"
    show c 侧视01 with dissolve:
        xpos .75 xanchor .75
    c "你也想吃吗？"
    narrator "程祎琳撕开了包装袋，拿出了一颗糖。"
    w "喵~"
    narrator "吓我一大跳，我还以为这丫头注意到我了呢。"
    show c 侧视02 with dissolve:
        xpos .75 xanchor .75
    c "但是不给你吃。"
    w "……."
    narrator "到底是闹哪样啊！！！"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "噢，原来这只猫是你家的啊。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "害得我找了好久呢。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "啥？"
    w "……."
    narrator "咦，气氛好像有点不太对？"
    narrator "怎么矛头突然又指向我来了？"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "它咋了？"
    w "喵？"
    show l 注视07 with dissolve:
        xpos .25 xanchor .25
    l "就是被它看到了一些不好的东西呢。"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "不好的东西？"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "……."
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "你是不知道呢还是装给我看的？不过这么无所谓了。"
    show l 慌张08 with dissolve:
        xpos .25 xanchor .25
    l "就算你给这死猫装了针孔摄像头都没有用的。"
    show l 慌张07 with dissolve:
        xpos .25 xanchor .25
    l "如果你想要靠视频来攻击我就大错特错了哦。"
    w "……."
    show y 恼火05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "哈？"
    show y 恼火04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "针孔摄像头？"
    narrator "袁艳看起来有些懵，虽然她不知道发生了什么。"
    narrator "可是我却总觉得有些明白了起来。"
    narrator "不过不是什么想回忆起来的遭遇…."
    
    nvl clear
    nvl hide
    window hide dissolve

    # TODO
    #"（场景：灰色回忆）"
    #【场景：医院房间】
    scene bf_黄昏 with dissolve:
        zoom .667
    
    show l 惊异03 at rt with dissolve
    l "！！！"
    show l 惊异03 at rt with dissolve
    l "啊啊啊啊啊啊！！！"
    w "现在的女孩子都喜欢乱发狂的吗？"
    show l 普通02 at rt with dissolve
    l "欸？"
    w "……"
    w "！！"
    narrator "林琴的手停在半空中。"
    narrator "我也因为林琴的疑惑声而僵住了身子。"
    narrator "一人一猫就在这个突然变得安静得有些恐怖的病房里头对视了起来。"
    show l 普通01 at rt with dissolve
    l "……"
    w "喵…喵~"

    nvl clear
    nvl hide
    window hide dissolve

    #【场景：房间】
    scene room_夜晚 with dissolve:
        zoom .667
    
    narrator "之前好像发生过这样子的事情呢。"
    narrator "哦呵呵呵呵！"
    narrator "这还真是不太好的回忆啊。"
    narrator "林琴这丫头现在的眼神怎么看起来那么怪啊。"
    narrator "就好像在看餐桌上的一道菜一样。"
    narrator "……."
    show y 恼火02 at ct with dissolve
    y "……."
    narrator "袁艳狠狠地瞪了我一眼。"
    w "喵~"
    narrator "我只能委屈地叫了起来。"
    show y 恼火02:
        linear .3 xpos 0.0 anchor 0.0
    show x 假笑02 at rt with dissolve
    x "欸。"
    show x 假笑01 at rt with dissolve
    x "这只猫还挺通人性的。"
    show x 怜悯02 at rt with dissolve
    x "要不送给我做宠物吧。"
    show x 怜悯01 at rt with dissolve
    x "哈哈哈。"
    show y 笑容01 at lt with dissolve
    y "好啊好啊。"
    narrator "喂，死丫头你答应能不能带点犹豫，我们好歹是命运链接的伙伴啊！"
    w "喵呜喵唔！"
    narrator "我不满地叫了两声之后整个身子后退了好几步。"
    show x 假笑01 at rt with dissolve
    x "喔，还真的是通人性啊。"
    show x 假笑02 at rt with dissolve
    x "好像能听懂我说话一样。"     
    narrator "什么叫好像？你们的话我全都听得懂好不好。"
    narrator "我神气地直了直身子。"
    show y 笑容02 at lt with dissolve
    y "别说好像了，它就是能听懂你的话。"
    narrator "噗，我瞪大了眼睛看着袁艳，这家伙不会突然想不开要把我供出来吧。"
    narrator "我突然像是炸毛一样紧张了起来。"
    show y 俏皮 at lt with dissolve
    y "真的啦。"
    show x 假笑01 at rt with dissolve
    x "噢！那还真是厉害啊！"
    narrator "夏静听到袁艳这么说之后，看了看我。"
    narrator "然后很明显兴致全无一样地咂了咂嘴，转移了视线。"
    narrator "这人真是何等地……让猫无法理解啊。"
    w "……."
    show y 开心 at lt with dissolve
    y "你喜欢的话这猫就送你了，怎么样？"
    show x 怜悯02 at rt with dissolve
    x "嘛，我不是很喜欢猫，还是算了。"
    narrator "对我瞬间失去兴趣的夏静很明显地表明了自己的想法。"
    narrator "就是有点太直接让我有点受伤。"
    show x 考虑01 at rt with dissolve
    x "不过你适应能力很强啊。"
    show y 正常04 at lt with dissolve
    y "为啥这么说？"
    show x 考虑02 at rt with dissolve
    x "你看你嘴上说不准我们进房间。"
    show x 普通01 at rt with dissolve
    x "慢慢地自己就先习惯了我们所在的房间呢。"
    show x 普通02 at rt with dissolve
    x "这是为什么呢？"
    narrator "尽管夏静是微微笑着看着程祎琳吃东西，但是她问出的问题在这个时候反而显得非常微妙、难以回答。"
    hide x with dissolve
    show y 正常01 at lt with dissolve
    y "……."
    w "………"
    narrator "我是没办法帮上什么忙的。"
    narrator "因为关于袁艳适应力强这点连我都无可否认的。"
    narrator "事实上我比夏静都想要知道为什么。"
    show y 正常02 at lt with dissolve
    y "唉…."
    show y 正常03 at lt with dissolve
    y "先声明。"
    show y 正常01 at lt with dissolve
    y "我可完全没有说允许你们闯进我房间啊。"
    show y 正常02 at lt with dissolve
    y "非要说就是我适应力强点而已。"
    show l 普通07 at ct with dissolve
    l "适应力强？"
    show y 正常04 at lt with dissolve
    y "只要把你们当成灾难这类的。"
    show y 正常05 at lt with dissolve
    y "我从中想办法求生就可以很好地跟你们相处了。"
    show x 惊异 at rt with dissolve
    x "噗…"
    show l 惊异 at ct with dissolve
    l "噗…"
    w "……."
    show x 惊讶01 at rt with dissolve
    x "哈哈哈，你这还真是过分啊！"
    show y 开心 at lt with dissolve
    y "彼此彼此了。"
    show l 普通08 at ct with dissolve
    l "乱说话会死的噢。"
    show y 笑容01 at lt with dissolve
    y "反正不说结果也差不多。"
    show x 惊异:
        linear .3 xpos 1.25 xanchor 1.25
    show y 笑容01:
        linear .3 xpos -0.08 xanchor 0.0
    show l 普通08:
        linear .3 xpos .75 xanchor .75 
    show c 恶心01 with dissolve:
        xpos .25 xanchor .25
    c "……"
    show c 注视01 with dissolve:
        xpos .25 xanchor .25
    c "嗯…吃完了。"
    show y 嘲笑 with dissolve:
        xpos -0.08 xanchor 0.0
    y "各种意义上来说你们的出现对我来说确实算是空前的灾难了。"
    show l 不满09 with dissolve:
        xpos .75 xanchor .75
    l "那也只能怪你自己啊。"
    show l 不满07 with dissolve:
        xpos .75 xanchor .75
    l "先招惹我们的可是你啊。"
    show y 嘲讽01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "话是这么说…."
    w "……"
    narrator "袁艳朝我看了过来，明知道这点的我则是像是躲避一样跟她错开了视线。"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "这么说起来，你们答应我要做的事情呢？"
    show y 正常05 with dissolve:
        xpos -0.08 xanchor 0.0
    y "不是让你们去谈恋爱的吗？"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "怎么谈着谈着谈到我家里来了啊喂！"
    narrator "咦？谈恋爱？"
    narrator "这是什么时候的主题？"
    narrator "好像有这么一回事来着？"
    narrator "连我都有些疑惑，这个话题好像是很久很久以前的事情了。"
    show y 无措 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你们别一脸好像从来没听说过这事的样子好不好！！！"
    show y 无措 with dissolve:
        xpos -0.08 xanchor 0.0
    y "这是我最初找你们的目的啊！"
    narrator "这个时候夏静则是歪了歪脑袋。"
    show x 惊讶02 with dissolve:
        xpos 1.25 xanchor 1.25
    x "啊，谈恋爱啊。"
    show x 惊讶01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "好像是有这么一回事来着。"
    show x 惊讶02 with dissolve:
        xpos 1.25 xanchor 1.25
    x "但是就算你这么说。"  
    show x 惊讶01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "一时半会的你让我怎么谈啊，我也没有谈过恋爱之类的。"
    show c 斜视01 with dissolve:
        xpos .25 xanchor .25
    c "嗯嗯，我也没有买到谈恋爱。"
    show l 惊异03 with dissolve:
        xpos .75 xanchor .75
    l "谈恋爱是可以买的吗？在哪里？"
    show y 嘲笑 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你们认真的吗？"
    show x 考虑01 with dissolve:
        xpos 1.25 xanchor 1.25
    x "要不你传授点经验之类的？恋爱经验谈？"
    show y 恼火02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我怎么跟你们传授经验啊！"
    show y 恼火01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我出生到现在自己都没谈过恋爱。"
    show x 怜悯02 with dissolve:
        xpos 1.25 xanchor 1.25
    x "什么啊，原来还是个处女，嘁。"
    show y 愤怒 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你是想打架吗？？"
    show c 惊讶02 with dissolve:
        xpos .25 xanchor .25
    c "噢噢…."
    show c 惊讶01 with dissolve:
        xpos .25 xanchor .25
    c "我可以去冰箱里拿牛奶喝吗？"
    narrator "……."
    narrator "房间里头不是一般的吵。"
    narrator "连我这种喜欢热闹的猫都觉得吵了，那肯定就是吵翻了天。"
    narrator "也不知道她们哪里来的那么多话题。"
    narrator "我听得都觉得困了。"
    narrator "于是在吵闹声中，我渐渐地闭上了眼睛，把早上没有补回来的觉又补了回去。"
    
    #【CG：黑眼袋的贤者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_blackxz = True
    scene cg_黑眼袋的贤者 with Dissolve(2)
    
    pause 1.0
    
    narrator "原本我以为，这种时候我能够好好的稍微休息一下。"
    narrator "但是，现实总是不尽猫意。"
    narrator "‘啪啪’两声响起，把我从梦里拉回了现实。"
    w "你…干什么啊！"
    narrator "我只感觉到我的下颚麻麻的没有感觉，似乎是某件事情又重复上演了。"
    narrator "睁开眼睛的时候。"
    narrator "袁艳在我的正上方。"
    narrator "顶着黑眼圈一脸幽怨地看着我。"
    #none lh
    y "醒了没。"
    w "醒了。"
    narrator "我喃喃地回答道。"
    #none lh
    y "醒了就好，准备吃饭了。"
    narrator "袁艳看见我醒了之后才起身，有气无力的样子让我觉得有些奇怪。"
    w "她们都走了吗？"
    narrator "翻了个身爬了起来。"
    #none lh
    y "还没….都在客厅等着开饭。"
    w "啥情况？她们来这里干啥的啊？"
    #none lh
    y "我怎么知道，估计是过来玩的吧。"
    w "……."
    narrator "我有些尴尬地跟袁艳对视着。"
    #none lh
    y "我在她们之间周旋的时候你居然躲在这里睡觉。"
    w "我…."
    w "我这不也是没办法么。"
    w "我啥也帮不到你啊她们在的时候。"
    #none lh
    y "你不帮忙就是帮了我大忙了。"
    #none lh
    y "谁知道你会给我添什么乱子。"
    w "那还真是对不起了啊。"
    #none lh
    y "别废话了，赶紧出来吃东西。"
    #none lh
    y "逃兵。"
    w "……."
    w "话说你进来叫我吃饭不会引起她们怀疑么？"
    #none lh
    y "你在说什么鬼，我早就跟她们说实话了。"
    #none lh
    y "只是她们自己不信而已，还以为我在装神弄鬼。"
    w "啊？"
    #none lh
    y "你听好了，死猫。"
    narrator "袁艳走到了房间的门边，非常正经且帅气的侧身回过头来对我说道。"
    #none lh
    y "所谓的人类这种生物啊，越是容易得到的真相就越是容易被认定为假象。"
    narrator "然后她就离开了房间。"

    #【CG结束】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    scene room_白天 with dissolve:
        zoom .667

    narrator "虽然她说得好像很有道理，而且今天那个夏静的表现也确实如此。"
    narrator "但是这个自以为是的家伙到底是闹哪样啊。"
    narrator "居然突然在我面前耍帅。"
    narrator "要不要脸啊！"
    w "……."
    w "搞得你好像不是人一样。"
    narrator "默默地吐槽之后便跟上袁艳一起离开了房间。"

    #【场景：客厅】
    nvl clear
    nvl hide
    window hide dissolve
    scene kt_白天 with dissolve:
        zoom .667
    
    show x 假笑01 at ct with dissolve
    x "噢，要开饭啦！"
    show x 假笑01:
        linear .3 xpos -0.08 xanchor 0.0
    show c 张嘴01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "开饭啦！！"
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "都说了你把外卖店的名字给我，我现在就叫人去买了那家店。"
    show l 不满07 at rt with dissolve:
        xpos .25 xanchor .25
    l "想吃什么我都请客。"
    show y 嘲讽04 with dissolve:
        xpos .75 xanchor .75
    y "唉……"
    w "喵。"
    narrator "很明显地袁艳压根就没想理会这三个女孩。"
    narrator "而是径直地从厨房里头拿出了重新装好的外卖套餐放到了桌面上。"
    show y 正常02 with dissolve:
        xpos .75 xanchor .75
    y "这次我点了五人份的套餐。"
    show y 正常01 with dissolve:
        xpos .75 xanchor .75
    y "怎么说都够吃了。"
    show y 正常02 with dissolve:
        xpos .75 xanchor .75
    y "死猫，这是你的。"
    narrator "袁艳连我的食物都准备好了。"
    narrator "只可惜，我并不是很饿。"
    narrator "倒是看着袁艳有气无力的干活。"
    narrator "作为神圣的我表示非常地担心啊。"
    narrator "这弄来的食物味道不会受影响吧。"
    w "……."
    narrator "好像思考的重点有点不太对。"
    narrator "算了，这个也不关我什么事。"
    narrator "吃饱了再说。"
    narrator "于是，我放下了心里那点担心开始吃起了晚餐。"
    #嘲讽
    show y 嘲讽01 with dissolve:
        xpos .75 xanchor .75
    y "呵….想不到把你们聚起来是到我家里来吃聚餐的。"
    show x 假笑02 with dissolve:
        xpos -0.08 xanchor 0.0
    x "这也没有办法啊。"
    show x 假笑01 with dissolve:
        xpos -0.08 xanchor 0.0
    x "来来来，小琳，这块鸡腿给你。"
    show c 惊讶02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……."
    show c 惊讶01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "不….不用了。"
    show x 怜悯01 with dissolve:
        xpos -0.08 xanchor 0.0
    x "不要客气嘛。"
    show c 惊讶01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "真….真的不用啦，你自己吃吧。"
    show x 嘲笑02 with dissolve:
        xpos -0.08 xanchor 0.0
    x "来嘛来嘛。"
    show c 惊讶02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "不要。"
    narrator "两个女孩碗里的鸡腿反复易手，看得袁艳内心都快崩溃了。"
    show y 正常02 with dissolve:
        xpos .75 xanchor .75
    y "我说你们啊…."
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "你们不吃就给我好了。"
    narrator "林琴非常不客气地伸出了筷子，把程祎琳碗里的鸡腿夹走就吃了起来。"
    show x 闭眼 with dissolve:
        xpos -0.08 xanchor 0.0
    x "……"
    show x 反驳01 with dissolve:
        xpos -0.08 xanchor 0.0
    x "我说你啊，我可没有说要给你吃啊。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "噢，是吗，反正那丫头也不愿意吃。"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "喂，你想要吗？"
    narrator "程祎琳弱弱地看了一眼林琴，然后摇了摇头。"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "看吧，她自己说的不想要。"
    show l 普通08 with dissolve:
        xpos .25 xanchor .25
    l "我只是遵从了她的愿望而已。"
    show x 反驳02 with dissolve:
        xpos -0.08 xanchor 0.0
    x "她不要是她的事情啊，你跑过来凑什么热闹。"
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "错了！这里大错特错了啊。"
    show x 反驳01 with dissolve:
        xpos -0.08 xanchor 0.0
    x "哈？"
    show l 普通07 with dissolve:
        xpos .25 xanchor .25
    l "有价值的东西不管怎么被多少人拒绝迟早会某一个人接受的。"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "她不要的东西不代表我不要啊。"
    show x 反驳02 with dissolve:
        xpos -0.08 xanchor 0.0
    x "可我也没说给你啊，而且你自己不是有一个吗？"
    show l 注视07 with dissolve:
        xpos .25 xanchor .25
    l "我这是要让你们明白这个社会的残酷啊。"
    show l 注视08 with dissolve:
        xpos .25 xanchor .25
    l "这点上面你们还要感谢我呢。"
    show l 注视09 with dissolve:
        xpos .25 xanchor .25
    l "我是我的方式抢过来的，现在是我的了，有什么不行吗？"
    show x 反驳01 with dissolve:
        xpos -0.08 xanchor 0.0
    x "这可是强抢，不太好吧。"
    show l 普通09 with dissolve:
        xpos .25 xanchor .25
    l "那当然不是，这只是资本主义竞争。"
    show y 恼火01 with dissolve:
        xpos .75 xanchor .75
    y "……"
    show x 反驳02 with dissolve:
        xpos -0.08 xanchor 0.0
    x "嘁，万恶的资本主义走狗。"
    show l 不满08 with dissolve:
        xpos .25 xanchor .25
    l "哼，无能的观察主义庶民。"
    narrator "就是连在默默吃东西的我都能明显感觉到空气中很明显的火药味。"
    narrator "但是这火药味莫名的带了点奇怪的本来不应该有的默契。"
    w "唔喵？"
    narrator "突然一双小手伸到了我的下腹，把我抱了起来。"
    show c 惊讶01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "我们快躲起来，神仙要打架了！！"
    w "……."
    narrator "能不能先让我把食物吃完…."
    
    #【场景：房间】
    nvl clear
    nvl hide
    window hide dissolve

    scene room_夜晚 with dissolve:
        zoom .667
    
    narrator "这个丫头个子不是很高。比袁艳至少矮一个头。"
    narrator "但是她的手却格外的温暖。"
    narrator "从抱我的手法中便能感受到她的温柔。"
    narrator "看得出来，她似乎是非常喜欢我的…"
    show c 注视01 at ct with dissolve
    c "嘿嘿，乖~乖！"
    narrator "好像非常喜欢我下腹的皮毛。"
    narrator "不停地用各种手法抚摸着我的下腹。"
    narrator "而且每当我想挣脱的时候她就会紧紧地抓住我…甚至把我抱在怀里。"
    narrator "带着淡淡牛奶香味的体香飘到我的鼻子里，跟袁艳身体的味道很明显的不一样。"
    narrator "我对牛奶算不上讨厌也算不上喜欢吧。"
    narrator "但是这种羞耻体验还是不要啊！！！"
    narrator "可是我又没办法挣脱。"
    narrator "心中的无力感逐渐升了起来。"
    narrator "……."
    narrator "我大概体会到了袁艳心里的那种无力感。"
    narrator "望着房间窗外渐渐升起的一轮明月。"
    narrator "我张了张嘴巴。"
    w "喵~~~"
    narrator "救…救命啊…."
    narrator "过了好一段时间，救我的人终于出现了。"
    show c 注视01:
        linear .3 xpos 1.0 xanchor 1.0
    show y 恼火05 at lt with dissolve
    y "我说….你差不多玩够了吧。"
    show c 张嘴01 at rt with dissolve
    c "欸？"
    show y 正常04 at lt with dissolve
    y "她们都走了，你是不是也差不多该离开这里了？"
    narrator "袁艳顶着非常严重的黑眼圈出现在了房间门口。"
    show c 张嘴02 at rt with dissolve
    c "啊？"
    show y 恼火05 at lt with dissolve
    y "还有你们能不能不要随便进我的房间。"
    show c 注视02 at rt with dissolve
    c "嗯…嗯。"
    show y 开心 at lt with dissolve
    y "要我送你吗？"
    narrator "程祎琳松开了紧紧抱住我的手，我连忙跑离了她的身边。"
    narrator "她摇了摇头。"
    show c 侧视01 at rt with dissolve
    c "那我明天继续过来玩。"
    hide c with dissolve
    narrator "说完这句话，她就离开了房间。"
    narrator "客厅那边的门响之后预示着最后一个人也离开了这里。"
    narrator "我和袁艳神情地对视着…."
    narrator "其实事实也不是这样——"
    show y 不爽01 at ct with dissolve
    narrator "而是袁艳顶着厚厚的黑眼圈和死鱼眼死盯着我。"
    w "……"
    w "你….你这么看着我干什么啊。"
    show y 笑容02 at ct with dissolve
    y "噢呵呵，没什么。"
    show y 笑容01 at ct with dissolve
    y "就是感觉你最近很享受啊。"
    show y 开心 at ct with dissolve
    y "明明都死到临头了。"
    w "哪有这回事。"
    w "现在是文明时代，不兴说瞎话。"
    w "我可是认真得一丝不苟的啊。"
    show y 恼火05 at ct with dissolve
    y "行了行了，你少废话了。"
    show y 恼火04 at ct with dissolve
    y "我有事要问你。"
    w "那你就问吧，只要是我知道的。"
    show y 正常05 at ct with dissolve
    y "就是我到底该做什么事情。"
    show y 正常04 at ct with dissolve
    y "今天我突然想明白。"
    show y 正常04 at ct with dissolve
    y "就算让她们去谈恋爱也没有什么实质性的作用吧。"
    w "啊？"
    show y 正常05 at ct with dissolve
    y "就是你之前不是说过吗？"
    show y 正常03 at ct with dissolve
    y "就算她们真的谈了恋爱，我的诅咒也没办法解除。"
    w "嗯，就算她们全部谈恋爱了。"
    w "你身上的诅咒也不会有丝毫的减弱。"
    show y 正常01 at ct with dissolve
    y "那我该怎么办？"
    w "选择。"
    show y 正常02 at ct with dissolve
    y "选择什么？"
    w "判断灵魂都要崩坏的女孩是谁。"
    show y 正常04 at ct with dissolve
    y "这件事情非得由我去判断吗？"
    w "不。"
    w "其实我自己也可以判断。"
    w "只不过…."
    show y 正常05 at ct with dissolve
    y "只不过你判断的准确率太低。"
    show y 正常06 at ct with dissolve
    y "基本是依靠猜测，类似于赌博一样的猜测。"
    show y 正常04 at ct with dissolve
    y "而且诅咒也连带到你的身上了。"
    w "所以我想把判断交给跟她们同样身为人的你来判断。"
    show y 正常02 at ct with dissolve
    y "那你就不怕我猜错？"
    w "emmmmm…."
    narrator "你要问我怕不怕，那我肯定是怕的。"
    w "但是这是我决定好的事情。"
    show y 正常01 at ct with dissolve
    y "你可要想清楚了噢。"
    narrator "袁艳揉了揉眼睛，从她的眼神里头我似乎读出了疲惫。"
    w "我自己决定的事情我是不会后悔的。"
    w "我认为我自己做出的决定是当下最好的了。"
    show y 正常04 at ct with dissolve
    y "你确定？"
    w "我确定。"
    show y 正常05 at ct with dissolve
    y "真的不后悔？"
    w "不后悔。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常06 at ct with dissolve
    y "唉。"
    show y 正常04 at ct with dissolve
    y "好吧。"
    show y 正常03 at ct with dissolve
    y "那我就稍微再努力一些吧。"
    narrator "袁艳起身开始收拾起房间。"
    show y 正常04 at ct with dissolve
    y "今天晚上就早点睡吧。"
    show y 正常05 at ct with dissolve
    y "没几天了，明天必须要好好干啊。"
    w "噢……噢。"
    narrator "尽管我对袁艳莫名其妙燃起的积极性还是感到非常的奇怪。"
    narrator "不过这个也姑且算是好事吧。"
    narrator "只不过我下午才睡完…晚上又让我睡…."
    narrator "可能有点睡不着啊。"
    w "我下午才睡，不是很想睡。"
    show y 正常04 at ct with dissolve
    y "是吗？那我就不管你先睡了。"
    w "噢…噢。"
    show y 正常02 at ct with dissolve
    y "外边还有一些零食吃，饿了自己去吃。"
    w "好。"
    show y 正常03 at ct with dissolve
    y "那我先睡了。"
    w "睡吧睡吧。"
    narrator "袁艳眨了眨似乎快撑不住了的眼皮，看了我一眼。"
    hide y with Dissolve(.7)
    narrator "然后便上床打算睡觉了。"
    narrator "她似乎比想象中要累得多。"
    narrator "以至于她上床之后就没了动静。"
    w "……"
    narrator "真没了动静？"
    narrator "我猫着脚步想要跳上去瞅瞅。"
    narrator "我为什么要这么在意这丫头呢。"
    narrator "搞不懂。"
    narrator "想到这里走到一半的脚步停了下来。"
    narrator "转身便离开了房间。"
    
    #【场景：客厅】
    nvl clear
    nvl hide
    window hide dissolve

    scene kt_夜晚 with dissolve:
        zoom .667
    
    narrator "客厅的灯还没有关。"
    narrator "只是站在房间门口的我能清楚地看见桌子上没吃完的零食。"
    w "这群丫头…真的是…."
    narrator "想要抱怨，但是又不知道从哪里抱怨起。"
    narrator "感觉自己跟她们的老妈子一样。"
    narrator "无奈叹了一口气。"
    narrator "我爬到了桌子上蹲着。"
    narrator "静静地跟零食对视了好一会，最后还是用鼻子去嗅了嗅。"
    narrator "然后就叼起一块尝了尝。"
    narrator "接着…就停不下来了。"
    narrator "转眼间一包零食就被我一扫而空。"
    narrator "我舔了舔爪子。"
    narrator "其实我一直在想一件事。"
    narrator "那就是为什么人类的做出来的食物会那么的好吃。"
    narrator "但是突然想起袁艳做出来的食物。"
    w "……"
    w "世界上也是有各种各样的人类呢。"
    narrator "我摇了摇头。"
    narrator "然后又瞄上了另外一个包装的零食。"
    narrator "……"
    narrator "哼哼哼，今天晚上就是我一只猫不眠的盛宴。"
    narrator "话虽然这么说，我也只是在吃零食而已。"
    narrator "吃得差不多了的时候，我就离开了客厅。"
    narrator "想想这几天所发生的事情。"
    narrator "各种意义上自己还是蛮幸运的。"
    narrator "除了有点对不起袁艳以外…."
    narrator "不过话说回来，那个东西到现在都没有到来吗？"
    narrator "时间应该差不多了才对。"
    narrator "难不成是袁艳比较特别？所以那个东西才没有降临？"
    narrator "只有这个解释可以解释得通了。"
    w "一定就是这样子啦。"
    narrator "像是想通了一样，我大摇大摆地叼着一包零食回到了袁艳的房间。"
    narrator "准备回自己的窝里头睡一觉再说了。"
    narrator "……."
    narrator "但是我似乎有点乐观——"
    narrator "——应该说是乐观得有点过头了。"
    #none lh
    y "……"
    w "……."
    narrator "袁艳坐在床上，眼睛瞪得老大…说实话有点可怕。"
    narrator "连见多识广的我都有点被吓到了。"
    w "那…那啥？你咋了？"
    show y 恼火02 at ct with dissolve
    y "……"
    show y 恼火01 at ct with dissolve
    y "你还没睡啊，死猫。"
    w "……."
    narrator "算了，已经懒得吐槽了，随她怎么称呼吧。"
    w "我不是说了吗？我下午睡了，现在不是特别困。"
    show y 恼火03 at ct with dissolve
    y "这样啊。"
    narrator "袁艳听懂了我的意思，发出了‘原来如此’一样的语气。"
    narrator "但是——"
    narrator "这个我好像之前就跟她说过吧。"
    narrator "难道这家伙记忆错乱了？"
    w "话说你不是累了要早点睡吗？"
    show y 恼火04 at ct with dissolve
    y "……."
    narrator "袁艳有点恍惚，好久才反应过来。"
    show y 恼火06 at ct with dissolve
    y "噢，那个啊….确实有这回事。"
    w "你怎么了？"
    show y 恼火04 at ct with dissolve
    y "啊？"
    narrator "在我的注视下，袁艳的嘴巴微微地张了张。"
    narrator "像是要说什么却说不出口的样子。"
    w "……."
    show y 恼火05 at ct with dissolve
    y "啊…"
    #（想发出声音）"
    narrator "看到这样子的袁艳，我似乎察觉到了什么。"
    narrator "直接跳上了床，坐到了袁艳的面前。"
    show y 恼火02 at ct with dissolve
    y "……"
    w "喝！"
    narrator "我一爪子朝着她懵懵的脸就呼了过去。"
    narrator "如果事后有谁问我会不会后悔的话……"
    narrator "那我肯定只有一个答案。"
    w "怎么会呢……"
    narrator "看到那样子的袁艳。"
    narrator "我发自内心地说道。"
    w "我只是恨手贱的自己。"
    narrator "月光透过窗户，洒在我的尾巴上。"
    narrator "影子看起来就像是狗尾巴草。"
    narrator "可是这个时候我一点玩的心思都没有。"
    narrator "不就是在那丫头脸上留个印子而已。"
    narrator "可她居然恩将仇报。"
    narrator "把我五花大绑在这破椅子上赏月。"
    narrator "我现在肠子都悔青了。"
    narrator "干嘛要去拍她啊。"
    narrator "干脆让她愣死得了。"
    narrator "……."
    w "……."
    narrator "被绑在椅子上的我越想越委屈。"
    narrator "我刚刚可是在救她啊。"
    narrator "凭什么救她还要受到这种待遇。"
    narrator "太过分了吧！"
    narrator "没过多久，袁艳出现在了我的面前。"
    narrator "她顶着黑眼圈注视着我，手里还拿着水果刀。"
    show y 不爽01 at ct with dissolve
    y "死猫。"
    w "……."
    narrator "我完全都不想理她了。"
    show y 不爽02 at ct with dissolve
    y "给你个解释的机会。"
    show y 不爽01 at ct with dissolve
    y "没解释清楚就杀了你。"
    w "你干脆就杀了我吧。"
    narrator "我委屈加上屈辱地闭上了眼睛。"
    show y 嘲讽02 at ct with dissolve
    y "哈？"
    show y 嘲讽01 at ct with dissolve
    y "那就杀了你好了。"
    narrator "然后我就感觉到肚子那块有一股莫名其妙的凉意靠近了过来。"
    narrator "死就死好了，搞得我好像怕死一样。"
    w "……"
    narrator "凡事都可以商量的不是吗？"
    narrator "就比如说现在的我虽然看起来像是嘴硬，委屈。"
    narrator "但是我是打算等刀碰到我的一瞬间就投降的。"
    narrator "只是让我没有想到的事情是——"
    show y 恼火06 at ct with dissolve
    y "唉….没心情陪你玩了。"
    narrator "袁艳帮我解开了绳子。"
    narrator "让我准备投降的手势坐了一半停在半空。"
    narrator "换而言之，这一次是袁艳先投降了。"
    narrator "我倒是有点没反应过来。"
    show y 恼火04 at ct with dissolve
    y "看都我脸上的爪子印没？"
    w "看…看到了。"
    show y 恼火05 at ct with dissolve
    y "你是故意的吧。"
    w "胡…胡说，我是因为不知道拍哪里了嘛。"
    w "在说….在说，我可是为了救你啊。"
    show y 正常02 at ct with dissolve
    y "这样啊。"
    w "可你居然恩将仇报。"
    show y 恼火02 at ct with dissolve
    y "行了行了，少在这里哭惨了。"
    show y 恼火01 at ct with dissolve
    y "搞得好像我不知道你一样。"
    show y 嘲笑 at ct with dissolve
    y "反正也没什么大不了的，只要举起爪子投降我就会原谅你，你说对吧？"
    w "……."
    narrator "这丫头不会觉醒了什么奇怪的力量吧。"
    show y 正常02 at ct with dissolve
    y "刚刚到底发生了什么？"
    show y 正常01 at ct with dissolve
    y "为什么我感觉身体跟网络延迟一样一卡一卡的。"
    w "网络延迟？"
    show y 正常04 at ct with dissolve
    y "额…总之就是反应不过来到底是怎么回事。"
    w "刚刚发生的就是诅咒的征兆而已。"
    narrator "我嘴上说得很轻松，其实自己也没有想到这个东西会突然在这种时候出现。"
    narrator "虽然不断地在思考如果出现了该怎么办。"
    narrator "但是真出现的时候我居然只想到了一巴掌呼脸。"
    show y 正常05 at ct with dissolve
    y "那你还真给我带来了个好消息。"
    w "……."
    w "噢…噢，不用客气。"
    show y 恼火04 at ct with dissolve
    y "我没有感谢你的意思。"
    w "喂喂喂，你冷静…冷静一下，别拿刀乱晃啊，扎到我该怎么办！"
    show y 恼火03 at ct with dissolve
    y "唉…"
    narrator "袁艳揉了揉眼睛，把手上的水果刀放到了桌子上。"
    show y 恼火01 at ct with dissolve
    y "遇见了你就没好事。"
    w "彼此彼此。"
    show y 恼火02 at ct with dissolve
    y "不客气不客气。"
    narrator "这是闹的哪门子相声啊。"
    show y 恼火05 at ct with dissolve
    y "不是，我说你在闹什么？赶紧给我讲清楚。"
    show y 恼火04 at ct with dissolve
    y "刚刚到底什么情况。"
    w "你确定？"
    show y 恼火03 at ct with dissolve
    y "废话少说。"
    w "……"
    w "就是之前跟你说的，其实从现在开始你的灵魂已经开始被诅咒侵蚀了。"
    show y 恼火02 at ct with dissolve
    y "坏消息一个接一个啊。"
    w "你别打乱我，让我先说完。"
    show y 恼火01 at ct with dissolve
    y "那你说吧。"
    w "我不太清楚具体的状况。"
    w "只不过最初的状况也只是魂不守舍这样的状态吧。"
    w "解决法我也是知道的，只要让你感觉到身体上的疼痛就能让你恢复了。"
    show y 恼火02 at ct with dissolve
    y "……"
    show y 恼火01 at ct with dissolve
    y "所以你就扇我一爪子？"
    w "所以我就扇了你一爪子。"
    show y 恐怖颜艺 at ct with dissolve
    y "呵呵…."
    w "等一下，有话好说！别拿刀别拿刀啊！"
    show y 恼火01 at ct with dissolve
    y "这次就算了，我去切点水果过来吃。"
    show y 恼火03 at ct with dissolve
    y "你要庆幸你没把我脸抓花，不然明年的这个时候就是你死掉的一周年纪念日。"
    w "……."
    w "我可是你的救命恩人啊，说话客气点行不行。"
    w "这么拽信不信我….吃光你的水果哦。"
    narrator "看到袁艳亮了亮锐利的刀子，我决定在言语上来个急转弯。"
    narrator "这个世界上注定了有些人啊，就是我惹不起的。"
    narrator "这丫头如果也是只猫的话，大概是只母老虎级别的猫——虽然这么说有点不合适，但是绝对就是这样没错的。"
    narrator "用袁艳的话来说的话——"
    narrator "——"
    w "我的直觉是不会有错的。"
    narrator "喔！我大声叫喊了起来！"
    show y 恼火01 at ct with dissolve
    y "哈？"
    w "这句话说起来还是蛮帅的嘛。"
    w "不错不错。"
    w "我会记住的。"
    show y 恼火04 at ct with dissolve
    y "你一个人自言自语在说什么鬼啊…"
    narrator "袁艳拿着一个苹果，嫌弃似的走到了桌子那边看着我说道。"
    w "……."
    narrator "我蹲在椅子上，看着袁艳。"
    narrator "总觉得有什么地方不太对。"
    show y 正常04 at ct with dissolve
    y "看什么？"
    show y 正常05 at ct with dissolve
    y "你把零食都吃得差不多了你也差不多该饱了吧。"
    w "别搞错了。"
    w "我对你切的水果一点都不感兴趣。"
    show y 正常01 at ct with dissolve
    y "噢？这样吗？"
    narrator "袁艳脸上完全写满了不信任。"
    narrator "……."
    w "真香……"
    narrator "为什么会这样呢。"
    narrator "原本是第一次有了拒绝这个女孩的勇气，第一次有了拒绝零食的心情。"
    narrator "这两个事物结合在一起应该会是双倍的快乐。"
    narrator "可是为什么呢….为什么呢？"
    narrator "为什么我会流下屈辱而兴奋的泪水呢？"
    show y 嘲笑 at ct with dissolve
    y "嘁….噢哟哟，吃得挺开心的嘛。"
    show y 嘲讽01 at ct with dissolve
    y "你在开心一点也没关系的噢。"
    w "呜呜呜….你少管我…呜呜呜。"
    show y 嘲讽03 at ct with dissolve
    y "哈哈哈哈…."
    narrator "虽然惨了点…但是这一天原本充斥在这个房间的紧张气息似乎在在这一个刻减轻了不少。"
    narrator "……."
    narrator "等一下？"
    narrator "这一天？"
    narrator "嘴里吃到一半的水果突然掉了下来。"
    show y 嘲讽05 at ct with dissolve
    y "嗯？"
    w "不对…."
    w "这不对啊！"
    show y 嘲讽04 at ct with dissolve
    y "哪里不对了？"
    w "哪里都不太对啊！"
    show y 正常05 at ct with dissolve
    y "你在说什么？"
    w "你看看这是什么时候了啊。"
    w "你昨天不是没睡觉吗？"
    show y 正常04 at ct with dissolve
    y "……."
    narrator "袁艳似乎一下子愣住了。"
    narrator "刚刚浅下去的黑眼圈似乎又加深了。"
    narrator "袁艳忍不住扶了扶额头。"
    show y 恼火02 at ct with dissolve
    y "我说你啊…这种时候就不要想那么多…."
    show y 恼火01 at ct with dissolve
    y "好好吃你的水果不行?"
    w "…."
    w "那我不管你了，我要去睡了。"
    narrator "这话好像曾经出现过来着。"
    show y 正常01 at ct with dissolve
    y "随便你。"
    narrator "看了一眼打开电视的袁艳，我踩着步子回到了房间。"
    narrator "蜷缩在窝里头准备睡觉。"
    narrator "我倒不是很担心袁艳那丫头。"
    narrator "因为她想睡的时候自然就会去睡了。"
    narrator "这么想着我就是闭上了眼睛。"
    narrator "可是之前的袁艳不是超级想睡吗？"
    narrator "后来还不是莫名其妙就起来了。"
    w "……."
    narrator "好吧，我也只能效仿一下好了。"

    nvl clear
    nvl hide
    window hide Dissolve(2)
    scene black with Dissolve(2)
    
    narrator "【距离诅咒发作还剩三天】"

    #【场景：客厅】
    scene kt_白天 with dissolve:
        zoom .667
    
    show y 愤怒 at ct with dissolve
    y "这就是你通宵跟我吃光我零食的理由？"
    w "……"
    narrator "电视里头的声音传到我耳朵里头，我只感觉特别的吵。"
    w "你起码得送我一大袋薄荷了。"
    show y 恼火01 at ct with dissolve
    y "呵，我不是让你去睡觉么。"
    w "你…你少废话。"
    w "怎么说都是你的错。"
    show y 恼火05 at ct with dissolve
    y "哎，行吧行吧。"
    show y 恼火04 at ct with dissolve
    y "我晚些去买咖啡的时候顺便帮你买好了。"
    w "买咖啡？"
    show y 正常02 at ct with dissolve
    y "提神用的。"
    show y 正常01 at ct with dissolve
    y "我看下时间….emmmm"
    show y 正常04 at ct with dissolve
    y "已经五点多了啊。"
    show y 正常05 at ct with dissolve
    y "死猫…去观察一下那三个家伙吧。"
    w "……"
    w "你确定？"
    show y 正常04 at ct with dissolve
    y "确定。"
    w "你不困吗？"
    narrator "我有些迷糊地提了几个非常愚蠢的问题。"
    show y 恼火05 at ct with dissolve
    y "胸口有点闷。"
    show y 恼火04 at ct with dissolve
    y "特别困，就是睡不着。"
    w "噢…我知道了。"
    #【袁艳】（恼火03-02）
    show y angry_3_2 at ct with dissolve
    y "你话怎么那么多啊，赶紧去看看她们啦。"
    w "好吧好好，那你打算先看看谁？"
    show y 恼火01 at ct with dissolve
    y "你怎么每次都要问这么明显的问题啊。"
    show y 恼火02 at ct with dissolve
    y "你要问谁的话，那当然是——"

    menu:
        "林琴":
            jump c2_c2_l
            
        "夏静":
            jump c2_c2_x
            
        "程祎琳":
            jump c2_c2_c

label c2_c2_l:

    $_dismiss_pause = False
    
    $c2_c2_l_select = True

    show y 恼火02 at ct with dissolve
    y "那当然是林琴啊。"
    show y 正常02 at ct with dissolve
    y "不如说除了她我实在是想不到别的谁。"
    w "我说你啊。"
    w "对她你还真是情有独钟啊。"
    w "该不是看上她了吧。"
    show y 正常01 at ct with dissolve
    y "啊？"
    show y 恼火02 at ct with dissolve
    y "为什么我非得看上她不可啊？"
    w "啥？"
    show y 恼火01 at ct with dissolve
    y "我可是花季少女。"
    w "花季少女是啥？"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "真不懂？"
    narrator "我摇了摇头。"
    show y 正常03 at ct with dissolve
    y "用你们的话来说就是刚好发情的雌性，这总行了吧。"
    show y 正常02 at ct with dissolve
    y "在你们的世界里头难道两头雌性也能谈恋爱吗？"
    w "懂了是懂了。"
    w "用雌性这个称呼有点…."
    show y 正常01 at ct with dissolve
    y "你饶了我吧，这已经是我能跟你描述的最好懂也是最原始的说法了。"
    narrator "我瞪大了眼睛。"
    w "好吧，在我们那边只要是彼此相爱都是会被祝福的，无关性别。"
    show y 正常04 at ct with dissolve
    y "真是开放的世界呢，不过如果那样的话。"
    show y 正常05 at ct with dissolve
    y "不能繁衍后代的话，你们种族不是会灭亡吗？"
    narrator "我仔细思考了一下。" 
    w "好像确实是这样，但是相爱难道不应该被祝福吗？"
    w "种族的命运难道比彼此相爱更重要吗？"
    show y 正常03 at ct with dissolve
    y "还真是偏激发言。"
    show y 正常04 at ct with dissolve
    y "那你自己呢？"
    w "我吗？"
    w "嗯…不太明白。"
    w "我暂时还不知道相爱是什么东西。"
    w "可能是因为我还没到发情期吧。"
    #【袁艳】（正常03-正常01）
    show y normal_3_1 at ct with dissolve
    y "这….这样啊，算了，开始观察吧。"
    w "噢，忍着点，稍微有点疼。"
    show y 正常03 at ct with dissolve
    y "放心，早就习惯了…."
    narrator "没有理会袁艳，而是静静地开始引导体内的力量。"
    show y 愤怒 at ct with dissolve
    y "这种东西怎么习惯得了啊！！！"
    narrator "然后惨叫着的袁艳就去林琴那边去了。"
    narrator "我当然也跟了过去。"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：街道】
    scene street_白天 with dissolve:
        zoom .667
    
    w "唉…."
    show y 正常02 at ct with dissolve
    y "为啥叹气啊？"
    w "总感觉什么地方使不上劲了。"
    show y 正常01 at ct with dissolve
    y "这样啊。"
    narrator "袁艳仔细地看了看我，然后认真地说道。"
    show y 笑容01 at ct with dissolve
    y "可能是肾亏了吧。"
    w "啊？是这样吗？"
    show y 嘲笑 at ct with dissolve
    y "大….大概吧。"
    w "原来这是肾虚吗？"
    w "既然你知道是肾虚那你一定有办法解决的吧。"
    show y 开心 at ct with dissolve
    y "啊哈哈哈…咦？林琴怎么不在医院？"
    show y 正常04 at ct with dissolve
    y "这家伙又从医院里头跑出来了？"
    w "看看也知道吧。"
    w "所以解决肾虚的办法是什么？"
    narrator "但是不知道为什么袁艳却回避了我的问题，眼睛笔直地看着林琴。"
    narrator "看起来她非常的惊讶，也不知道是真的还是假装的。"
    narrator "反正我是一点都不惊讶的…."
    narrator "正如我们所看到的。"
    narrator "林琴穿着和昨天一样的便服，在清早微微亮的大街上走着。"
    show y 正常04 at ct with dissolve
    y "问题是…她这一大早是要干什么？"
    w "跟着她不就知道了？"
    show y 正常05 at ct with dissolve
    y "有道理。"
    narrator "于是似曾相识的跟踪再一次展开。"
    show y 正常03 at ct with dissolve
    y "……."
    show y 正常01 at ct with dissolve
    y "死猫，你不觉得有什么不对吗？？"
    w "啊？？"
    w "你在说啥？"
    show y 恼火02 at ct with dissolve
    y "你看她啊，她去的方向啊。"
    narrator "我看了看林琴走动的方向。"
    w "怎么了？"
    show y 恼火01 at ct with dissolve
    y "哈，你是真不懂还是假不懂啊。"
    w "……."
    show y 恼火01 at ct with dissolve
    y "那是我们家的方向啊。"
    w "这有什么吗？"
    w "啊？"
    w "她…不会吧…她她她怎么又…."
    show y 恼火05 at ct with dissolve
    y "我怎么知道啊！！！"
    show y 恼火04 at ct with dissolve
    y "在拐几个弯她就要到了！"
    show y 愤怒 at ct with dissolve
    y "快！快回去！"
    w "噢噢噢噢！"
    narrator "虽然不知道是什么紧急情况，总之我还是先按照袁艳说的做好了。"
    narrator "很快袁艳就被我又送了回去。"
    w "……."
    narrator "最近总觉得观察她们的时间越来越少，现实中的接触趋势倒是越来越多了。"
    narrator "之前提出观察的可是她啊。"
    narrator "真让猫头大。"
    w "咦？"
    narrator "正当我准备也回去的时候，却看见了一个十分不可思议的场景。"
    
    jump c2_c2

label c2_c2_x:

    $_dismiss_pause = False

    $c2_c2_x_select = True

    show y 恼火02 at ct with dissolve
    y "怎么想也只有她了吧。"
    w "谁啊？"
    show y 正常02 at ct with dissolve
    y "夏静咯。"
    w "你不会是爱上她了吧。"
    show y 正常01 at ct with dissolve
    y "啊？"
    show y 恼火01 at ct with dissolve
    y "为什么我非得爱上她不可啊？"
    w "不是这样子的吗？"
    show y 恼火02 at ct with dissolve
    y "我可是花季少女。"
    w "花季少女是啥？"
    show y 正常02 at ct with dissolve
    y "真不懂？"
    narrator "我摇了摇头。"
    #【袁艳】（正常03-01）
    show y normal_3_1 at ct with dissolve
    y "用你们的话来说就是雌性，这总行了吧。"
    show y 正常01 at ct with dissolve
    y "在你们的世界里头难道两头雌性也能谈恋爱吗？"
    w "懂了是懂了。"
    w "用雌性这个称呼有点…."
    show y 嘲笑 at ct with dissolve
    y "你饶了我吧，这已经是我能跟你描述的最好懂也是最原始的说法了。"
    narrator "我瞪大了眼睛。"
    w "好吧，在我们那边只要是彼此相爱都是会被祝福的，无关性别。"
    show y 正常04 at ct with dissolve
    y "哇…."
    show y 正常04 at ct with dissolve
    y "那还真是开放的世界。"
    show y 正常01 at ct with dissolve
    y "不过不能繁衍后代的话，你们种族不是会灭亡吗？"
    narrator "我仔细思考了一下。" 
    w "好像确实是这样，但是相爱难道不应该被祝福吗？"
    w "种族的命运难道比彼此相爱更重要吗？"
    w "更何况我们种族也没有几个同性相爱的，相杀倒是有不少。"
    show y 嘲讽04 at ct with dissolve
    y "你们种族还真是恐怖啊，虽然更可怕的是你偏激的发言。"
    show y 嘲讽01 at ct with dissolve
    y "那你自己呢？"
    w "我吗？"
    w "嗯…不太明白。"
    w "我暂时还不知道相爱是什么东西。"
    w "彼此厮杀我倒是很清楚。"
    #none lh
    y "……."
    show y 正常04 at ct with dissolve
    y "这….这样啊，算了，开始观察吧。"
    w "噢，忍着点，稍微有点疼。"
    show y 正常03 at ct with dissolve
    y "放心，早就习惯了…."
    narrator "没有理会袁艳，而是静静地开始引导体内的力量。"
    show y 恼火01 at ct with dissolve
    y "……"
    show y 愤怒 at ct with dissolve
    y "这种东西怎么习惯得了啊！！！"
    narrator "然后惨叫着的袁艳就去夏静那边去了。"
    narrator "我当然也跟了过去。"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667
    
    w "唉…."
    show y 正常02 at ct with dissolve
    y "为啥叹气啊？"
    w "总感觉什么地方使不上劲了。"
    show y 正常01 at ct with dissolve
    y "这样啊。"
    narrator "袁艳仔细地看了看我，然后认真地说道。"
    show y 笑容01 at ct with dissolve
    y "可能是肾亏了吧。"
    w "啊？是这样吗？"

    show y 嘲笑 at ct with dissolve
    y "大….大概吧。"
    w "原来这是肾虚吗？"
    w "既然你知道是肾虚那你一定有办法解决的吧。"
    show y 正常04 at ct with dissolve
    y "啊哈哈哈…咦？为什么又是这里。 "
    show y 正常05 at ct with dissolve
    y "这家伙难道是住河边的吗？"
    w "看看也知道吧。"
    w "所以解决肾虚的办法是什么？"
    narrator "但是不知道为什么袁艳却回避了我的问题，眼睛笔直地看着夏静。"
    narrator "看起来她非常的惊讶，也不知道是真的还是假装的。"
    narrator "反正我是一点都不惊讶的…."
    narrator "正如我们所看到的。"
    narrator "夏静穿着和昨天一样的便服，伫立在河边，就像假的一样。。" 
    show y 正常02 at ct with dissolve
    y "问题是…她这一大早是要干什么？观察谁吗？程祎琳难道在附近？"
    hide y with dissolve
    narrator "但是周围一个人都没有。"
    show x 考虑02 at ct with dissolve
    x "嗯？"
    narrator "而就在这个时候夏静却朝着我们的方向投来了视线。"
    narrator "虽然明知道她是看不见我们的——我这么确信着。"
    narrator "但是她看过来的时候总是让我有点感觉心惊肉跳。"
    narrator "我看了看袁艳，也不知道她怎么想。"
    hide x with dissolve
    narrator "夏静笑了笑，然后离开了这个地方。"
    show y 正常04 at ct with dissolve
    y "她要去哪里？"
    w "……"
    w "跟着她不就知道了？"
    show y 正常05 at ct with dissolve
    y "有道理。"
    narrator "于是似曾相识的跟踪再一次展开。"
    show y 正常03 at ct with dissolve
    y "……."
    show y 正常02 at ct with dissolve
    y "死猫，你不觉得有什么不对吗？？"
    w "啊？？"
    w "你在说啥？"
    show y 恼火01 at ct with dissolve
    y "你看她啊，她去的方向啊。"
    narrator "我看了看夏静走动的方向。"
    w "怎么了？"
    show y 恼火03 at ct with dissolve
    y "哈，你是真不懂还是假不懂啊。"
    w "……."
    show y 不爽01 at ct with dissolve
    y "那是我们家的方向啊。"
    w "这有什么吗？"
    w "啊？"
    w "你的…你的意思她要去…."
    show y 不爽02 at ct with dissolve
    y "我怎么知道啊！！！"
    show y 恼火01 at ct with dissolve
    y "在拐几个弯她就要到了！"
    show y 愤怒 at ct with dissolve
    y "快！快回去！"
    w "噢噢噢噢！"
    narrator "虽然不知道是什么紧急情况，总之我还是先按照袁艳说的做好了。"
    narrator "很快袁艳就被我又送了回去。"
    w "……."
    narrator "最近总觉得观察她们的时间越来越少，现实中的接触趋势倒是越来越多了。"
    narrator "之前提出观察的可是她啊。" 
    narrator "这到底算是好现象还是坏现象呢。"
    narrator "真让猫头大。"
    w "咦？"
    narrator "正当我准备也回去的时候，却看见了一个十分不可思议的场景。"

    jump c2_c2

label c2_c2_c:

    $_dismiss_pause = False

    $c2_c2_c_select = True

    show y 正常04 at ct with dissolve
    y "总觉得放心不下那个小丫头。"
    w "谁啊？"
    show y 正常01 at ct with dissolve
    y "程祎琳咯。"
    #【袁艳】（正常03-02）
    show y normal_3_2 at ct with dissolve
    y "你看她呆的样子。"
    w "虽然也有这方面的原因。"
    w "不过你不会是喜欢上她了吧。"
    show y 正常05 at ct with dissolve
    y "可能有点吧，不过不是那种喜欢哦。"
    show y 正常04 at ct with dissolve
    y "要说的话应该是有点担心吧。"
    w "噢欸？"
    narrator "我有点不太懂地歪了歪脑袋。"
    show y 恼火01 at ct with dissolve
    y "再说了我可是花季少女。"
    w "花季少女是啥？"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "真不懂？"
    narrator "我摇了摇头。"
    show y 正常03 at ct with dissolve
    y "用你们的话来说就是刚好发情的雌性，这总行了吧。"
    show y 正常02 at ct with dissolve
    y "在你们的世界里头难道两头雌性也能谈恋爱吗？"
    w "懂了是懂了。"
    w "用雌性这个称呼有点…."
    show y 正常01 at ct with dissolve
    y "你饶了我吧，这已经是我能跟你描述的最好懂也是最原始的说法了。"
    narrator "我瞪大了眼睛。"
    w "好吧，在我们那边只要是彼此相爱都是会被祝福的，无关性别。"
    show y 正常04 at ct with dissolve
    y "真是开放的世界呢，不过如果那样的话。"
    show y 正常05 at ct with dissolve
    y "不能繁衍后代的话，你们种族不是会灭亡吗？"
    narrator "我仔细思考了一下。"
    w "好像确实是这样，但是相爱难道不应该被祝福吗？"
    w "种族的命运难道比彼此相爱更重要吗？"
    show y 正常03 at ct with dissolve
    y "还真是偏激发言。"
    show y 正常04 at ct with dissolve
    y "那你自己呢？"
    w "我吗？"
    w "嗯…不太明白。"
    w "我暂时还不知道相爱是什么东西。"
    w "可能是因为我还没到发情期吧。"
    #【袁艳】（正常03-正常01）
    show y normal_3_1 at ct with dissolve
    y "这….这样啊，算了，开始观察吧。"
    w "噢，忍着点，稍微有点疼。"
    show y 正常03 at ct with dissolve
    y "放心，早就习惯了…."
    narrator "没有理会袁艳，而是静静地开始引导体内的力量。"
    show y 愤怒 at ct with dissolve
    y "这种东西怎么习惯得了啊！！！"
    narrator "然后惨叫着的袁艳就去程祎琳那边去了。"
    narrator "我当然也跟了过去。"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：家门口】
    scene door_白天 with dissolve:
        zoom .667
    
    #show c 斜视01 at ct with dissolve
    #c "嗯？"
    w "唉…."
    #show c 斜视01:
    #    linear .3 xpos 1.0 xanchor 1.0
    show y 正常02 at ct with dissolve
    y "为啥叹气啊？"
    w "总感觉什么地方使不上劲了。"
    show y 正常01 at ct with dissolve
    y "这样啊。"
    narrator "袁艳仔细地看了看我，然后认真地说道。"
    show y 笑容01 at ct with dissolve
    y "可能是肾亏了吧。"
    w "啊？是这样吗？"

    show y 嘲笑 at ct with dissolve
    y "大….大概吧。"
    w "原来这是肾虚吗？"
    w "既然你知道是肾虚那你一定有办法解决的吧。"
    show y 正常05 at ct with dissolve
    y "她在干嘛呢？"
    w "看看也知道吧。"
    w "所以解决肾虚的办法是什么？"
    show y 嘲笑 at ct with dissolve
    y "……"
    w "……"
    narrator "我们两个的对话还真是空虚啊。"
    show y 不爽01 at ct with dissolve
    y "这家伙怎么就在我们家门口啊！！！！"
    narrator "反正我是一点都不惊讶的…."
    narrator "正如我们所看到的。"
    narrator "程祎琳穿着和昨天一样的便服，歪着脑袋很疑惑地站在袁艳家的门口。"
    w "怎么了？"
    show y 愤怒 at ct with dissolve
    y "哈，你是真不懂还是假不懂啊。"
    w "……."
    show y 恼火01 at ct with dissolve
    y "她现在在我们家里门口啊！"
    narrator "袁艳指着门口的程祎琳这么说道。"
    w "这有什么吗？"
    w "啊？"
    w "你的…你的意思她？？？"
    show y 恼火02 at ct with dissolve
    y "我怎么知道啊！！！"
    show y 愤怒 at ct with dissolve
    y "快！快回去啊！"
    w "噢噢噢噢！"
    narrator "虽然不知道是什么紧急情况，总之我还是先按照袁艳说的做好了。"
    narrator "很快袁艳就被我又送了回去。"
    w "……."
    narrator "最近总觉得观察她们的时间越来越少，现实中的接触趋势倒是越来越多了。"
    narrator "之前提出观察的可是她啊。"
    narrator "这到底算是好现象还是坏现象呢。"
    narrator "真让猫头大。"
    w "咦？"
    narrator "正当我准备也回去的时候，却看见了一个十分不可思议的场景。"
    
    jump c2_c2


label c2_c2:

    $_dismiss_pause = False

    $c2_c2_select = True
    
    nvl clear
    nvl hide
    window hide dissolve
    #【场景：房间】
    scene room_白天 with dissolve:
        zoom .667
    
    w "不是吧？她们仨？剧本是不是搞错了啊？？"
    narrator "就在我惊叹的时候，袁艳皱着眉头出现在我的视野里头。"
    #【袁艳】（恼火03-02）
    show y angry_3_2 at ct with dissolve
    y "她们就在门外。"
    show y 恼火02 at ct with dissolve
    y "情况很惨。"
    show y 恼火01 at ct with dissolve
    y "应该是在等我起床。"
    w "……"
    w "你确定？"
    show y 恼火05 at ct with dissolve
    y "啊？"
    narrator "袁艳像是看傻子一样看了我一眼。"
    show y 恼火04 at ct with dissolve
    y "你自己去门那里确定吧。"
    w "好吧好吧，那你打算怎么办？"
    show y 嘲讽01 at ct with dissolve
    y "要不….咱们装作不知道？"
    narrator "我看了看窗外的天空。"
    narrator "然后伸出了爪子。"
    w "我觉得没问题。"
    show y 开心 at ct with dissolve
    y "我也觉得完全没有问题。"
    narrator "袁艳眯了眯眼握住了我的爪子，仿佛达成了什么共识。"
    narrator "……."
    narrator "任凭是谁，放任三个少女在自己门口伫立着多少还是会有些不安的。"
    narrator "就算是我，也稍微有那么一点点吧。"
    narrator "就那么一点点。"
    w "我说袁艳…从刚刚开始你就一直在看门那里干什么？"
    show y 正常01 at ct with dissolve
    y "看看而已，怎么了？"
    w "……."
    show y 正常02 at ct with dissolve
    y "过了多久了？"
    w "到现在才十分钟而已。"
    show y 正常04 at ct with dissolve
    y "她们到底是想干什么啊？"
    w "我才想问你到底想干什么呢。"
    show y 正常05 at ct with dissolve
    y "要不咱们再去观察她们吧？ "
    w "你不是疯了吧，她们就在门外啊。"
    show y 正常02 at ct with dissolve
    y "那有什么嘛，反正她们也没敲门不是吗？"
    show y 正常04 at ct with dissolve
    y "再说了，你就不好奇那三个神经病聚在我门口干什么吗？"
    w "……."
    narrator "我总觉得现在的你更像是个神经病。"
    narrator "不过我也很好奇，在没有袁艳这个维系点存在的时候。"
    narrator "那三个定时炸弹会迸发出什么火花呢？"
    w "好吧，那就去观察看看？"
    show y 正常05 at ct with dissolve
    y "嗯。"
    w "那么选择题来了，你打算选哪一个看呢？"
    show y 正常01 at ct with dissolve
    y "都在门外有啥意义嘛，选谁不是都可以吗？"
    w "虽然现在差不多就是这样子啦。"
    w "反正我这么做也是有意义的，之后你就知道了。"
    w "快——选择吧！是——"

    menu:
        "程祎琳":
            jump c2_c3_c
            
        "夏静":
            jump c2_c3_x
            
        "林琴":
            jump c2_c3_l

label c2_c3_c:

    $_dismiss_pause = False
    
    $c2_c3_c_select = True

    show y 嘲讽01 at ct with dissolve
    y "好吧，那你没办法。"
    show y 正常05 at ct with dissolve
    y "就选程祎琳吧。"
    show y 正常04 at ct with dissolve
    y "不是一样的吗，这个时候选谁不都是一样么。"
    w "你懂个屁啊。"

    jump c2_c3

label c2_c3_x:

    $_dismiss_pause = False

    $c2_c3_x_select = True

    show y 嘲讽01 at ct with dissolve
    y "好吧，那你没办法。"
    show y 正常05 at ct with dissolve
    y "就选夏静吧。"
    show y 正常04 at ct with dissolve
    y "不是一样的吗，这个时候选谁不都是一样么。"
    w "你懂个屁啊。"
    
    jump c2_c3

label c2_c3_l:

    $_dismiss_pause = False

    $c2_c3_l_select = True

    show y 嘲讽01 at ct with dissolve
    y "好吧，那你没办法。"
    show y 正常05 at ct with dissolve
    y "就选林琴吧。"
    show y 正常04 at ct with dissolve
    y "不是一样的吗，这个时候选谁不都是一样么。"
    w "你懂个屁啊。"
    
    jump c2_c3

label c2_c3:

    $_dismiss_pause = False

    $c2_c3_select = True

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：街道】
    scene street_gj with dissolve:
        zoom .667
    
    narrator "实际上…现实可能往往会出乎我们的意料之外。"
    narrator "原本我和袁艳的预想基本都是三个人会吵成什么样子。"
    narrator "毕竟…她们之前在袁艳家里的时候那表现…."
    show y 正常04 at ct with dissolve
    y "不过还是怎么也不敢信她们居然会这么安静啊。"
    w "是啊。"
    narrator "有点让猫跟人都很惊讶。"
    
    nvl clear
    nvl hide
    window hide dissolve
    scene door_白天 with dissolve:
        zoom .667

    show l 不满08 at rt with dissolve
    pause .3
    show c 注视02 at ct with dissolve
    pause .3
    show x 考虑02 at lt with dissolve
    pause .3
    narrator "三个女孩像是彼此割据一样站在袁艳家门的三个方向上。"
    narrator "林琴拿着自己的手机不停地稍微像是有点烦躁地刷着。"
    narrator "夏静安安静静地坐在一旁花园的台阶上看着书，尽管光线有点不太好。"
    narrator "程祎琳直接干脆就伫立在袁艳的家门口，看样子似乎是在发呆。"
    narrator "完全让人想不通这三个丫头在干什么。"
    
    nvl clear
    nvl hide
    window hide dissolve

    scene street_gj with dissolve:
        zoom .667
        
    show y 正常05 at ct with dissolve
    y "不过这么看起来，感觉是她们没带钥匙回不了家一样。"
    show y 正常04 at ct with dissolve
    y "可是这里是我家啊！"
    w "……"
    narrator "跟我之前随口的猜测完全吻合了起来。"
    narrator "所以在这个时候，我大胆地做了一个猜想。"
    narrator "这三个人的关系其实是真的维系在袁艳身上的。"
    narrator "如果缺乏了袁艳这个女孩。"
    narrator "想到了这里我看了看困扰得跟炸了毛一样的袁艳，又看了看互相割据的三人组。"
    narrator "或许就会变成这样吧。"
    w "要不咱们回去吧，这么观察也没有用啊。"
    show y 正常02 at ct with dissolve
    y "等一下。"
    narrator "然而就在这个时候。"
    narrator "原本安静在看书的夏静却突然抬起了头。"
    narrator "漫不经心地朝着我们看了过来。"
    narrator "袁艳认真地看着她。"
    narrator "这么看起来，我们就像跟她在彼此对视一样。"
    narrator "原本这并没有什么….之前也应该有过的。"
    narrator "然而就在这个时候，在一旁很烦躁的林琴也抬起了头。"
    narrator "似乎是注意到夏静的奇特之处，顺着她的视线也朝我们投来了目光。"
    narrator "至于程祎琳….不知道什么时候也朝着我们看了过来。"

    show y 无措 at ct with dissolve
    y "……."
    w "……."
    show y 嘲笑 at ct with dissolve
    y "喂，死猫。"
    show y 嘲讽02 at ct with dissolve
    y "我们不会是给看到了吧？"
    w "这不可能！"
    narrator "我振振有词地叫到。"
    w "现在我们的状态，凭你们人类的眼睛是绝对看不到的！"
    w "不信我证明给你看！！！"
    narrator "为了证明给袁艳这丫头看，我决定用自己的身体去尝试。"
    narrator "于是我刷刷地就跑到了夏静面前。"
    show y 嘲讽04 at ct with dissolve
    y "你在干嘛？"
    w "看好了！"
    show y 嘲讽05 at ct with dissolve
    y "噗….你这是？？？"
    narrator "然后我就在这个丫头面前卖弄身姿。"
    narrator "正确的说法就是在跳舞。"
    narrator "而且还跳得很夸张。"
    narrator "如果她看得到我的话我就不信她会无动于衷。"
    narrator "证据就是我身后笑得跟傻子一样的袁艳。"
    show y 开心 at ct with dissolve
    y "哈哈哈哈哈，你在哪里瞎扭啥…哈哈哈！！"
    w "你少废话，我这是在证明给你看。"
    w "你看，她们根本就看不到我们。"
    w "你看你看！！"
    show y 开心 at ct with dissolve
    y "哈哈哈….啊？"
    show y 嘲讽05 at ct with dissolve
    y "……"
    narrator "就在我得意的时候，袁艳的笑声却嘎然而止。"
    w "怎么？"
    
    #【CG：两个世界的守望】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_2wsw = True
    scene cg_两个世界的守望 with Dissolve(2)
    
    pause 1.0
    
    narrator "夏静有些恍惚地朝着我伸出了手。"
    narrator "尽管没有真正意义上地触碰到我。"
    narrator "可是…."
    narrator "我呆呆地看着夏静，明明是两个世界….为什么她？？"
    narrator "难道她要死了？"
    narrator "不对，她还活得好好的，也没有死亡的气息。"
    narrator "那她是怎么发现我的？"
    narrator "这不可能啊？"
    narrator "难道…难道？"
    w "……"
    narrator "我愣愣地回头看了跟我一样甚至比我还要吃惊的袁艳。"
    w "袁艳，我....."
    #none lh
    y "……."
    narrator "袁艳愣着点了点头。"
    narrator "我回过头，夏静依旧伸着手，可是眼睛却没有完全焦点。"
    narrator "看着这样的夏静，我带着袁艳消失在这里。"
    narrator "在消失的瞬间，我似乎很明显看到了，那个名字叫做夏静的女孩无比惊愕的表情。"
    narrator "……."
    
    nvl clear
    nvl hide
    window hide dissolve
    #（视角 转变——夏静）

    scene street_gj with dissolve:
        zoom .667

    narrator "不见了？"
    narrator "那两个影子消失了。"
    show l 普通07 at ct with dissolve
    l "你在看什么鬼？"
    w "……"
    narrator "我不知道，可能它们两个真的就是什么鬼吧。"
    w "没什么，只是跟自己另一个世界的朋友在打招呼而已。"
    show l 普通08 at ct with dissolve
    l "你不会是脑袋坏了吧？"
    w "彼此彼此。"
    narrator "我虽然不明白发生了什么，但是总觉得….有些怅然若失。"
    narrator "如果它们就这样永远消失的话，搞不好我也会很难过。"
    narrator "毕竟对于我来说，它们可能真的就是我另一个世界的朋友也说不定呢。"
    w "呵呵呵…."
    narrator "对于有这样想法的我，我只能苦笑了起来。"

    #（视角转变——主线 猫）
    #【场景：房间】

    nvl clear
    nvl hide
    window hide dissolve
    scene room_白天 with dissolve:
        zoom .667
        
    w "呼呼…呼。"
    narrator "我喘着气，尽管之前没有做过任何激烈的运动。"
    narrator "总感觉精神上的压力压得我有些喘不过气来。"
    show y 正常04 at ct with dissolve
    y "来，喝口水，别呛着了。"
    w "我…我喵~~"
    w "这事…."
    narrator "连句完整的话都说不出来。"
    show y 正常05 at ct with dissolve
    y "哈…想不到世界上还真存在这种人。"
    w "你在….说什么？"
    w "外面那个…那个叫夏静的可是能看到我们灵魂状态的啊！！"
    narrator "我说出了连自己都不信的话，但是这个是事实。"
    show y 正常02 at ct with dissolve
    y "啊？是吗？"
    w "你为什么还能这么淡定啊啊喂？"
    #【袁艳】（正常03-02）
    show y normal_3_2 at ct with dissolve
    y "我当然淡定咯。"
    show y 正常01 at ct with dissolve
    y "只不过是被看到而已，至于那么大惊小怪吗？"
    w "……"
    w "你当然觉得没什么啊。"
    show y 正常03 at ct with dissolve
    y "被看到了你也没有什么损失啊。"
    show y 正常02 at ct with dissolve
    y "大不了坦白呗。"
    w "你这么说….咦，好像是没有损失来着。"
    show y 正常05 at ct with dissolve
    y "对吧。"
    w "但是坦白是绝对不能坦白的，会出事的。"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "开个玩笑啦。"
    show y 正常01 at ct with dissolve
    y "我觉得，夏静她确实是看到我们了。"
    w "都这时候了你还在说什么啊？"
    narrator "我有些抓狂地抓住自己的脑袋。"
    show y 正常02 at ct with dissolve
    y "但是她应该没看出是我们才对？"
    show y 正常01 at ct with dissolve
    y "死猫，你之前就说了，我们这是以灵魂的状态去观察她们不是吗？"
    w "是…啊？"
    narrator "我有些不明白袁艳这个时候还在讲什么东西。"
    show y 正常04 at ct with dissolve
    y "死猫…"
    show y 正常05 at ct with dissolve
    y "你知道吗？"
    w "我知道什么？"
    show y 正常04 at ct with dissolve
    y "这个世界上就是有一种人可以看见灵魂的存在。"
    w "……"
    narrator "我还以为什么呢。"
    narrator "不过就是可以看见灵魂的存在嘛…."
    w "……"
    w "什么….什么？？？"
    w "竟然有人类可以看到灵魂的存在？"
    show y 恼火04 at ct with dissolve
    y "你怪叫什么？"
    show y 恼火05 at ct with dissolve
    y "这种事情在我们人类的世界里头又不是什么稀奇的事情。"
    w "……."
    w "可是…可是你说的是你们人类可以看见灵魂啊。"
    show y 恼火02 at ct with dissolve
    y "我也是稍微吃了一惊。"
    show y 恼火01 at ct with dissolve
    y "后来仔细想想觉得也没什么。"
    show y 恼火02 at ct with dissolve
    y "总有那么些人在这个世界上是比较特别的嘛。"
    narrator "袁艳耸了耸肩，做出了无奈的姿势。"
    narrator "可是我却总觉得有哪里不对。"
    w "不对…."
    show y 正常01 at ct with dissolve
    y "怎么了？"
    narrator "很早以前就想说了。"
    w "这完全是你适应能力太强了吧！！！！"
    y "……."
    w "被诅咒也是，知道我会说话也是…."
    show y 俏皮 at ct with dissolve
    y "诶呀。"
    narrator "袁艳摆了摆手，怪不好意思地笑着。"
    show y 开心 at ct with dissolve
    y "这种事情就不要说出来啦，我也知道我挺厉害的。"
    w "大姐，我没有夸你啊！"
    narrator "我无奈地抹了抹眼睛。"
    show y 笑容01 at ct with dissolve
    y "不过这也是没办法的事情嘛。"
    show y 开心 at ct with dissolve
    y "就算我不去适应也没办法去改变这个事实呀。"
    narrator "袁艳又耸了耸肩，做出了无奈的姿势。"
    narrator "但是眼睛却并没有看着我，仿佛看向更远的地方一般。"
    w "……."
    w "额…."
    narrator "一时之间我反而不知道该说什么。"
    show y 开心 at ct with dissolve
    y "怎么样？"
    w "啊？"
    w "什么怎么样？"
    show y 笑容02 at ct with dissolve
    y "当然是我刚刚的样子啊。"
    show y 开心 at ct with dissolve
    y "是不是像极了一个有故事的女人？"
    w "……."
    narrator "看着她突然莫名其妙的得意，似乎某种气氛被瞬间打破。"
    narrator "我现在只想一爪子直接朝着她脸呼过去。"
    narrator "但是想到之前的捆绑…."
    narrator "还是算了吧。"
    narrator "让她得意我也安生不少。"
    w "像…像极了。"
    show y 俏皮 at ct with dissolve
    y "那肯定，哼哼。"
    w "所以你打算把外边那三只晾到什么时候？"
    show y 正常05 at ct with dissolve
    y "…."
    show y 正常04 at ct with dissolve
    y "这还真是个开心不起来的话题啊。"
    narrator "说道这里，袁艳看了看时间——指针指着某个数字的位置。"
    show y 正常01 at ct with dissolve
    y "闹腾了这么久都还没到七点。"
    show y 正常02 at ct with dissolve
    y "正常上班时间可都是八点啊。"
    show y 正常04 at ct with dissolve
    y "我这么早上班有加班费吗？"
    w "你在说啥？"
    show y 正常04 at ct with dissolve
    y "……"
    show y 正常02 at ct with dissolve
    y "没啥，就是到底还是想不通她们到底在想些什么。"
    show y 正常03 at ct with dissolve
    y "女人心海底针啊。"
    w "……."
    narrator "这点我还是同意的…毕竟我面前的这个家伙就是活生生的例子。"
    narrator "有时候我都会想这死丫头究竟脑子里头装的是什么东西。"
    w "要是能劈开来看看就好了。"
    show y 正常01 at ct with dissolve
    y "你说什么？"
    w "……"
    w "我是说真想知道那三个丫头到底在想些什么东西。"
    show y 正常04 at ct with dissolve
    y "就是啊。"
    show y 正常03 at ct with dissolve
    y "先让我想想该怎么去对付这三个人吧。"
    show y 正常04 at ct with dissolve
    y "这么来可不是办法。"
    show y 正常05 at ct with dissolve
    y "总不能今天又让她们几个窝在我家里吧。"
    narrator "时间一点一点的过去，紧皱着眉头的袁艳却开始打起吨来了。"
    w "……."
    narrator "按照道理我这个时候应该放她让她好好休息一下才是。"
    narrator "然而就在这个时候…."
    narrator "她却睁开了眼睛，两只眼睛里头充满了血丝。"
    hide y with Dissolve(7)
    #【袁艳立绘渐渐消失】
    narrator "这个女孩愣愣地看着我——迷茫、无助……"
    narrator "仿佛瞬间失去了什么一般。"

    w "不是吧…这种时候。"
    narrator "看到这样子的她，我决定在呼她一巴掌。"
    narrator "于是我窜进了她的怀里，仰起头看了看她，然后又看了看自己的爪子。"
    w "也不知道还能拍醒她几次，不快点做决定的话……"
    w "……."
    narrator "就在我爪子即将落到她脸上的时候，突然有一段回忆闪过了我的脑海。"
    narrator "自从上次…其实也没过多久的捆绑之后。"
    narrator "我脑子里头就时不时回响起这些画面…."
    narrator "总觉得有什么不对，我干嘛那么惦记捆绑啊。"
    narrator "不过伸出去的爪子又收了回来。"
    w "不行，我得慎重考虑一下该拍哪里。"
    narrator "我又从袁艳的怀里跳了出来。"
    narrator "仔细地打量了发愣看着我的袁艳。"
    narrator "找起来还是挺容易的。"
    narrator "只要拍这个地方的话，一定可以让她恢复过来。"
    w "就决定是这里了！"
    narrator "找到了目标的我再一次朝着袁艳的怀里窜了过去。"
    narrator "朝着选好的地方使出了浑身的劲。"
    narrator "我甚至能够想象得到时候这家伙满嘴感谢的模样。"
    narrator "到那个时候在问问她肾虚该怎么治疗好了——"
    narrator "……."
    
    nvl clear
    nvl hide
    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with dissolve
    pause 1
    
    #【场景：房间】
    scene room_白天 with dissolve:
        zoom .667
        
    show y 恐怖颜艺 at ct with dissolve
    y "嗯，你继续说。"
    narrator "袁艳并没有多余的话语，而是笑眯眯地看着我。"
    narrator "似乎是等着我继续解释。"
    w "所以说……"
    w "心脏是人类很关键的位置，跟灵魂也是有紧密联系的。"
    narrator "我有些战栗地举着自己的爪子，跟面前这个似乎已经不讲理的女孩不停地解释着。"
    w "我这一次可没有打你的脸啊，完美地规避了那件事不是吗？"
    w "应该是皆大欢喜啊！"
    show y 颜艺02 at ct with dissolve
    y "这样啊，真是谢谢你啊！"
    narrator "她这个谢谢怎么听得我有点瘆。"
    w "…."
    w "能…能把你背后的刀藏好一点吗？"
    w "我有点怕。"
    show y 颜艺02 at ct with dissolve
    y "呵呵呵…."
    narrator "然后….然后这家伙就一刀划了过来，虽然像是在做做样子，没有真的划到我。"
    narrator "但是…这得归功于我闪得快的原因吧。"
    w "哇…"
    w "你….你干嘛！！！！"
    narrator "袁艳噙着眼泪，举着手中的刀颤抖着说着。"
    show y 恐怖颜艺 at ct with dissolve
    y "我完了….居然被你这样的…这样的猫袭击了。"
    show y 颜艺02 at ct with dissolve
    y "我已经嫁不出了…."
    w "……."
    narrator "我满脸的黑线，这都什么跟什么啊。"
    w "等一下等一下，我知道了我知道了。"
    narrator "接下来，房间里头开始混乱了起来。"
    narrator "这是一场不知道是不是亡命的追逐。"
    narrator "她拿着危险品追逐我的脚步蹒跚。"
    narrator "我真怕她一不小心摔一跤弄伤了她自己。"
    narrator "这样下去不是办法，袁艳这个丫头的情绪已经开始有些不稳定了。"
    narrator "必须得稳定一下她的情绪。"
    narrator "追溯起来的原因就是我在唤醒她的时候直接拍了她的胸？"
    narrator "不…这肯定不是重点…可恶，重点到底是什么？"
    narrator "房间里头噼里啪啦地向着各种声音。"
    narrator "几次我都被逼入绝境。"
    narrator "但是这场闹剧最终还是结束了。"
    narrator "袁艳依靠着墙坐在了木质的地板上，把刀扔到了远远的那边去了。"
    narrator "她微微地喘着气，似乎是累了。"
    narrator "我这才敢稍微靠近坐在地上的这个女孩。"
    w "那啥….你没事吧。"
    show y 不爽02 at ct with dissolve
    y "……"
    narrator "袁艳无力地看了我一眼。"
    show y 不爽01 at ct with dissolve
    y "我觉得还行。"
    w "不会发疯了？"
    show y 正常03 at ct with dissolve
    y "暂时。"
    w "好吧。"
    w "话说为什么你会说你嫁不出去了啊？"
    show y 恼火01 at ct with dissolve
    y "想我为了自己纯洁无暇的身躯艰苦奋斗了这么多年。"
    show y 不爽02 at ct with dissolve
    y "最后居然被你这只死猫捷足先登，被你这种死猫…这种死猫…."
    show y 恼火02 at ct with dissolve
    y "只是想想 我都觉得…."
    w "我只是只猫啊！"
    show y 正常02 at ct with dissolve
    y "……"
    show y 正常03 at ct with dissolve
    y "这我知道！"
    show y 正常01 at ct with dissolve
    y "你是只公的还是母的？"
    w "你听我这么可爱的声音难道还不知道我是什么性别吗？"
    narrator "袁艳看了看我，然后摇了摇头。"
    w "不会吧？"
    narrator "袁艳点了点头。"
    w "啊？"
    narrator "看她真的不知道的模样，我耳朵拉耸了下来。"
    w "我是雌性啦。"
    show y 无措 at ct with dissolve
    y "啊？"
    narrator "袁艳瞪大了眼睛。"
    show y 无措 at ct with dissolve
    y "真的假的？"
    w "我骗你干啥？"
    show y 正常04 at ct with dissolve
    y "你过来。"
    w "干啥？"
    narrator "我身体不由自主地…毫无防备地就这么过去了…."
    narrator "袁艳一把抱住了我把我举了起来——这丫头在干啥。"
    show y 嘲讽03 at ct with dissolve
    y "哇，还真是….之前都没注意到。"
    w "啊？"
    show y 嘲讽03 at ct with dissolve
    y "咳咳…."
    narrator "袁艳似乎是注意到我的疑惑，然后红着脸把我放了下来，轻咳了两声。"
    show y 嘲笑 at ct with dissolve
    y "你是母猫你就早说嘛。"
    show y 嘲讽05 at ct with dissolve
    y "我都没注意到。"
    w "你又没问，难道还怪我咯？"
    narrator "袁艳像是松了一口气一样，终于….终于露出了笑脸。"
    narrator "然而就在这个时候，敲门声响了起来。"
    narrator "袁艳的笑容顿时僵在了脸上。"
    narrator "看起来好恶心。"
    narrator "我们也没闹腾多久，表上的指针其实也就刚好转一圈而已。"
    show y 正常02 at ct with dissolve
    y "其实我就是觉得压力有点大，想疯一下而已。"
    w "…."
    show y 开心 at ct with dissolve
    y "所以刚才的行为一点意义都没有啦，诶嘿嘿…."
    w "嘿嘿你大爷啊！"
    narrator "你可是要拿刀捅我的啊，那是在开玩笑吗？"
    narrator "我看着房间，满目疮痍不忍直视。"
    show y 笑容01 at ct with dissolve
    y "不跟你闹啦，我得去陪客了。"
    narrator "真不知道这个笑嘻嘻去开门的女孩到底是怎么想的，这丫头不会是疯了吧。"
    narrator "要是这样的我….那我可怎么办啊。"
    narrator "想到这里，我不由得担忧地透过房间的门注视着前往客厅的袁艳。"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：客厅】
    scene kt_白天 with dissolve:
         zoom .667
    
    show c 侧视02 at ct with dissolve
    c "……"
    narrator "程祎琳推开了门，伸出了一个小脑袋。"
    show c 侧视02:
        linear .3 xpos 1.0 xanchor 1.0
    show y 开心 at lt with dissolve
    y "看什么，进来吧。"
    show c 侧视01 at rt with dissolve
    c "嗯。"
    show y 正常04 at lt with dissolve
    y "门敲两次就行了，敲那么多次是想把我家的门给敲破吗？"
    show y 正常04:
        linear .3 xpos 0.5 xanchor 0.5
    show l 注视07 at lt with dissolve
    l "额…."
    narrator "刚进门的林琴愣了愣，似乎不理解为什么袁艳会对着她说。"
    show y 正常04 at ct with dissolve
    y "你身后还有人吧，愣在这里干啥？"
    show l 慌张07 at lt with dissolve
    l "噢…噢噢。"
    narrator "这才反应过来，推开了门让她身后的夏静进到了客厅。"
    show y 正常04:
        linear .3 xpos .25 xanchor .25
    show l 慌张07:
        linear .3 xpos -0.08 xanchor 0.0
    show c 侧视01:
        linear .3 xpos 1.25 xanchor 1.25
    show x 考虑01 with dissolve:
        xpos .75 xanchor .75
    x "……"
    show l 普通08 with dissolve:
        xpos -0.08 xanchor 0.0
    l "……"
    narrator "夏静和林琴面面相觑，程祎琳四处搜索着。"
    narrator "看到此情此景，袁艳只是淡淡地笑了笑，仿佛已经理所应当。"
    show y 笑容01 with dissolve:
        xpos .25 xanchor .25
    y "过来坐吧。"
    narrator "林琴皱着眉头"
    show l 普通09 with dissolve:
        xpos -0.08 xanchor 0.0
    l "首先我要声明一下…"
    show l 普通08 with dissolve:
        xpos -0.08 xanchor 0.0
    l "我只是路过。"
    show l 普通07 with dissolve:
        xpos -0.08 xanchor 0.0
    l "反正我也没什么事就顺便过来看看而已。"
    show x 假笑02 with dissolve:
        xpos .75 xanchor .75
    x "……."
    narrator "夏静抿着嘴像是想笑又不能笑的样子。"
    show y 恼火02 with dissolve:
        xpos .25 xanchor .25
    y "啊…你都快把我家门都敲破了。"
    show y 恼火01 with dissolve:
        xpos .25 xanchor .25
    y "那另外两个又是怎么回事呢？"
    show y 恼火02 with dissolve:
        xpos .25 xanchor .25
    y "现在才早上八点啊。"
    show x 怜悯02 with dissolve:
        xpos .75 xanchor .75
    x "当然是来见亲爱的伙伴呀。"
    show x 怜悯01 with dissolve:
        xpos .75 xanchor .75
    x "昨晚想你想得都快睡不着了。"
    #嘲讽
    show y 嘲讽01 with dissolve:
        xpos .25 xanchor .25
    y "巧了，我也是想你想得都睡不着了。"
    show x 惊异 with dissolve:
        xpos .75 xanchor .75
    x "这…这样吗？"
    show x 惊讶02 with dissolve:
        xpos .75 xanchor .75
    x "……."
    show x 惊讶01 with dissolve:
        xpos .75 xanchor .75
    x "那我还真是个罪孽深重的女人啊。"
    show y 愤怒 with dissolve:
        xpos .25 xanchor .25
    y "喂喂喂！你别擅自理解啊！"
    narrator "袁艳的表情终于开始有些抓狂起来。"
    show y 正常02 with dissolve:
        xpos .25 xanchor .25
    y "算了，坐吧坐吧。"
    show c 斜视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……"
    narrator "夏静，林琴走到了客厅里头。"
    show x 普通02 with dissolve:
        xpos .75 xanchor .75
    x "还真是一点变化都没有啊。"
    show l 普通08 with dissolve:
        xpos -0.08 xanchor 0.0
    l "这点倒是没错呢。"
    show y 恼火02 with dissolve:
        xpos .25 xanchor .25
    y "你们醒醒啊！！！！你们昨天才刚来过这里。"
    show y 恼火01 with dissolve:
        xpos .25 xanchor .25
    y "别搞得你们好久没来过一样好不好！！"
    show c 侧视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "……."
    show y 正常02 with dissolve:
        xpos .25 xanchor .25
    y "……"
    show y 开心 with dissolve:
        xpos .25 xanchor .25
    y "小琳啊，进来呀。"
    show y 笑容01 with dissolve:
        xpos .25 xanchor .25
    y "还在门口干什么呢？"
    show c 恶心01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "我…我是因为想吃东西才过来的。"
    #嘲讽
    show y 嘲讽01 with dissolve:
        xpos .25 xanchor .25
    y "啊…这个不用你说啦。"
    show c 注视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "因为…因为你刚刚没有问我。"
    narrator "我看着袁艳的表情，大概就读懂了——‘就算你不说我也知道啦’。"
    
    nvl clear
    nvl hide
    window hide dissolve
    #【场景；黑屏】
    scene black with Dissolve(.7)
    
    narrator "我不由得抹了抹眼睛。"
    narrator "嘛…不知道为什么看到这样子的场景…"
    narrator "我倒是反而安心了。"
    narrator "其实这样下去倒也没什么不好。"
    
    nvl clear
    nvl hide
    window hide dissolve
    #【场景：客厅】
    scene kt_白天 with dissolve:
        zoom .667
    
    narrator "不由得这样感叹了起来。"
    narrator "看来猫上了年纪就会变得很惆怅呢。"
    narrator "看着不知道在跟那三个丫头一本正经地说些什么的袁艳。"
    narrator "就好像在看自己的女儿跟朋友聚在一起一样。"
    w "……"
    narrator "然后我一头撞到了墙上。"
    narrator "我还这么年轻啊！"
    narrator "我到底在乱七八糟想什么鬼啊，而且我跟那死丫头根本就不是同一种生物。"
    narrator "为什么会想到她是我女儿啊！！！"
    narrator "对着这样的自己，莫名其妙地无语了起来。"
    narrator "肯定是因为昨晚没睡好的原因。"
    narrator "不过那丫头好像已经两天没有睡觉了。"
    narrator "她还能撑得住么？"
    narrator "有点担心的我猫着步子凑了过去。"
    show y 不爽01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "所以说你们仨今天是特意来我这里捣乱的麼？"
    show l 不满09 with dissolve:
        xpos .25 xanchor .25
    l "简直胡说八道，本小姐需要到你这里来捣乱吗？"
    show l 不满07 with dissolve:
        xpos .25 xanchor .25
    l "你别给我捣乱就行。"
    show x 反驳03 with dissolve:
        xpos .75 xanchor .75
    x "哦豁？大小姐到底是大小姐。"
    show x 反驳02 with dissolve:
        xpos .75 xanchor .75
    x "霸占人家的地盘反而说人家捣乱。"
    show y 恼火01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你也好不到哪里去吧。"
    show x 惊讶02 with dissolve:
        xpos .75 xanchor .75
    x "哎呀，我可是在帮你啊。"
    show x 惊讶01 with dissolve:
        xpos .75 xanchor .75
    x "我们不是伙伴吗？"
    show y 无措 with dissolve:
        xpos -0.08 xanchor 0.0
    y "额，不。"
    narrator "袁艳的小脸一红，好像想起了什么。"
    show y 恼火02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "我…我只是怀疑你有什么别的目的。"
    show c 侧视02 with dissolve:
        xpos 1.25 xanchor 1.25
    c "袁艳袁艳，我可以去冰箱里头拿牛奶吗？"
    show y 正常04 with dissolve:
        xpos -0.08 xanchor 0.0
    y "你去啊。"
    #【程祎琳】（侧视01—消失）
    show c 侧视01 with dissolve:
        xpos 1.25 xanchor 1.25
    c "好呀。"
    hide c with dissolve
    narrator "然后程祎琳屁颠屁颠地就跑去冰箱里头拿了牛奶，还刚好拿了五份…."
    narrator "嗯？为什么会有五份？"
    show c 斜视01 with dissolve:
        xpos .75 xanchor .75
    c "袁艳袁艳，我可以喂你的猫喝牛奶吗？"
    show y 正常01 with dissolve:
        xpos -0.08 xanchor 0.0
    y "啊？"
    narrator "袁艳听到我的时候，回过头来看了看我。"
    narrator "然后莫名其妙地瞪了我一眼。"
    show y 正常02 with dissolve:
        xpos -0.08 xanchor 0.0
    y "随便你。"
    w "喵…."
    narrator "我叫着像是抗议一样的声音。"
    narrator "鼻子酸酸的，感觉有点难受。"
    show c 注视01 with dissolve:
        xpos .75 xanchor .75
    c "诶嘿嘿。"
    hide c with Dissolve(.7)
    narrator "程祎琳跑到了厨房找了一个小白碗，然后把从冰箱里头拿出来的牛奶倒了一盒在碗里。"
    narrator "接着朝着我靠近。"
    narrator "我本能地后退了两步。"
    narrator "当然这不是怕这个丫头，而是在表示拒绝。"
    narrator "但是不知道为什么程祎琳反而以为这是很正常的一样。"
    narrator "把碗放在了我的面前不远处，自己后退了好几步。"
    narrator "然后蹲在那里看着我。"
    w "……."
    narrator "这丫头倒是挺礼貌的。"
    narrator "不过干嘛要喂我喝牛奶。"
    narrator "我看了看袁艳，袁艳还在跟另外两个丫头在说话。"
    narrator "看都不往我这边看一眼，看来是不打算理会我这边了。"
    narrator "哼，像我这么神圣的存在又怎么会去喝嗟来之食呢。"
    narrator "昂起头颅，用我自认为最高傲的方式一摆头，溜到房间里头去了。"
    show c 注视02 at ct with dissolve
    c "……."
    narrator "只不过这个丫头似乎还有点不死心。"
    narrator "还跟在我身后，像是在跟踪我。"
    narrator "然后我看到狼藉的房间，不由得郁闷了起来。"
    narrator "显然我后边那位也是被房间的样子镇住了。"
    show c 惊讶02 at ct with dissolve
    c "欸？"
    narrator "虽然她疑惑的声音不是很大"
    narrator "但是这个声音却成功地引起了另外两个….不，是三个人的注意力。"
    narrator "……"

    
    #【场景：房间】
    nvl clear
    nvl hide
    window hide dissolve
    #1
    scene room_白天 with dissolve:
        zoom .667
    
    narrator "林琴看到房间的惨状之后不由得摇了摇头，有些同情似地看着袁艳。"
    show x 假笑02 at ct with dissolve
    x "这个地方还真变化蛮大呢。"
    show y 恼火02 at ct with dissolve
    y "所以说你不要一副很久没来了模样啊！"
    show l 普通08 at rt with dissolve
    l "啧啧啧。"
    show l 惊异03 at rt with dissolve
    l "你家里是进了强盗吗？"
    show y 恼火02 at ct with dissolve
    y "你家里才进了强盗呢。"
    show y 恼火01 at ct with dissolve
    y "我说你们能不能有客人的自觉啊。"
    show y 愤怒 at ct with dissolve
    y "你们这都是第几次随便进我的房间了。"
    show l 不满07 at rt with dissolve
    l "哼，也不知道是谁前几天还特意请我们来的呢。"
    show y 无措 at ct with dissolve
    y "……."
    show y 嘲讽03 at ct with dissolve
    y "那…那个不一样啦。"
    show y 嘲讽04 at ct with dissolve
    y "而且当时你们不是也不同意帮我吗？"
    show y 嘲讽01 at ct with dissolve
    y "再说了，你们几个到底什么时候谈恋爱啊。"
    show x 嘲笑01 at ct with dissolve
    x "我觉得我随时都可以。"
    narrator "夏静笑眯眯地看着袁艳，连我都觉得浑身一冷。"
    narrator "袁艳就自然不必说。"
    show y 无措 at ct with dissolve
    y "别吧….我性取向还算是正常的那种的。"
    show x 闭眼 at ct with dissolve
    x "那我问你几个问题好了。"
    show y 正常04 at ct with dissolve
    y "额，你问吧。"
    show x 反驳02 at ct with dissolve
    x "你很讨厌我吗？"
    show y 无措 at ct with dissolve
    y "啊？"
    show y 俏皮 at ct with dissolve
    y "倒也算不上讨厌。"
    narrator "袁艳很老实地就回答了….可是我总觉得有那么一点点不安。"
    narrator "这点不安是替她不安。"
    show x 反驳02 at ct with dissolve
    x "原来如此，我们在一起的时候，你觉得开心吗？"
    show x 反驳01 at ct with dissolve
    x "比起以前热闹吗？"
    narrator "袁艳愣住了，看了一眼夏静然后莫名其妙地揉了揉眼睛。"
    show y 愤怒 at ct with dissolve
    y "你不说还好…."
    #嘲讽
    show y 嘲讽01 at ct with dissolve
    y "这几天被你们折腾得要死要死的…."
    show y 恼火02 at ct with dissolve
    y "哭都来不及。"
    show y 嘲讽04 at ct with dissolve
    y "哪里还笑得出来啊。"
    show x 怜悯01 at ct with dissolve
    x "但是你看起来很开心。"
    show y 嘲讽05 at ct with dissolve
    y "……."
    narrator "袁艳脸微微地红了一点。"
    show y 嘲讽03 at ct with dissolve
    y "哪里有很开心，最多只是有一点吧。"
    show l 普通09 at rt with dissolve
    l "……"
    show l 普通07 at rt with dissolve
    l "原谅我在气氛正好的时候打扰你们两个。"
    show l 普通08 at rt with dissolve
    l "我听了你们说的话…"
    show l 普通07 at rt with dissolve
    l "感觉有什么地方不太对，所以想请教一下。"
    show x 假笑01 at ct with dissolve
    x "有意思。"
    show x 假笑02 at ct with dissolve
    x "说说看。"
    show l 惊异03 at rt with dissolve
    l "你…该不会是想跟袁艳谈恋爱吧…."
    show y 无措 at ct with dissolve
    y "（吓！！！）"
    show l 不满08 at rt with dissolve
    l "别吧，"
    show x 反驳03 at ct with dissolve
    x "呵呵….其实我觉得也没多少关系的，就算跟袁艳在一起又怎么样。"
    show x 反驳01 at ct with dissolve
    x "我不介意，只要能谈恋爱不就可以了吗？"
    show x 假笑01 at ct with dissolve
    x "袁艳，只要谈恋爱的话，对象是谁不也都无所谓吗？"
    w "……."
    narrator "原来还有这样子的选择吗？"
    narrator "搞不好还真是个不错的办法。"
    narrator "袁艳看了看我，向我使了个眼色。"
    narrator "只可惜这个时候的我也不知道该怎么判断。"
    narrator "所以没办法回应袁艳。"
    narrator "于是我摇了摇头。"
    narrator "但是不知道怎么回事，袁艳像是明白了什么一样点了点头。"
    narrator "咦？她这是明白了啥？"
    narrator "我是说我不知道啊。"
    show y 恼火02 at ct with dissolve
    y "打住打住！！！"
    show y 恼火01 at ct with dissolve
    y "我有异议！"
    show x 考虑02 at ct with dissolve
    x "说。"
    show y 正常05 at ct with dissolve
    y "那是无效的！不是真心谈恋爱是无效的。"
    show y 正常04 at ct with dissolve
    y "难道你看到我会有心跳的感觉吗？"
    show x 考虑01 at ct with dissolve
    x "……."
    narrator "夏静听了袁艳说的话然后捂着自己的胸看着袁艳，却没有说话。"
    narrator "虽然不知道袁艳误会了什么。"
    narrator "看着夏静。"
    narrator "我总觉得有什么地方出错了，而且错得很离谱。"
    show y 正常04 at ct with dissolve
    y "听好了啊，这个恋爱不好好谈是无效的，你们知道吗？"
    show y 恼火04 at ct with dissolve
    y "而且你们可还是花季少女啊，整天把时间浪费在我这里真的好吗？"
    show y 恼火05 at ct with dissolve
    y "你们在不谈恋爱我可是会死的噢。"
    show l 惊异03 at rt with dissolve
    l "噗…."
    show y 正常04 at ct with dissolve
    y "你笑什么？"
    show l 慌张07 at rt with dissolve
    l "你这个丫头还真是…."
    show x 怜悯02 at ct with dissolve
    x "呵呵…."
    show c 侧视02 at ct with dissolve
    c "嗯？"
    narrator "就是连我都觉得看不下去了。"
    narrator "全场似乎就只有袁艳和程祎琳还很疑惑。"
    show l 普通07 at rt with dissolve
    l "那你自己的命来威胁我们你不觉得有什么不对劲吗？"
    show l 普通08 at rt with dissolve
    l "还是说你脑袋秀逗了？"
    show y 无措 at ct with dissolve
    y "……."
    #嘲讽
    show y 嘲讽01 at ct with dissolve
    y "话…是这么说…可是没有我的话，你们想要找的人大概是没机会见到了。"
    show l 惊异03 at rt with dissolve
    l "……."
    show x 惊异 at ct with dissolve
    x "……."
    show c 张嘴01 at ct with dissolve
    c "……."
    narrator "‘铛’的一声，牛奶盒从程祎琳的手里滑落，掉在地上。"
    narrator "这个场景似曾相识。"
    narrator "之前的话我可能还会惊讶，不过现在我只觉得实在是没力气去理会了。"

    
    nvl clear
    nvl hide
    window hide dissolve
    #场景：客厅】
    scene kt_白天 with dissolve:
        zoom .667
    
    w "唉。"
    narrator "离开了房间，又走回了之前程祎琳放小碗牛奶的地方开始舔了起来。"
    narrator "只要留在那里，就能很明显感觉时间被浪费了。"
    narrator "这丫头到底在想什么。"
    narrator "赶紧判断出来我直接点火就是了。"
    narrator "搞得那么麻烦，把命完成了过家家。"
    narrator "顺带一提，过家家这个词我是跟以前跟一个友人学的…."
    narrator "也不知道它现在在哪里过得怎么样就是了…."
    w "……"
    narrator "欸….不过说到底，袁艳好像没什么朋友来着。"
    narrator "就我这几天来看，她除了偶尔出去买点东西，平常都窝在家里。"
    narrator "这丫头怎么回事？"
    narrator "怎么感觉她的身份好像有点神秘啊。"
    narrator "如果换做以前的话，我说不定还能用自己的能力去查探一下她。"
    narrator "不过现在的话还是免了吧。"
    narrator "自己的力量用一点就少一点。"
    narrator "如果这次点错了火，诅咒下来之后还不知道会发生什么事情呢。"
    w "哈 …."
    w "接下来到底该怎么办啊…."
    narrator "无奈的我只能把内心的郁闷发泄在碗里——这个碗里面有程祎琳倒好的酸奶。"
    w "味道还不错…."
    narrator "至于里面到底发生了什么我是不太想知道了。"
    narrator "我现在有点困，只想找个沙发躺躺。"
    narrator "明明知道时间不多了….明明我自己也是知道的。"
    narrator "舔了两口牛奶之后我就溜达到了沙发上，盘着身子想要就这样睡。"
    narrator "当然这种时候我的愿望是很难如愿的。"
    narrator "喧闹的几个人被袁艳从房间里头推了出来，看这个架势是打算又重新聚到我这边来了。"
    narrator "就是因为知道会这样，所以我颤颤巍巍又准备溜到房间里头去。"
    narrator "但是不知道是谁把我抱了起来….不会是程祎琳吧…"
    w "喵…."
    #none lh
    y "……"
    narrator "困顿过头的我也没有太注意抱住我的人居然会是袁艳。"
    w "……."
    narrator "不一会儿，我就在非常温和地抚摸下睡了过去。"
    narrator "……"

    nvl clear
    nvl hide
    window hide Dissolve(1)
    #【场景：黑屏】
    scene black with dissolve
    pause 1
    
    #【场景：客厅】
    scene kt_白天 with dissolve:
        zoom .667
    
    w "啊…."
    narrator "半睁着眼感觉自己有些迷糊…"
    show y 嘲笑 at ct with dissolve
    y "你们吃饱了可以走了吗？"
    show y 嘲讽01 at ct with dissolve
    y "我现在很困，想睡觉。"
    narrator "袁艳的声音在我上方响起的时候，我瞬间就精神了。"
    w "啊?"
    narrator "我抬起头，顶着袁艳的下颚。"
    show y 嘲笑 at ct with dissolve
    y "别闹…."
    narrator "说着伸出手把我的脑袋按了下去。"
    narrator "我眨了眨眼睛，桌面上的四个方向有着三个不同的女孩。"
    narrator "看了看天色，已经接近傍晚，脑海中的记忆逐渐连成了一条线。"
    narrator "这几个女孩居然在这里待了整整一天？"
    show y 嘲讽05 at ct with dissolve
    y "你们吃了午饭还要吃晚饭，干脆夜宵都在这里吃了得了。"
    show x 假笑02 at lt with dissolve
    x "别那么无情嘛。"
    narrator "夏静摆了摆手。"
    show x 假笑01 at lt with dissolve
    x "我们不是在商讨恋爱战略吗？"
    narrator "程祎琳连忙跟着点了点头，似乎她对袁艳要赶走她持反对意见。"
    show y 正常02 at ct with dissolve
    y "那讨论了一下午，到底出了点什么主意呢？"
    show y 正常03 at ct with dissolve
    y "这个程丫头就算了，脑袋里头只有零食。"
    show y 正常01 at ct with dissolve
    y "你们两个呢？"
    show l 普通08 at rt with dissolve
    l "有什么不行的吗？"
    show l 普通07 at rt with dissolve
    l "我可以准备一个大型男友招聘会呀。"
    show y 正常01 at ct with dissolve
    y "……"
    #【袁艳】（正常03-02）
    show y normal_3_2 at ct with dissolve
    y "那不太可能的吧。"
    show l 普通08 at rt with dissolve
    l "有什么不可能的？不就是要花点钱吗？"
    show y 恼火01 at ct with dissolve
    y "既然你那么有钱就不要我请你吃饭啊。"
    show y 恼火02 at ct with dissolve
    y "你以为这些外卖不要钱的吗？"
    show l 注视08 at rt with dissolve
    l "你想的话我给你把你给我们点餐的外卖店买了送给你。"
    show y 无措 at ct with dissolve
    y "额…."
    show x 闭眼 at lt with dissolve
    x "嘁，散发着资本主义臭味的走狗。"
    show l 不满07 at rt with dissolve
    l "哦呵，说我资本主义，那你做得到吗？"
    show l 不满08 at rt with dissolve
    l "你看看你出的主意。"
    show x 反驳02 at lt with dissolve
    x "我的主意怎么了？"
    show l 不满08 at rt with dissolve
    l "居然想靠计算机帮统计这个城市男人的数据挑选合适的人，你以为我不知道吗？"

    #【林琴】（不满09-08）"不愧是无能的观测主义呢。"
    show x 反驳01 at lt with dissolve
    x "你又好到哪里去呢？"
    show y 嘲笑 at ct with dissolve
    y "停.，你们都吵了一天了。"
    #【袁艳】（正常03-02）"你们不嫌累我听着都累。"
    show y 正常01 at ct with dissolve
    y "啊，算了。"
    show y 正常02 at ct with dissolve
    y "你们自己去想办法吧。"
    #【袁艳】（正常03-2）"我也无能为力了。"
    show x 考虑01 at lt with dissolve
    x "其实你也没出啥力…."
    show y 恼火01 at ct with dissolve
    y "这种事实麻烦你不要说出来谢谢。"
    w "……."
    narrator "我大概知道今天是怎么度过的了。"
    show y 嘲笑 at ct with dissolve
    y "所以你们赶紧走吧，太晚走不安全。"
    show y 嘲讽05 at ct with dissolve
    y "你们各个身份都挺特殊的，又特别显眼。"
    show y 嘲讽04 at ct with dissolve
    y "老跑我这里来对我来说不是件好事。"
    show l 慌张07 at rt with dissolve
    l "我只是路过而已…."
    show y 正常02 at ct with dissolve
    y "……"
    show y 嘲笑 at ct with dissolve
    y "回去早点睡，明天继续路过我家吧。"
    narrator "袁艳露出了跟以往不一样的笑容，对着三个人这样说道。"
    show x 嘲笑02 at lt with dissolve
    x "……"
    hide x with dissolve
    show y 嘲笑:
        linear .3 xpos 0.0 xanchor 0.0
    show l 慌张08 at rt with dissolve
    l "好…好吧。"
    #【林琴】（慌张09-08）
    show l worry_9_8 at rt with dissolve
    l "既然你这样说….那就没办法了。"
    show l 慌张07 at rt with dissolve
    l "反正我明天出来的时候刚好也会路过你这里。"
    show l 慌张08 at rt with dissolve
    l "勉强来一下也是没关系的。"
    show y 开心 at lt with dissolve
    y "哈哈哈…."
    narrator "看到笑起来的袁艳，不知道为什么林琴也微微地露出了微笑。"
    show l 普通08 at rt with dissolve
    l "算啦，今天就到这里好了。"
    show l 普通07 at rt with dissolve
    l "你的事情我会努力的。"
    show y 笑容01 at lt with dissolve
    y "那还真是拜托了。"
    #【林琴】（普通07-立绘消失）
    show l 普通08 at rt with dissolve
    l "呵呵…."
    hide l with Dissolve(.7)
    narrator "然后林琴起身就准备走。"
    show y 正常02 at lt with dissolve
    y "阿琳，你呢？"
    narrator "程祎琳刚刚喝完一盒酸奶，不小心撒了一点点在手上，这个时候的她正在舔自己的手指。"
    show y 正常01 at lt with dissolve
    y "……"
    show c 侧视01 at rt with dissolve
    c "……."
    show c 斜视01 at rt with dissolve
    c "要…要走了吗？"
    show l 普通07 at ct with dissolve
    l "是啊，要不要跟我走？我给你去买吃的怎么样？"
    show c 注视01 at rt with dissolve
    c "……."
    narrator "程祎琳看了看袁艳，好像打算征求她的同意一样。"
    w "……"
    narrator "这种东西你还要袁艳同意啊。"
    show y 正常04 at lt with dissolve
    y "很晚了，女孩子一个人回去的话太危险了。"
    show y 正常05 at lt with dissolve
    y "你们两个一起回去我比较放心。"
    show c 侧视02 at rt with dissolve
    c "奥…"
    show c 斜视01 at rt with dissolve
    c "我明天来找你玩！"
    narrator "程祎琳歪着脑袋露出了笑脸，就好像是在跟自己的朋友道别一样。"
    show y 开心 at lt with dissolve
    y "嗯。"
    show c 恶心01 at rt with dissolve
    c "明天想吃酸辣土豆丝。"
    show y 恼火01 at lt with dissolve
    y "你当我家是餐馆啊！"
    #【程祎琳】（恶心02-01）
    show c disguest_2_1 at rt with dissolve
    c "不…不行吗？"
    narrator "看着可怜兮兮的这个女孩…袁艳愣了两秒。"
    show y 嘲笑 at lt with dissolve
    y "行行…你卖萌还是留给你未来的男朋友吧。"
    show y 正常04 at lt with dissolve
    y "赶紧走赶紧走。"
    show c 侧视02 at rt with dissolve
    c "嗯。"
    show l 不满08 at ct with dissolve
    l "架子不小呢，让我等这么久。"
    show c 斜视01 at lt with dissolve
    c "唔…是吗？"
    show l 普通08 at ct with dissolve
    l "算了，就这样走吧。"
    show c 注视01 at lt with dissolve
    c "嗯，好。"
    hide c with dissolve
    show x 假笑02 at rt with dissolve
    x "…."
    show l 普通07 at ct with dissolve
    l "那个臭屁的观测者呢？"
    show l 注视07 at ct with dissolve
    l "你打算什么时候走？"
    show x 考虑02 at rt with dissolve
    x "一会就走了。"
    show l 慌张08 at ct with dissolve
    l "那一起吗？"
    show x 惊异 at rt with dissolve
    x "……."
    show x 假笑01 at rt with dissolve
    x "噢哟，吹了什么风居然会让大小姐亲自等我。"
    show x 假笑02 at rt with dissolve
    x "受宠若惊啊。"
    show l 不满07 at ct with dissolve
    l "少废话，你走不走？你不走我不管你了。"
    show x 普通01 at rt with dissolve
    x "在外边等我一下，我一会就来。"
    show l 普通07 at ct with dissolve
    l "……."
    narrator "林琴看了看夏静，看她的表情似乎是打算提出反对意见的。"
    narrator "但是马上又像是想到了什么一样阻止了本来要说出来的话。"
    show l 普通08 at ct with dissolve
    l "那你快点，我不会等你太久的。"
    show x 考虑01 at rt with dissolve
    x "好。"
    hide l with Dissolve(.7)
    narrator "说完林琴就带着程祎琳出去了。"
    show x 注视02 at rt with dissolve
    x "……."
    #【夏静】（注视03-01）
    show x stair_3_1 at rt with dissolve
    x "那家伙可能以为我要跟你表白。"
    show y 嘲笑 at lt with dissolve    
    y "那还真是饶了我吧。"
    show y 嘲讽01 at lt with dissolve
    y "都是女孩，你总不会真的打算跟我谈恋爱吧。"
    show y 嘲讽05 at lt with dissolve
    y "我这几天没休息好，有点犯迷糊。"
    show y 嘲讽04 at lt with dissolve
    y "你有什么要说的就快点说吧，我怕我撑不住。"
    w "……"
    show x 反驳01 at rt with dissolve
    x "程祎琳那个丫头有问题。"
    show x 反驳02 at rt with dissolve
    x "虽然不知道是不是你想要找的人。"
    show x 反驳01 at rt with dissolve
    x "不过我可以给你提供关于她的所有信息。"
    show y 正常02 at lt with dissolve
    y "她只是不喜欢吃肉吧。"
    narrator "袁艳的精神似乎有些萎靡，我看着她浑浑噩噩的。"
    narrator "夏静愣了愣。"
    #【夏静】（反驳03-普通02）
    show  x fb3_normal2 at rt with dissolve
    x "确实是这样，你的观察力很厉害呢。"
    narrator "袁艳看了一眼夏静，然后无奈地笑了笑。"
    show y 正常04 at lt with dissolve
    y "是她自己说的。"
    show x 无奈02 at rt with dissolve
    x "原来如此，你也算是做了各种各样的努力呢。"
    show y 嘲笑 at lt with dissolve
    y "是吗？呵呵….我也算是努力过了啊。"
    show x 考虑02 at rt with dissolve
    x "不过…她可能跟你想象中不太一样…."
    show x 考虑01 at rt with dissolve
    x "或者说，你在继续让她接近你搞不好会有点危险。"
    show y 嘲讽01 at lt with dissolve
    y "已经没有什么好怕的了。"
    show x 无奈01 at rt with dissolve
    x "真的吗？"
    show y 嘲讽02 at lt with dissolve
    y "你看我现在这个状态…."
    narrator "夏静沉默了一下。"
    show x 怜悯01 at rt with dissolve
    x "这样啊，那还真是….哈哈哈。"
    show x 怜悯02 at rt with dissolve
    x "我先走了，她们两个还在等我。"
    show x 假笑02 at rt with dissolve
    x "不能让那个资本主义小姐等太久了呢，不然她又要发病了。"
    show y 正常02 at lt with dissolve
    y "你也知道她有病吗？"
    show x 注视01 at rt with dissolve
    x "多少知道一点吧。"
    #none lh
    #【夏静】（反驳03-02）
    show x fb_3_2 at rt with dissolve
    x "不过还是小心程祎琳那丫头最好…."
    show y 正常04 at lt with dissolve
    y "为啥？"
    show x 怜悯02 at rt with dissolve
    x "说不定她会吃了你哦。"
    show y 俏皮 at lt with dissolve
    y "哈哈…"
    show y 开心 at lt with dissolve
    y "我倒是比较担心你会吃了我。"
    narrator "夏静听出了话里头的意思。"
    show x 假笑01 at rt with dissolve
    x "呵呵呵，你果然很有意思，如果跟你在一起的话一定不会无聊呐。"
    show y 笑容01 at lt with dissolve
    y "那还真是多谢了，彼此彼此吧。"
    show x 假笑02 at rt with dissolve
    x "那你就小心点…别被‘吃了’噢。"
    show x 怜悯01 at rt with dissolve
    x "不论是她还是我。"
    show y 正常04 at lt with dissolve
    y "嘶….你还要不要走啊！"
    narrator "明显地袁艳倒吸了一口凉气。"
    show x 考虑01 at rt with dissolve
    x "那就这样……"
    hide x Dissolve(.7)
    narrator "夏静说完摆了摆手，然后离开了客厅。"
    narrator "转眼间客厅就只剩下了我和袁艳。"
    narrator "随着喧闹声远离以后，客厅变得愈发的空荡了起来。"
    w "突然间就变得很安静了。"
    narrator "我从袁艳的身上溜了下来。"
    show y 嘲笑 at ct with dissolve
    y "哈哈…是呢。"
    narrator "袁艳莫名其妙地扶了扶脑袋。"
    narrator "虽然嘴上在说话，但是我总觉得袁艳的视线很奇怪，像是根本不是看着我。"
    w "最后的那个情报挺重要的。"
    w "我们是不是该把目标多往那个叫程祎琳的女孩身上放放了。"
    show y 正常01 at ct with dissolve
    y "可能是吧…."
    w "搞不好真的是她，只要朝着她点火我们的诅咒说不定就能马上解开了。"
    #【袁艳】（正常03-02）
    show y normal_3_2 at ct with dissolve
    y "大概吧…."
    w "如果是这样的话我们就针对她去多收集情报吧，你觉得怎么样？"
    show y 正常01 at ct with dissolve
    y "好…好啊，我觉得很不错。"
    w "……"
    w "我说你啊…"
    w "怎么从一开始就像是在敷衍我的样子啊。"
    show y 正常01 at ct with dissolve
    y "有吗？"
    w "有啊。"
    show y 正常02 at ct with dissolve
    y "你的错觉啦…"
    w "是这样吗？"
    #【袁艳】（正常03-02）
    show y normal_3_2 at ct with dissolve
    y "是这样啦。"
    narrator "我盯着袁艳，袁艳露出的却是一张有些勉强的笑容。"
    
    #【CG：呕吐】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_yot = True
    scene cg_呕吐 with Dissolve(2)
    
    pause 1.0
    
    narrator "袁艳的脸色非常的苍白。"
    #none lh
    y "……"
    #none lh
    y "抱歉…."
    narrator "袁艳眼睛睁了一下，然后连忙起身跑到了厕所。"
    #none lh
    y "呕…."
    narrator "十分痛苦的声音从厕所里头传了出来。"
    w "……."
    narrator "我甚至不知道发生了什么事情。"
    narrator "只是莫名奇妙地2担心从心底升了起来。"

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    #【CG：结束】

    scene kt_白天 with dissolve:
        zoom .667
    
    narrator "声音并没有持续多久。"
    narrator "冲水的声音从厕所响起之后。"
    narrator "袁艳就抱着肚子躬着身躯从厕所里头走了出来。"
    narrator "整个人变得十分的憔悴。"
    narrator "看得我感觉有些心疼。"
    w "喂…袁艳…你…没事吧。"
    narrator "袁艳无力地看了看我一眼。"
    show y 嘲讽02 at ct with dissolve
    y "大…大概…."
    w "真…真的假的，怎么看起来你跟快死的人一样啊。"
    show y 无措 at ct with dissolve
    y "有…那么严重吗？"
    w "你脸色看上去很恐怖啊。"
    #【袁艳】（正常03-01）
    show y normal_3_1 at ct with dissolve
    y "是吗？"
    show y 恼火02 at ct with dissolve
    y "你听我说死猫。"
    show y 恼火01 at ct with dissolve
    y "所谓的人类呢，就是三天不睡会死的生物噢，好好记住了。"
    w "哇，你这是哪里来的理论啊。"
    narrator "袁艳说着身体不由自主的就倒在了地上。"
    narrator "她似乎还没意识到自己发生了什么，嘴里还在跟我进行着对话。"
    w "喂喂喂，你没事吧你没事吧！"
    
    #【场景：黑屏】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with dissolve
    
    #show y 嘲讽03 at ct with dissolve
    y "大概…我..还能在…抢救一下……"
    narrator "回过神的她，艰难地朝我伸出了手。"
    narrator "这般说道…."
    narrator "……."

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：街道】
    scene street_白天 with dissolve:
        zoom .667
    
    w "呼…"
    #奔跑喘气）"
    narrator "死丫头，成天尽给我添麻烦。"
    narrator "我的力量能拯救精神，但是没办法治疗身体。"
    narrator "这种要命的节骨眼上居然倒下。"
    narrator "你要我怎么办啊。"
    narrator "我遵循着记忆里头的道路，在道路上狂奔着。"
    narrator "只要找到那几个刚走没多久的那三个人。"
    narrator "也许就会有办法。"
    narrator "可是……"
    narrator "……"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：街道2】
    scene street_gj with Dissolve(1):
        zoom .667
    
    narrator "已经不知道跑了多长的时间了。"
    narrator "我还是在街道里头穿梭着。"
    narrator "根本就找不到路。"
    narrator "停下来的一小会我才发现，我已经完全迷路了。"
    narrator "这种时候怎么连我自己都掉链子啊！"
    narrator "我焦急地在路口伫立着，周围的人们都朝我投来惊奇的目光。"
    narrator "然而在这种时候我已经没有时间去享受万众瞩目的视线了。"
    narrator "我必须尽快找到那三个家伙，不然不需要等诅咒降临，今晚我家里那只就完蛋了。"
    narrator "她完蛋了是小事，我的猫生跟着完蛋就是大事了。"
    narrator "所以我不能停下来，必须去不断地寻找。"
    narrator "我是为了我自己。"
    narrator "正是因为这样想着，所以我才会玩命地在街道上到处乱窜。"
    "小孩" "哇，这里有一只猫，快抓住它！！！"
    narrator "在奔跑的途中似乎被一群莫名其妙的小屁孩给盯上了。"
    narrator "我可是神圣的猫精灵，对付几个小屁孩那还不是简简单单的事情吗？"
    narrator "只不过…那群小屁孩最后追不到我的时候就气急败坏地拿石头扔我了。"
    narrator "我也算是倒霉的，身上被砸到了好几处。"
    w "现在熊孩子也是够狠的，碗大的石头就这么扔过来。"
    narrator "好好尊重一下生命啊。"
    narrator "尤其是我这么尊贵的生命。"
    narrator "要不是我现在有事情在身上，我一定要好好教育你们。"
    narrator "让你们洗心革面，重新做人。"
    narrator "从熊孩子们的围捕中逃脱之后。"
    narrator "稍微有点儿累的我找了一个地方休息了起来。"
    narrator "身上被石头砸到的地方传来阵阵疼痛感。"
    narrator "估计伤得不轻。"
    narrator "回头可要那个袁艳丫头好好补偿我…."
    narrator "不过这家伙快要死了所以补偿也很难入手。"
    narrator "这就让我很纠结了…."
    narrator "但是这家伙如果真的死了的话，我大概会很难过吧。"
    narrator "想不到我也会有为区区人类难过的时候呢。"
    w "得快点找到她们才行啊。"
    w "得快点。"
    narrator "……."
    narrator "我忍着阵阵地疼痛继续在街上跑了起来。"
    narrator "但是她们到底在哪里？明明可以感觉到她们的位置。"
    narrator "却就是找不到她们。"
    narrator "这个街道仿佛被什么附身了一样，不断着阻碍着我前进的道路。"
    narrator "明明可以救袁艳的人就近在咫尺…可是我却….觉得身体比以往更加疲惫了起来。"
    narrator "我可是神圣的猫精灵啊。"
    narrator "不能就这样放弃啊。"
    narrator "这不就和以前无力的自已一样了吗？"
    narrator "不要停啊…停下来就结束了。"
    w "喵…."

    menu:
        "我跑往了……"

        "医院":
            jump l_in_1
            
        "河边":
            jump x_in_1

        "河岸":
            jump c_in_1
####################################################################################################

label l_in_1:

    $_dismiss_pause = False

    $l_in_1_select = True

    #"（注解：林琴个人线）"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：医院】
    scene yy_前台 with dissolve:
        zoom .667

    narrator "气喘吁吁的我终于跑到了医院。"
    narrator "然而我刚刚准备越过人群跑到里面去，就被人一把抱住。"
    "护士" "小猫咪，这里不是你可以来的地方哦。"
    narrator "这个穿着白色衣服的女性柔和地朝着我说着。"
    w "喵~"
    narrator "可是我没时间了啊！"
    narrator "快让我过去啊！"
    "护士" "知道了就走吧。"
    narrator "护士把我放到了医院门外去了。"
    narrator "我还想进去，但是护士却站在门口带着善意的笑容看着我。"
    narrator "看得我快哭了。"
    narrator "就算你这么温柔地看着我又怎么样啊。"
    narrator "我要进去啊！"
    w "喵~"
    "护士" "呵呵…"
    narrator "她还朝我摆摆手，像是非常喜欢我的模样。"
    narrator "无奈的我只能打算用之前的办法了。"
    narrator "爬到那个楼层就可以了。"
    narrator "我是这么想的。"
    narrator "于是…."
    w "这岂能难得到我？"
    narrator "在爬到一半的我不由得稍微有点得意了起来。"
    narrator "但是…."
    w "妈呀…."
    narrator "爪子一滑整只摔了下去。"
    narrator "不过…"
    narrator "我在空中翻了个身，非常完美地掉到了地上。"
    w "哎…我的腰…."
    narrator "不知道怎么回事，身体突然一痛。"
    narrator "身体差点完全趴在了地上。"
    narrator "那几个熊孩子造的孽啊……"
    narrator "还是稳稳妥妥地爬上去吧。"
    narrator "先找这个叫林琴的丫头救命再说。"
    narrator "然而…."
    narrator "在身体疼痛愈演愈烈的情况下。"
    narrator "爬起来倍感艰难。"
    narrator "总感觉想要到林琴的病房里头这个任务是异常困难的。"
    narrator "只不过想到如果不完成这个事情，袁艳就完了…."
    narrator "袁艳完了我就完了…."
    w "这还真是让猫头大的事情啊。"
    narrator "还能怎样，爬吧。"
    narrator "无奈之下的我只能再一次往上面爬。"
    narrator "每到关键的时候身体被剧烈的疼痛扯住，使不出劲。"
    narrator "不管多么想要爬上去…都无法成功。"
    narrator "攀岩对我来说现在几乎已经成了一件不可能的事情。"
    # TODO
    #【袁艳】（效果 回忆 恼火01）
    '(应该需要回忆效果？)'
    show y 恼火01 at ct with dissolve
    y '死猫.，不行就别死撑了。'
    show y 恼火02 at ct with dissolve
    y "看你那糗样。"
    hide y with Dissolve(.7)
    w "……."
    narrator "脑海里头突然响起她的声音。"
    narrator "如果她现在在这里的话，一定会这么跟我说的吧。"
    narrator "可是现在这个家伙说不定快要死了。"
    narrator "哪里还有空跑过来说我。"
    w "啊…."
    narrator "我这么想的同时不由得扶了扶脑袋。"
    narrator "我好像还承担着救她的使命来着…."
    narrator "现在见不到里面那个丫头就很难办了。"
    narrator "所以，我还在想啥呢…爬吧。"
    narrator "这么跟自己说着似乎好像就能有点力气忍住疼痛一样。"
    narrator "一点点地朝着上面攀爬着。"
    narrator "只是这么一点小事，根本不可能难住我。"
    w "欸？"
    w "喵！！！！"
    narrator "当然也有不可避免的失误，然后从半空中掉下来。"
    narrator "最严重的一次是脑袋磕到了莫名的台子上，躺在地上躺了还一会儿才清醒过来。"
    narrator "其余的都还好。"
    w "三十份薄荷…."
    narrator "喊着迟早要找某个人讨回来的口号，我终于爬到了那个丫头病房的窗前。"
    w "害我…这么摔了三十多次。"
    w "迟早会找你全部要回来的。"

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：病房】
    scene bf_白天 with dissolve:
        zoom .667

    narrator "然而…."
    narrator "一切并没有想象中的那么顺利。"
    narrator "月光洒在这个病房，我的影子在月光下映射在房间里被拉得老长。"
    narrator "可是这个病房…却是空荡荡的。"
    narrator "明明就在这里…明明我感觉到她就在这里才对…."
    narrator "……."
    narrator "我从窗户的间隙跃进了病房，在房间里不断的踱步。"
    narrator "所有的地方都找了找——真的没人。"
    w "……."
    narrator "那我到底是为了什么东西才拼命的往这里爬的啊！"
    w "太心酸了吧。"
    narrator "我扶了扶晕乎乎的脑袋。"
    narrator "想到了袁艳——我仿佛看到天空三十份薄荷就这么从我眼前飞走了。"
    narrator "并不是完全没有做好准备，就是觉得…有点点愧疚。"
    narrator "想不到自己真的连这点小事都做不好。"
    narrator "那自己究竟还能做到点什么呢？"
    narrator "说到底现在的这种情况就是自己造成的。"
    narrator "我摇摇晃晃的从这个病房里头出去了。"
    "护士1" "有猫！！！！"
    "护士2" "快！快抓住它，把它扔出去。"
    "护士2" "不然这个月的绩效就没了！"
    narrator "恍惚中，我被几双手提了起来。"
    narrator "在上下楼梯的颠簸中，莫名其妙我的视线就模糊了起来。"
    narrator "仅仅是因为最后自己什么都没有办到…明明自己以为可以办到的事情。"
    narrator "……."
    narrator "我被随手丢在了医院旁边的某个草丛里头。"
    narrator "仿佛又回到了几天前的那个夜晚——"
    narrator "我对我自己的生命已经无能为力的那个夜晚。"
    narrator "但是那个时候有个女孩冒着大雨把我轻轻地包裹起来，然后抱回了家。"
    narrator "……."
    narrator "之后一直在给她添麻烦。"
    narrator "虽然嘴上不说，心里也很少去想….但是偶尔想起来。"
    narrator "就有有种哪怕只有一次也好，我想帮她这样的冲动。"
    narrator "可是我什么都办不到。"
    narrator "就是连暴露自己的存在这样的小事都做不到….不对…暴露自己好像会发生很不得了的事情…"
    narrator "当场暴毙这种事情还是算了吧，就算强行暴露了自己也不会被人所记下。"
    narrator "啊…."
    narrator "接下来到底该怎么办啊。"
    w "真绝望…."
    narrator "袁艳，我现在该怎么办才好啊。"
    narrator "这种时候要是那丫头在就好了….额…那家伙好像…算了…"
    narrator "我爬了起来，这个时候不振作不行啊。"
    w "啊，好疼…（木讷的声音）"
    narrator "第一件事情，我是一只神圣的猫精灵，这是我的本能我绝对不会认同其他以外的身份。"
    narrator "第二件事情，我现在是为了我的生存在行动，拒绝接受任何以外的其他答案。"
    narrator "第三件事情，我要救那个小丫头，那个让人操心到心都碎了的家伙。"
    narrator "然后我就窜出了草丛。"
    narrator "她就在附近，今天我就是跑断这四条腿，也要把那个叫林琴的丫头揪出来。"
    narrator "把她带过去救人。"
    
    #【CG：夜之大小姐】（礼服）
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_yzdxj = True
    scene cg_夜之大小姐 with Dissolve(2)
    
    pause 1.0
    
    #show l 普通01 at ct with dissolve
    l "告诉她们，我马上就到。"
    "管家" "大小姐….现在已经很晚了。"
    "管家" "不如明天再去吧…."
    #【林琴】（普通03-01）
    l "不必了，我有很重要事情要做。"
    #show l 普通02 at ct with dissolve
    l "备好车就行了。"
    "管家" "好的。"
    narrator "医院，门口，这个时间点。"
    narrator "从草丛里头窜出来的我瞬间愣住了。"
    narrator "如果非要我说的话，那就是真的感受到了命运的指示一样。"
    narrator "所谓的奇迹，其实就是在关键的时间里头相遇正确的人。"
    narrator "而在那头，她就在那，我相遇了她。"
    w "……."
    narrator "本来这应该是一件令人高兴的事情…."
    narrator "本来是应该高兴的…."
    narrator "可是为什么突然眼泪就止不住了…."
    narrator "我踩着有些木讷的猫步，朝着那个女孩走了过去。"
    narrator "只不过这个女孩似乎还没意识到我的存在。"

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    #【CG：结束】

    scene yy_门口 with dissolve:
        zoom .667

    w "喵~！！！！"
    narrator "然后不知道从哪里来了一个无影脚…"
    narrator "正好踢到我把我直接踢回了草丛。"
    w "！@……\%@*……\%"
    narrator "哪个乌龟王八蛋居然敢暗算我！！！"
    narrator "被踢到的腿隐隐作痛，回头让我知道是谁我非扒了他的皮不可。"
    narrator "怒不可遏的我一瘸一拐就直接冲了出去。"
    narrator "感受我的狂怒吧，愚蠢的人类。"
    w "喵！！！"
    show l 普通05 at rt with dissolve
    l "嗯？"
    narrator "然后不知道哪里来的一只脚，突然又把我踹到草丛里头去了。"
    w "……"
    narrator "整个爪子都麻了。"
    narrator "趴在地上一时半会使不上力。"
    show l 普通04 at rt with dissolve
    l "你们在干什么呢?"
    "保镖" "报…报告大小姐， 附近有老鼠。"
    show l 普通05 at rt with dissolve
    l "……"
    show l 普通05 at rt with dissolve
    l "哦，那你还真是勤勉啊，我听到的可是猫叫。"
    hide l with dissolve
    "保镖" "是…是大小姐….欸？大小姐？"
    narrator "说着，那个女孩的声音似乎要远去了。"
    narrator "之前她好像说要去办什么事情…"
    narrator "喂…不行啊，你不能走….好不容易找到你的…."
    narrator "好不容易找到你的…."
    narrator "别走啊…."
    w "呜猫！！"
    narrator "别走！"
    narrator "我使劲全力叫了出来，然后一点一点地拖着自己的身体朝着草丛外边蠕动。"
    w "……."
    narrator "稍微恢复了一点知觉，我艰难地撑起了自己的身体，然后一个翻滚再次窜出了草丛。"
    narrator "理所当然的那个身影正逐渐地远去——一定要想办法引起那丫头的注意才行。"
    narrator "不然一切都结束了。"
    "保镖1" "这黑猫怎么回事？"
    "保镖2" "快处理掉它，让大小姐看到就完了，这邪门玩意。"
    narrator "听懂他们对话的我当然不可能就这样束手就擒。"
    narrator "压了压身子，警戒地看着两个穿着黑衣服的王八蛋。"
    narrator "刚刚绝对就是这两个家伙中的一个踢的我。"
    narrator "不过在没有被偷袭的情况下，就凭你们区区两个人类也想抓到我？"
    narrator "开玩笑也要有一个限度。"
    narrator "我不屑地亮了亮牙齿，放马过来吧！"
    narrator "………"
    narrator "这还是人类的力量吗….我不信我也不想信。"
    narrator "被抓住四只腿的我不知道该用什么表情来面对这个事实。"
    narrator "完了…完了完了完了完了"
    narrator "完了完了完了完了…."
    narrator "想到袁艳，我现在满脑子都是这些。"
    w "唔喵！！！"
    w "喵！！！！"
    w "喵呜！"
    w "哇哇哇哇啊！"
    narrator "我撕心裂肺地叫了起来。"
    "保镖1" "哇，这猫怎么回事？"
    show l 惊异 at rt with dissolve
    l "嗯？"
    narrator "得手了，我看着终于为我侧目的林琴。"
    narrator "其实我等的就是这一刻。"
    narrator "然而…."
    narrator "我只感觉到了身体突然一凉，就像飞出去了一样…事实上就是飞出去了。"
    narrator "然后撞到了什么东西瞬间被撞得七荤八素的。"
    narrator "一时间分不清东南西北了，虽然我也不知道什么是东南西北。"
    narrator "只不过双眼倒是短暂地有些失明，嘴里不断地流出点腥味的液体。"
    w "…."
    w "唔….喵…."
    narrator "这个时候我是不是该喊一声救命来着？"
    narrator "好像….好像绝对不能说话的才对，说了也没有用啊。"
    narrator "除了那丫头以外…"
    w "瑞呼气（对不起）\n\n\{注解：本句话类似嘴里有水，含糊不清的语气。\}"
    narrator "恍惚之中，似乎有一双非常温暖的手朝我递了过来。"
    narrator "袁艳？"
    narrator "不行….不行啊。"
    narrator "不要碰我….不要碰我 。"
    w "喵！（非常凶）"
    narrator "我翻身起来作出了攻击的姿态，望着蹲在我面前的，散发着柔和气息的女性。"
    narrator "不要碰我….我身上有诅咒啊。"
    narrator "女孩似乎被我吓退了一步——但是这样就好。"
    narrator "这样子最好。"
    narrator "这样你就不会遭到诅咒了——袁艳。"
    narrator "然后我转身朝着自认为不容易被人发现的位置，蜷缩了起来。"
    narrator "这样她就看不见我了。"

    nvl clear
    nvl hide
    window hide dissolve
    #【人物切换，视角：林琴】
    scene yy_门口 with dissolve:
        zoom .667
        
    show l 注视04 at ct with dissolve
    l "那只猫…不是袁艳家里的么？"
    narrator "看着遍体鳞伤蜷缩在角落的黑猫却面露警戒似的凶光，我不由得皱了皱眉头。"
    narrator "虽然还有很多疑问，但是我现在非常的不爽。"
    show l 注视05 at ct with dissolve
    l "这是怎么回事？"
    "保镖1" "您出行的时候有只猫窜出来了。"
    narrator "我看了看这个一本正经的家伙，他似乎还以为做了什么为我好的事情。"
    show l 不满05 at ct with dissolve
    l "这么说你刚刚驱逐的就是它咯？"
    "保镖1" "是的，实在抱歉，让您看到了。"
    show l 不满04 at ct with dissolve
    l "你可以走了。 "
    "保镖1" "啊？"
    "保镖1" "大小姐….不…不好意思，是这只猫它非要窜到您那边去的…"
    narrator "他似乎还以为是他的失职…."
    show l 不满05 at ct with dissolve
    l "没听见吗？我说你可以去领工资了。"
    "保镖1" "小姐…."
    show l 不满04 at ct with dissolve
    l "滚。"
    narrator "看着悻悻离开的那个男人，我的内心变得异常冰冷了起来。"
    narrator "没有人会理解我此时此刻为什么会突然大发脾气。"
    narrator "莫名其妙的愤怒、莫名其妙的行动，这就是我。"
    narrator "还有总是会受到莫名其妙的视线。"
    narrator "这都无所谓了。"
    narrator "我靠近了那只蜷缩在角落遍体鳞伤的家伙——它似乎完全没有感觉我的到来。"
    narrator "我轻轻地把这个家伙抱了起来，几乎没了之前的抵抗。"
    narrator "它浑身发抖，似乎伤得不轻。"
    show l 普通05 at ct with dissolve
    l "联系最好的兽医，救活它。"
    "管家" "好的。"
    narrator "为什么这家伙会这么晚还从袁艳家里突然跑出来呢？"
    narrator "还跑到我这里来…."
    narrator "我不由得想起前些天这个小家伙出现在我病房的时候。"
    narrator "难不成这家伙是来找我的？"
    narrator "在把它交付给管家的一瞬间，我似乎突然意识到了什么…."
    show l 惊异 at ct with dissolve
    l "通知医生，让他带上急救药品跟我去救人！！"
    "管家" "好的小姐。"
    narrator "又是一个莫名其妙的视线，可是这种时候我已经没心情去在意这些事情了。"
    narrator "稍微地有些担心起那个敢找我麻烦的死丫头了。"
    narrator "那家伙不会出什么事了吧。"

    scene black with dissolve
    narrator "……."
    #"【视角结束。】"

    jump x_in_1

#（夏静线） 
label x_in_1:

    #"（注解：夏静个人线）"

    $_dismiss_pause = False

    $x_in_1_select = True

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667
        
    narrator "气喘吁吁的我不知不觉已经赶到了河边。"
    narrator "在我的记忆里头，好几次她都是在这里的。"
    narrator "下意识我都觉得这里应该是她的家了。"
    narrator "夏静，一个神秘莫测的女孩。"
    w "啊…."
    w "我为什么会有这种愚蠢的想法啊。"
    narrator "但是明明感觉她应该就在附近的。"
    narrator "可是却偏偏一个人都没有。"
    narrator "这个丫头让我根本一点头绪都没有，完全琢磨不透。"
    narrator "但是家里的那只袁艳虽然不喜欢她，却总是能很好的洞悉这个女孩的想法。"
    narrator "果然是因为都是人吗？"
    # TODO
    #【袁艳】（效果 回忆 恼火01）
    #'(应该需要回忆效果？)'
    show y 恼火01 at ct with dissolve
    y "死猫，别胡说八道。"
    show y 恼火02 at ct with dissolve
    y "是因为我们都是女人…."
    hide y with Dissolve(.7)
    narrator "袁艳的声音在脑海里头扩散开来…当然，袁艳并没有出现在这里。"
    narrator "这段话也是我臆想出来的。"
    narrator "那丫头在的话，肯定也会说出类似这样的话来吧。"
    narrator "啊，最近怎么只要一停下来就会想到那家伙的事情。"
    narrator "我脑子不会是坏掉了吧。"
    narrator "河边的微冷的风吹了过来，身体被蹭破皮的地方有点灼热的痛感。"
    narrator "抬头仰望那片清澈的夜空——我究竟在干什么？"
    narrator "我不是在找那个丫头吗？"
    narrator "伫立在围栏上，我不断地扫视着来往的人群。"
    narrator "尽管有不少来往的人，不过那都不是我要找的。"
    narrator "里面没有那个叫夏静的女孩。我在看了看之前程祎琳坐的椅子的方向。"
    narrator "那边也没有另外一个女孩子的存在。"
    narrator "果然来找她是错误的决定么。"
    narrator "现在还是转身赶紧去医院找那个叫林琴的女孩会比较好？"
    narrator "虽然这种时候有可能会被撕了就。"
    narrator "我不由得讪讪地咧了咧嘴。"
    narrator "不对啊….可是为什么那个家伙的气息就在这个附近。"
    w "……."
    narrator "这种感觉真的很不爽。"  
    narrator "要是这个时候袁艳在就好了。"
    narrator "在经历了这么多天以后我发现。"
    narrator "只要我跟着袁艳前往能感受到她们气息的地方，就一定能遇到这群奇怪的家伙。"
    narrator "然而袁艳如果不在的话，即使能感受到她们的气息，她们也像是人间蒸发了一样。"
    w "完全…就找不到啊。"
    "小孩" "妈妈…妈妈，这个猫会说话！！"
    w "……"
    narrator "完了…被…被人听到了。"
    "母亲" "嗯？"
    narrator "女人看了看我，和我对上了眸子，显得异常的惊讶。"
    narrator "不过更加惊讶的人是我。"
    "母亲" "小孩子胡说什么？"
    narrator "母亲牵着小孩的手，非常严肃地说着。"
    w "……."
    "小孩" "可是我真的听到猫说话了….它说找不到什么的。"
    "母亲" "……."
    narrator "那个女人朝我投来有些惊恐的视线。"
    "母亲" "你看错了…."
    narrator "那个母亲把孩子推了推，恰好是小孩视线别过去的一瞬间。"
    narrator "这位伟大的母亲无比敏捷地摔了一跤…莫名其妙看起来很温柔地推力推在了我的身上。"
    w "唔喵！！！！"
    narrator "于是我就被这个看起来很温柔其实充满杀机的一推——你以为我会这样被推到河里去吗？"
    narrator "这简直太天真了。"
    narrator "我轻松地跃到了另外一个桥墩上。"
    narrator "轻蔑地看着这位年轻的女士。"
    narrator "‘吱’这个桥墩突然歪了一下。"
    narrator "只是一瞬间的事情我半空中张开了四条腿，飞了下去。"
    narrator "我的心顿时凉了一大截。"
    w "￥&#……￥"
    narrator "扑通一声掉下水。"
    narrator "在这里我不得不陈述一个事实。"
    narrator "我….其实是不会游泳的。"
    w "唔….咕噜咕噜…喵！！"
    narrator "当然挣扎几下我还是会的。"
    narrator "河床上的那群人纷纷开始凑起了热闹，听着声音似乎是在说有只猫落水了。"
    narrator "猫你们大爷的啊~我是猫精灵啊。"
    narrator "在水中扑腾的我根本就不在乎自己的危险，但是如果把我跟普通的猫相提并论的就是对我最大的侮辱。"
    w "你们…唔….我…要…."
    narrator "但是我根本就喊不出来。"
    narrator "声音也传达不到上面去。"
    narrator "挣扎的稻草最终也逃不过无情的镰刀。"
    narrator "大概就是形容现在的我、还有我们吧。"
    w "哇…."
    narrator "现在不是想这些的时候啊！"
    narrator "我不会游泳啊！我要死啦，我要死啦！！！"
    narrator "快来个人救救我啊！！"
    w "咕噜咕噜…."

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    #【视角：夏静】
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667

    narrator "白天待在那个丫头家里的时间虽然很长，但是意外的倒是觉得过得很快。"
    narrator "就是导致了今天原本要做的课题都没有做完。"
    show x 考虑02 at ct with dissolve
    x "随便记录一下就行了吧。"
    narrator "最近做社会性观察也变得好无聊。"
    narrator "我不由得叹了口气。"
    narrator "想要用数据来证明人性，这群所谓的高级领导未免把自己放得太高了吧。"
    narrator "搞得跟自己不是人一样。"
    show x 考虑01 at ct with dissolve
    x "嗯？"
    narrator "就在我抱怨之际，我突然发现某一个地方的人突然全部聚集到了一起。"
    narrator "好像是发生了什么有趣的事情。"
    narrator "也许是哪个想不开的突然跳河了？"
    narrator "很有意思，去看一下人求生本能时候的样子似乎也不错。"
    narrator "抱着看热闹的状态我慢悠悠地走了过去。"
    narrator "在哪里扑腾扑腾的好像不是一个人。"
    narrator "而是一只动物，是一只猫。"
    narrator "我扶了扶眼镜…."
    show x 惊讶02 at ct with dissolve
    x "那….那不是袁艳家里的那只么？"
    narrator "我目瞪口呆地看着下面正在扑腾挣扎着的那只。"
    narrator "不愧是那丫头家里的存在，连挣扎都这么有个性，呜哇呜哇地叫着。"
    show x 惊讶01 at ct with dissolve
    x "啊，不对。"
    narrator "我在想什么鬼啊。"
    show x 惊讶02 at ct with dissolve
    x "话说袁艳那丫头现在在干嘛呢。"
    narrator "为什么她的猫会自己跑出来跳河？"
    "猫" "咕噜噜…"
    narrator "难不成她的猫都受不了她了吗？"
    "猫" "呜…."
    narrator "我觉得很有可能，看着眼前桥下就快要沉下去的猫。"
    
    #【CG：水下的美人鱼】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_xjm = True
    scene cg_夏救猫 with Dissolve(2)
    
    pause 1.0

    narrator "来不及多想，鞋子一脱，直接跳下了河岸。"
    narrator "下水的一瞬间，可笑的想法从我的脑海涌了出来。"
    narrator "啊….衣服要湿透了啊，这可得让那个小丫头好好付出点什么了。"
    narrator "不然啊….可就太吃亏了不是吗？"
    narrator "托住并不是很重的躯体，浮了起来。"
    w "呸呸呸…."
    narrator "河水有点深，而且这个河水让我感觉很不舒服。"
    narrator "下水道的味道在我嘴里扩散着。"
    narrator "难以言喻的恶心。"
    narrator "不过好在河流的流速并不是很快，而且我以前跟着某个教练学过游泳。"
    narrator "十米以内我的速度可是出人意料的快。"
    narrator "不过也只限十米….十米以后，就会发生很严重的问题。"
    
    #【CG结束】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    narrator "我的体力会下降得很快…."
    narrator "但是距离岸边至少有二十米…."
    "路人" "那个小姑娘溺水了！！"
    narrator "就是这样严重的地步，当然现在还没有完全溺水就是了。"
    narrator "其实我早就知道会发生这样的事情，所以我并不是直接朝着岸边游过去的。"
    narrator "而是朝着桥墩。"
    narrator "只要把这家伙扔到那上面去就可以了。"
    narrator "我是这么想的。"
    "猫" "唔喵…."
    narrator "猫无意识的惨叫声响起来的时候，伴随着‘噗通’一声。"
    narrator "它再一次掉到了水里。"
    narrator "啊….只是失了准头而已，砸到了墙上….应该没事吧。"
    narrator "我连忙游了过去，把这东西又抓了起来。"
    #show x 惊异 at ct with dissolve
    x "抱…抱歉啦。"
    narrator "然后怀着稍微有一点….可能一点都没有的愧疚感再一次脱手。"
    narrator "一条优美的抛物线出现的时候，我不由得笑了笑。"
    narrator "这预示着我又赢了。"
    narrator "笑着…然后腿抽筋了。"
    narrator "当一件事情好坏几率相同的时候，事情往往会朝着糟糕的方向发展——墨菲定律。"
    narrator "当然在事情最初我已经预计好了，只是身体不小心比理性和大脑快了一步。"
    narrator "所以一直可以规避的墨菲定律，今天终于又发生了。"
    narrator "为什么是又？"
    narrator "最近好像染上了奇怪的习惯，这样的关头都还能这样想，到底是谁传染给我的。"
    narrator "明明身体开始在河里挣扎，但是内心反而愈来愈平静。"
    narrator "仿佛这一刻早就应该来临一样。"
    narrator "最后的时光里头，似乎渐渐地可以体会袁艳眼里那份淡淡的绝望了。"
    narrator "然而，这个时候一个穿着白色衬衫的身影从上方跃了下来….真是令人讨厌的家伙。"
    narrator "呵呵……"
    narrator "程祎琳，看来我要欠你一个人情了。"

    scene black with dissolve

    jump c_in_1


#（程祎琳线）
label c_in_1:

    #"（注解：程祎琳个人线）"

    $_dismiss_pause = False

    $c_in_1_select = True

    nvl clear
    nvl hide
    window hide dissolve
    #【场景：河边】
    scene river_白天 with dissolve:
        zoom .667

    narrator "不知不觉地就跑到了河岸……"
    narrator "虽然说道河岸最先想到的应该是那个叫做夏静的女孩子。"
    narrator "但是平心而论的话，我对林琴和夏静这两个丫头并不是很亲近。"
    narrator "估计找她们也不可能有多大的作用。"
    narrator "其实找这三个丫头压根就不靠谱。"
    narrator "可是我也没有依靠的对象了。"
    narrator "这个人类的世界里头，我所认识的仅这四人。"
    narrator "最可笑的事情是，明明我们可以与她们正常交谈。"
    narrator "但是却除了被诅咒的袁艳以外，我不能对另外的三个开口哪怕说一句话。"
    narrator "不只是一句话。而是所有带有暗示性的行动都不行。"
    narrator "……."
    narrator "找都找了，干脆找那个跟我比较亲近的程祎琳好了。"
    narrator "只不过在这里我并没有看见那个女孩子的身影。"
    narrator "明明能够感觉到她们就在这里的气息。"
    narrator "可是无论我如何去追寻，我无法追寻到任何有关她们的影子。"
    narrator "我穿梭在人群里头，迷茫地寻找着。"
    narrator "心中的压力逐渐地凝聚，背负着那丫头生命的使命让我有点喘不过气来。"
    narrator "但是我还是得去寻找。"
    narrator "这丫头还真是各种意义上会给猫添麻烦啊。"
    narrator "她难道就不知道羞愧嘛。"
    narrator "虽然心里这么抱怨着，但是人还是要去寻找的。"
    narrator "要是愿袁艳那个丫头在这种时期掉链子的话。"
    narrator "就算是我也会觉得特别头疼的。"
    narrator "毕竟我也没办法判断这三个丫头究竟哪个是要出问题的人。"
    narrator "靠赌的虽然也可以，不过我还是想听听袁艳究竟是怎么想的。"
    narrator "所以程祎琳到底在什么地方?"
    w "喵…."
    "小孩" "啊，找到了找到了！"
    narrator "几个莫名熟悉的小孩声音在我的身后响起。"
    narrator "让我顿时汗毛竖起，不至于吧….追这么远？"
    narrator "在我回首的一瞬间，一双手环过了我的腹部，直接把我夹住拖走了。"
    w "喵！！！"
    narrator "现在的小孩都这么执着的吗？"
    narrator "几个小孩彼此争闹的声音在我耳边响起。"
    narrator "这种感觉似曾相识——那是在与袁艳相遇以前的事情。"
    narrator "似乎也有过这样的事情呢。"
    narrator "只是犯一点点错误就被打入深渊，周围环绕的全是敌人。"
    narrator "稍加不注意便会万劫不复。"
    narrator "虽然后来侥幸逃到了人间就是了。"
    narrator "不过现在这个光景让我有和之前有相同的危机感。"
    narrator "我觉得…这几个小孩把我扛走一定不会是做什么好事。"
    narrator "果然…这群小孩不知道从哪里找到了绳子把我绑了起来，在某个没有多少人的小树林空地。"
    narrator "跟袁艳的绑法完全不一样，有了对比我才发现。"
    narrator "这群家伙们是完全不在意我的死活直接胡乱勒紧。"
    narrator "喘不过气来不说，还特别疼。"
    narrator "你们就不知道照顾一下我这只老年猫么？尊老爱幼不会啊！"
    narrator "袁艳的五花大绑跟这几个熊孩子的绑法比起来简直能用温柔来形容。"
    w "……."
    narrator "我是怎样现在才还有心情去对比这种事情啊。"
    narrator "更加让我无语的是这种时候才有吐槽余裕的自己。"
    narrator "且不说这个，这几个小孩到底是想要干什么啊。"
    narrator "看他们拿着小瓶子装着水。"
    narrator "放在由几个石头砌成的小灶上面，下面的火不断地向小瓶子传递着恐怖的温度。"
    narrator "不一会儿小瓶子里头的水就沸腾了起来。"
    narrator "隔着老远我都能听到瓶子里头水冒泡的声音。"
    narrator "我越发地不安了起来。"
    narrator "咽了口口水，这群小鬼到底是想什么？"
    narrator "很快….我就知道了。"
    narrator "就在我看到小瓶子瓶口某个肢体动物尸体随着沸腾的水上下浮动时候。"
    narrator "我的心顿时就凉了半截。"
    narrator "尽管我不知道他们到底要干什么，可是强烈的危机感让我已经不由自主地颤抖了起来。"
    "小孩1" "熟了吧…."
    "小孩2" "应该熟了…."
    "小孩1" "来，给小宝宝端上去吃吧。"
    "小孩3" "好耶！"
    narrator "小宝宝？端给小宝宝？"
    narrator "谁是小宝宝？"
    narrator "那个瓶子里头的东西要给小宝宝吃吗？"
    narrator "这个小宝宝那还真是倒霉啊。"
    narrator "真是庆幸自己跟着袁艳在一起的这段日子锻炼出了强大的抗压能力。"
    narrator "在这种情况下还能轻松地调侃。"
    narrator "调…侃？"
    narrator "为什么他们要把那看起来装满了各种小虫子尸体的瓶子端到我面前来？"
    narrator "不会吧….不会吧…."
    narrator "难不成他们说的小宝宝是我？"
    narrator "顿时我就傻了眼。"
    "小孩1" "筷子啊！没有筷子怎么喂 啊！"
    "小孩2" "快快快，去找筷子。"
    narrator "看着因为筷子这一物品忙碌起来的几个孩子。"
    narrator "这个场景似乎似曾相识….袁艳似乎也喂我吃过些古怪的东西…."
    narrator "但是那东西好歹能吃啊，这个东西….空气中飘荡的带一点草香味让我越发恐惧了起来。"
    narrator "这并不是能让我开心得起来的味道，不如说闻这味道到以后连吃别的东西的心情都没有了。"
    narrator "我的心乱如麻。"
    narrator "不行，我不能就这样坐以待毙。"
    narrator "瓶子就在我身前不远处，如果我想办法打翻那个东西的话……."
    narrator "可能会死….但是就是死我也不想吃那东西啊。"
    w "……."
    narrator "蠕动着身子，在没有被几个小孩发现的时候。"
    narrator "一点一点地靠近了瓶子。"
    w "（小声）这简直太轻松了。"
    narrator "稍微动了动屁股，瓶子很轻松地被我弄倒了。"
    w "喵~"
    narrator "有点烫，我的妈呀。"
    narrator "瓶子直接倒在了我的身上，然后……."
    w "喵！！！！！"
    narrator "我宛如杀猪般的叫声凄厉地在这片小树林响了起来。"
    narrator "话说为什么会是杀猪般的叫声……."
    narrator "而且我干啥这种时候都能想这种事啊！！！"
    narrator "杀猪声瞬间吸引了几个小孩的视线。"
    narrator "其中一个小孩立马发现了我的情况，立刻跑到了我边上。"
    narrator "将我拖离了危险区域，那是一大片温度超高的水组成的区域。"
    narrator "痛得我呲牙咧嘴。"
    narrator "之后几个熊孩子便聚集在一起讨论了起来。"
    narrator "我看着皱着眉头的她们不由得咧了咧嘴。"
    narrator "跟我斗，你们还太嫩了。"
    narrator "以为我是谁啊！我可是神圣的猫精灵啊。"
    narrator "虽然付出的代价也有点惨重就是了。"
    narrator "我屁股的那一大块背脊区疼得都麻木了，好像被什么拉扯着皮一样。"
    "小孩1" "啊…浪费了。"
    "小孩2" "这只猫怎么回事。"
    narrator "这个小孩似乎很生气，瞪了我一眼，因为离我近所以还踢了我一脚。"
    narrator "臭小子….我记住了。"
    "小孩3" "这样子….不太好吧。"
    narrator "这个小孩似乎还有点良心，而且刚刚就是她把我拖出危险区域的，"
    "小孩2" "好不容易弄出来的…都泼了。"
    narrator "他指着地上并不是很多的虫子尸体…让我有些毛骨悚然的反而是瓶口向着我的瓶子里面。"
    narrator "密密麻麻各式各样的小虫子蜷着肢体，有的都被煮的泛白了。"
    w "……."
    "小孩1" "应该还剩下一些。"
    "小孩1" "好不容易抓到它，总得喂它吃点吧。"
    "小孩1" "不然我们辛苦做出来的东西就全部浪费了噢。"
    "小孩2" "我同意。"
    "小孩3" "我….我也同意。"
    w "……."
    narrator "我不同意！！！"
    narrator "内心的抗议可惜他们是听不到的。"
    narrator "可是即便如此我也绝对不能开口用他们能够听懂的语言说出这一切。"
    narrator "而且就算说出来这几个熊孩子搞不好完全不会放过我了。"
    narrator "………"
    narrator "但是我是不会屈服的。"
    w "唔猫~！！！"
    narrator "我凄厉的叫声警示着这几个家伙。"
    narrator "但是根本无法阻止他们。"
    narrator "他们强硬地夹住了我，然后直接扳开了我的嘴。"
    narrator "接下来的事情不用脑子想都能知道会发生什么。"
    w "唔猫…."
    narrator "抗拒着，但是那令我浑身发麻的触感还是顺着两根棍子，伸入了我的嘴里。"
    narrator "我的..."
    narrator "不争气的眼泪又稀里哗啦地流出来了。"

    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    scene river_白天 with dissolve:
        zoom .667

    #【视角转变：程祎琳】
    narrator "好想睡在她家里……."
    narrator "最近总觉得自己有点点心神不宁…一定是因为之前吃的东西味道的原因。"
    narrator "最近总觉得自己会回想起很多事…一定是因为之前听艳仔说了奇怪的话。"
    narrator "最近总觉得自己比以前过得开心….一定是因为艳仔家里的猫可爱的原因。"
    show c 侧视01 at ct with dissolve
    c "唔…."
    narrator "嘴里还有一点点味道，不过只有这么一点点的话还是能够承受得了的。"
    "猫" "唔猫！！！！"
    narrator "凄厉的叫声，我愣了愣。"
    narrator "然后不由自主地就朝着声音所在的地方走了过去。"
    narrator "那个….好像是….艳仔家里的猫？？？"
    show c 斜视01 at ct with dissolve
    c "那是？"
    narrator "那群小孩子在对它做什么？"
    narrator "为什么要拿虫子喂它？"
    show c 张嘴01 at ct with dissolve
    c "啊….（慌张）"
    narrator "许多不好的回忆瞬间涌上了脑海。"
    narrator "看着猫挣扎的模样，记忆里头相同的画面浮现了出来。"
    c "不对….我不要…."
    narrator "身体里头涌出了奇怪的情绪。"

    #【CG：凄厉的幸存者】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)
    $renpy.pause(3,hard=True)
    $ persistent.cg_takeknifeG = True
    scene cg_拿刀少女 with Dissolve(2)
    
    pause 1.0

    narrator "我捡起了地上的碎玻璃碎片，紧紧地攥在了手里，露出一点尖头。"
    narrator "微微的割痛感从我的手掌心传到我的脑海。"
    narrator "才让我短暂的时间没有被奇怪情绪给冲昏头脑。"
    narrator "一步一步…."
    narrator "我紧紧地捏着的玻璃碎片一步一步地朝着他们走去。"
    narrator "我不知道我在干什么，但是我知道我做的事情是对的。"
    narrator "我只是想去救它….或者说…我想救昔日的那个自己。"
    "小孩1" "这猫怎么老是乱动啊。"
    "小孩2" "揍几下就好了。"
    narrator "说完便动手捶了猫几下。"
    "小孩3" "啊！有人过来了。"
    narrator "三个孩子看到我的时候，瞬间露出了恐惧的眼神。"
    narrator "他们看着我，大概是惧怕血的样子，都不由自主被吓得后退了好几步。"
    narrator "我…好像已经控制不住了…."
    "小孩3" "快跑！"
    narrator "有个小孩大概是看出来我的状态了，连忙大声喊着。"
    narrator "说着小孩们像是被吓破了胆一样把猫扔在了一旁跑了起来。"
    narrator "可是，你们跑得掉么？"
    narrator "呼啸的风从我的耳边吹过，回过神的时候，我已经把一个小孩紧紧地压在了身下。"
    narrator "小孩恐惧地…害怕地看着我，满眼都是泪水，吓得一句话都说不出来了。"
    narrator "他的脸上还有着被地面擦伤的痕迹。"
    narrator "我手里还捏着的玻璃渣高举着，似乎随时有可能落下。"
    narrator "如果不是及时回过神来，我想我现在压住的也许是一个小孩子的尸体也说不定。"
    narrator "不知道为什么，这个时候我却想起了袁艳。"
    narrator "然后我不由得看了看袁艳的猫咪。"
    narrator "它静静地躺在了那里，也不知道情况怎么样了。"
    
    #【CG结束】
    nvl clear
    nvl hide
    window hide dissolve
    scene black with Dissolve(.7)

    scene river_白天 with Dissolve(.7)
    
    show c 斜视01 at ct with dissolve
    c "……"
    narrator "然后我看了看面前的小孩。"
    narrator "把手上沾满了血的玻璃片给扔了。"
    narrator "指着艳仔的猫说着。"
    show c 斜视02 at ct with dissolve
    c "说…说…对不起。"
    "小孩2" "……."
    narrator "他已经完全被吓傻了。"
    narrator "我拍了拍手掌，确认上面没有玻璃碎渣之后，直接扇了这个小孩一巴掌。"
    show c 恶心02 at ct with dissolve
    c "说…对不起。"
    "小孩2" "啊…对…对不起！！！！"
    narrator "确认了他的声音以后，我放开了他。"
    "小孩2" "哇…."
    narrator "这个小孩大声哭了起来。"
    "小孩2" "对不起….对不起…."
    narrator "然而这个时候我已经不在意这些事情了。"
    narrator "只管着自己抱着猫离开了这里。"

    jump c3