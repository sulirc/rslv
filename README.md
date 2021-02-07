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
cat << 'EOF' >> ~/.zshrc

# rslv alias command wrapper function
_rslv_cd() {
  cd $(rslv -e "$1")
}

_rslv_open() {
  open $(rslv -e "$1")
}

_rslv_code() {
  code $(rslv -e "$1")
}

_rslv_less() {
  less $(rslv -e "$1")
}

_rslv_cat() {
  cat $(rslv -e "$1")
}

alias rcd=_rslv_cd
alias ropen=_rslv_open
alias rcode=_rslv_code
alias rless=_rslv_less
alias rcat=_rslv_cat
EOF
```

And then open a new terminal window, try to use original cmd.
