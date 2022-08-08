from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowtabs import WindowTabs
from libqtile.widget.tasklist import TaskList
from libqtile.widget.prompt import Prompt

from unicodes import right_arrow, left_arrow
from colors import gruvbox

### BAR ON SCREEN 1 ###
bar = Bar([
    GroupBox(
        disable_drag=True,
        active=gruvbox['groupboxactive'],
        inactive=gruvbox['groupboxinactive'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['groupboxcurrent'],
        borderwidth=0,
        highlight_color=gruvbox['groupboxbg'],
        background=gruvbox['groupboxbg']
    ),

    right_arrow(gruvbox['background'], gruvbox['groupboxbg']),
    Spacer(8),
    TaskList(padding=3, highlight_method='block', border='#3a3a3a',unfocused_border='#262626', foreground=gruvbox['bartext']),

    left_arrow(gruvbox['background'], gruvbox['arrow1']),
    WindowCount(text_format='{num} 缾', background=gruvbox['arrow1'], foreground=gruvbox['bartext'], show_zero=True,),
    
    left_arrow(gruvbox['arrow1'], gruvbox['arrow2']),
    CurrentLayout(background=gruvbox['arrow2'], foreground=gruvbox['bartext']),

    ], background=gruvbox['background'], size=24, margin=0, opacity=0.95)

### BAR ON SCREEN 2 ###
bar2 = Bar([
    CurrentLayout( background=gruvbox['arrow2'], foreground=gruvbox['bartext']),
    right_arrow(gruvbox['arrow1'], gruvbox['arrow2']),

    WindowCount(text_format='缾 {num}', background=gruvbox['arrow1'], foreground=gruvbox['bartext'], show_zero=True,),

    right_arrow(gruvbox['background'], gruvbox['arrow1']),
    Spacer(8),
    TaskList(padding=3, highlight_method='block', border='#3a3a3a',unfocused_border='#262626', foreground=gruvbox['bartext']),

    left_arrow(gruvbox['background'], gruvbox['arrow1']),
    CPU(format=' {freq_current}GHz {load_percent}%', background=gruvbox['arrow1'], foreground=gruvbox['bartext']),

    left_arrow(gruvbox['arrow1'], gruvbox['arrow2']),
    Memory(format=' {MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}', background=gruvbox['arrow2'], foreground=gruvbox['bartext']),

    left_arrow(gruvbox['arrow2'], gruvbox['arrow1']),
    Net(format='↓ {down} ↑{up}', background=gruvbox['arrow1'], foreground=gruvbox['bartext']),

    left_arrow(gruvbox['arrow1'], gruvbox['arrow2']),
    Clock(background=gruvbox['arrow2'], foreground=gruvbox['bartext'], format=' %Y-%m-%d %R'),

    left_arrow(gruvbox['arrow2'], gruvbox['arrow1']),
    Systray(background=gruvbox['arrow1']),

    Spacer(length=15, background=gruvbox['arrow1'])

    ], background=gruvbox['background'], size=24, margin=0, opacity=0.95)
