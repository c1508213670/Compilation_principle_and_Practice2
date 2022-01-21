#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : MiJiu
# @FileName: util.py
# @Software: PyCharm

def clear_text(text):
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 0:
            lines.append(line)
    return ' '.join(lines)
