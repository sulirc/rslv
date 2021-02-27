# rslv ⛳️

使用 rslv 来注册常用文件路径的别名。

# 如何安装？

请确认已经安装 pip3 的前提下，拷贝下述命令并在终端运行。该命令会自动安装对应的脚本到你的机器上。

```bash
bash <(curl -s https://raw.githubusercontent.com/sulirc/rslv/main/install.sh)
```

# 如何使用

安装完 rslv 后，请记得重启终端。

## 基础用法

使用 -r 短命令注册别名。

```bash
rslv -r @examples "/Users/sulirc/Desktop/webpack/examples/"
```

通过 -l 端命令罗列所有已注册的别名。

```bash
rslv -l

@react => ~/Desktop/workspace/projects/react
@examples => /Users/sulirc/Desktop/webpack/examples/
```

然后尝试如下命令：

```bash
cd $(rslv -e @examples)
```

原理上，它会展开给 cd 命令进行执行，等价于：`cd ~/Desktop/workspace/projects/react`

所以同理，rslv 可以结合很多方式进行使用

```bash
open $(rslv -e @react)
code $(rslv -e @react)
less $(rslv -e @react/README.md)
# ...
```

## 进阶

将上述脚本拷贝并在终端运行。（如果是 bash 则请注意替换 zshrc 为 bashrc）

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

打开终端，进行尝试。

```bash
rslv -l
Registered alias list:
@rslv => /Users/yanguangjie/Desktop/cli-resolve
@react => /Users/yanguangjie/Desktop/workspace/projects/react
```

使用 `rcd` 来快速切换路径。

```bash
rcd @react
```

又或者使用 `ropen` 快速打开文件夹。

```bash
ropen @react
```

以及很多很多，你能想象到的，都可以结合进行发挥，原理同上。最后，贴上博客：[《Shell “实趣”系列 —— CLI 疯狂逗号 & 任意门》](https://www.yuque.com/sulirc/zen/vae1wc)
