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
