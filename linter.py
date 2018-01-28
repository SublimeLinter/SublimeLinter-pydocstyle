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

from SublimeLinter.lint import PythonLinter


class Pydocstyle(PythonLinter):
    """Provides an interface to the pydocstyle python module/script."""

    syntax = 'python'
    cmd = 'pydocstyle'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.3.0'
    regex = r'^.+?:(?P<line>\d+).*:\r?\n\s*(?P<warning>D\d{3}):\s(?P<message>.+)$'
    multiline = True
    default_type = highlight.WARNING
    error_stream = util.STREAM_BOTH
    line_col_base = (1, 0)  # uses one-based line and zero-based column numbers
    tempfile_suffix = 'py'
    defaults = {
        '--add-ignore=': '',
        '--add-select=': '',
        '--ignore=': '',
        '--select=': '',
        '--config=': '',
        '--convention=': '',
        '--ignore-decorators=': ''
    }
    inline_overrides = [
        'add-ignore',
        'add-select',
        'ignore',
        'select',
        'config',
        'convention',
        'ignore-decorators'
    ]
