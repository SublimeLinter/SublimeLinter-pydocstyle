SublimeLinter-pydocstyle
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pydocstyle.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pydocstyle)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [pep257](https://github.com/PyCQA/pydocstyle). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `pep257` is installed on your system. To install `pep257`, do the following:

1. Install [Python](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `pydocstyle` by typing the following in a terminal:
   ```
   [sudo] pip install pydocstyle
   ```

**Note:** This plugin requires `pydocstyle` 0.3.0 or later.

### Linter configuration
In order for `pydocstyle` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `pydocstyle` is installed and configured, you can proceed to install the SublimeLinter-pydocstyle plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `pydocstyle`. Among the entries you should see `SublimeLinter-pydocstyle`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-pep257 provides its own setting which may also be used as an [inline override](http://www.sublimelinter.com/en/latest/settings.html#inline-overrides).

|Setting|Description|
|:------|:----------|
|add-ignore|A comma-separated list of error codes to add the the default ignore list|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pydocstyle linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
