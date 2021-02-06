# rslv 🕳 ⛳️

Use rslv to register any resource path and then resolve it as an alias name.

# Usage

## Basic

Register resoure path to your favourite name

```bash
rslv -r @react "~/Desktop/workspace/projects/react"
```

and then try to use it in your terminal

```bash
rslv cd @react
```

it will expand to `cd ~/Desktop/workspace/projects/react`

Similarly. See below.

```bash
# open ~/Desktop/workspace/projects/react/
rslv open @react

# open editor of folder ~/Desktop/workspace/projects/react/
rslv code @react

# use less to view ~/Desktop/workspace/projects/react/README.md
rslv less @react/README.md
```

## Advance

Use `rslv` in an even shorter way.

Alias your frequently and favourite command with `rslv --wrap` in ~/.zshrc or ~/.bashrc.

```bash
alias cd="rslv --wrap cd"
```

Then we can use the alias just like original way.

```bash
cd @react
```
