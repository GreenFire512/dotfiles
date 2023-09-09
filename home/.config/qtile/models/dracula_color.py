bg = "#282A36"
fg = "#F8F8F2"
selection = "#44475A"
selection_transparent = "#44475A80"
comment = "#6272A4"
red = "#FF5555"
orange = "#FFB86C"
yellow = "#F1FA8C"
green = "#50fa7b"
purple = "#BD93F9"
cyan = "#8BE9FD"
pink = "#FF79C6"
bright_red = "#FF6E6E"
bright_green = "#69FF94"
bright_yellow = "#FFFFA5"
bright_blue = "#D6ACFF"
bright_magenta = "#FF92DF"
bright_cyan = "#A4FFFF"
bright_white = "#FFFFFF"
menu = "#21222C"
visual = "#3E4452"
gutter_fg = "#4B5263"
nontext = "#3B4048"

# Basic Colors
BLACK = '#111111'
WHITE = '#ffffff'
GREY = '#333333'

# Colors classes
BAR_BACKGROUND = selection
WIDGET_BG = selection
WIDGET_FG = bright_white
GROUPBOX_ACTIVE = WHITE
GROUPBOX_INACTIVE = gutter_fg
GROUPBOX_THIS_SCREEN_BORDER = purple
GROUPBOX_OTHER_SCREEN_BORDER = GREY
GROUPBOX_THIS_CURRENT_SCREEN_BORDER = purple
GROUPBOX_OTHER_CURRENT_SCREEN_BORDER = GREY
WINDOW_FOCUSED_BORDER = bright_white
WINDOW_BORDER = visual
BORDER_CPU = bright_green
BORDER_MEM = bright_yellow
BORDER_WEATHER = bright_magenta
BORDER_NET = bright_cyan
BORDER_TRAY = bright_green
BORDER_CLOCK = purple

def bold(text: str):
    """ Return text between bold tags """
    return f'<b>{text}</b>'