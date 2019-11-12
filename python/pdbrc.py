"""pdbpp config."""
# pylint:disable=E1101,W0212

import pdb

from pygments.formatters import TerminalTrueColorFormatter
from pygments.lexers import Python3Lexer
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    String,
    Text,
)

# Palette (onedarkish)
white = '#abb2bf'
mono_2 = '#828997'
comment_grey = '#5c6370'
mono_4 = '#4b5263'
cyan = '#56b6c2'
light_blue = '#61afef'
blue = '#528bff'
purple = '#c678dd'
green = '#98c379'
red = '#e06c75'
dark_red = '#be5046'
dark_yellow = '#d19a66'
yellow = '#e5c07b'
black = '#24272e'
cursor_grey = '#282c34'
gutter_fg_grey = '#636d83'
special_grey = '#3b4048'
visual_grey = '#3e4452'
pmenu = '#333841'
syntax_fg = white
syntax_fold_bg = comment_grey


class OneDarkish(Style):
    """OneDarkish pygments style."""

    styles = {
        Text: syntax_fg,
        Error: red,
        Comment: comment_grey,
        Keyword: f'{purple} nobold',
        Keyword.Constant: green,
        Keyword.Namespace: purple,
        Name.Namespace: f'{syntax_fg} nobold',
        Name.Builtin: red,
        Name.Function: light_blue,
        Name.Class: f'{light_blue} nobold',
        Name.Decorator: light_blue,
        Name.Exception: yellow,
        Name.Variable.Magic: red,  # dunder methods
        Number: dark_yellow,
        Operator: purple,
        Operator.Word: f'{purple} nobold',
        Literal: green,
        Literal.String.Doc: f'{green} noitalic',
        Literal.String.Interpol: f'{light_blue} nobold',
        Literal.String.Escape: f'{light_blue} nobold',
        String: green,
    }


class Config(pdb.DefaultConfig):  # type: ignore
    """Actual pdbpp config."""

    prompt = '(Pdb++)> '
    sticky_by_default = True

    highlight = True
    use_pygments = True
    use_terminal256formatter = True
    filename_color = pdb.Color.yellow  # type: ignore
    # This also defines the color for echoed output (note it's an SRG code)
    line_number_color = '38;2;99;109;131'  # 636d83
    current_line_color = '48;2;40;44;52'  # 282c34

    def setup(self, pdb):  # pylint:disable=W0621
        """Override pdbpp mappings and colors."""
        # See https://github.com/antocuni/pdb/issues/36
        pdb_class = pdb.__class__
        # Aliases
        pdb_class.do_l = pdb_class.do_longlist
        pdb_class.do_ll = pdb_class.do_list
        pdb_class.do_st = pdb_class.do_sticky
        pdb_class.do_ev = pdb_class.do_edit
        pdb_class.do_ip = pdb_class.do_interact
        pdb_class.do_gf = pdb_class.do_frame
        # Colors
        pdb_class._lexer = Python3Lexer()
        pdb_class._fmt = TerminalTrueColorFormatter(style=OneDarkish)
