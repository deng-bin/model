import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["axes.unicode_minus"] = False
sns.set_style("whitegrid")
sns.set_palette("husl")

if __name__ == "__main__":
    x = np.linspace(0, 8, 1000)
    y1 = np.cos(4 * x) * np.exp(-x / 2)
    y2 = np.exp(-x / 2)
    y3 = -np.exp(-x / 2)

    plt.figure(figsize=(8, 5), dpi=80)

    plt.plot(x, y1, color="#e21743e9", lw=2.5, label=r"$y=cos(4x)e^{-x/2}$")
    plt.plot(x, y2, color="#4053c0e9", lw=2, linestyle="--", label=r"$y=e^{-x/2}$")
    plt.plot(x, y3, color="#20d73ce9", lw=2, linestyle="--", label=r"$y=-e^{-x/2}$")

    plt.xlabel("X Axis", color="#8A0719E4", fontsize=12)
    plt.ylabel("Y Axis", color="#8A0719E4", fontsize=12)
    plt.title("Function Plot", color="#000000", fontsize=14)
    plt.legend()
    plt.grid(linestyle="--", color="gray", alpha=0.6, linewidth=0.7)

    plt.xticks(np.arange(0, 9, 1))
    plt.yticks(np.arange(-1.5, 1.5, 0.5))

    plt.xlim(0, 8)
    plt.ylim(-1.5, 1.5)
    plt.show()
