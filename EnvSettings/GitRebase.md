# Git 版本控制

## 删除大文件

使用[BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)工具

```shell
java -jar bfg.jar --strip-blobs-bigger-than 100M some-big-repo.git # 若是在项目内，则即为.git
java -jar bfg.jar -D *.pdf some-big-repo.git # 删除特定的文件
cd some-big-repo.git # cd .git
git reflog expire --expire=now --all && git gc --prune=now --aggressive
git push -f
```

## 删除若干个版本

在 VS Code 中，选择 bash 作为 terminal

```shell
git rebase -i HEAD~2 # rebase方法, 想要删掉从前往后的2个版本
git push -f

git reset --hard HEAD~2 # 删掉从前往后的2个版本
git push -f
```

## 合并多个仓库

[参考stackoverflow回答](https://stackoverflow.com/questions/1425892/how-do-you-merge-two-git-repositories)

A single branch of another repository can be easily placed under a subdirectory retaining its history. For example:

```bash
git subtree add --prefix=rails git://github.com/rails/rails.git master
```

This will appear as a single commit where all files of Rails master branch are added into "rails" directory. However the commit's title contains a reference to the old history tree:

> Add 'rails/' from commit <rev>

Where <rev> is a SHA-1 commit hash. You can still see the history, blame some changes.

```bash
git log <rev>
git blame <rev> -- README.md
```

Note that you can't see the directory prefix from here since this is an actual old branch left intact. You should treat this like a usual file move commit: you will need an extra jump when reaching it.

```bash
# finishes with all files added at once commit
git log rails/README.md

# then continue from original tree
git log <rev> -- README.md
```

There are more complex solutions like doing this manually or rewriting the history as described in other answers.

The git-subtree command is a part of official git-contrib, some packet managers install it by default (OS X Homebrew). But you might have to install it by yourself in addition to git.

## Git - Windows AND linux line-endings

[Reference](https://stackoverflow.com/questions/34610705/git-windows-and-linux-line-endings)

On Windows:

``shell
$ git config --global core.autocrlf true
```

On Linux:


``shell
$ git config --global core.autocrlf input
```
