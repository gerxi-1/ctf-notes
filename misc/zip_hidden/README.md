# zip_hidden

## 基本信息
- 类型：Misc
- 难度：入门

## 思路
题目给了压缩包，优先检查压缩包注释、伪加密、目录结构，以及是否存在图片隐写或文件拼接。

## 常用命令
```bash
file chall.zip
strings chall.zip | head
binwalk chall.zip
```
