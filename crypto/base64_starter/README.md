# base64_starter

## 基本信息
- 类型：Crypto
- 难度：入门

## 思路
观察字符串特征，发现由大小写字母、数字、加号、斜杠组成，并且末尾带等号，优先考虑 Base64。

## Python 示例
```python
import base64

cipher = 'ZmxhZ3tleGFtcGxlfQ=='
print(base64.b64decode(cipher).decode())
```

## 复盘
编码题先看特征，不要急着手工算。
