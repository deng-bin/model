import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib import cm
from matplotlib.lines import Line2D
from matplotlib.gridspec import GridSpec

# ========== LaTeX配置 ==========
plt.rcParams.update(
    {
        "text.usetex": True,
        "text.latex.preamble": r"\usepackage{amsmath} \usepackage{amssymb} \usepackage{mathrsfs}",
        "font.family": "serif",
        "font.serif": ["Computer Modern"],
        "axes.labelsize": 12,
        "font.size": 11,
        "legend.fontsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "figure.dpi": 100,
        "axes.unicode_minus": False,
    }
)

# ========== 参数设置 ==========
x_min, x_max = -4.5, 4.2
y_min, y_max = -4.5, 4.2
n_points = 300

# 创建网格
x = np.linspace(x_min, x_max, n_points)
y = np.linspace(y_min, y_max, n_points)
X, Y = np.meshgrid(x, y)

# 复平面上的点
Z = X + 1j * Y

# 计算伽马函数的模
Gamma_vals = gamma(Z)
mod_Gamma = np.abs(Gamma_vals)

# 裁剪过大的值
mod_Gamma_clipped = np.clip(mod_Gamma, 0, 8)

# 等高线层次
levels = np.linspace(0, 8, 20)

# ========== 创建1x2子图布局（左右排列） ==========
fig = plt.figure(figsize=(14, 6))

# 使用GridSpec，左右排列，宽度相等
gs = GridSpec(1, 2, figure=fig, width_ratios=[1, 1], wspace=0.30)  # 水平方向间距

# 创建3D子图（左）和2D子图（右）
ax1 = fig.add_subplot(gs[0, 0], projection="3d")  # 左：3D曲面
ax2 = fig.add_subplot(gs[0, 1])  # 右：等高线图

# ========== 左侧：3D曲面 ==========
# 设置透明背景
fig.patch.set_facecolor("none")
ax1.set_facecolor("none")

# 绘制曲面
surf = ax1.plot_surface(
    X,
    Y,
    mod_Gamma_clipped,
    cmap=cm.viridis,
    linewidth=0,
    antialiased=True,
    alpha=0.9,
    rstride=2,
    cstride=2,
)

# 添加等高线投影到底部平面
ax1.contour(
    X,
    Y,
    mod_Gamma_clipped,
    levels=levels,
    zdir="z",
    offset=0,
    cmap=cm.plasma,
    alpha=0.5,
    linewidths=0.6,
)

# 设置坐标轴标签
ax1.set_xlabel(r"$\Re(z)$", fontsize=12, labelpad=8)
ax1.set_ylabel(r"$\Im(z)$", fontsize=12, labelpad=8)
ax1.set_zlabel(r"$|\Gamma(z)|$", fontsize=12, labelpad=8)

# 设置z轴范围
ax1.set_zlim(0, 8)

# 设置视角
ax1.view_init(elev=30, azim=-45)

# 设置刻度字体大小
ax1.tick_params(labelsize=9)

# 设置标题
ax1.set_title(r"Modulus of Gamma Function", fontsize=13, fontweight="bold", pad=0)

# 不添加颜色条

# ========== 右侧：等高线图（带颜色条，调整比例） ==========
# 设置图形比例为正方形，避免拉长
ax2.set_aspect("equal")

contour2 = ax2.contourf(
    X, Y, mod_Gamma_clipped, levels=levels, cmap=cm.viridis, alpha=0.85
)
# 添加颜色条
cbar2 = fig.colorbar(contour2, ax=ax2, shrink=0.7, aspect=25, pad=0.08)
cbar2.set_label(r"$|\Gamma(z)|$", fontsize=11)
cbar2.ax.tick_params(labelsize=9)

ax2.set_xlabel(r"$\Re(z)$", fontsize=12)
ax2.set_ylabel(r"$\Im(z)$", fontsize=12)
ax2.set_title(r"Contour Plot of $|\Gamma(z)|$", fontsize=13, fontweight="bold", pad=10)
ax2.grid(True, alpha=0.3)

# 标记极点（负整数）
for n in [-4, -3, -2, -1, 0]:
    if x_min <= n <= x_max:
        ax2.scatter(n, 0, color="red", s=40, marker="x", zorder=5, linewidths=2)
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(y_min, y_max)

# ========== 添加图例到等高线图 ==========
legend_elements = [
    Line2D(
        [0],
        [0],
        marker="x",
        color="red",
        label="Poles (negative integers)",
        markersize=8,
        linestyle="None",
        markeredgecolor="red",
        markerfacecolor="red",
        linewidth=2,
    ),
]
ax2.legend(
    handles=legend_elements,
    loc="upper right",
    frameon=True,
    fancybox=True,
    facecolor="white",
    framealpha=0.8,
    fontsize=10,
)

# ========== 添加公式说明框 ==========
integral_text = (
    r"$\displaystyle \Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \,\mathrm{d}t, \Re(z)>0$"
)
reflection_text = r"$\Gamma(1-z)\Gamma(z) = \dfrac{\pi}{\sin(\pi z)},\forall z\in\mathbb{C}\setminus\mathbb{Z}$"

fig.text(
    0.02,
    0.9,
    integral_text,
    fontsize=13,
    verticalalignment="center",
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8, edgecolor="none", pad=1),
)
fig.text(
    0.78,
    0.9,
    reflection_text,
    fontsize=13,
    verticalalignment="center",
    bbox=dict(
        boxstyle="round", facecolor="lightblue", alpha=0.8, edgecolor="none", pad=1
    ),
)

# ========== 总标题 ==========
fig.suptitle(
    r"The Gamma Function $\Gamma(z)$ on the Complex Plane",
    fontsize=16,
    fontweight="bold",
    y=0.98,
)

# ========== 调整布局 ==========
plt.subplots_adjust(top=0.92, wspace=0.30)

# ========== 导出图片 ==========
plt.savefig(
    "gamma_1x2.svg", dpi=300, bbox_inches="tight", facecolor="white", edgecolor="none"
)
plt.savefig("gamma_1x2.pdf", dpi=300, bbox_inches="tight", transparent=True)

plt.show()
