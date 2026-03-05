#!/usr/bin/env python3
# scripts/plot_rewards.py
import os
import numpy as np
import matplotlib.pyplot as plt


def moving_avg(x: np.ndarray, k: int) -> np.ndarray:
    if k is None or k <= 1:
        return x
    k = int(k)
    pad = k // 2
    xp = np.pad(x, (pad, pad), mode="edge")
    return np.convolve(xp, np.ones(k, dtype=np.float32) / k, mode="valid")


def main(npz_path="reward_logs.npz", out_dir="reward_plots", smooth=25):
    d = np.load(npz_path, allow_pickle=True)

    os.makedirs(out_dir, exist_ok=True)

    names = [str(x) for x in d["reward_names"].tolist()]
    total = d["total_reward"]
    t = np.arange(total.shape[0])

    # Plot total reward
    plt.figure(figsize=(10, 5))
    plt.plot(t, moving_avg(total, smooth), linewidth=2)
    plt.title("total_reward vs Step")
    plt.xlabel("step")
    plt.ylabel("reward")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    total_path = os.path.join(out_dir, "total_reward.png")
    plt.savefig(total_path, dpi=300)
    plt.close()

    print(f"Saved {total_path}")

    # Plot individual rewards
    for name in names:
        if name in d:
            plt.figure(figsize=(10, 5))
            plt.plot(t, moving_avg(d[name], smooth), label=name)
            plt.title(f"{name} vs Step (env 0 only)")
            plt.xlabel("step")
            plt.ylabel("reward")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()

            out_path = os.path.join(out_dir, f"{name}.png")
            plt.savefig(out_path, dpi=300)
            plt.close()

            print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
