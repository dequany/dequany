#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("This is a test for Python.")
print('中文'.encode('utf-8'))
print('\xe4\xb8\xad\xe6\x96\x87')
print('\u4e2d\u6587')
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 書式を持って文字列を出力
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# -------------------------------
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
