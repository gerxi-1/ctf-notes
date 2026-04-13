# CTF Notes Template

一个适合个人学习展示的 CTF GitHub 模板仓库。

这个仓库适合用来记录：
- 题目 Writeup
- 解题脚本
- 知识点总结
- 工具使用笔记

## 你可以怎么用

1. Fork 或下载这个仓库模板
2. 把 `templates/` 里的模板复制到对应目录
3. 每做完一道题，就补一份结构化 writeup
4. 把脚本、截图、附件分别放到合适位置
5. 持续更新 README 中的进度

---

## 仓库结构

```text
ctf-github-template/
├── README.md
├── .gitignore
├── LICENSE
├── .github/
│   └── ISSUE_TEMPLATE/
├── templates/
│   ├── writeup-template.md
│   ├── summary-template.md
│   └── exploit-template.py
├── web/
├── crypto/
├── pwn/
├── reverse/
├── misc/
├── tools/
└── assets/
```

---

## 学习方向

### Web
- SQL 注入
- 文件上传
- 命令执行
- SSRF
- XSS

### Crypto
- 古典密码
- 编码转换
- RSA
- 常见脚本题

### Pwn
- 栈溢出
- ret2libc
- ROP
- 格式化字符串

### Reverse
- 静态分析
- 动态调试
- 字符串定位
- 简单反混淆

### Misc
- 隐写
- 流量分析
- 取证
- 编码脑洞题

---

## Writeup 导航

### Web
- [示例：easy_sql](./web/easy_sql/README.md)

### Crypto
- [示例：base64_starter](./crypto/base64_starter/README.md)

### Pwn
- [示例：ret2win](./pwn/ret2win/README.md)

### Reverse
- [示例：simple_reverse](./reverse/simple_reverse/README.md)

### Misc
- [示例：zip_hidden](./misc/zip_hidden/README.md)

---

## 知识总结导航

- [Web 基础总结模板](./templates/summary-template.md)

你也可以自己新增：
- `web/sql-injection-summary.md`
- `crypto/rsa-summary.md`
- `pwn/rop-summary.md`
- `reverse/ida-notes.md`

---

## 个人学习进度

> 可以把这部分当成你的公开学习记录。

- [ ] Web：完成 10 题
- [ ] Crypto：完成 10 题
- [ ] Pwn：完成 10 题
- [ ] Reverse：完成 10 题
- [ ] Misc：完成 10 题

---

## Writeup 规范建议

建议每篇 writeup 至少包含：
- 题目信息
- 知识点
- 解题思路
- 具体步骤
- 脚本或 payload
- 复盘总结

这样别人能看懂，你自己以后也能复习。

---

## 文件命名建议

推荐每道题单独建文件夹，例如：

```text
web/
└── easy_sql/
    ├── README.md
    ├── exp.py
    └── images/
```

这样管理会更清晰。

---

## GitHub 展示建议

为了让仓库更像作品集，可以做到：
- README 保持整洁
- 每篇 writeup 结构统一
- 脚本可直接运行或带注释
- 截图放在 `images/` 子目录
- 题目来源写清楚（如 BUUCTF / picoCTF / XCTF）

---

## 后续可扩展内容

你之后还可以继续加入：
- 自动生成目录脚本
- 题目统计脚本
- GitHub Actions 自动检查 Markdown 链接
- 个人主页 README 展示学习数据

---

## License

默认使用 MIT License，你可以自行修改。
