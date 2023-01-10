%Main code
clear all;close all

%DF=[9,10,12,16,20,24,28,32,40,50,60,70,132,136,144,148,150,151];%simultaneous
%DF=[9,10,12,16,20,24,28,32,40,50,60,70,132,136,140,144,148,150,151];%preexistinghole
DF=20;%Just for analysing vv 
[line, column]=size(DF);
INC=(0.1:0.1:1); %APDL subtraction (no reference)% %0:0.1:1
ref=1;%Harmonic %Reference value (12=df70) vv
%%Saving the raw data from apdl txt's%%
for n_df=1:1:column
%address=['F:\simulation\biaxial_r1mm\thickcase_surface_inc\df',num2str(DF(n_df)/2), 'mm'];    
address=['C:\Users\thiag\OneDrive\Área de Trabalho\Cálculo método não-uniforme'];
%address=['E:\simulationdistance3d\harmonicosplasticidade\Inc',num2str(DF(n_df))];
createobject_str = ['df',int2str(DF(n_df)),' =processsurfacedata;'];
cd('C:\Users\thiag\OneDrive\Área de Trabalho\Cálculo método não-uniforme');      
eval(createobject_str); % Creating the object (Instance of the class)

        for n_inc=1:1:10 %APDL subtraction (no reference)% %0:1:10  
         cd(address);   
        %fileID=fopen(['datasurf_inc_',num2str(INC(n_inc+1)),'mm.txt']);%INC(n_inc+1) because n_inc must vary between 0 and 10
        fileID=fopen(['u',num2str(INC(n_inc)*10),'.txt']);%INC(n_inc) because n_inc must vary between 1 and 10.There is no reference in this case
        file=fscanf(fileID,'%f %f %f %f %f ',[5 inf]);
        fclose(fileID); 

        %m=['df',int2str(DF(n_df)),'.datainc{',num2str(n_inc+1),'} = transpose(file);']; %INC(n_inc+1) because n_inc must vary between 0 and 10
        m=['df',int2str(DF(n_df)),'.datainc{',num2str(n_inc),'} = transpose(file);']; %INC(n_inc) harmonic 

        cd('C:\Users\thiag\OneDrive\Área de Trabalho\Cálculo método não-uniforme');    
        eval(m);
        end%for n_inc=1:1:10 
end %for n_df=1:1:column
%%

%Calling funcprocesssurfacedata for every object
 cd('C:\Users\thiag\OneDrive\Área de Trabalho\Cálculo método não-uniforme');  
for n_df=1:1:column
m=['df',int2str(DF(n_df)),'.funcprocesssurfacedata;']; %INC(n_inc+1) because n_inc must vary between 0 and 10
        eval(m); %df10.funcprocesssurfacedata; df(x)
end% for n_df=1:1:column
m;

%Linear model(Works for every rosette position)
for n_df=1:1:column
m=['df',int2str(DF(n_df)),'.interpfunc;']; %INC(n_inc+1) because n_inc must vary between 0 and 10
eval(m); %df10.funcprocesssurfacedata; df(x)

end
%% Comands employed to load the raw data
    %cd('F:\simulationdistance3d\OOP treino');  
    %save('preexistinghole')% load('preexistinghole') %equibiaxial (F:\simulationdistance3d\OOP treino)
    %save('pureshear')%load('pureshear') %preexisting hole pure shear
    %save('uniaxialy')%load('uniaxialy')% PREEXISTING HOLE UNIAXIAL Y 
    %save('uniaxialx')%load('uniaxialx')%PREEXISTING HOLE UNIAXIAL X
%theta1=-90; theta2=-45;theta3=0;%G2 %insert theta values here (0,45,90 means a type b in the first quadrant)
%theta1=0; theta2=45;theta3=90;%G1 
%%
%Parameterizing the SG angle to vary from G1 to G2 at increments of 10°
count=1;theta_inc=0;
            %for theta_inc=0:1:360 ;  %180:5:540 hole-hole / 0:5:360 hole-edge / THIS LOOP MUST BE REMOVED IN ORDER TO ANALYSE THE STRESSES AS A FUNCTION OF DF
            %theta1=-135+theta_inc; theta2=-90+theta_inc;theta3=-45+theta_inc;
            theta1=0+theta_inc; theta2=45+theta_inc;theta3=90+theta_inc;
%% Creating the threee gages for the Rosette 1 (I can leave this so that it will be possible to change these values whenever it is necessary)

    for n_df=1:1:column
    m=['df',int2str(DF(n_df)),'.sgrotation(',int2str(theta1),',',int2str(theta2),',',int2str(theta3),');']; %dfxx.sgrotation(-90,-45,0)%Gage location having the point (0,0) as a reference)
    eval(m);
%Gage location considering the position of the hole df(x,y))
   x=40; 
    df=DF(n_df);
    y=40+df/4; 
    x=0;y=0; 
    m=['[SIGMA_MAX(n_df),SIGMA_MIN(n_df),SHEARXY(n_df),G2_E(n_df)]=df',int2str(DF(n_df)),'.sgdisp(n_df,x,y,',int2str(theta1),',',int2str(theta2),',',int2str(theta3),');'];%n_inc should vary from 2 to 11 because n_inc=1 represents the no hole case 
%m=['[G2_E(n_df)]=df',int2str(DF(n_df)),'.sgdisp(n_df,x,y,',int2str(theta1),',',int2str(theta2),',',int2str(theta3),');'];%n_inc should vary from 2 to 11 because n_inc=1 represents the no hole case 
    %FORNECER THETA1,2 E 3
    eval(m) 
    end % for n_df=1:1:column

 %Non-uniform
 for n_df=1:1:column
     %F from first increment. L from last increment. A from average
      m=['[FSIGMA_MAXN(n_df),FSIGMA_MINN(n_df),LSIGMA_MAXN(n_df),LSIGMA_MINN(n_df),ASIGMA_MAXN(n_df),ASIGMA_MINN(n_df)]=df',int2str(DF(n_df)),'.nuni;'];%n_inc should vary from 2 to 11 because n_inc=1 represents the no hole case 
    
      val=DF(n_df);
      %m=['df',int2str(DF(n_df)),'.nuni'];
      %FORNECER THETA1,2 E 3
    eval(m) 
    %pause(2)
    end % for n_df=1:1:column
%Stress non-uniform (f first inc, L last, A average)
