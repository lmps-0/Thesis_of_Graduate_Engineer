# Developed scripts for simulation and data computation


**Developed code in APDL for the execution of simulations** (Appendix B) 

The *txt_inc20.f* script was developed for the execution of the numerical simulations in the Ansys Mechanical APDL software. The script was coded in Ansys APDL parametric language (Fortran based). 


**Code for the computation of the Stress values** (Appendix D) 

The MATLAB script (main_code.m) is the main file for the computation of the stress values of the standard ASTM E837 – 13a [6]. The script was developed by the LABMETRO researchers. This code computes the stress values as a function of the deformations, which are also calculated as a function of the supplied displacements. The code was provided by LABMETRO and adapted to the use case of this undergraduate thesis. The computation of the stress values was made according to the Eq. (2.9)-(2.29) shown in Section 2.2.1.

The calibration coefficients (mentioned in Section 2.2) are implemented in the code according to the standard ASTM E837 – 13a [6]. Uniform as well as non-uniform stresses were calculated, even though a constant stress was applied along the hole wall of the model


