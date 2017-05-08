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

from contextlib import contextmanager
from functools import partial
from SublimeLinter.lint import PythonLinter, highlight, persist, util


class Pydocstyle(PythonLinter):
    """Provides an interface to the pydocstyle python module/script."""

    syntax = 'python'
    cmd = 'pydocstyle@python'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.3.0'
    regex = r'^.+?:(?P<line>\d+).*:\r?\n\s*(?P<message>.+)$'
    multiline = True
    default_type = highlight.WARNING
    error_stream = util.STREAM_STDERR
    line_col_base = (1, 0)  # uses one-based line and zero-based column numbers
    tempfile_suffix = 'py'
    module = 'pydocstyle'
    defaults = {
        '--add-ignore=': '',
        '--add-select=': ''
    }
    inline_overrides = [
        'add-ignore',
        'add-select'
    ]

    def check(self, code, filename):
        """Run pydocstyle on code and return the output."""
        args = self.build_args(self.get_view_settings(inline=True))

        if persist.settings.get('debug'):
            persist.printf('{} args: {}'.format(self.name, args))

        conf = self.module.config.ConfigurationParser()
        with partialpatched(conf,
                            '_parse_args',
                            args=args + [filename],
                            values=None):
            conf.parse()

        errors = []
        for fname, checked_codes, ignore_decorators in \
                conf.get_files_to_check():
            errors.extend(
                self.module.check(
                    [fname],
                    select=checked_codes,
                    ignore_decorators=ignore_decorators))

        return errors


@contextmanager
def partialpatched(obj, name, **kwargs):
    """Monkey patch instance method with partial application."""
    pre_patched_value = getattr(obj, name)
    setattr(obj, name, partial(pre_patched_value, **kwargs))
    yield
    setattr(obj, name, pre_patched_value)
