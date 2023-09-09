import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import (Click, Drag, DropDown, Group, Key, Match,
                             ScratchPad, Screen)
from libqtile.lazy import lazy
from models.keybind import keys
from models.settings import *
from models.widget import bar_style, init_bar

groups = [
    Group(name='1', label='󰖟', matches=[Match(wm_class=MAIN_BROWSER)], layout='max'),
    Group(name='2', label='', matches=[Match(wm_class='code')], layout='max'),
    Group(name='3', label='󰆍'),
    Group(name='4', label=''),
    Group(name='5', label='󰧉'),
    Group(name='6', label=''),
]
for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()) )
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen()) )

groups.extend([
    ScratchPad("browser_dev", [DropDown("browser_dev", "firefox", x=0.05, y=0.03, width=0.90, height=0.90, on_focus_lost_hide=False)]),
    ScratchPad("browser_search", [DropDown("browser_search", "microsoft-edge-stable", x=0.05, y=0.05, width=0.90, height=0.90, on_focus_lost_hide=False)]),
    ScratchPad("popup_terminal", [DropDown("popup_terminal", "alacritty", x=0.15, y=0.15, width=0.70, height=0.70, on_focus_lost_hide=False)]),
    ScratchPad("discord", [DropDown("discord", 'discord', x=0.1, y=0.15, width=0.80, height=0.70, on_focus_lost_hide=False)]),
    ScratchPad("obsidian", [DropDown("obsidian", 'obsidian', x=0.08, y=0.10, width=0.84, height=0.80, on_focus_lost_hide=False)]),
    ScratchPad("telegram", [DropDown("telegram", 'telegram-desktop', x=0.08, y=0.10, width=0.84, height=0.80, on_focus_lost_hide=False)]),
    ScratchPad("spotify", [DropDown("spotify", 'alacritty -e ncspot', x=0.15, y=0.15, width=0.70, height=0.70, on_focus_lost_hide=False)]),
    ScratchPad("file_manager", [DropDown("file_manager", 'alacritty -e lf', x=0.15, y=0.15, width=0.70, height=0.70, on_focus_lost_hide=False)]),
    ScratchPad("postman", [DropDown("postman", 'postman', x=0.15, y=0.15, width=0.70, height=0.70, on_focus_lost_hide=False)]),
])


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4, margin=2),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=WIDGET_FONT,
    fontsize=WIDGET_FONT_SIZE,
    padding=3,
)
extension_defaults = widget_defaults.copy()



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Screens
screens = [
    Screen(top=bar.Bar(init_bar(), size=BAR_HEIGHT, **bar_style))
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="kitty"),
        Match(wm_class="xarchiver"),
        Match(wm_class='ark'),
        Match(wm_class='discord'),
        Match(wm_class='telegram'),
        Match(wm_class='bitwarden'),
        Match(wm_class='skype'),
        Match(wm_class='steam'),
        Match(title='Monitask'),
        Match(title='Initilization'),
        Match(title='Screenshots'),
        
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# Autostart
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser(SCRIPTS_DIR + 'autostart.sh')
    subprocess.call([home])
    
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


# Picture-in-Picture
sticky_windows = []

@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in sticky_windows:
        sticky_windows.remove(window)
        
@hook.subscribe.setgroup
def move_sticky_windows():
    for window in sticky_windows:
        window.togroup()
    return

@hook.subscribe.client_managed
def auto_sticky_windows(window):
   info = window.info()
   if info['name'] == 'Picture in picture':
       sticky_windows.append(window)


# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "QTile"
