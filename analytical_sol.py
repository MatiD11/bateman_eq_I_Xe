from parameters import par
import numpy as np

def Xe_flux(t):
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
