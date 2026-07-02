"""Generate representative graphs and a simple animation for the channel MPs project."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_xy_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={c: c.strip() for c in df.columns})
    if {"x", "y"}.issubset(df.columns):
        return df[["x", "y"]].dropna()
    raise ValueError(f"Expected x and y columns in {path}")


def plot_digitized_profile(source_root: Path, output_dir: Path) -> Path:
    csv_path = source_root / "verification_hydro_data" / "exp4_lv.csv"
    df = read_xy_csv(csv_path)

    fig, ax = plt.subplots(figsize=(6.5, 4.5), constrained_layout=True)
    ax.scatter(df["x"], df["y"], s=36, color="#f0b429", edgecolor="#222222", linewidth=0.7)
    ax.set_xlabel("Normalized velocity or digitized x")
    ax.set_ylabel("Normalized depth or digitized y")
    ax.set_title("Experimental Velocity Profile Example")
    ax.grid(True, color="#d9d9d9", linewidth=0.8)

    output_path = output_dir / "exp4_lv_profile.png"
    fig.savefig(output_path, dpi=220)
    plt.close(fig)
    return output_path


def plot_hydro_verification(source_root: Path, output_dir: Path) -> Path:
    csv_path = source_root / "verification_hydro_data" / "exp_1.csv"
    df = pd.read_csv(csv_path)
    df = df.rename(columns={c: c.strip() for c in df.columns})
    required = {"U_Magnitude", "Points_1"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns in {csv_path}: {sorted(missing)}")

    fig, ax = plt.subplots(figsize=(6.5, 4.5), constrained_layout=True)
    ax.plot(df["U_Magnitude"], df["Points_1"], color="#1f77b4", linewidth=2.0)
    ax.set_xlabel("Velocity magnitude")
    ax.set_ylabel("Vertical coordinate")
    ax.set_title("Hydrodynamic Verification Profile")
    ax.grid(True, color="#d9d9d9", linewidth=0.8)

    output_path = output_dir / "hydrodynamic_verification_profile.png"
    fig.savefig(output_path, dpi=220)
    plt.close(fig)
    return output_path


def animate_particle_cloud(output_dir: Path) -> Path:
    rng = np.random.default_rng(7)
    n_particles = 140
    x0 = rng.normal(0.08, 0.015, n_particles)
    y0 = rng.uniform(0.02, 0.23, n_particles)
    drift = rng.normal(0.0038, 0.0007, n_particles)
    settling = rng.normal(-0.00012, 0.00008, n_particles)

    fig, ax = plt.subplots(figsize=(7.2, 3.4), constrained_layout=True)
    sc = ax.scatter([], [], s=18, color="#2a9d8f", alpha=0.82, edgecolor="none")
    ax.set_xlim(0, 0.55)
    ax.set_ylim(0, 0.25)
    ax.set_xlabel("Channel distance")
    ax.set_ylabel("Flow depth")
    ax.set_title("Illustrative Microplastic Particle Transport")
    ax.grid(True, color="#e2e2e2", linewidth=0.8)

    def update(frame: int):
        t = frame / 45
        x = x0 + drift * frame + 0.012 * np.sin(2 * np.pi * (t + y0))
        y = np.clip(y0 + settling * frame + 0.007 * np.sin(2 * np.pi * (t + x0 * 3)), 0.005, 0.245)
        sc.set_offsets(np.column_stack([x, y]))
        return (sc,)

    anim = animation.FuncAnimation(fig, update, frames=90, interval=55, blit=True)
    output_path = output_dir / "particle_transport_demo.gif"
    anim.save(output_path, writer=animation.PillowWriter(fps=18))
    plt.close(fig)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path(".."), help="Path to the parent data workspace.")
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    project_root = args.project_root.resolve()
    figures_dir = project_root / "figures"
    animations_dir = project_root / "animations"
    figures_dir.mkdir(parents=True, exist_ok=True)
    animations_dir.mkdir(parents=True, exist_ok=True)

    outputs = [
        plot_digitized_profile(source_root, figures_dir),
        plot_hydro_verification(source_root, figures_dir),
        animate_particle_cloud(animations_dir),
    ]

    print("Generated:")
    for output in outputs:
        print(f"  {output}")


if __name__ == "__main__":
    main()

