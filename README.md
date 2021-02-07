# rslv ⛳️

Use rslv to register any resource path and then resolve it as an alias name.

# Installation

// WIP

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

Write rslv use case in alias, and then use `rslv` in an even shorter way. (Just like the original way)

```bash
# rslv commands
_rslv_cd() {
  cd $(rslv -e $1)
}

_rslv_open() {
  open $(rslv -e $1)
}

_rslv_code() {
  code $(rslv -e $1)
}

alias cd=_rslv_cd
alias open=_rslv_open
alias code=_rslv_code
```
