
import os

from libqtile import bar, qtile, widget
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import (BorderDecoration,
                                             PowerLineDecoration,
                                             RectDecoration)
from widgets.new_open_weather import OpenWeatherMap

from .dracula_color import *
from .settings import *

bar_style = dict(
    background=BAR_BACKGROUND,
    border_color=BAR_BACKGROUND,
    margin=[0, 0, 0, 0])

power_line = {
    "decorations": [
        BorderDecoration(border_width=[0, 0, 2, 0], colour='white'),
    ]
}


def init_bar():
    return [
        widget.Image(
            filename=ICON_DIR + 'arch-logo.png',
            margin=4,
            background=WIDGET_BG,
            mouse_callbacks={'Button1': lambda : qtile.cmd_spawn('rofi -show run')}
        ),
        widget.Chord(background=bright_red, fmt=bold("MODE: ") + "{}"),
        widget.GroupBox(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            active=GROUPBOX_ACTIVE,
            inactive=GROUPBOX_INACTIVE,
            disable_drag=True,
            highlight_color=WIDGET_BG,
            highlight_method='line',
            this_current_screen_border=GROUPBOX_THIS_CURRENT_SCREEN_BORDER,
            this_screen_border=GROUPBOX_THIS_SCREEN_BORDER,
            other_current_screen_border=GROUPBOX_OTHER_CURRENT_SCREEN_BORDER,
            other_screen_border=GROUPBOX_OTHER_SCREEN_BORDER,
            borderwidth=3,
        ),
        widget.CurrentLayoutIcon(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            # custom_icon_paths = [ICON_DIR],
            scale=0.55,
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.WindowCount(
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.WindowTabs(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
        ),
        widget.CPU(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            active=GROUPBOX_ACTIVE,
            format='󰓅 {freq_current}GHz',
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(POPUP_TERMINAL + ' -e htop')},
            decorations=[
                BorderDecoration(
                    colour = BORDER_CPU,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.ThermalSensor(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            format='{temp:.1f}{unit}',
            tag_sensor='Core 0',
            threshold=90.0,
            decorations=[
                BorderDecoration(
                    colour = BORDER_CPU,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.Memory(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            format=" {MemUsed:.2f}{mm}" ,measure_mem='G',
            mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(POPUP_TERMINAL + ' -e htop')},
            decorations=[
                BorderDecoration(
                    colour = BORDER_MEM,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.OpenWeather(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            location='Podgorica',
            format='{icon} {main_temp}',
            decorations=[
                BorderDecoration(
                    colour = BORDER_WEATHER,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.Net(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            format='↓↑{down}', #'󰕒 {up} 󰇚 {down} ↓↑ {total}'
            decorations=[
                BorderDecoration(
                    colour = BORDER_NET,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.Systray(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
        ), # X11
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=2,
        ),
        widget.CheckUpdates(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            update_interval = 1800,
            distro = "Arch_checkupdates",
            display_format = "🗘 {updates}",
            no_update_string = "🗘 Up",
			# colour_have_updates = self.color.white,
			# colour_no_updates = self.color.white
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(POPUP_TERMINAL + ' -e yay -Syu')},
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        # widget.StatusNotifier(), # wayland
        widget.UPowerWidget(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            text_charging='{percentage:.0f}% {ttf}',
            text_discharging='{percentage:.0f}% {ttf}',
            percentage_low=0.25,
            percentage_critical=0.12,
        ),
        # widget.GenPollText(
        #     name='uptime',
        #     update_interval=1,
        #     func = lambda: subprocess.check_output("/home/green/.config/qtile/scripts/uptime.sh").decode("utf-8"),
        # ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=1,
        ),
        widget.Clock(
            format=f" %H:%M %d.%m",
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            decorations=[
                BorderDecoration(
                    colour = BORDER_CLOCK,
                    border_width = [0, 0, 2.5, 0],
                )
            ],
        ),
        widget.Sep(
                background=WIDGET_BG,
                foreground=WIDGET_BG,
                linewidth=4,
        ),
        widget.TextBox(
            background=WIDGET_BG,
            foreground=WIDGET_FG,
            fmt=' ',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn('archlinux-logout')},
        ),
        # widget.QuickExit(
        #     background=WIDGET_BG,
        #     foreground=WIDGET_FG,
        #     default_text=' ',
        #     countdown_format='{} '
        # ),
    ]