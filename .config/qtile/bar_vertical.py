from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowtabs import WindowTabs
from libqtile.widget.tasklist import TaskList
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.quick_exit import QuickExit
from libqtile.widget.sensors import ThermalSensor
from libqtile.widget.volume import Volume
from libqtile.widget.bluetooth import Bluetooth
from libqtile.widget.sep import Sep

from unicodes import right_arrow, left_arrow
from colors import gruvbox

### BAR ON SCREEN 1 ###
bar = Bar([
    QuickExit(
        countdown_format='',
        countdown_start=1,
        default_text='',
        background=gruvbox['arrow3'],
        foreground=gruvbox['bartext']
    ),

    Spacer(
        background=gruvbox['arrow3'],
        length=5
    ),

    Sep(
        background=gruvbox['arrow3'],
        foreground=gruvbox['sep'],
        size_percent=60,
        linewidth=1
    ),

    Spacer(
        background=gruvbox['arrow3'],
        length=1
    ),

    CheckUpdates(
        display_format="  {updates}" ,
        background=gruvbox['arrow3'],
        foreground=gruvbox['bartext']
    ),

    Systray(
        background=gruvbox['arrow3']
    ),

    Spacer(
        background=gruvbox['arrow3'],
        length=2
    ),

    right_arrow(
        gruvbox['arrow2'],
        gruvbox['arrow3']
    ),

    Clock(
        background=gruvbox['arrow2'],
        foreground=gruvbox['bartext'],
        format=' %Y-%m-%d %R'
    ),

    right_arrow(
        gruvbox['arrow1'],
        gruvbox['arrow2']
    ),

    Memory(
        format=' {MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}',
        background=gruvbox['arrow1'],
        foreground=gruvbox['bartext']
    ),

    right_arrow(
        gruvbox['arrow2'],
        gruvbox['arrow1']
    ),

    CPU(
        format='{load_percent}%',
        background=gruvbox['arrow2'],
        foreground=gruvbox['bartext']
    ),

    right_arrow(
        gruvbox['arrow1'],
        gruvbox['arrow2']
    ),

    ThermalSensor(
        format=" {temp:.1f}{°}",
        background=gruvbox['arrow1'],
        foreground=gruvbox['bartext']
    ),

    right_arrow(
        gruvbox['background'],
        gruvbox['arrow1']
    ),

    Spacer(length=8),

    TaskList(
        padding=3,
        highlight_method='block',
        border='#3a3a3a',
        unfocused_border='#262626',
        foreground=gruvbox['bartext']
    ),

    Spacer(8),

    left_arrow(
        gruvbox['background'],
        gruvbox['arrow1']
        ),

    CurrentLayout(
        background=gruvbox['arrow1'],
        foreground=gruvbox['bartext']
    ),

    left_arrow(
        gruvbox['arrow1'],
        gruvbox['arrow2']
    ),

    WindowCount(
        text_format='{num} 缾',
        background=gruvbox['arrow2'],
        foreground=gruvbox['bartext'],
        show_zero=True,
    ),

    left_arrow(
        gruvbox['arrow2'],
        gruvbox['groupboxbg']
    ),

    GroupBox(
        disable_drag=True,
        visible_groups=['8', '6', '4', 'Left'],
        active=gruvbox['groupboxactive'],
        inactive=gruvbox['groupboxinactive'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['groupboxcurrent'],
        borderwidth=0,
        highlight_color=gruvbox['groupboxbg'],
        background=gruvbox['groupboxbg']
    ),

    Spacer(
        length=5,
        background=gruvbox['arrow3']
    ),

    ], background=gruvbox['background'], size=24, margin=0, opacity=0.95)

### BAR ON SCREEN 2 ###
bar2 = Bar([
    GroupBox(
        disable_drag=True,
        visible_groups=['Right', '3', '5', '7'],
        active=gruvbox['groupboxactive'],
        inactive=gruvbox['groupboxinactive'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['groupboxcurrent'],
        borderwidth=0,
        highlight_color=gruvbox['groupboxbg'],
        background=gruvbox['groupboxbg']
    ),

    right_arrow(
        gruvbox['arrow2'],
        gruvbox['groupboxbg']
    ),

    WindowCount(
        text_format='{num} 缾',
        background=gruvbox['arrow2'],
        foreground=gruvbox['bartext'],
        show_zero=True,
    ),

    right_arrow(
        gruvbox['arrow1'],
        gruvbox['arrow2']
    ),

    CurrentLayout(
        background=gruvbox['arrow1'],
        foreground=gruvbox['bartext']
    ),

    right_arrow(
        gruvbox['background'],
        gruvbox['arrow1']
        ),

    Spacer(length=8),

    TaskList(
    padding=3,
    highlight_method='block',
    border='#3a3a3a',
    unfocused_border='#262626',
    foreground=gruvbox['bartext']
    ),

    Spacer(length=8),

    ], background=gruvbox['background'], size=24, margin=0, opacity=0.95)
