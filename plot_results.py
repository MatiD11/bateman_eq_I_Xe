import matplotlib.pyplot as plt
import numpy as np
from parameters import par

def plot_population(results, filename):
    """
    Plots the population of Iodine and Xenon over time.

    Args:
        results: A list of tuples where each tuple contains time and state values.
        filename: The name of the file where the plot will be saved.
    """
    # Extract time and concentration values for Iodine and Xenon
    t = [t/3600 for t, _ in results]  #time in hours
    I_t = [y[0] for _, y in results]  
    Xe_t = [y[1] for _, y in results]  

    plt.figure(figsize=(10, 6))
    plt.plot(t, I_t, marker='o', linestyle='-', markersize=5, color='darkred', markeredgecolor='darkred', markeredgewidth=0.8, label='Iodine')
    plt.plot(t, Xe_t, marker='o', linestyle='-', markersize=5, color='darkblue', markeredgecolor='darkblue', markeredgewidth=0.8, label='Xenon')

    plt.xlabel('Time (h)', fontsize=14)
    plt.ylabel("Population", fontsize=14) 
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title('I and Xe populations vs Time', fontsize=16, fontweight='bold') 
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"populations/{filename}.png")
    plt.close()

def plot_rho(rho_results, filename):
    """
    Plots the poisoning rho over time for different flux percentages.

    Args:
        rho_results: A list where each element contains time and rho values for a specific flux percentage.
        filename: The name of the file where the plot will be saved.
    """
    markers = ['o', 's', '^', 'd', 'x']  
    plt.figure(figsize=(10, 6))
    for i, (rho_t, perc) in enumerate(zip(rho_results, par.FLUX_PERCS)):
        t = [ti/3600 for ti, _ in rho_t]  #time in hours
        rho_values = [y for _, y in rho_t]
        plt.plot(t, rho_values, marker=markers[i], linestyle='-', markersize=4, label=f'Flux = {100*perc}%', color=f'C{i}')
    
    plt.xlabel('Time (h)', fontsize=14)
    plt.ylabel(r'$\rho$ (pcm)', fontsize=14)  
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Poisoning vs Time for Different Neutron Flux', fontsize=16)
    plt.legend(fontsize=12)
    plt.tight_layout() 
    plt.savefig(f"output/{filename}.png", dpi=300)  
    plt.close()

def plot_err(rho_results, errors, filename):
    """
    Plots the relative error of the rho values over time for flux at 100%.

    Args:
        rho_results: A list containing time and rho values for different flux percentages.
        errors: A list of lists containing relative errors with the analytical solution for each flux percentage.
        filename: The name of the file where the plot will be saved.
    """
    index = par.FLUX_PERCS.index(1)  
    rho_t, err = rho_results[index], errors[index][1:]  
    t_hours = [ti / 3600 for ti, _ in rho_t[1:]]  

    plt.figure(figsize=(10, 6))
    plt.plot(t_hours, err, marker='o', linestyle='-', markersize=4, color='darkblue')
    
    plt.xlabel('Time (h)', fontsize=14)
    plt.ylabel('Relative error', fontsize=14)  
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title(r'Relative error on $\rho$ in time (Flux = 100%)', fontsize=16)
    plt.tight_layout() 
    plt.savefig(f"output/{filename}.png", dpi=300)  
    plt.close()

def plot_rho_matrix_3d(rho_matrix_3D_all, filename):
    """
    Plots the xenon transient surface: rho calculated with the matrix method versus time and different values of flux.

    Args:
        rho_matrix_3D_all: List of rho values computed with the matrix method and time for different flux percentages.
        filename: The name of the file where the plot will be saved.
    """
    t_hours_list = []
    rho_matrix_list = []

    for rho_matrix in rho_matrix_3D_all:
        t_hours = [t / 3600 for t, _ in rho_matrix]  # time in hours
        rho_values = [rho for _, rho in rho_matrix]  
        t_hours_list.append(t_hours)
        rho_matrix_list.append(rho_values)
    
    t_hours = t_hours_list[0] if t_hours_list else []
    flux_values = [par.PHI * flux for flux in par.FLUX_PERCS_3D]  
    X, Y = np.meshgrid(t_hours, flux_values)  
    Z = np.array(rho_matrix_list)  

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', linewidth=0.5, alpha=0.8) 

    ax.set_xlabel('Time (hours)', fontsize=12, labelpad=10)
    ax.set_ylabel(r'Flux ($10^{20} neutrons/cm^2 s$)', fontsize=12, labelpad=10)
    ax.set_zlabel(r'$\rho$ (pcm)', fontsize=12, labelpad=10)

    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title(r'$\rho$ vs time for different flux values', fontsize=16, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f"output/{filename}.png", dpi=300)
    plt.show()
    plt.close()
