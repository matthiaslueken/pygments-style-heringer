# -*- coding: utf-8 -*-
"""
    pygments-style-heringer
    ~~~~~~~~~~~~~~~~~~~~~~~

    Based on the default highlighting style.

    :copyright: Copyright 2021 Matthias Lüken
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class DefaultStyle(Style):
    """
    The Heringer style.
    """

    background_color = "#F4F5F5"
    default_style = ""

    styles = {
        Whitespace:                "#869191",
        Comment:                   "italic #00668F",
        Comment.Preproc:           "noitalic #F55A00",

        #Keyword:                   "bold #FF0A33",
        Keyword:                   "bold #7DF28B",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #A3001B",

        Operator:                  "#342E37",
        Operator.Word:             "bold #FF0A33",

        Name.Builtin:              "#7DF28B",
        Name.Function:             "#00a1e0",
        Name.Class:                "bold #00a1e0",
        Name.Namespace:            "bold #00a1e0",
        Name.Exception:            "bold #FF5E5B",
        Name.Variable:             "#00668F",
        Name.Constant:             "#A3001B",
        Name.Label:                "#FFE74C",
        Name.Entity:               "bold #869191",
        Name.Attribute:            "#B5F8BD",
        Name.Tag:                  "bold #7DF28B",
        Name.Decorator:            "#FF0A33",

        String:                    "#A3001B",
        String.Doc:                "italic",
        String.Interpol:           "bold #FFA91F",
        String.Escape:             "bold #F55A00",
        String.Regex:              "#FFA91F",
        #String.Symbol:             "#B8860B",
        String.Symbol:             "#00a1e0",
        String.Other:              "#7DF28B",
        Number:                    "#342E37",

        Generic.Heading:           "bold #00668F",
        Generic.Subheading:        "bold #F55A00",
        Generic.Deleted:           "#A3001B",
        Generic.Inserted:          "#0CAC64",
        Generic.Error:             "#FF0A33",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #00a1e0",
        Generic.Output:            "#869191",
        Generic.Traceback:         "#00a1e0",

        Error:                     "border:#FF0A33"
    }
