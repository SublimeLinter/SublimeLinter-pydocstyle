from SublimeLinter.lint import PythonLinter, util, const


class Pydocstyle(PythonLinter):
    cmd = 'pydocstyle'
    regex = r'''(?x)
        ^(?P<filename>.+):(?P<line>\d+)[^`\n]*(`(?P<near>.+)`)?.*:\n
        \s*(?P<warning>D\d{3}):\s(?P<message>.+)
    '''
    multiline = True
    default_type = const.WARNING
    error_stream = util.STREAM_BOTH
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

    def split_match(self, match):
        match = super().split_match(match)
        if match.near and '__init__' not in match.message:
            return match._replace(
                message='{} `{}`'.format(match.message, match.near))

        return match
