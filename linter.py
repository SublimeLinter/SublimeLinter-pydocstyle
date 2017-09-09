#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015-2016 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Pydocstyle plugin linter class."""

from SublimeLinter.lint import PythonLinter, highlight, util


class Pydocstyle(PythonLinter):
    """Provides an interface to the pydocstyle python module/script."""

    syntax = 'python'
    if PythonLinter.which('pydocstyle'):
        cmd = 'pydocstyle@python'
    else:
        cmd = 'pep257@python'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.3.0'
    regex = r'^.+?:(?P<line>\d+).*:\r?\n\s*(?P<message>.+)$'
    multiline = True
    default_type = highlight.WARNING
    error_stream = util.STREAM_BOTH
    line_col_base = (0, 0)  # pydocstyle uses one-based line and zero-based column numbers
    tempfile_suffix = 'py'
    defaults = {
        '--add-ignore=': ''
    }
    inline_overrides = ('add-ignore')
