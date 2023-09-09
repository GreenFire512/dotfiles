from libqtile.config import Key
from libqtile.lazy import lazy
from models.settings import *

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panesle
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    
    # Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "Tab", lazy.group.next_window(), desc=""),
    Key([mod, "shift"], "Tab", lazy.group.prev_window(), desc=""),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([mod], "r", lazy.reload_config(), desc="Reload the config"),
    # Key([mod, "control"], "p", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # ScratchPad
    Key([mod], "q", lazy.group["browser_dev"].dropdown_toggle("browser_dev")),
    Key([mod], "e", lazy.group["browser_search"].dropdown_toggle("browser_search")),
    Key([mod], "o", lazy.group["obsidian"].dropdown_toggle("obsidian")),
    Key([mod], "t", lazy.group["telegram"].dropdown_toggle("telegram")),
    Key([mod], "s", lazy.group["spotify"].dropdown_toggle("spotify")),
    Key([mod], "f", lazy.group["file_manager"].dropdown_toggle("file_manager")),
    Key([mod], "p", lazy.group["postman"].dropdown_toggle("postman")),
    Key([mod, 'shift'], "d", lazy.group["discord"].dropdown_toggle("discord")),
    Key([mod], "Return", lazy.group["popup_terminal"].dropdown_toggle("popup_terminal")),
]