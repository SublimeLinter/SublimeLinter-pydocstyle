#
# pep257.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-pep257
# License: MIT
#

"""Exports the Pep257 linter class."""


from SublimeLinter.lint import highlight, PythonLinter


class Pep257(PythonLinter):

    """Provide an interface to the pep257 python script."""

    language = 'python'
    cmd = 'pep257@python'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<error>.+)'
    default_type = highlight.WARNING
    line_col_base = (1, 0)
    tempfile_suffix = '.py'
