# Microplastic Modeling in Water Systems

![Animated microplastic transport through turbulent channel flow](assets/readme-flow-microplastic-animated.gif)

This repository contains numerical tools for simulating microplastic transport in water systems. The current focus is turbulent open-channel flow with and without vegetation, where microplastic motion is controlled by advection, turbulent dispersion, buoyancy, drag, lift, wall interaction, and the structure of the carrier flow.

## Objective

The objective of this project is to develop practical numerical codes for predicting the transport, dispersion, and fate of microplastics in aquatic environments. The model is intended to bridge the gap between simplified tracer models and computationally expensive fully resolved CFD-DEM simulations.

In short, this project aims to provide a computational framework that can:

- compute or import hydrodynamic fields for water systems;
- track microplastic particles with a force-based Lagrangian model;
- represent vegetation effects on flow and dispersion;
- compare numerical predictions with laboratory measurements;
- generate figures, breakthrough curves, and animations for analysis and publication.

## Scientific Background

Microplastics can persist in rivers, channels, estuaries, coastal waters, sediments, and biological systems. Their transport depends on particle properties such as size, density, shape, buoyancy, and settling behavior, as well as flow properties such as turbulence, shear, residence time, and vegetation-induced momentum loss.

The paper associated with this repository develops a GPU-accelerated Eulerian-Lagrangian framework for dilute microplastic transport. The carrier flow is computed with OpenFOAM using a vegetation-aware RANS turbulence model. The microplastic phase is advanced with a custom Python/CuPy solver that tracks individual particles through the simulated flow field.

The particle model includes:

- nonlinear hydrodynamic drag;
- buoyancy;
- added mass;
- Saffman lift;
- stochastic turbulent dispersion;
- wall interaction;
- breakthrough-curve diagnostics;
- an exponential drag integrator for efficient time stepping.

The model is evaluated against laboratory experiments for no-vegetation, low-vegetation, and high-vegetation channel-flow cases. The purpose is to retain the dominant physics of microplastic transport while keeping the model efficient enough for scenario testing and environmental-scale applications.

## Repository Layout

```text
microplastic_modeling/
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

## Current Capabilities

- Project documentation for microplastic transport modeling.
- Scripts for producing representative graphs and particle-motion animations.
- A structure for adding numerical solvers, OpenFOAM case setup files, validation data, and post-processing scripts.
- GitHub-friendly ignore rules to avoid committing large simulation outputs.

## Planned Code Components

- OpenFOAM case setup for hydrodynamic carrier-flow simulation.
- Python/CuPy Lagrangian particle solver.
- Validation scripts for velocity profiles and longitudinal dispersion coefficients.
- Breakthrough-curve and particle-distribution analysis tools.
- Publication-quality plotting and animation workflows.

## Contributors

- Danial Goodarzi  
  Postdoctoral researcher in fluid mechanics, environmental hydraulics, CFD, and microplastic transport modeling. Lead developer and main contributor to this repository.

- Prof. Majid Mohammadian  
  Professor, Department of Civil Engineering, University of Ottawa. Academic supervisor and research advisor for this project.

## Cite Our Work

If you use this repository, the numerical codes, or the generated data products in your research, please cite the related manuscript once the final bibliographic information is available:

1. Goodarzi, D., & Mohammadian, A. (in preparation). *A GPU-accelerated Eulerian-Lagrangian model for microplastic transport in water systems*. Manuscript in preparation.

You can also cite the repository directly:

```bibtex
@misc{microplastic_modeling,
  author       = {Goodarzi, Danial and Mohammadian, Majid},
  title        = {Microplastic Modeling in Water Systems: Numerical Codes for Microplastic Transport and Dispersion},
  year         = {2026},
  url          = {https://github.com/HydroCFD/microplastic_modeling},
  note         = {GitHub repository}
}
```

## Data Policy

Large OpenFOAM, TELEMAC, VTK, Excel, PDF, and result folders are intentionally excluded by `.gitignore`. For GitHub, keep this repository focused on source code, documentation, small processed examples, figures, and animations. Large datasets should be archived through Zenodo, OSF, institutional storage, Git LFS, or a separate data release.

## Main Local Sources

The broader local workspace includes:

- `experimental_data/`: raw laboratory spreadsheets;
- `verification_hydro_data/`: verification CSV, Excel, and image files;
- `plotting_codes/`: existing plotting scripts and generated figures;
- `microplastic_mine/`: model code, paper material, schematics, and particle-tracking results;
- `OpenFOAM/`: CFD cases and outputs;
- `Telemac/`: TELEMAC mesh and hydrodynamic files;
- `ref/`: reference literature.
