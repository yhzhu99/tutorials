# manjaro KDE

## 源镜像与系统更新

### 排列源

```sh
sudo pacman-mirrors -i -c China -m rank   #只留下清华源能令带宽跑满
```

### 同步并优化（类似磁盘整理，固态硬盘无需操作）

```sh
sudo pacman-optimize && sync
```

### 增加 archlinuxcn 库和 antergos 库

```sh
echo -e "\n[archlinuxcn]\nSigLevel = TrustAll\nServer = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/\$arch\n\n[antergos]\nSigLevel = TrustAll\nServer = https://mirrors.tuna.tsinghua.edu.cn/antergos/\$repo/\$arch\n"|sudo tee -a /etc/pacman.conf
```

### 升级系统：

```sh
sudo pacman -Syyu --noconfirm
```

### 安装 archlinuxcn 签名钥匙&antergos 签名钥匙

```sh
sudo pacman -S --noconfirm archlinuxcn-keyring antergos-keyring
```

## 小鹤音形的配置安装

```sh
sudo pacman -S --noconfirm yaourt pacaur
```

然后再使用 Aur 安装 ibus-rime。

```sh
pacaur -S ibus-rime
```

由于还需要修改文本，所以我们需要安装一个文本编辑器，这里使用 vim。

```sh
sudo pacman -S vim
```

安装完成后打开 Terminal，输入

```sh
ibus-setup
```

选择输入法（input）>添加（Add）>汉语(Chinese)>Rime 这样就可以在 ibus 中添加 RIME 了，然后我们需要 export 三个变量 GTK_IM_MOUDLE XMDIFIERS QT_IM_MOUDL 三个变量，并且在开机的时候启动 ibus-rime。

我们使用 vim 来编辑~/.xprofile，也许这个文件会不存在，不要紧。

```sh
vim ~/.xprofile
```

然后在里面添加这些东西

```sh
export GTK_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export QT_IM_MODULE=ibus
ibus-daemon -x -d
```

ESC :x 保存退出;注销账户重新登录以后就能正常使用 RIME 了

之后就是导入小鹤的方案

在鹤大的网盘里下载 linux 下的配置文件，解压后，将 yaml 文件拷贝至 Rime 配置目录内，bin 文件拷贝至 Rime build 目录内。

以 Linux 平台 ibus-rime 为例，Rime 配置目录为 ~/.config/ibus/rime，Rime build 目录为 ~/.config/ibus/rime/build。(/home/tualatin/.config/ibus/rime/)

此外，还要在 rime 目录下新建 yaml 文件：default.custom.yaml

内容为：

```sh
patch:
 schema_list:
   - schema: flypy  #flypy
   - schema: flypyplus  #flypyplus
```

## 其他软件（Updating）

### VSCode，网易云音乐，ftp 管理 FileZilla，深度截图，录屏 obs-studio，geogebra，flash(firefox&chrome)

```sh
yaourt -Sy --noconfirm visual-studio-code-bin netease-cloud-music filezilla deepin-screenshot obs-studio geogebra flashplugin pepper-flash
```
