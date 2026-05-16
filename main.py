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
        "figure.dpi": 80,
        "axes.unicode_minus": False,
    }
)

if __name__ == "__main__":
    x = np.linspace(0, 8, 1000)
    y = np.cos(4 * x) * np.exp(-x / 2)
    envelope_pos = np.exp(-x / 2)
    envelope_neg = -np.exp(-x / 2)

    _, ax = plt.subplots(figsize=(8, 5))

    ax.plot(x, y, color="#e21743", alpha=0.91, lw=2.5, label=r"$y=\cos(4x)e^{-x/2}$")
    ax.plot(x, envelope_pos, color="#4053c0", alpha=0.91, lw=2, linestyle="--", label=r"$y=e^{-x/2}$")
    ax.plot(x, envelope_neg, color="#20d73c", alpha=0.91, lw=2, linestyle="--", label=r"$y=-e^{-x/2}$")

    ax.set_xlabel("$X Axis$", color="#8A0719", fontsize=12)
    ax.set_ylabel("$Y Axis$", color="#8A0719", fontsize=12)
    ax.set_title("$Function Plot$", color="#000000", fontsize=14)
    ax.legend()
    ax.grid(linestyle="--", color="gray", alpha=0.6, linewidth=0.7)

    ax.set_xticks(np.arange(0, 9, 1))
    ax.set_yticks(np.arange(-1.5, 1.5, 0.5))
    ax.set_xlim(0, 8)
    ax.set_ylim(-1.5, 1.5)
    plt.show()
