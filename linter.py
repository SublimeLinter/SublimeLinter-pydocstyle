from SublimeLinter.lint import PythonLinter, util, const


class Pydocstyle(PythonLinter):
    cmd = 'pydocstyle'
    regex = r'^.+?:(?P<line>\d+).*:\r?\n\s*(?P<warning>D\d{3}):\s(?P<message>.+)$'
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
