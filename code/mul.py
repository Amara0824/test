#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""九九乘法表"""


def mul_table(n: int = 9) -> None:
    """打印 n 行下三角形式的九九乘法表"""
    for i in range(1, n + 1):
        # 每行由若干 "j×i=积" 组成，用制表符对齐
        row = [f"{j}x{i}={i * j}" for j in range(1, i + 1)]
        print("\t".join(row))


if __name__ == "__main__":
    mul_table()
