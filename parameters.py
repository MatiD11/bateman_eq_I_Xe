import numpy as np

class Parameters:
    """
    A class to store the various parameters used in the simulation.
    """
    GAMMA_I = 0.061         #Fission yield of I-135
    SIGMA_F = 0.008         #Macroscopic absorption cross-section (cm^2 ) 
    LAMBDA_I = 2.874E-5     #Decay constant of I-135 (s^-1 )
    GAMMA_XE = 0.003        #Fission yield of Xe-135      
    LAMBDA_XE = 2.027E-5    #Decay constant of Xe-135 (s^-1 )
    SIGMA_A_XE = 2.75E-18   #Microscopic absorption cross-section of Xe-135 (cm^2)
    PHI = 4.42E20           #Thermal neutron flux (cm^-2 s^-1)
    NI= 2.3                 #n of neutrons released per fission

    FLUX_PERCS = (np.linspace(10, 2, 5)/10.).tolist()           #flux percentages used for poisoning
    FLUX_PERCS_3D = (np.linspace(120, 80, 11)/100.).tolist()    #flux percentages used for the xenon transient surface

par=Parameters