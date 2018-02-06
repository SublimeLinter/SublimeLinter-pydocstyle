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
import SublimeLinter.lint
from SublimeLinter.lint import PythonLinter, persist, util

if getattr(SublimeLinter.lint, 'VERSION', 3) > 3:
    from SublimeLinter.lint import const
    WARNING = const.WARNING
    cmd = 'pydocstyle'
    module = None
else:
    from SublimeLinter.lint import highlight
    WARNING = highlight.WARNING
    cmd = 'pydocstyle@python'
    module = 'pydocstyle'


class Pydocstyle(PythonLinter):
    """Provides an interface to the pydocstyle python module/script."""

    syntax = 'python'
    cmd = cmd
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.3.0'
    regex = r'^.+?:(?P<line>\d+).*:\r?\n\s*(?P<warning>D\d{3}):\s(?P<message>.+)$'
    multiline = True
    default_type = WARNING
    error_stream = util.STREAM_BOTH
    line_col_base = (1, 0)  # uses one-based line and zero-based column numbers
    tempfile_suffix = 'py'
    module = module
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

    if getattr(SublimeLinter.lint, 'VERSION', 3) < 4:
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
