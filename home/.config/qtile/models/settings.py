
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

# Directory
HOME_DIR = '/home/green/'
QTILE_DIR = '.config/qtile/'
SCRIPTS_DIR = HOME_DIR + '.config/scripts/qtile/'
MODEL_DIR = HOME_DIR + QTILE_DIR +'models/'
ICON_DIR = HOME_DIR + QTILE_DIR +'icons/'

MAIN_BROWSER = 'google-chrome-stable'
TERMINAL = 'alacritty'
POPUP_TERMINAL = 'kitty'


# Panel configuration
BAR_HEIGHT = 32
WIDGET_FONT = "JetBrainsMono Nerd Font"
WIDGET_FONT_SIZE = 14