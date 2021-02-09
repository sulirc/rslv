# rslv ⛳️

Use rslv to register any resource path and then resolve it as an alias name.

# Installation

Copy script below and run in CLI.

```bash
bash <(curl -s https://raw.githubusercontent.com/sulirc/rslv/main/install.sh)
```

# Usage

## Basic

Register resoure path to your favourite name:

```bash
rslv -r @examples "/Users/sulirc/Desktop/webpack/examples/"
```

List all alias:

```bash
rslv -l

@react => ~/Desktop/workspace/projects/react
@examples => /Users/sulirc/Desktop/webpack/examples/
```

And then try to use it in your terminal:

```bash
cd $(rslv -e @examples)
```

it will expand to `cd ~/Desktop/workspace/projects/react`

Similarly, rslv can be used in many ways, see below:

```bash
# open ~/Desktop/workspace/projects/react/
open $(rslv -e @react)

# open editor of folder ~/Desktop/workspace/projects/react/
code $(rslv -e @react)

# use less command to view ~/Desktop/workspace/projects/react/README.md
less $(rslv -e @react/README.md)
```

Imagine any shell command which can combine with rslv :)

## Advance

Wrap rslv command in shell alias, and then use `rslv` in an even shorter way. (Just like the original way)

Copy script below and run in CLI.

```bash
SHFILE=

if [ -n "$ZSH_VERSION" ]; then
  SHFILE='.zshrc'
elif [ -n "$BASH_VERSION" ]; then
  SHFILE='.bashrc'
else
  echo "rslv: unsupported shell" >&2
  return
fi

cat <<'EOF' >>~/$SHFILE

# rslv - CLI alias resolve ⛳️
# https://github.com/sulirc/rslv
# 
# usage: rslv [-h] [-v] [-e EXPAND] [-l] [-r REGISTER REGISTER] [-R UNREGISTER] [-c CHANGE CHANGE]
# 
# CLI-Resolve(rslv): Make and resolve alias in CLI. ⛳️
# 
# optional arguments:
#   -h, --help            show this help message and exit
#   -v, --version         show program's version number and exit
#   -e EXPAND, --expand EXPAND
#                         expand alias
#   -l, --list            List all registered alias
#   -r REGISTER REGISTER, --register REGISTER REGISTER
#                         Register an alias
#   -R UNREGISTER, --unregister UNREGISTER
#                         Unregister an alias
#   -c CHANGE CHANGE, --change CHANGE CHANGE
#                         Change existed alias to a new alias
# 
# Enjoy rslv and have fun. More information please refer to https://github.com/sulirc/rslv
# 
# @version 0.1.0
# @author sulirc

_rslv_extend_cd() {
  cd $(rslv -e "$1")
}

_rslv_extend_open() {
  open $(rslv -e "$1")
}

_rslv_extend_code() {
  code $(rslv -e "$1")
}

_rslv_extend_less() {
  less $(rslv -e "$1")
}

_rslv_extend_cat() {
  cat $(rslv -e "$1")
}

alias rcd=_rslv_extend_cd
alias ropen=_rslv_extend_open
alias rcode=_rslv_extend_code
alias rless=_rslv_extend_less
alias rcat=_rslv_extend_cat
EOF
```

And then open a new terminal window, try to use rcd/ropen/rcode/rless/rcat.

```bash
rslv -l
Registered alias list:
@rslv => /Users/yanguangjie/Desktop/cli-resolve
@react => /Users/yanguangjie/Desktop/workspace/projects/react
```

Use rcd to cd registered path by alias

```bash
rcd @react
```

Use ropen to open registered path by alias

```bash
ropen @react
```

etc.

Hope you enjoy~ 😎
