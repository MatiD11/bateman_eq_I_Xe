import numpy as np
from parameters import par
from scipy.optimize import root

def bateman_equations(y, a=0, b=0):
    """
    Define the Bateman equations for Iodine and Xenon.

    Args:
        y: A list containing the current values of iodine (I) and xenon (Xe).
        a: The rate of fission production of iodine (default is 0).
        b: The rate of fissionproduction of xenon and absorption of thermal neutrons contribution in xenon loss(default is 0).

    Returns:
        The rates of change for iodine and xenon concentrations.
    """
    I, Xe = y
    dI_dt = a - par.LAMBDA_I * I  # Iodine concentration equation
    dXe_dt = par.LAMBDA_I * I - par.LAMBDA_XE * Xe + b  # Xenon concentration equation
    return [dI_dt, dXe_dt]

def calc_initial_conditions(flux_per):
    """
    Calculate the initial conditions for iodine and xenon concentrations.

    Args:
        flux_per: The neutron flux percentage (as a fraction).

    Returns:
        Initial concentrations of iodine (I_0) and xenon (Xe_0).
    """
    def initial_bateman(var):
        """
        Define the system of equations to find the initial conditions for iodine and xenon.

        Args:
            A list containing the initial guesses for iodine (I_0) and xenon (Xe_0).

        Returns:
            The residuals of the Bateman equations to be minimized.
        """
        I_0, Xe_0 = var
        
        a = par.GAMMA_I * par.SIGMA_F * flux_per * par.PHI
        b = par.GAMMA_XE * par.SIGMA_F * flux_per * par.PHI - par.SIGMA_A_XE * Xe_0 * flux_per * par.PHI
        
        return bateman_equations([I_0, Xe_0], a, b)  

    initial_guess = [1E21, 1E14]  
    initial_values = root(initial_bateman, initial_guess)  
    I_0, Xe_0 = initial_values.x  
    return I_0, Xe_0

def calculate_rho(Xe):
    """
    Calculate the poisoning (rho) based on xenon concentration.

    Args:
        Xe: The current xenon concentration.

    Returns:
        The poisoning (rho).
    """
    rho = par.SIGMA_A_XE * Xe / (par.NI * par.SIGMA_F) 
    return rho

#analytical solution comparison
def Xe_pop_analytical(t):
    """
    Compute the analytical solution for the xenon concentration

    Args:
        t: Time at which evaluate the xenon concentration.

    Returns:
        The xenon concentration at time t.
    """
    term1 = par.SIGMA_F * par.PHI
    term2 = ((par.GAMMA_I + par.GAMMA_XE) / (par.LAMBDA_XE + par.SIGMA_A_XE * par.PHI)) * np.exp(-par.LAMBDA_XE * t)
    term3 = par.GAMMA_I / (par.LAMBDA_I - par.LAMBDA_XE) * (np.exp(-par.LAMBDA_XE * t) - np.exp(-par.LAMBDA_I * t))
    
    return term1 * (term2 + term3)

def calculate_errors(rho_numerical, rho_analytic):
    """
    Calculate the relative errors between numerical and analytical solutions of rho.

    Args:
        rho_numerical: Numerical values of rho.
        rho_analytic: Analytical values of rho.

    Returns:
        Relative errors of the numerical solutions compared to the analytical solutions.
    """

    return [(rho_ana - rho_num) / rho_ana for rho_num, rho_ana in zip(rho_numerical, rho_analytic)]
