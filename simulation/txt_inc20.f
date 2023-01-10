!Mechanical APDL（ANSYS）→PlotCtrls→Style→Color→Reverse Video
fini
/clear
/CWD,'D:\lucas.manasses\Changes_of_the_mesh_at_the_model_extremity'!SAVE IN D:
/filname, Inc20NewMesh

/prep7

mp,ex,1,200e9

mp,prxy,1,0.30

sy=250e6

tm=10e9

tb,bkin,1,,0,
tbtemp,0.0
tbdata,1,sy,tm

/axlab,x,log strain (mm/mm)
/axlab,y,true stress (N/mm^2)

tbpl,bkin,1

et,1,186

!variables
inc=20
rf=0.9
ra=7.5
c=1e-4
pro=1
n=20
esp=6
h=pro/n
pi=3.14159265359
ea=1
eb=1.2
ec=2
ed=5

!creation of geometry
cylind,0,rf,esp-inc*h,esp,0,90!volume 1
cylind,rf,1.1*rf,esp-eb,esp,0,90!volume 3
cylind,0,rf,esp-eb,esp-inc*h,0,90!volume 2
cylind,1.1*rf,5*rf,esp-eb,esp,0,90!volume 5
cylind,0,1.1*rf,esp-ec,esp-eb,0,90!volume 4
cylind,1.1*rf,5*rf,esp-ec,esp-eb,0,90!volume 6

!cylind,5*rf,ra,esp-eb,esp,0,90!volume 7
!cylind,5*rf,ra,esp-ec,esp-eb,0,90!volume 8
cylind,0,1.1*rf,0,esp-ec,0,90!volume 9
cylind,1.1*rf,5*rf,0,esp-ec,0,90!volume 10
cylind,5*rf,6*rf,0,esp,0,90!volume ** !Coarse mesh at the boundary 'thiago` 20210325
cylind,0,1.1*rf,0,esp-ec-rf,0,90!volume ** 'thiago` 20210325

cylind,1.1*rf,5*rf,0,esp-ec-rf,0,90!volume**'thiago` 20210325
cylind,5*rf,6*rf,0,esp-ec-rf,0,90!volume**'thiago` 20210325
cylind,0,1.1*rf,0,esp-ec-rf,0,90!volume**'thiago` 20210325
cylind,5*rf,ra,0,esp-ec,0,90!volume 11
block,0,ra,0,ra,esp-eb,esp!volume 7
block,0,ra,0,ra,esp-ec,esp-eb!volume 8
block,0,ra,0,ra,0,esp-ec

vovlap,all
vsel,all
vglue,all

!Selection of volumes for MESH

!1ºvolume(V18)(folhinha)
asel,s,loc,x,0
asel,r,loc,z,esp-eb,esp-inc*h
asel,r,loc,y,0,rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-eb,esp-inc*h
asel,r,loc,x,0,rf
*get,area_target,area,,num,max
esize,0.05
mat,1
vsweep,volume_sweep,area_source,area_target,1

!2ºvolume(V01)
asel,s,loc,x,0
asel,r,loc,z,esp-inc*h,esp
asel,r,loc,y,0,rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-inc*h,esp
asel,r,loc,x,0,rf
*get,area_target,area,,num,max
esize,0.05 
mat,1
vsweep,volume_sweep,area_source,area_target,1

!3ºvolume(V31) 
asel,s,loc,x,0
asel,r,loc,z,esp-eb,esp
asel,r,loc,y,rf,1.1*rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-eb,esp
asel,r,loc,x,rf,1.1*rf
*get,area_target,area,,num,max
esize,0.05 
mat,1
vsweep,volume_sweep,area_source,area_target,1

!4ºvolume(V22) 
asel,s,loc,x,0
asel,r,loc,z,esp-ec,esp-eb
asel,r,loc,y,0,1.1*rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-ec,esp-eb
asel,r,loc,x,0,1.1*rf
*get,area_target,area,,num,max
esize,0.2
mat,1
vsweep,volume_sweep,area_source,area_target,1

!5ºvolume(V23)
asel,s,loc,x,0
asel,r,loc,z,esp-eb,esp
asel,r,loc,y,1.1*rf,5*rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-eb,esp
asel,r,loc,x,1.1*rf,5*rf
*get,area_target,area,,num,max
esize,0.2
mat,1
vsweep,volume_sweep,area_source,area_target,1

!6ºvolume(V25)
asel,s,loc,x,0
asel,r,loc,z,esp-ec,esp-eb
asel,r,loc,y,1.1*rf,5*rf
*get,area_source,area,,num,max
vsla
*get,volume_sweep,volu,,num,max
asel,s,loc,y,0
asel,r,loc,z,esp-ec,esp-eb
asel,r,loc,x,1.1*rf,5*rf
*get,area_target,area,,num,max
esize,0.2
mat,1
vsweep,volume_sweep,area_source,area_target,1

!FIRST cOARSE Mesh (VADD E VMESH COM ESIZE)
!The goal here is to select the volumes and glue them for generation the later mesh

!Selecting V20,V27,V28,V21,V32
asel,s,loc,z,0
vsla
!Gluing V20,V27,V28,V21,V32 -> V02
VADD, ALL 

asel,s,loc,x,ra
vsla
!Gluing V02,V34,V33 -> V03
VADD, ALL 

! V03 is the COARSE Mesh Volume
mshape,1 !Tetrahedral (coarse mesh)
!smrtsize,10
esize,1.5  !4
vmesh,all

!SECOND INTERMEDIATE MESH (SMRTSIZE, ,, 1.2,1.3,,,1.2,,,20)

!selecting volumes V19,V29,V30
asel,s,loc,y,0
asel,r,loc,z,esp-ec-rf,esp-ec
vsla
!Gluing V19,V29,V30 -> V02
VADD, ALL 

!selecting volumes V24,V26,V02
asel,s,loc,y,0
asel,r,loc,x,5*rf,6*rf
asel,r,loc,z,esp-ec-rf,esp
vsla
!Gluing V24,V26,V02 -> V04
VADD, ALL 

mshape,1 !Tetrahedral (coarse mesh)
smrtsize,10
esize,1.5  
vmesh,all
!------------25.04.2021

lsel,all,all

/solve
!nlgeom,on !03.05.2021
!nsubst,10,20,9

nropt,full

ANTYPE,STATIC
!KBC,1
nsel,all

nsel,s,loc,x,0
d,all,ux,0

nsel,s,loc,y,0
d,all,uy,0

nsel,s,loc,x,0
nsel,r,loc,y,0
nsel,r,loc,z,0
d,all,uz,0

nsel,all,all
!Sigma x
asel,s,loc,x,ra
sfa,all,1,pres,-237.5e6

!Sigma y
asel,s,loc,y,ra
sfa,all,1,pres,-237.5e6

allsel
solve

TIME,1
AUTOTS,ON
OUTRES,ALL,ALL
OUTPR,ALL,ALL

!!!PART 1

nsel,s,loc,x,0
d,all,ux,0

nsel,s,loc,y,0
d,all,uy,0

nsel,s,loc,x,0
nsel,r,loc,y,0
nsel,r,loc,z,0
d,all,uz,0

nsel,all,all

!Sigma x
asel,s,loc,x,ra
sfa,all,1,pres,-237.5e6

!Sigma y
asel,s,loc,y,ra
sfa,all,1,pres,-237.5e6

allsel
! vsel,s,loc,z,esp-inc*h+0.001,esp
! vsel,r,loc,x,0,rf-0.001
! vsel,r,loc,y,0,rf-0.001
asel,s,loc,x,0
asel,r,loc,y,0,rf
asel,r,loc,z,esp-inc*h,esp
vsla
! vsel,r,loc,z,esp-inc*h,esp
! vsel,r,loc,y,0,rf

eslv,s
ekill,all
allsel

solve

TIME,2
AUTOTS,ON
OUTRES,ALL,ALL
OUTPR,ALL,ALL

!PART 2

save

/post1

lcdef,1,1

lcdef,2,2

lcase,2
lcsum,all
lcoper,sub,1
lcwrite,3,sub,,,
rappnd,3

! ! set,1
! lcwrite,2,inc2,,,
! lcfile,1,Semfuro,L01,,
! !lcfile,2,inc2,L02,,
! lcase,2
! lcsum,all
! lcoper,sub,1
! lcwrite,3,sub,,,
! !manually procedure for picture with subtraction cases===load case->read load case->3->->plot results->nodal solu->x-component of displacement

nsel,s,loc,z,esp
allsel
*get,highestnode,node,,num,max
*get,lowestnode,node,,num,min
*get,nnodesl,node,,count

*dim,u20,array,nnodesl,5             
*vget,u20(1,1),node,lowestnode,loc,x
*vget,u20(1,2),node,lowestnode,loc,y
*vget,u20(1,3),node,lowestnode,loc,z
*vget,u20(1,4),node,lowestnode,u,x
*vget,u20(1,5),node,lowestnode,u,y           
*cfopen,u20NewMesh,txt                              
/INPUT,'vwriteu20','txt','D:\lucas.manasses\Changes_of_the_mesh_at_the_model_extremity\vwrite',, 0
*cfclos 
!VISUALIZATION OF IMAGE WITH HOLE
! vsel,s,volu,,1
! eslv,r
! esel,inve
! !postprocvse
! plesol,eppl,eqv
! ! 
! *get,deformacao,node,105,nl,epeq
!!!!!nsubstep
!
