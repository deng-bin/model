import numpy as np
import control as ct
import matplotlib.pyplot as plt

# 中文正常显示 + 负号正常
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 定义系统：K / s(s+1)(s+2)
num = [1]
den = [1, 3, 2, 0]
sys = ct.tf(num, den)

# 创建画布
plt.figure(figsize=(8, 6), dpi=80)

# 绘制根轨迹
gains = np.linspace(0, 20, 8000)
ct.rlocus(sys, gains=gains, grid=False)

plt.xlim(-4, 1)
plt.ylim(-3, 3)
plt.axis("equal")

# 网格和标题
plt.grid(linestyle="--", color="gray", alpha=0.6, linewidth=0.7)
plt.title("控制系统根轨迹", fontsize=14)
plt.xlabel("实轴 Re(s)", fontsize=12)
plt.ylabel("虚轴 Im(s)", fontsize=12)

plt.show()
