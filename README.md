# shed - the sh editor

Don't run `curl | sh` again. Use `curl | shed` to verify scripts before running.

# Usage

Replace `sh` with `shed` in any pipe-sh commands you run. shed will:

* save the piped script to a temp file
* open the temp file in `$SHED_EDITOR` or `$EDITOR` to let you view and modify the script
* ask you if you still want to run the script, preserving any changes you made

# Installation

This is a Python 3 script, so use `pip3` to install:

```
pip3 install shed_sh
```

**Note the spelling:** `shed_sh` is different from `shed`.

After this, run `shed` or `bashed` from your terminal to verify it's installed properly.

# Examples

## Piping to sh

Take your questionable **curl**-pipe-sh or **wget**-pipe-sh command

```shell
curl -L https://npmjs.org/install.sh | sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

and use shed to view and edit your script before running it:

```shell
curl -L https://npmjs.org/install.sh | shed
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | shed
```

## Piping to bash

bashed protects your **bash** shell, too: take this unknown script

```shell
wget -q -O - https://fixubuntu.com/fixubuntu.sh | bash
```

and verify the contents before running:

```shell
wget -q -O - https://fixubuntu.com/fixubuntu.sh | bashed
```

# Config

Set your preferred editor:

```
export SHED_EDITOR=vim
```

shed also checks `$EDITOR`, then falls back to `nano`, `vim`, `vi`, and `emacs` in order.

# Alternatives

Python is probably overkill for something like this. I wrote this as a learning exercise, but there are definitely more concise ways to accomplish this goal.

@sunaku wrote a [short shell script](https://gist.github.com/sunaku/f5f79e20b6f92ab1e524) that does the exact same thing.

@christianbundy suggests using [vipe](http://linux.die.net/man/1/vipe): `curl -L https://npmjs.org/install.sh | vipe | sh`

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time. You can also tweet me at [@mplewis](http://twitter.com/mplewis) or email me at [matt@mplewis.com](mailto:matt@mplewis.com).

# License

Copyright (c) 2014 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).
