# rslv ⛳️

Use rslv to register any resource path and then resolve it as an alias name.

# Installation

Make sure you had install pip3. Then copy this script and run in CLI.

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

Just copy script below and run in CLI. Note: change .zshrc to .bashrc depend on your shell.

```bash
cat <<'EOF' >>~/.zshrc

# rslv alias function
export rcd() { cd $(rslv -e "$1"); }
export rcode() { code $(rslv -e "$1"); }
export rless() { less $(rslv -e "$1"); }
export rcat() { cat $(rslv -e "$1"); }
export ropen() { open $(rslv -e "$1"); }
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
