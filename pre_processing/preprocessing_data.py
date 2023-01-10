# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:38:25 2021

@author: twi
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Chupakhin based
 
# first test: slide 28 - pre-processing

list_f = ['f=0.70','f=0.75','f=0.8','f=0.85','f=0.9','f=0.95','f=1']
df_1 = pd.DataFrame()

for f_sim in range(len(list_f)):

    df_f = pd.read_excel (r'C:\Users\twi\Downloads\dados_uni_f.xlsx',sheet_name=list_f[f_sim])
    
    sim_id = [[f_sim+1]]
    sim_id = pd.DataFrame(sim_id)
    sim_id = sim_id.reset_index(drop=True)
    
    ft_2 = [[0.25/200]]
    ft_2 = pd.DataFrame(ft_2)
    ft_2 = ft_2.reset_index(drop=True)
    
    df_f_unif_stress = df_f.iloc[30:31,2:4]
    df_f_unif_stress = df_f_unif_stress.reset_index(drop=True)
    
    label = df_f.iloc[3:4,0:1]
    label = pd.DataFrame(label)
    label = label.reset_index(drop=True)
    
    f_id = df_f.iloc[3:4,2:3]
    f_id = pd.DataFrame(f_id)
    f_id = f_id.reset_index(drop=True)
    
    
    df_f = pd.concat([sim_id,ft_2, df_f_unif_stress, label, f_id], axis=1)
    df_f.columns = ['Sim_id','stress_yeld_div_E','stress_max','stress_min','stress_wall','f']
    df_2 = df_f
    
    
    df_f = pd.concat([df_1,df_2], axis=0)
    
    df_1 = df_f

df_f = df_f.reset_index(drop=True)

#df_f.to_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_chupakhin_based.csv',index=False)


#%%

data = pd.read_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_chupakhin_based.csv')

#%% Data science approach

list_f = ['f=0.70','f=0.75','f=0.8','f=0.85','f=0.9']#,'f=0.95','f=1']
df_1 = pd.DataFrame()

for f_cont in range(len(list_f)):

    df_f = pd.read_excel (r'C:\Users\twi\Downloads\dados_uni_f.xlsx',sheet_name=list_f[f_cont])
    
    df_f_inc_depth_strains = df_f.iloc[34:44,0:5]
    df_f_inc_depth_strains = df_f_inc_depth_strains.reset_index(drop=True)
    
    ppts = np.empty(10); ppts.fill(0.25/200)
    ft_ppts = pd.DataFrame(ppts)
    ft_ppts = ft_ppts.reset_index(drop=True)
    
    df_f_unif_stress = df_f.iloc[30:31,2:4]
    stress = df_f_unif_stress.to_numpy()
    stress_max = np.empty(10); stress_max.fill(stress[0][0])
    df_f_unif_stress_max = pd.DataFrame(stress_max)
    stress_min = np.empty(10); stress_min.fill(stress[0][1])
    df_f_unif_stress_min = pd.DataFrame(stress_min)

    label = df_f.iloc[3:4,0:1]
    label = label.to_numpy()
    label_incs = np.empty(10); label_incs.fill(label[0][0])
    label = pd.DataFrame(label_incs)
    #label = label.reset_index(drop=True)
    
    f_id = df_f.iloc[3:4,2:3]
    f_id = f_id.to_numpy()
    f_id_incs = np.empty(10); f_id_incs.fill(f_id[0][0])
    f_id = pd.DataFrame(f_id_incs)

    
    df_f = pd.concat([df_f_inc_depth_strains,ft_ppts, df_f_unif_stress_max, df_f_unif_stress_min, label, f_id], axis=1)
    df_f.columns = ['Inc','depth','SG1','SG2','SG3','stress_yeld_div_E','stress_max','stress_min','stress_border','f']
    df_2 = df_f
        
    df_f = pd.concat([df_1,df_2], axis=0)
    
    df_1 = df_f

df_f = df_f.reset_index(drop=True)

#df_f.to_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_ds_approach.csv',index=False)


#%%

data = pd.read_csv(r'C:\Users\twi\Desktop\TC_2\A04\pre_processing\dataset_uniform_stress_ds_approach.csv')

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
