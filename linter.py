from contextlib import contextmanager
import os
import tempfile

from SublimeLinter.lint import PythonLinter
from SublimeLinter.lint.linter import TransientError


class Pydocstyle(PythonLinter):
    cmd = 'pydocstyle ${temp_file}'
    regex = r'''(?x)
        ^(?P<filename>.+):(?P<line>\d+)[^`\n]*(`(?P<near>.+)`)?.*:\n
        \s*(?P<warning>D\d{3}):\s(?P<message>.+)
    '''
    multiline = True
    line_col_base = (1, 0)  # uses one-based line and zero-based column numbers
    tempfile_suffix = 'py'
    defaults = {
        'selector': 'source.python',
        '--add-ignore=': '',
        '--add-select=': '',
        '--ignore=': '',
        '--select=': '',
        '--config=': '',
        '--convention=': '',
        '--ignore-decorators=': ''
    }

    def tmpfile(self, cmd, code, suffix=None):
        filename = (
            self.context.get('file_name')
            or "{}{}".format(
                self.context['canonical_filename'][1:-1],
                suffix or self.get_tempfile_suffix()
            )
        )
        with self._make_temp_file(filename, code) as temp_filename:
            self.context['file_on_disk'] = self.filename
            self.context['temp_file'] = temp_filename
            cmd = self.finalize_cmd(
                cmd, self.context, at_value=temp_filename, auto_append=True)
            return self._communicate(cmd)

    @contextmanager
    def _make_temp_file(self, filename, code):
        folder_prefix = "{}-".format(self.plugin_name)
        with tempfile.TemporaryDirectory(prefix=folder_prefix) as tmp_dir_name:
            temp_filename = os.path.join(tmp_dir_name, filename)
            with open(temp_filename, "w+b") as file:
                file.write(bytes(code, "utf-8"))

            try:
                yield temp_filename
            finally:
                os.remove(temp_filename)

    @property
    def plugin_name(self):
        return self.__class__.__module__.split(".", 1)[0]

    def on_stderr(self, stderr):
        # For a doc style tester, parse errors can be treated 'transient',
        # for the benefit, that we do not re-draw, but keep the errors from
        # the last run.
        if 'Cannot parse file' in stderr:
            raise TransientError('Parse error.')

        return super().on_stderr(stderr)

    def split_match(self, match):
        match = super().split_match(match)
        if match.near and '__init__' not in match.message:
            return match._replace(
                message='{} `{}`'.format(match.message, match.near))

        return match
