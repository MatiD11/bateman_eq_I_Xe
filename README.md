# Bateman Equation Solver for Xe Poisoning

## Overview

This project implements two different numerical methods for solving the Bateman equations for Xe-135 and I-135, to calculate the Xe poisoning after the reactor shutdown. The methods implemented are the fourth-order Runge-Kutta (RK4) and matrix exponential. The project also features visualizations of the results, including I and Xe populations and poisoning. In the project it is also calculated the relative error on the poisoning of the two numerical methods with respect to analytical solution. The matrix method have more accurate solution with respect to the analytical solution, so for this method it is also produced the 3D plot of the xenon poisoning surface at different thermal neutron flux levels. The project follows what proposed in [this paper](#references).

## Project Structure

- **[`parameters.py`](./parameters.py)**: Defines the parameters used throughout the calculations. All the parameters are taken from [1](#references).
- **[`bateman_eq.py`](./bateman_eq.py)**: Defines the Bateman equations, the function to calculate initial conditions, and the function to calculate reactor poisoning. Contains also the analytical solution of the Bateman equation for Xe and calculates the error on the poisoning between analytical and numerical solution.
- **[`runge_kutta.py`](./runge_kutta.py)**: Implements the Runge-Kutta method for solving differential equations.
- **[`matrix_method.py`](./matrix_method.py)**: Implements the matrix exponential method for solving differential equations.
- **[`plot_results.py`](./plot_results.py)**: Contains functions for plotting results, including I and Xe populations, reactor poisoning, errors with respect to the analytical solution, and a 3D plot of the xenon transient surface.
- **[`compute_solutions.py`](./compute_solutions.py)**: Compute solutions of the Bateman equations using both matrix method and Runge-Kutta method, for different neutron flux values and calculates errors.
- **[`estimate_ex_time.py`](./estimate_ex_time.py)**: Contains a function that measures the execution time of a method.
- **[`populations/`](./populations)**: Directory where I and Xe population plots are saved.
- **[`output/`](./output)**: Directory where other plots are saved.


## Bateman Equations

The Bateman equations describe the time evolution of radioactive isotopes in a decay chain. The differential equations taken into account for I and Xe population in this project are:

1. **Equation for Iodine (I)**:
   
  $$ \frac{dI(t)}{dt} = \gamma_I \Sigma_f \phi - \lambda_I I(t)
  $$

2. **Equation for Xenon (Xe)**:
   
  $$ \frac{dXe(t)}{dt} = \gamma_{Xe} \Sigma_f \phi + \lambda_I I(t) - \lambda_{Xe} Xe(t) - \sigma_{aXe} Xe(t) \phi
  $$

where $\gamma_I$ and $\gamma_{Xe}$ are the fission yield of I and Xe, $\Sigma_f \phi$ is the fission rate, $\sigma_{aXe}$ is the microscopic absorption cross-section of Xe and $\phi$ is the neutron flux.
The initial population of iodine $I_0$ and of xenon $Xe_0$, for reactors that have been working long enough to reach equilibrium, can be calculated through the equation since the rate of change of the two populations, $\frac{dI(t)}{dt}$ and $\frac{dXe(t)}{dt}$ are all zero. The two equations are solved after the reactor shutdown, when the neutron flux $\phi$ is zero (assumed to be zero istantaneously).
The analytical solutions, used to check the precision of the numerial method employed, are given by: 

$$ I(t) = \frac{\gamma_I \Sigma_f \phi}{\lambda_I} e^{-\lambda_I t}
$$

$$ X(t) = \Sigma_f \phi \left[ \left( \frac{\gamma_I + \gamma_X}{\lambda_X + \sigma_{aX} \phi} e^{-\lambda_X t} \right) + \frac{\gamma_I}{\lambda_I - \lambda_X} \left( e^{-\lambda_X t} - e^{-\lambda_I t} \right) \right]
$$

The poisoning is calculated using the formula:

$$ \rho_{Xe} = -\frac{\sigma_{aXe}Xe}{\nu \Sigma_f}
$$

where $\nu$ is the number of neutrons released per fission.

## Requirements

This code is written in **Python**. To run it, you'll need the following Python libraries:

- NumPy
- SciPy
- Matplotlib

## Usage

To run the code, you can use the provided `Makefile`. Below are the commands available and their usage:

-To run the main script with default parameters, use the `make run` command:

   ```bash
   make run
   ```
-To run the main script selecting manually the parameters of the simulation, use the following command:
```bash
   make run ARGS='--time-range <start> <end> --dt <value>'
   ```
-To measure the execution time of the two numerical methods, use the `make performance` command:

```bash
   make performance
   ```

## References

1. Zechuan Ding, "Solving Bateman Equation for Xenon Transient Analysis Using Numerical Methods," *MATEC Web of Conferences*, vol. 186, 01004, ICEMP 2018. DOI: [https://doi.org/10.1051/matecconf/201818601004](https://doi.org/10.1051/matecconf/201818601004). 