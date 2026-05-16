"""四阶龙格-库塔法 (RK4) 求解常微分方程初值问题"""

import numpy as np
import matplotlib.pyplot as plt

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


def rk4(f, t_span, y0, h=0.01):
    """通用四阶龙格-库塔法求解 dy/dt = f(t, y)

    参数
    ----------
    f : callable
        函数 f(t, y)，接受标量 t 和数组 y，返回 dy/dt
    t_span : (float, float)
        积分区间 [t0, tf]
    y0 : array_like
        初值 y(t0)
    h : float
        步长

    返回
    -------
    t : ndarray, shape (N,)
        时间节点
    y : ndarray, shape (N, len(y0))
        每个时间节点上的数值解
    """
    y0 = np.asarray(y0, dtype=float)
    t0, tf = t_span
    n_steps = int(np.ceil((tf - t0) / h))
    h = (tf - t0) / n_steps  # 修正步长使整数步到达 tf

    t = np.empty(n_steps + 1)
    y = np.empty((n_steps + 1, *y0.shape))
    t[0], y[0] = t0, y0

    for i in range(n_steps):
        ti, yi = t[i], y[i]

        k1 = f(ti, yi)
        k2 = f(ti + h / 2, yi + h / 2 * k1)
        k3 = f(ti + h / 2, yi + h / 2 * k2)
        k4 = f(ti + h, yi + h * k3)

        t[i + 1] = ti + h
        y[i + 1] = yi + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return t, y


# ============================================================
# 示例
# ============================================================
if __name__ == "__main__":

    # ---- 示例 1：单变量 ODE，dy/dt = -2y, y(0) = 1 ----
    def f1(t, y):
        return -2 * y

    t, y = rk4(f1, (0, 5), [1.0], h=0.05)
    y_exact = np.exp(-2 * t)  # 解析解

    # ---- 示例 2：二阶 ODE 化为一阶方程组，谐振子 ----
    # u'' + 2ζω u' + ω² u = 0
    # 令 y = [u, u']，则 dy/dt = [y[1], -2ζω y[1] - ω² y[0]]
    zeta, omega = 0.1, 5.0

    def oscillator(t, y):
        u, v = y
        return np.array([v, -2 * zeta * omega * v - omega**2 * u])

    t2, y2 = rk4(oscillator, (0, 10), [1.0, 0.0], h=0.02)

    # ---- 绘图对比 ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(t, y[:, 0], label=r"$RK4$", linewidth=1.8)
    ax1.plot(t, y_exact, "--", label=r"$Exact$", alpha=0.7, linewidth=1.8)
    ax1.set(xlabel=r"$t$", ylabel=r"$y$", title=r"$\frac{dy}{dt} = -2y$")
    ax1.legend()
    ax1.grid(True, linestyle="--", color="gray", alpha=0.6, linewidth=0.7)

    ax2.plot(t2, y2[:, 0], label=r"$displacement u$", linewidth=1.8)
    ax2.plot(t2, y2[:, 1], label=r"$velocity v$", linewidth=1.8)
    ax2.set(
        xlabel=r"$t$",
        ylabel=r"$y$",
        title=rf"$Damped oscillator$ ($\zeta={zeta}$, $\omega={omega}$)",
    )
    ax2.legend()
    ax2.grid(True, linestyle="--", color="gray", alpha=0.6, linewidth=0.7)

    fig.tight_layout()
    plt.show()
