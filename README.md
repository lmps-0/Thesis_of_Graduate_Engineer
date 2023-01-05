# Bachelors_Thesis
Files and scripts involved in my Bachelor's Thesis of the Mechanical Engineering Program at UFSC


**1. Subject, topic:** 

<p align="center">
  <strong>IMPLEMENTATION OF A DEEP NEURAL NETWORK FOR THE CORRECTION OF PLASTICITY EFFECTS IN THE HOLE DRILLING METHOD FOR MEASURING HIGH LEVELS OF RESIDUAL STRESS IN FLEXIBLE RISERS </strong>
</p>

(Oil & Gas Industry)

**2. Motivation:**  working with ANN (Machine Learning, Deep Learning), FEA, Simulation with Ansys APDL, mechanical metrology, residual stress, the ASTM E837-13a.

**3. Those involved in the project:** 

- Advisor:    Prof. Armando Albertazzi Gonçalves Jr, Dr. Eng.; 
- Co-advisor: Matias Roberto Viotti, Dr. Eng.; 
- Co-advisor: Thiago Wilvert, Ms. Eng.

**4. Company involved:** Metrology and Measurement Automation Laboratory - LABMETRO/EMC/UFSC

**5. Steps:**

  - Study ASTM E837-13a and its limitations regarding the effects of plasticity (State of the art)
  - Develop simulation model considering plasticity effects
  - From simulated results establish neural network database
  - Train and validate neural network models 
  - Build and test a deep learning model (State of the art) 

<p align="center">
  <strong> ABSTRACT </strong>
</p>

  In the work of this undergraduate thesis, a Deep Artificial Neural Network (DANN) model was implemented to perform the correction of plasticity effects in the Hole-Drilling Method when measuring high levels of residual stresses in flexible risers, given the limitations of the American Society for Testing and Materials standard E837-13a in the plastic regime. The model was trained on data resulting from several elastoplastic numerical simulations performed via Finite Element Method. Two databases were established for the training and test of the DANN model, one based on uniform stress values, and another based on non-uniform stress values along the hole wall. The pre-processing of the features of the databases was based on similar works. In the validation of the test set of the two databases, both DANN models performed relatively accurately with prediction errors on the order of 4.4 x 10^(-3) for the database of Test 1 and 3.8 x 10^(-3) for the database of Test 2. A classical Multivariable Linear Regression (MLR) model was also implemented to compare the performance and errors of the DANN model, it was found that the prediction error from the MLR model was higher than that of the DANN model for the database of Test 1, whereas for the database of Test 2, the MLR model prediction error was lower than that of the DANN model. The result questioned the computational efficiency of implementing a DANN model. The values of the Plasticity Factors f in the testing set were investigated. It was observed that the predictions with the largest errors were simulated with the same value of f (1.30). For exemplification purposes and not model validity, values of four profiles (with different values of f) were taken from the total set of data from each database and used as input for the correction.


**Keywords**: Residual Stress. Hole-Drilling Method. Deep Artificial Neural Network. Plasticity Effect.


