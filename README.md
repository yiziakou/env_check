# 医学影像开发环境自检

一个用于验证医学影像处理开发环境是否就绪的脚本。

## 项目作用

一次性检查 Python 版本、10 个常用库是否可用，以及 PyTorch 能否调用 GPU。

## 运行环境

| 项目 | 版本 |
| --- | --- |
| Python | 3.11.17 |
| PyTorch | 2.5.1 + CUDA 12.1 |
| GPU | NVIDIA GeForce RTX 3060 Laptop GPU |
| 操作系统 | Windows 11 |

## 使用方法

```bash
conda activate medimg
python check_env.py

