# -*- coding: utf-8 -*-
"""
Created on Fri Dec 3 10:38:25 2021

@author: twi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# first test: slide 28 - pre-processing


#list_f = ['f0','f0.1','f0.2','f0.3','f0.4','f0.5','f0.6','f0.65','f0.7','f0.75','f0.8','f0.85','f0.9','f0.92','f0.93','f0.94','f0.95','f0.96','f0.97','f0.98','f0.99','f1','f1.05','f1.1']
list_f = ['f0','f0.1','f0.2','f0.3','f0.4','f0.5','f0.6','f0.65','f0.7','f0.71','f0.72','f0.73','f0.74','f0.75','f0.76','f0.77','f0.78','f0.79','f0.8','f0.81','f0.82','f0.83','f0.84','f0.85','f0.86','f0.87','f0.88','f0.89','f0.9','f0.92','f0.93','f0.94','f0.95','f0.96','f0.97','f0.98','f0.99','f1','f1.05','f1.1','f1.25','f1.3']

df_1 = pd.DataFrame()

#df_info = pd.read_excel (r'C:\Users\twi\Downloads\Uniaxial_dataV1.xlsx',sheet_name='INFORMATION')
#df_info = pd.read_excel (r'C:\Users\twi\Downloads\Uniaxial_dataV2.xlsx',sheet_name='Planilha1')
#df_info = pd.read_excel (r'D:\PC_LABMETRO\TC_2\A04\Uniaxial_dataV2.xlsx',sheet_name='Planilha1')
df_info = pd.read_excel (r'F:\PC_LABMETRO\TC_2\A04\Uniaxial_dataV2.xlsx',sheet_name='Planilha1')


# filtered
df_info = df_info.iloc[1:43,0:5]
df_info = df_info.reset_index(drop=True)

#%%

# Chupakhin table values


# Chupakhin - Data science approach

#list_f = ['f0','f0.1','f0.2','f0.3','f0.4','f0.5','f0.6','f0.65','f0.7','f0.75','f0.8','f0.85','f0.9','f0.92','f0.93','f0.94','f0.95','f0.96','f0.97','f0.98','f0.99','f1','f1.05','f1.1']
list_f = ['f0','f0.1','f0.2','f0.3','f0.4','f0.5','f0.6','f0.65','f0.7','f0.71','f0.72','f0.73','f0.74','f0.75','f0.76','f0.77','f0.78','f0.79','f0.8','f0.81','f0.82','f0.83','f0.84','f0.85','f0.86','f0.87','f0.88','f0.89','f0.9','f0.92','f0.93','f0.94','f0.95','f0.96','f0.97','f0.98','f0.99','f1','f1.05','f1.1','f1.25','f1.3']

df_1 = pd.DataFrame()

E = 207.5e3 # MPa
Sigma_yeld = 1056  # MPa

for f_cont in range(len(list_f)):

    #df_f = pd.read_excel (r'C:\Users\twi\Downloads\Uniaxial_dataV2.xlsx',sheet_name=list_f[f_cont])
    #df_f = pd.read_excel (r'D:\PC_LABMETRO\TC_2\A04\Uniaxial_dataV2.xlsx',sheet_name=list_f[f_cont])
    df_f = pd.read_excel (r'F:\PC_LABMETRO\TC_2\A04\Uniaxial_dataV2.xlsx',sheet_name=list_f[f_cont])

    
    df_f_inc_depth = df_f.iloc[17:27,0:6]
    df_f_inc_depth = df_f_inc_depth.reset_index(drop=True)
    
    #df_f_strains = df_f.iloc[34:44,3:5]
    #df_f_strains = df_f_strains.reset_index(drop=True)
    
    ppts = np.empty(10); ppts.fill(Sigma_yeld/(E*1e-2)) # Chupakhin -> feature Sigma_yeld / E*10^-2
    ft_ppts = pd.DataFrame(ppts)
    ft_ppts = ft_ppts.reset_index(drop=True)
    
    df_f_unif_stress = df_f.iloc[17:27,6:8]
    stress = df_f_unif_stress.to_numpy()
    sigma_IM = np.empty(10); sigma_IM = stress[:,0]
    #sigma_IM = np.empty(10); sigma_IM.fill(stress[0][0]) # IN OTHER TESTS WE CHANGE HERE
    df_f_unif_sigma_IM = pd.DataFrame(sigma_IM)
    
    #stress_min = np.empty(10); stress_min.fill(stress[0][1]) # IN OTHER TESTS WE CHANGE HERE
    stress_min = np.empty(10); stress_min = stress[:,1] 
    df_f_unif_stress_min = pd.DataFrame(stress_min)
          
    
    sigma_IM_10 = df_f.iloc[26:27,6:7]
    sigma_IM_10 = sigma_IM_10.to_numpy()
    sigma_IM_10_incs = np.empty(10); sigma_IM_10_incs.fill(sigma_IM_10[0][0]) # IN OTHER TESTS WE CHANGE HERE
    sigma_IM_10 = pd.DataFrame(sigma_IM_10_incs)
    
    ###
    mat =[]
    for l in range(10): # line -> increment
        #print(l)    
        row = []
        for c in range(9): # column -> feature -> sigma_IM* 
            sigma_IM_star = (sigma_IM[c] + 2*Sigma_yeld)/(sigma_IM_10_incs[c] + 2*Sigma_yeld)
            row.append(sigma_IM_star)
        sigma_IM_star = (sigma_IM_10_incs[0] + 2*Sigma_yeld)/(2.2*Sigma_yeld)
        row.append(sigma_IM_star)
        mat.append(row)
    
    ###

    sigma_IM_star_matrix = pd.DataFrame(mat)

    label = df_info.iloc[f_cont:f_cont+1,0:1]
    label = label.to_numpy()
    label_incs = np.empty(10); label_incs.fill(label[0][0]) # IN OTHER TESTS WE CHANGE HERE
    label = pd.DataFrame(label_incs)
    #label = label.reset_index(drop=True)
    
    label_sigma_PD_incs = np.empty(10);
    for i in range(10):
        label_sigma_PD_incs[i] = (sigma_IM[i] + 2*Sigma_yeld)/(label_incs[i] + 2*Sigma_yeld)
    label_sigma_PD_incs = pd.DataFrame(label_sigma_PD_incs)
    
    
    f_id = df_info.iloc[f_cont:f_cont+1,2:3]
    f_id = f_id.to_numpy()
    f_id_incs = np.empty(10); f_id_incs.fill(f_id[0][0])
    f_id = pd.DataFrame(f_id_incs)
    
    ###
    ###
    # depth = i/10
    df_f = pd.concat([df_f_inc_depth, ft_ppts, sigma_IM_star_matrix, df_f_unif_sigma_IM, df_f_unif_stress_min, sigma_IM_10, f_id, label_sigma_PD_incs], axis=1)  # sigma_IM := stress_max 
    df_f.columns = ['Inc','i/10','stress_max_non_uni_reg','stress_min_non_uni_reg','stress_max_non_uni_non_reg','stress_min_non_uni_non_reg','Sigma_yeld/E10-2','sigma_IM_1*','sigma_IM_2*','sigma_IM_3*','sigma_IM_4*','sigma_IM_5*','sigma_IM_6*','sigma_IM_7*','sigma_IM_8*','sigma_IM_9*', '(sigma_IM_10+2*Sigma_yeld)/(2.2*Sigma_yeld)', 'sigma_IM','stress_min','sigma_IM_10','f','label_sigma_PD_incs']
    df_2 = df_f
        
    df_f = pd.concat([df_1,df_2], axis=0)
    
    df_1 = df_f

df_f = df_f.reset_index(drop=True)

#df_f.to_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_ds_approach.csv',index=False)

# Export total Matrix for prediction purposes later ...
df_f.to_csv(r'F:\PC_LABMETRO\TC_2\A04\analysis_2_only_plotting_results_Colab_does_not_work_well\total_df_t2.csv',index=False)



# filters

#df_f.drop(['stress_max_non_uni_reg','stress_min_non_uni_reg','stress_max_non_uni_non_reg','stress_min_non_uni_non_reg','stress_min','f'], axis='columns',inplace=True)

# reordering

#df_f = df_f[['sigma_IM_1*','sigma_IM_2*','sigma_IM_3*','sigma_IM_4*','sigma_IM_5*','sigma_IM_6*','sigma_IM_7*','sigma_IM_8*','sigma_IM_9*', '(sigma_IM_10+2*Sigma_yeld)/(2.2*Sigma_yeld)', 'Sigma_yeld/E10-2','i/10','label_sigma_PD_incs']]

#df_f.to_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_test_2_all_simulations.csv',index=False)


#%% 

    # # defining values for each sigma star (Chupakhin Feature) 
    # sigma_IM_star = np.empty(10);
    # for i in range(9):
    #     sigma_IM_star[i] =  (sigma_IM[i] + 2*Sigma_yeld)/(sigma_IM_10_incs[i] + 2*Sigma_yeld)
        
    # sigma_IM_star[9]=(sigma_IM_10_incs[0] + 2*Sigma_yeld)/(2.2*Sigma_yeld)
    
    # #sigma_IM_star = np.transpose(sigma_IM_star)
    
    # # defining values now for each increment
    # sigma_IM_star_incs = np.empty(10);
    # for i in range(10):
    #     sigma_IM_star_incs
               
    # sigma_IM_star_matrix = np.empty(shape=(10,9));
    # sigma_IM_star_matrix.fill(sigma_IM_star[0])
#%%


#data = pd.read_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_ds_approach.csv')

#%%
# slide <28

# df_f08 = pd.read_excel (r'C:\Users\twi\Downloads\dados_uni_f.xlsx',sheet_name='f=0.8')

# df_f08_stress = df_f08.iloc[17:27,0:4]
# df_f08_stress = df_f08_stress.reset_index(drop=True)
# df_f08_strain = df_f08.iloc[34:44,2:5]
# df_f08_strain = df_f08_strain.reset_index(drop=True)


# df_f08 = pd.concat([df_f08_stress, df_f08_strain], axis=1)
# df_f08.columns=['Increment','Depth(mm)','f=0.8_max','f=0.8_min','SG1','SG2','SG3']

# df_f08_t = df_f08.transpose()
# #%%

# #fig = plt.figure(figsize=(16/2.54,10/2.54))
# sigma_target = 216.6*np.linspace(1,1,10) 
# sigma_non_uniform_f08 = 216.6*np.linspace(1,1.2,10) 

# plt.plot(df_f08['Depth(mm)'],sigma_non_uniform_f08,"c-o",label='$\sigma_{wall}$(target) - fake data, 235.77*id*1.2')
# plt.plot(df_f08['Depth(mm)'],df_f08['f=0.8_max'],"g-*",label='Non-uniform $\sigma_{x}$')

# plt.legend()

# plt.xlabel('Depth(mm)')
# plt.ylabel('$\sigma_{x_{max}}$ for f=0.8')
# plt.grid(which='major')
# #%%
# sigma_target = 216.6*np.linspace(1,1,10) 
# sigma_uniform_f08 = 235.77*np.linspace(1,1,10) 

# plt.plot(df_f08['Depth(mm)'],df_f08['f=0.8_max'],"g-*",label='Non-uniform $\sigma_{x}$')

# plt.plot(df_f08['Depth(mm)'],sigma_uniform_f08,"b-o",label='Uniform $\sigma_{x}$')
# plt.plot(df_f08['Depth(mm)'],sigma_target,"r-o",label='$\sigma_{wall}$(target)')
# plt.legend()
# #plt.title('$\sigma_{x}$ for f=0.8')
# plt.xlabel('Depth(mm)')
# plt.ylabel('$\sigma_{x_{max}}$ for f=0.8')
# plt.grid(which='major')
