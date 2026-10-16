"""环境自检脚本 —— 确认医学影像开发环境是否就绪"""
import sys


def check():
    print("=" * 46)
    print("  医学影像开发环境自检")
    print("=" * 46)

    print(f"\nPython 版本 : {sys.version.split()[0]}")

    libs = [
        ("numpy", "数值计算"),
        ("scipy", "科学计算"),
        ("matplotlib", "绘图"),
        ("pandas", "表格数据"),
        ("skimage", "经典图像处理"),
        ("cv2", "OpenCV"),
        ("pydicom", "DICOM 读写"),
        ("SimpleITK", "3D 图像处理"),
        ("nibabel", "NIfTI 读写"),
        ("torch", "PyTorch"),
    ]

    print("\n依赖库检查：")
    ok = 0
    for mod, desc in libs:
        try:
            m = __import__(mod)
            ver = getattr(m, "__version__", "?")
            print(f"  [OK]   {desc:<12} {mod:<12} {ver}")
            ok += 1
        except ImportError:
            print(f"  [缺失] {desc:<12} {mod}")

    print(f"\n结果：{ok}/{len(libs)} 个库可用")

    try:
        import torch
        if torch.cuda.is_available():
            print(f"GPU  : {torch.cuda.get_device_name(0)}")
            print(f"CUDA : {torch.version.cuda}")
        else:
            print("GPU  : 不可用（CPU 模式）")
    except ImportError:
        print("GPU  : PyTorch 未安装")

    print("=" * 46)


if __name__ == "__main__":
    check()
