################################################################################
## Initialization
################################################################################
default persistent.playername = "佚名"

label splashscreen:
    $ renpy.movie_cutscene("Lighter_PV.mpg")


################################################################################
## Initialization
################################################################################

init offset = -1

define config.main_menu_music = 'music/晨曦_主控.wav'

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"
        

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 1000
    
    if quick_menu:
            
        button:
            pos(747,685)
            xmaximum 70 ymaximum 25
            xfill True yfill True
            idle_background "gui/quickmenu/快速保存.png"
            hover_background "gui/quickmenu/快速保存按钮002.png"
            action QuickSave()

        button:
            pos(815,685)
            xmaximum 70 ymaximum 25
            xfill True yfill True
            idle_background "gui/quickmenu/快速读取按钮.png"
            hover_background "gui/quickmenu/快速读取按钮002.png"
            action QuickLoad()

        add "gui/quickmenu/快速读取按钮.png" pos(815,685)
            
        button:
            pos(885,685)
            xmaximum 70 ymaximum 25
            xfill True yfill True
            idle_background "gui/quickmenu/保存按钮.png"
            hover_background "gui/quickmenu/保存按钮002.png"
            action ShowMenu("save")

        button:
            pos(940,685)
            xmaximum 70 ymaximum 25
            xfill True yfill True
            idle_background "gui/quickmenu/读取按钮.png"
            hover_background "gui/quickmenu/读取按钮002.png"
            action ShowMenu("load")


        button:
            #xpos 955 ypos 680
            pos(1000,680)
            xmaximum 34 ymaximum 34
            xfill True yfill True
            idle_background "gui/quickmenu/对话框系统按钮.png"
            hover_background "gui/quickmenu/对话框系统按钮002.png"
            action ShowMenu("preferences")
            
        add "gui/quickmenu/对话框上一个选择按钮.png" pos(1045,680)
        #pos(1000,680)
        button:
            #xpos 1000 ypos 680
            pos(1045,680)
            xmaximum 34 ymaximum 34
            xfill True yfill True
            idle_background "gui/quickmenu/对话框上一个选择按钮.png"
            hover_background "gui/quickmenu/对话框上一个选择按钮002.png"
            action Rollback()
            
        button:
            #xpos 1050 ypos 680
            pos(1090,680)
            xmaximum 34 ymaximum 34
            xfill True yfill True
            #idle_background "gui/quickmenu/对话框播放按钮.png"
            #hover_background "gui/quickmenu/对话框播放按钮002.png"
            idle_background "gui/quickmenu/对话框下一个选择按钮.png"
            hover_background "gui/quickmenu/对话框下一个选择按钮002.png"
            action Preference("auto-forward", "toggle")
            
        #button:
        #    xpos 1090 ypos 680
        #    xmaximum 34 ymaximum 34
        #    xfill True yfill True
        #    idle_background "gui/quickmenu/对话框下一个选择按钮.png"
        #    hover_background "gui/quickmenu/对话框下一个选择按钮002.png"
        #    action ShowMenu("save")
        #add "gui/quickmenu/对话框下一个选择按钮.png" pos(1090,680)
            
        add "gui/quickmenu/对话框快进按钮.png" pos(1135,680)
        button:
            xpos 1135 ypos 680
            xmaximum 34 ymaximum 34
            xfill True yfill True
            idle_background "gui/quickmenu/对话框快进按钮.png"
            hover_background "gui/quickmenu/对话框快进按钮002.png"
            action Skip() alternate Skip(fast=False, confirm=True)
            
        button:
            xpos 1180 ypos 680
            xmaximum 34 ymaximum 34
            xfill True yfill True
            idle_background "gui/quickmenu/对话框文本按钮.png"
            hover_background "gui/quickmenu/对话框文本按钮002.png"
            action ShowMenu("history")
            
        button:
            xpos 1225 ypos 680
            xmaximum 34 ymaximum 34
            xfill True yfill True
            idle_background "gui/quickmenu/对话框关闭按钮.png"
            hover_background "gui/quickmenu/对话框关闭按钮002.png"
            #action MainMenu()
            action HideInterface()

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    if main_menu:
            
        imagebutton:
            xpos 60 ypos 290
            idle "gui/navigation/ks开始游戏001.png"
            hover "gui/navigation/ks开始游戏002.png"
            action Start()
                
        imagebutton:
            xpos 60 ypos 350
            xmaximum 240 ymaximum 80
            idle "gui/navigation/ks继续游戏001.png"
            hover "gui/navigation/ks继续游戏002.png"
            action ShowMenu("load")

        imagebutton:
            xpos 60 ypos 410
            idle "gui/navigation/ks个人故事.png"
            hover "gui/navigation/ks个人故事2.png"
            action ShowMenu("dlc_grx")

        imagebutton:
            xpos 60 ypos 470
            idle "gui/navigation/ks环境设定001.png"
            hover "gui/navigation/ks环境设定002.png"
            action ShowMenu("preferences")

        imagebutton:
            xpos 60 ypos 530
            idle "gui/navigation/ks鉴赏001.png"
            hover "gui/navigation/ks鉴赏002.png"
            action ShowMenu("gallery")
                
        imagebutton:
            xpos 60 ypos 590
            idle "gui/navigation/ks结束游戏001.png"
            hover "gui/navigation/ks结束游戏002.png"
            action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

##DLC#########################################################################
init -100 python:
    
    def findfile(tarfile,path):
        import os
        indi_dlc =False
        filelist= []
        for root, dirs, files in os.walk(path):
            filelist= files

        for i in filelist:
            a = str(i)
            if i == tarfile:
                return True
        return False

screen dlc_grx():

    style_prefix "main_menu"

    add gui.main_menu_background
    
    frame:
        add 'gui/maincover.png'
        add 'gui/mainlogo.png'

        if renpy.exists("/scripts/dlc_confirm.rpy"):
        #if findfile('dlc_confirm.rpy',"./game/scripts"):
            imagebutton:
                xpos 135 ypos 300
                idle "gui/dlc/x_dlc_idle.png"
                hover "gui/dlc/x_dlc_hover.png"
                action Start("x_indi_1")
        else:
            imagebutton:
                xpos 135 ypos 300
                idle "gui/dlc/x_dlc_idle.png"
                hover "gui/dlc/x_dlc_hover.png"
                action NullAction()
        
        text _("夏静个人线"):
            xalign .5
            xpos 230 ypos 410
            size 18 color "000"
        
        if renpy.exists("/scripts/dlc_confirm.rpy"):
        #if findfile('dlc_confirm.rpy',"./game/scripts"):
            imagebutton:
                xpos 135 ypos 430
                idle "gui/dlc/l_dlc_idle.png"
                hover "gui/dlc/l_dlc_hover.png"
                action Start("l_indi_1")
        else:
            imagebutton:
                xpos 135 ypos 430
                idle "gui/dlc/l_dlc_idle.png"
                hover "gui/dlc/l_dlc_hover.png"
                action NullAction()
        
        text _("林琴个人线"):
            xalign .5
            xpos 230 ypos 540
            size 18 color "000"

        if renpy.exists("/scripts/dlc_confirm.rpy"):
        #if findfile('dlc_confirm.rpy',"./game/scripts"):
            imagebutton:
                xpos 135 ypos 560
                idle "gui/dlc/c_dlc_idle.png"
                hover "gui/dlc/c_dlc_hover.png"
                action Start("c_indi_1")
        else:
            imagebutton:
                xpos 135 ypos 560
                idle "gui/dlc/c_dlc_idle.png"
                hover "gui/dlc/c_dlc_hover.png"
                action NullAction()
        
        text _("程祎琳个人线"):
            xalign .5
            xpos 230 ypos 670
            size 18 color "000"
            
        imagebutton:
            xalign .5
            xpos 100 ypos 630
            idle "gui/dlc/返回.png"
            hover "gui/dlc/返回2.png"
            action Hide("dlc_grx",transition=dissolve)

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        add 'gui/maincover.png'
        add 'gui/mainlogo.png'

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    #if gui.show_name:

        #vbox:
            #text "[config.name!t]":
                #style "main_menu_title"

            #text "[config.version]":
                #style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    #xsize 280
    xfill True
    yfill True

    #background "gui/overlay/main_menu.png"

#style main_menu_vbox:
  #  xalign 1.0
  #  xoffset -20
  #  xmaximum 800
  #  yalign 1.0
  #  yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    button:
        xpos 1180 ypos 730
        xmaximum 148 ymaximum 44
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/返回游戏001.png"
        hover_background "gui/sl/返回游戏002.png"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            text _("All the copy right belongs to Yuki AVG Production Team.")
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    
    frame:
        add "gui/sl/保存.png" pos(-4,-4)

    tag menu
    
    button:
        xpos 208 ypos 268
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/1.png"
        hover_background "gui/sl/1.2.png"
        action FilePage(1)

    button:
        xpos 208 ypos 375
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/3.png"
        hover_background "gui/sl/3.2.png"
        action FilePage(3)
            
    button:
        xpos 208 ypos 482
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/5.png"
        hover_background "gui/sl/5.2.png"
        action FilePage(5)
            
    button:
        xpos 208 ypos 589
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/7.png"
        hover_background "gui/sl/7.2.png"
        action FilePage(7)
        
    button:
        xpos 125 ypos 321
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/2.png"
        hover_background "gui/sl/2.2.png"
        action FilePage(2)
        
    button:
        xpos 125 ypos 428
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/4.png"
        hover_background "gui/sl/4.2.png"
        action FilePage(4)
            
    button:
        xpos 125 ypos 535
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/6.png"
        hover_background "gui/sl/6.2.png"
        action FilePage(6)
        
    button:
        xpos 125 ypos 642
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/8.png"
        hover_background "gui/sl/8.2.png"
        action FilePage(8)
        
    button:
        xpos 1180 ypos 730
        xmaximum 148 ymaximum 44
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/返回游戏001.png"
        hover_background "gui/sl/返回游戏002.png"
        action Return()
        
    button:
        xpos 480 ypos 730
        xmaximum 148 ymaximum 44
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/navigation/返回标题按钮.png"
        hover_background "gui/navigation/返回标题按钮002.png"
        action MainMenu()
    
    fixed:
        grid 2 3:
            style_prefix "slot"
            xalign 0.65 yalign 0.6
            xspacing 70
            for i in range(2 * 3):
                $ slot = i + 1
                button:
                    action FileAction(slot)
                    add FileScreenshot(slot) xalign 0.5 yalign 0.5
                    text FileTime(slot, format=_("{#file_time}%A, %Y年%B%d日, %H:%M"), empty=_("empty slot")):
                       style "slot_time_text"
                       ypos 150
                    #text FileSaveName(slot):
                    #   style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
    
    #use file_slots(_("储存"))

screen load():
    
    add "gui/sl/读取.png"

    tag menu
    
    
    button:
            xpos 208 ypos 268
            xmaximum 67 ymaximum 66
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/sl/1.png"
            hover_background "gui/sl/1.2.png"
            action FilePage(1)

    button:
        xpos 208 ypos 375
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/3.png"
        hover_background "gui/sl/3.2.png"
        action FilePage(3)
            
    button:
            xpos 208 ypos 482
            xmaximum 67 ymaximum 66
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/sl/5.png"
            hover_background "gui/sl/5.2.png"
            action FilePage(5)
            
    button:
            xpos 208 ypos 589
            xmaximum 67 ymaximum 66
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/sl/7.png"
            hover_background "gui/sl/7.2.png"
            action FilePage(7)
            
    button:
        xpos 125 ypos 321
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/2.png"
        hover_background "gui/sl/2.2.png"
        action FilePage(2)
        
    button:
        xpos 125 ypos 428
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/4.png"
        hover_background "gui/sl/4.2.png"
        action FilePage(4)
            
    button:
        xpos 125 ypos 535
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/6.png"
        hover_background "gui/sl/6.2.png"
        action FilePage(6)
        
    button:
        xpos 125 ypos 642
        xmaximum 67 ymaximum 66
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/8.png"
        hover_background "gui/sl/8.2.png"
        action FilePage(8)
        
    button:
        xpos 1180 ypos 730
        xmaximum 148 ymaximum 44
        xalign 1.0 xoffset -20
        yalign 1.0 yoffset -20
        xfill True yfill True
        idle_background "gui/sl/返回游戏001.png"
        hover_background "gui/sl/返回游戏002.png"
        action Return()
    
    fixed:
        grid 2 3:
            style_prefix "slot"
            xalign 0.65 yalign 0.6
            xspacing 70
            for i in range(2 * 3):
                $ slot = i + 1
                button:
                    action FileAction(slot)
                    add FileScreenshot(slot) xalign 0.5 yalign 0.5
                    text FileTime(slot, format=_("{#file_time}%A, %Y年%B%d日, %H:%M"), empty=_("empty slot")):
                       style "slot_time_text"
                       ypos 150
                    #text FileSaveName(slot):
                    #   style "slot_name_text"
                    key "save_delete" action FileDelete(slot)

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_button:
    xmaximum 280 ymaximum 165
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences    

screen preferences():
    
    tag menu
    
    frame:
        add "gui/slider/环境设置.png" pos(-4,-4)
        
        add "gui/slider/preferences_text/文章设置.png" pos(350 , 150)
        add "gui/slider/preferences_text/wz003.png" pos(350 , 220)
        add "gui/slider/preferences_text/wz005.png" pos(350 , 290)
        add "gui/slider/preferences_text/MaxMin.png" pos(370 , 273)
        add "gui/slider/preferences_text/MaxMin.png" pos(370 , 348)
        
        add "gui/slider/preferences_text/音量设置.png" pos(770 , 150)
        add "gui/slider/preferences_text/yl002.png" pos(770 , 220)
        add "gui/slider/preferences_text/yl003.png" pos(770 , 290)
        add "gui/slider/preferences_text/yl004.png" pos(770 , 370)
        
        add "gui/slider/preferences_text/MaxMin.png" pos(790 , 273)
        add "gui/slider/preferences_text/MaxMin.png" pos(790 , 348)
        add "gui/slider/preferences_text/MaxMin.png" pos(790 , 423)

        button:
            xpos 1180 ypos 730
            xmaximum 148 ymaximum 44
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/sl/返回游戏001.png"
            hover_background "gui/sl/返回游戏002.png"
            action Return()
            
    vbox:
        #hbox:
        #    box_wrap True
            #if renpy.variant("pc"):
            #    vbox:
            #        style_prefix "radio"
            #        label _("显示模式")
            #        textbutton _("窗口") action Preference("display", "window")
            #        textbutton _("全屏幕") action Preference("display", "fullscreen")

            #vbox:
            #    style_prefix "radio"
            #    label _("Rollback Side")
            #    textbutton _("Disable") action Preference("rollback side", "disable")
            #    textbutton _("Left") action Preference("rollback side", "left")
            #    textbutton _("Right") action Preference("rollback side", "right")
            
            #vbox:
            #    style_prefix "check"
            #    label _("快进模式")
            #    textbutton _("Unseen Text") action Preference("skip", "toggle")
            #    textbutton _("选项后") action Preference("after choices", "toggle")
            #    textbutton _("转场特效") action InvertSelected(Preference("transitions", "toggle"))

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        #null height (4 * gui.pref_spacing)

        hbox:
            pos(350,150)
            style_prefix "slider"
            box_wrap True
            
            vbox:  
                #label _("文字显示速度")
                bar value Preference("text speed") ypos 130
                #label _("自动模式等待时间")
                bar value Preference("auto-forward time") ypos 180
                
            vbox:
                xpos -30
                if config.has_music:
                    #label _("音乐音量")
                    hbox:
                        bar value Preference("music volume") ypos 130

                if config.has_sound:
                    #label _("音效音量")
                    hbox:
                        bar value Preference("sound volume") ypos 180
                        if config.sample_sound:
                            textbutton _("测试") action Play("sound", config.sample_sound)
                            
                if config.has_voice:
                    #label _("语音音量")
                    hbox:
                        bar value Preference("voice volume") ypos 230
                        if config.sample_voice:
                            textbutton _("测试") action Play("voice", config.sample_voice)
                            
                #if config.has_music or config.has_sound or config.has_voice:
                #    null height gui.pref_spacing
                #    textbutton _("Mute All"):
                #        action Preference("all mute", "toggle")
                #        style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xpos 55
    xsize 230

style slider_button:
    maximum(31,30)
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html



screen history():
    
    add "gui/history/文本界面底图.png" pos(-2,-2)
    add "gui/history/文本界面边框.png" pos(-2,-2)
    add "gui/history/文本界面文字.png" pos(50,240)

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False


    use game_menu(_(""), yinitial=1.0):
        
        style_prefix "history"
        
        viewport:
            area (-100,-60,1280,720)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            
            vbox:
                for h in _history_list:
                    window:
                        ## This lays things out properly if history_height is None.
                        has fixed:
                           yfit True
                        if h.who:
                            label h.who:
                                style "history_name"
                                ## Take the color of the who text from the Character, if
                                ## set.
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what
                if not _history_list:
                    #label _("The dialogue history is empty.")
                    label _("历史对话为空")

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True yfill True
    #ysize gui.history_height
    ysize 130
    xpos -80

style history_name:
    color "#000000"
    #xpos gui.history_name_xpos
    #xanchor gui.history_name_xalign
    xpos -10
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    color "#000000"
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

        
## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助文档"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    #add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                button:
                    maximum(148,44)
                    idle_background "gui/confirm/是.png"
                    hover_background "gui/confirm/是002.png"
                    action yes_action
                button:
                    maximum(148,44)
                    idle_background "gui/confirm/否.png"
                    hover_background "gui/confirm/否002.png"
                    action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    font "SourceHanSansCN-Heavy.otf"
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"
                           
        xalign 0.5
        yalign 1.0

        textbutton _("返回") action Rollback()
        textbutton _("快进模式") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("自动") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600

    

## Gallery screen #################################################################
screen gallery():
    
    modal True
    tag menu
    
    frame:
        add "gui/gallery/cg欣赏.png" pos(-4,-4)

        button:
            xpos 1180 ypos 730
            xmaximum 148 ymaximum 44
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/gallery/返回游戏001.png"
            hover_background "gui/gallery/返回游戏002.png"
            action Return()
    
        ##################################################################################
        
        button:
            pos(400 , 310)
            maximum(264 , 98)
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/gallery/tx袁艳001.png"
            hover_background "gui/gallery/tx袁艳002.png"
            action Show("yg"),Hide("xg"),Hide("lg"),Hide("cyg")
            #action Return()
            
        button:
            pos(400 , 410)
            maximum(264 , 98)
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/gallery/tx夏静001.png"
            hover_background "gui/gallery/tx夏静002.png"
            action Show("xg"),Hide("yg"),Hide("lg"),Hide("cyg")
            
        button:
            pos(400 , 510)
            maximum(264 , 98)
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/gallery/tx林琴001.png"
            hover_background "gui/gallery/tx林琴002.png"
            action Show("lg"),Hide("yg"),Hide("xg"),Hide("cyg")
            
        button:
            pos(400 , 610)
            maximum(264 , 98)
            xalign 1.0 xoffset -20
            yalign 1.0 yoffset -20
            xfill True yfill True
            idle_background "gui/gallery/tx程祎琳001.png"
            hover_background "gui/gallery/tx程祎琳002.png"
            action Show("cyg"),Hide("yg"),Hide("lg"),Hide("xg")
            
            
            
################################################################################
#default persistent.girl = True
default persistent.cg_ys = False
default persistent.cg_dxj = False
default persistent.cg_sw = False
default persistent.cg_byyx = False
default persistent.cg_eyz = False
default persistent.cg_swz = False

default persistent.cg_blackxz = False
default persistent.cg_zzz = False
default persistent.cg_yzhy = False
default persistent.cg_2wsw = False
default persistent.cg_yot = False
default persistent.cg_yzdxj = False
default persistent.cg_xjm = False
default persistent.cg_takeknifeG = False

## C_INDIVIDUAL#######################################
default persistent.cg_c_cc = False
default persistent.cg_c_cc2 = False
default persistent.cg_c_dbc = False
default persistent.cg_c_wx = False
default persistent.cg_c_czz = False
default persistent.cg_c_f = False
default persistent.cg_c_yb = False
default persistent.cg_c_zszr1 = False
default persistent.cg_c_zszr2 = False
default persistent.cg_c_yz = False
default persistent.cg_c_mmdys = False
default persistent.cg_c_sd = False
default persistent.cg_c_sd2 = False
default persistent.cg_c_ct = False
default persistent.cg_c_ydcq = False
default persistent.cg_c_gd = False
default persistent.cg_c_cdss = False
default persistent.cg_c_sw = False
default persistent.cg_c_cn = False
default persistent.cg_c_yd = False
default persistent.cg_c_dk = False
default persistent.cg_c_wcbq = False
default persistent.cg_c_ls = False
default persistent.cg_c_hg = False
default persistent.cg_c_xk = False
default persistent.cg_c_dk = False
default persistent.cg_c_znxc = False

## X_INDIVIDUAL#######################################
default persistent.cg_x_bf = False
default persistent.cg_x_bf_n = False
default persistent.cg_x_sn = False
default persistent.cg_x_sn_n = False
default persistent.cg_x_happyday = False
default persistent.cg_x_readn = False
default persistent.cg_x_read_weak = False
default persistent.cg_x_read_one = False
default persistent.cg_x_sleep = False
default persistent.cg_x_wq = False
default persistent.cg_x_study = False
default persistent.cg_x_studyhard = False
default persistent.cg_x_studyhard_n = False
default persistent.cg_x_boysleep = False
default persistent.cg_x_happytest = False
default persistent.cg_x_bg = False
default persistent.cg_x_zl = False
default persistent.cg_x_sick = False
default persistent.cg_x_cx_dark = False
default persistent.cg_x_cx_turn = False
default persistent.cg_x_cx_turn_smile = False
default persistent.cg_x_cx_confuse = False
default persistent.cg_x_genius = False
default persistent.cg_x_yz = False
default persistent.cg_x_gc = False

######################################################


default persistent.cg_xc = False
default persistent.cg_ydz1 = False
default persistent.cg_ydz2 = False
default persistent.cg_jsz = False
default persistent.cg_jsz_smile = False
default persistent.cg_pcq = False
default persistent.cg_psz = False
default persistent.cg_lxj = False
default persistent.cg_mf = False

default persistent.cg_end2 = False
default persistent.cg_girlcat = False
default persistent.cg_jh1 = False
default persistent.cg_jh2 = False

default persistent.cg_cylcry = False
default persistent.cg_xjcry = False


screen yg():
    
    predict False
    style_prefix "history"
    
    if renpy.get_screen("gallery") and renpy.get_screen("yg"):
        viewport:
            yinitial 0.0
            area (500 , 196 , 680 , 400)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            if persistent.cg_ys:
                add "gui/gallery/cg/k_浴室.png"
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_浴室.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_浴室.jpg")
            else:
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()
                     
            if persistent.cg_eyz:
                add "gui/gallery/cg/k_耳语者.png" xpos 325
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_耳语者.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_耳语者.jpg")
            else:
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()

##############################################################
######
##############################################################
screen cyg():
    
    predict False
    style_prefix "history"
    
    if renpy.get_screen("gallery") and renpy.get_screen("cyg"):
        viewport:
            yinitial 0.0
            area (500 , 196 , 680 , 400)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            if persistent.cg_sw:
                add "gui/gallery/cg/k_泪水中的守望.png"
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_泪水中的守望.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_泪水中的守望.jpg")
            else:
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()
                    
            if persistent.cg_byyx:
                add "gui/gallery/cg/k_别有用心的馈赠.png" xpos 325
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_别有用心的馈赠.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_别有用心的馈赠.jpg")
            else:
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()

##############################################################
######
##############################################################
screen lg():
    
    predict False
    style_prefix "history"
    
    if renpy.get_screen("gallery") and renpy.get_screen("lg"):
        viewport:
            yinitial 0.0
            area (500 , 196 , 680 , 400)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            
            if persistent.cg_dxj:
                add "gui/gallery/cg/k_发狂的大小姐.png"
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_发狂的大小姐.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_发狂的大小姐.jpg")
            else:
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()

##############################################################
######
##############################################################
screen xg():
    
    predict False
    style_prefix "history"
    
    if renpy.get_screen("gallery") and renpy.get_screen("xg"):
        viewport:
            yinitial 0.0
            area (500 , 196 , 680 , 400)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True

            if persistent.cg_eyz:
                add "gui/gallery/cg/k_耳语者.png"
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_耳语者.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_耳语者.jpg")
            else:
                button:
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()
                    
            if persistent.cg_byyx:
                add "gui/gallery/cg/k_别有用心的馈赠.png" xpos 325
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_别有用心的馈赠.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_别有用心的馈赠.jpg")
            else:
                button:
                    xpos 325
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()
                    
            if persistent.cg_eyz:
                add "gui/gallery/cg/k_隐藏的守望者.png" ypos 200
                button:
                    ypos 200
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg/k_隐藏的守望者.png"
                    hover_background "gui/gallery/cg框透明.png"
                    action Show("collection_slot", name = "images/cg/cg_隐藏的守望者.jpg")
            else:
                button:
                    ypos 200
                    maximum(307 , 173)
                    idle_background "gui/gallery/cg框01.png"
                    hover_background "gui/gallery/cg框01.png"
                    action NullAction()
                    
                    
####Show Specitife########################################################################
screen collection_slot(name):
    zorder 999
    modal True
    imagebutton:
        idle "black.jpg"
        action Hide("collection_slot")
        
    imagebutton:
        idle im.FactorScale(name, 1)
        action Hide("collection_slot")
