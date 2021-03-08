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
git rebase -i HEAD~2 # 想要删掉从前往后的2个版本
git push -f
```
