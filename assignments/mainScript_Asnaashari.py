import os
os.chdir("D:/polimi note books/energy and enviromnetal technologies for building systems/assignments")
import wallcalculations_Asnaashari as WCA

wallpar1=["out_Surface_winter","gypsum","woodBevel","GlassFiber","brick","woodFiber","inside_Surface"]
wallpar2=["out_Surface_winter","gypsum","woodBevel","woodStud90","brick","woodFiber","inside_Surface"]
f1=0.3
f2=0.7
wall_results=wallCalc_withParallel(wallpar1,wallpar2,f1,f2)


door_layers = ["OutsideSurface_Winter" , "Wood_50mm" , "Inside_Surface" ]
roof_layers = [ 'OutsideSurface_Winter' , 'asphaltshiningroof' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

wall_results = WCA.WallCalcOnlyinSeries ( wall_results )
resultsfordoor = WCA.WallCalcOnlyinSeries ( door_layers )
resultsforroof = WCA.WallCalcOnlyinSeries ( roof_layers )

Wall_A = 105.8
Roof_A = 20*10

Door_A = 1*2.2
Tout = -4.8
Tin = 20
deltaT = Tin - Tout


Qwall = Wall_A * deltaT * wall_results['U_overall']
Qroof = Roof_A * deltaT * resultsforroof ['U_overall']
Qdoor = Door_A * deltaT * resultsfordoor ['U_overall']


Qtot = Qwall + Qdoor + Qroof

print "Qwall= " + str(Qwall) 
print "Qdoor= " + str(Qdoor) 
print "Qroof= " + str(Qroof) 

print "Qtot= " + str (Qtot) 




