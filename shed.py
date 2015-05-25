#!/usr/bin/env python3

"""
shed v1.0.0

Don't run "curl | sh" again.
Use "curl | shed" to verify scripts before running.

More info: http://github.com/mplewis/shed
"""

import sys
import shlex
import subprocess
import os
from shutil import which
from tempfile import NamedTemporaryFile


def default_editor():
    """
    The user's preferred editor. Tries the env vars $SHED_EDITOR and $EDITOR.
    If those variables aren't set, tries sensible-editor, editor, nano, vim,
    vi, and emacs.
    """
    editor_varibles = ('SHED_EDITOR', 'EDITOR')
    fallback_editors = ('sensible-editor',
                        'editor',
                        'nano',
                        'vim',
                        'vi',
                        'emacs')

    for var in editor_varibles:
        if var in os.environ:
            return os.environ[var]

    for editor in fallback_editors:
        if which(editor):
            return editor

    raise ValueError('Failed to find $SHED_EDITOR, $EDITOR, '
                     'nano, vim, vi, or emacs')


def open_editor(filename):
    """Opens the given file in the user's default editor."""
    try:
        editor = default_editor()
    except ValueError:
        print()
        print("Couldn't find a valid editor in $SHED_EDITOR or $EDITOR. "
              "Try setting one:")
        print('    export SHED_EDITOR=/path/to/my/editor')
        sys.exit(-1)
    editor_split = shlex.split(editor)
    if len(editor_split) > 1:
        editor_split.append(filename)
        subprocess.check_call(editor_split)
    else:
        subprocess.check_call([editor, filename])


def confirm_exec():
    """
    Confirm the user still wants to execute the script.
    Returns True for yes, False for no. No response defaults to yes.
    """

    print()  # Pretty print spacing
    raw_resp = input('Do you still want to execute this script? [Y/n]: ')

    while True:
        resp = raw_resp.strip().lower()
        if not resp:
            return False
        if 'yes'.startswith(resp):
            return True
        if 'no'.startswith(resp):
            return False
        raw_resp = input('Please respond with "yes" or "no" [y/N]: ')


def main():
    """Reads the script from stdin, edit it and execute it."""
    # Print a helpful message if this looks like a user ran it standalone
    my_name = os.path.basename(sys.argv[0])
    if sys.stdin.isatty():
        print('Usage: curl -L https://example.com/some_script.sh | {}'
              .format(my_name))
        return

    # Figure out if we're running as "shed" (sh) or "bashed" (bash).
    # Use sh as the default shell.
    if my_name == 'bashed':
        shell = 'bash'
    else:
        shell = 'sh'

    # Save arguments to be added to sh later.
    # These change later in the script, so be careful!
    extra_args = sys.argv[1:]

    # Get script from pipe
    script = sys.stdin.read()
    # After we consume stdin, we need to reopen it for interactive input
    tty = open('/dev/tty')
    os.dup2(tty.fileno(), 0)

    # Create a temp file to hold our piped script
    with NamedTemporaryFile() as temp:
        temp.write(script.encode('utf-8'))
        temp.flush()
        open_editor(temp.name)

        # Ask user for permission to execute modified script
        if confirm_exec():
            print()  # Pretty print spacing
            # Call selected shell with any extra args passed to shed
            args = [shell]
            args.extend(extra_args)
            args.append(temp.name)
            subprocess.call(args)


if __name__ == '__main__':
    main()
