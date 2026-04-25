# 函数曲线可视化项目
基于 Python + NumPy + Matplotlib + Seaborn 实现的数学函数可视化项目，绘制衰减余弦函数及其上下包络线曲线。

## 项目功能
实现三条数学函数曲线的可视化绘制：
1. 衰减振荡主函数：$y=\cos(4x)e^{-x/2}$
2. 上包络线：$y=e^{-x/2}$
3. 下包络线：$y=-e^{-x/2}$

## 开发环境
- Python 版本：≥3.14
- 核心依赖：numpy、matplotlib、seaborn
- 包管理工具：uv（高性能Python包管理器）
- 版本控制：Git

## 运行指南
### 1. 安装项目依赖
```bash
uv sync
```