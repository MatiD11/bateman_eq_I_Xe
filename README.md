# Bateman Equations Solver for Xe Poisoning

## Overview

This project implements two different numerical methods for solving the Bateman equations for Xe-135 and I-135, and calculate the Xenon poisoning after the reactor shutdown. The methods implemented are the fourth-order Runge-Kutta (RK4) and matrix exponential. The results of the project, including Iodine and Xenon populations as well as poisoning effects, are visualized through various plots. Additionally, the relative error in the poisoning values for both numerical methods is calculated with respect to the analytical solution. The matrix method provides a more accurate solution compared to the analytical one, and for this method, a 3D plot of the xenon poisoning surface at different thermal neutron flux levels is also produced. The project follows what proposed in [this paper](#references).

## Bateman Equations

The Bateman equations describe the time evolution of radioactive isotopes in a decay chain. The differential equations that are taken into account for I and Xe population in this project are:

1. **Iodine (I)**:
   
  $$ \frac{dI(t)}{dt} = \gamma_I \Sigma_f \phi - \lambda_I I(t)
  $$

2. **Xenon (Xe)**:
   
  $$ \frac{dXe(t)}{dt} = \gamma_{Xe} \Sigma_f \phi + \lambda_I I(t) - \lambda_{Xe} Xe(t) - \sigma_{aXe} Xe(t) \phi
  $$

where $\gamma_I$ and $\gamma_{Xe}$ are the fission yields of I and Xe, $\Sigma_f \phi$ is the fission rate, $\sigma_{aXe}$ is the microscopic absorption cross-section of Xe and $\phi$ is the neutron flux.
The initial population of iodine $I_0$ and of xenon $Xe_0$, for reactors that have been working long enough to reach equilibrium, can be obtained from the equation since the rate of change of the two populations, $\frac{dI(t)}{dt}$ and $\frac{dXe(t)}{dt}$ are equal to zero. The two equations are solved after the reactor shutdown, when the neutron flux $\phi$ is assumed to be zero istantaneously.
The analytical solutions, used to check the precision of the numerical method employed, are given by: 

$$ I(t) = \frac{\gamma_I \Sigma_f \phi}{\lambda_I} e^{-\lambda_I t}
$$

$$ Xe(t) = \Sigma_f \phi \left[ \left( \frac{\gamma_I + \gamma_{Xe}}{\lambda_{Xe} + \sigma_{aXe} \phi} e^{-\lambda_{Xe} t} \right) + \frac{\gamma_I}{\lambda_I - \lambda_{Xe}} \left( e^{-\lambda_{Xe} t} - e^{-\lambda_I t} \right) \right]
$$

The poisoning is calculated using the formula:

$$ \rho_{Xe} = -\frac{\sigma_{aXe}Xe}{\nu \Sigma_f}
$$

where $\nu$ is the number of neutrons released per fission.

## Project Structure

- **[`parameters.py`](./parameters.py)**: Defines the parameters used throughout the calculations. All the parameters are taken from [1](#references).
- **[`bateman_eq.py`](./bateman_eq.py)**: Defines the Bateman equations, the function to compute initial conditions, and the function to compute reactor poisoning $\rho$. It contains also the analytical solution of the Bateman equations for Xe and computes the relative error of poisoning of the numerical solution with respect to the analytical one.
- **[`runge_kutta.py`](./runge_kutta.py)**: Implements the fourth-order Runge-Kutta method for solving differential equations.
- **[`matrix_method.py`](./matrix_method.py)**: Implements the matrix exponential method for solving differential equations.
- **[`plot_results.py`](./plot_results.py)**: Contains functions for plotting results, including Iodine and Xenon populations, reactor poisoning, relative errors, and a 3D plot of the xenon transient surface.
- **[`compute_solutions.py`](./compute_solutions.py)**: Compute solutions of the Bateman equations using both matrix method and Runge-Kutta method, for different neutron flux values.
- **[`estimate_ex_time.py`](./estimate_ex_time.py)**: Contains the function that measures the execution time of a method.
- **[`populations/`](./populations)**: Directory where I and Xe population plots are saved.
- **[`output/`](./output)**: Directory where all other plots are saved.

## Requirements

This code is written in **Python**. To run it, you'll need the following Python libraries:

- NumPy
- SciPy
- Matplotlib

## Usage

To run the code, you can use the provided `Makefile`. Below are the commands available and their usage:

- To run the main script with default parameters, use the `make run` command:

   ```bash
   make run
   ```
- To run the main script selecting manually the parameters of the simulation, use the following command:
   ```bash
   make run ARGS='--time-range <start> <end> --dt <value>'
   ```
- To measure the execution time of the two numerical methods, use the `make performance` command:

   ```bash
   make performance
   ```
- To see the available commands:

   ```bash
   make help
   ```

## References

1. Zechuan Ding, "Solving Bateman Equation for Xenon Transient Analysis Using Numerical Methods," *MATEC Web of Conferences*, vol. 186, 01004, ICEMP 2018. DOI: [https://doi.org/10.1051/matecconf/201818601004](https://doi.org/10.1051/matecconf/201818601004). 
