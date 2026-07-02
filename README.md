# Channel Microplastics Project

This repository organizes the channel-flow microplastic transport project for sharing, documentation, plotting, and animation.

## Project Focus

The work combines laboratory observations, hydrodynamic verification, Eulerian-Lagrangian particle tracking, and numerical model outputs for microplastic transport in channel flow. The folder is designed to keep the GitHub version clean while still pointing back to the heavier local data and simulation products.

## Repository Layout

```text
channel-mps-project/
  README.md
  docs/
    project_overview.md
    github_setup.md
  scripts/
    generate_visuals.py
  data/
    README.md
  figures/
  animations/
  requirements.txt
```

## Quick Start

Install the plotting dependencies:

```powershell
python -m pip install -r requirements.txt
```

Generate example graphs and an animation from local project data:

```powershell
python scripts/generate_visuals.py --source-root ".."
```

Outputs are written to:

- `figures/`
- `animations/`

## Data Policy

Large OpenFOAM, TELEMAC, VTK, Excel, PDF, and result folders are intentionally excluded by `.gitignore`. For GitHub, keep this repository focused on source code, documentation, small processed examples, figures, and animations. Add large datasets through Zenodo, OSF, institutional storage, Git LFS, or a separate data release.

## Main Local Sources

The current local workspace includes:

- `experimental_data/`: raw laboratory spreadsheets
- `verification_hydro_data/`: verification CSV, Excel, and image files
- `plotting_codes/`: existing plotting scripts and generated figures
- `microplastic_mine/`: model code, paper material, schematics, particle tracking results
- `OpenFOAM/`: CFD cases and outputs
- `Telemac/`: TELEMAC mesh and hydrodynamic files
- `ref/`: reference literature

