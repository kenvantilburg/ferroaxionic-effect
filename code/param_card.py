from natural_units_GeV import *

##############################
##### SOURCE PARAMETERS ######
##############################

R_S = 10; #relativistic enhancement factor divided by effective quantum numbers
Z_S = 92; # charge of Schiff atom
A_S = 200; # atomic number of Schiff atom
M_S = Z_S**2 * R_S / a_0**4 # atomic matrix element

rho = 1.2e4 * kg * meter**-3 # mass density
N_c = 10 # number of atoms in unit cell
N_S = 5 # number of Schiff atoms
V_c = amu * A_S * N_S / rho # volume of unit cell

n_N = N_S/V_c # number density of Schiff spins
S_schiff_over_theta = 5 * e_EM * fm**3; # Schiff moment proportionality constant with theta

P_nuc = 1 # nuclear spin polarization fraction

mu_N = mu_nuclear # nuclear magnetic moment

##############################
##### READOUT PARAMETERS #####
##############################
