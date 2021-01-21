# -*- coding: utf-8 -*-
"""
    pygments.style.ssms
    ~~~~~~~~~~~~~~~~~~~~~~~

    A Pygments style inspired by Microsoft SSMS but with modified colors.

    :copyright: Copyright 2021 Matthias Lüken
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Punctuation


class HeringerStyle(Style):
    """
    A Pygments style inspired by Microsoft SSMS but with modified colors.
    """

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Comment:                   "#0CAC64",
        Keyword:                   "#00a1e0",
        Operator:                  "#869191",
        Name:                      "#000000",
        Name.Function:             "#FFA91F",
        Name.Builtin:              "#7DF28B",
        Name.Class:                "#00a1e0",
        String:                    "#FF0A33",
        Error:                     "border:#FF0A33",
        Number:                    "#000000",
        Punctuation:               "#869191"
    }
