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

import os

# If possible, import pep257 and use it directly for better performance
try:
    from pep257 import check_source
except ImportError:
    check_source = None

from SublimeLinter.lint import highlight, PythonLinter, Registrar


class Pep257Meta(Registrar):

    """
    Metaclass for Pep257 that dynamically sets the 'cmd' attribute.

    If a linter can work both using an executable and built in code,
    the best way to deal with that is to set the cmd class attribute
    during class construction. This allows the linter to take advantage
    of the rest of the SublimeLinter machinery for everything but run().

    """

    def __init__(cls, name, bases, attrs):
        # If pep257 could not be imported, use the executable.
        # We have to do this before super().__init__ because
        # that registers the class, and we need this attribute set first.
        if check_source is None:
            setattr(cls, 'cmd', ('pep257@python', '-'))
        else:
            setattr(cls, 'cmd', None)

        super().__init__(name, bases, attrs)


class Pep257(PythonLinter, metaclass=Pep257Meta):

    """Provide an interface to the pep257 python script."""

    language = 'python'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)'
    default_type = highlight.WARNING
    line_col_base = (1, 0)  # pep257 uses one-based line and zero-based column numbers

    def run(self, cmd, code):
        """Run pep257 on the source and return the output."""
        if check_source is None:
            return super().run(cmd, code)
        else:
            try:
                errors = check_source(code, os.path.basename(self.filename))
            except:
                errors = []

            return '\n'.join([str(e) for e in errors])
