import os
import subprocess
from typing import List  # noqa: F401

from libqtile import hook

from libqtile import extension
from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
from libqtile.extension.command_set import CommandSet

from libqtile.layout.ratiotile import RatioTile
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

from libqtile.config import Click, Drag, KeyChord, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy

from colors import gruvbox

from bar import bar, bar2

mod1 = "Alt"
mod = "mod4"
myBrowser = "chromium"
myTerm = "alacritty"
###
### KEYBINDINGS ###
keys = [
        #ESSENTIALS
        Key([mod], "Return", lazy.spawn(myTerm), desc='Launches My Terminal'),
        Key([mod], "Tab", lazy.next_layout(), desc='Toggle through layouts'),
        Key([mod], "q",lazy.window.kill(), desc='Kill active window'),
        Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
        Key([mod, "shift"], "q",lazy.shutdown(), desc='Shutdown Qtile'),

        #SWITCH MONITOR FOCUS
        Key([mod], "Left", lazy.to_screen(0), desc='Move focus to next monitor'),
        Key([mod], "Right", lazy.to_screen(1), desc='Move focus to next monitor'),

        #WINDWOW CONTROLS
        Key([mod], "Down", lazy.layout.down(), desc='Move focus down in current stack pane'),
        Key([mod], "Up", lazy.layout.up(), desc='Move focus up in current stack pane'),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), lazy.layout.section_down(), desc='Move windows down in current stack'),
        Key([mod, "shift"], "Up",lazy.layout.shuffle_up(), lazy.layout.section_up(), desc='Move windows up in current stack'),
        Key([mod, "control"], "Left", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
        Key([mod, "control"], "Right", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc='Expand window (MonadTall), increase number in master pane (Tile)'),
        Key([mod, "control"], "n", lazy.layout.normalize(), desc='normalize window size ratios'),
        Key([mod, "control"], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
        Key([mod], "f", lazy.window.toggle_floating(), desc='toggle floating'),
        Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
        Key([mod], "z", lazy.window.toggle_minimize(), lazy.group.next_window(), desc="Minimize window"),

        #APPS
        Key([mod], "c", lazy.spawn(myBrowser), desc='Chromium'),
        Key([mod], "d", lazy.spawn("/usr/bin/discord"), desc='Discord'),
        Key([mod], "s", lazy.spawn("/usr/bin/spotify"), desc='Spotify'),
        Key([mod], "period", lazy.spawn("/usr/bin/pavucontrol"), desc='Pavucontrol'),
        Key([mod], "e", lazy.spawn("/usr/bin/emacs"), desc='Emacs'),
        Key([mod], "comma", lazy.spawn("/usr/bin/nm-connection-editor"), desc='NewtorkManager'),
        Key([mod], "o", lazy.spawn("/usr/bin/virtualbox"), desc='Virtualbox'),

        #URL
        Key([mod], "r", lazy.spawn("/home/jonalm/scripts/url/ticktick.sh"), desc='Ticktick'),
        Key([mod], "a", lazy.spawn("/home/jonalm/scripts/url/avanza.sh"), desc='Avanza'),
        Key([mod], "v", lazy.spawn("/home/jonalm/scripts/url/ig.sh"), desc='Ig'),
        Key([mod], "p", lazy.spawn("/home/jonalm/scripts/url/lastpass.sh"), desc='Lastpass'),
        Key([mod], "k", lazy.spawn("/home/jonalm/scripts/url/gmail.sh"), desc='Outlook'),
        Key([mod], "m", lazy.spawn("/home/jonalm/scripts/url/outlook.sh"), desc='Gail'),
        Key([mod], "y", lazy.spawn("/home/jonalm/scripts/url/youtube.sh"), desc='Youtube'),
        Key([mod], "t", lazy.spawn("/home/jonalm/scripts/url/tradingview.sh"), desc='Tradingview'),
        Key([mod], "b", lazy.spawn("/home/jonalm/scripts/url/swedbank.sh"), desc='Swedbank'),
        Key([mod], "g", lazy.spawn("/home/jonalm/scripts/url/github.sh"), desc='Github'),

        #TERM
        Key([mod], "n", lazy.spawn("/home/jonalm/scripts/term/nnn.sh"), desc='nnn'),
        Key([mod], "h", lazy.spawn("/home/jonalm/scripts/term/htop.sh"), desc='htop'),

        #DMENU
        Key([mod], "space", lazy.run_extension(DmenuRun(
        ### END KEYBINDINGS ###
        font="TerminessTTF Nerd Font",
        fontzise="13",
        dmenu_command="dmenu_run",
        dmenu_prompt=">",
        dmenu_height=10,
        background=gruvbox["dmenubg"],
        foreground=gruvbox["dmenufg"],
        selected_foreground=gruvbox["dmenuselfg"],
        selected_background=gruvbox["dmenubg"],
        ))),
        ] 

### GROUP SETTINGS ###
groups = [
        Group('Left', label="", matches=[Match(wm_class='myTerm'),Match(wm_class='/usr/bin/emacs'), Match(wm_class='')], layout="monadtall"),
        Group('Right', label="", matches=[Match(wm_class='chromium'), Match(wm_class='/usr/bin/spotify'),  Match(wm_class='/usr/bin/discord')], layout="monadtall"),
]

### MOVE WINDOW TO WORKSPACE ###
for i in groups:
    keys.extend([
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),desc="move focused window to group {}".format(i.name)),
        ])

### LAYOUT SETTINGS ###
layouts = [
    Stack(
        border_normal=gruvbox['windowoutline'],
        border_focus=gruvbox['windowfocus1'],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
    MonadTall(
        border_normal=gruvbox['windowoutline'],
        border_focus=gruvbox['windowfocus0'],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
    )
]


#FLOATING LAYOUT SETTINGS AND ASSIGNED APPS
floating_layout = Floating(
    border_normal=gruvbox['windowoutline'],
    border_focus=gruvbox['windowfocus1'],
    border_width=3,
    float_rules=[
        *Floating.default_float_rules,
        #APPS
        Match(wm_class="nitrogen"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="nm-connection-editor"),
        ])

#DRAG FLOATING LAYOUTS
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
    ]

### WIDGET SETTINGS ###
widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=13,
    padding=10,
    )

extension_defaults = widget_defaults.copy()

### DECLARING PANEL ###
screens = [Screen(top=bar), Screen(top=bar2)]  

### OTHER QTILE SETTINGS ###
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

