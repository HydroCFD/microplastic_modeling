# Project Overview

## Scientific question

How do vegetation, the velocity structure of the flow and the properties of the particles (size, density and shape) control the transport, dispersion and fate of microplastics in open channels?

## Workflow

1. The flow in vegetated and non-vegetated channels is computed in OpenFOAM with the RNG k-ε turbulence model, with vegetation represented by a drag force and an additional dissipation of turbulence from the stem wakes.
2. The flow fields are mapped once onto a structured lookup grid on the GPU.
3. Every microplastic is tracked on the GPU with its own force balance: drag (spherical or shape-dependent), gravity and buoyancy, added mass, Saffman lift and a random displacement with drift correction, advanced with an exponential drag integrator.
4. Boundary rules handle deposition and re-entrainment at the bed, rebound at the walls and trapping at the free surface.
5. Virtual stations at the locations of the laboratory instruments give response curves and longitudinal dispersion coefficients.

## Testing

Each sub-model is verified against an analytical solution. The coupled model is compared without calibration with four laboratory datasets: Stride et al. (2023), Stride et al. (2024), Goral et al. (2023) and Ijaz et al. (2024). The full references and DOIs are listed in the README.

## Project page

<https://hydrocfd.github.io/vegetated-channel-microplastics/>
