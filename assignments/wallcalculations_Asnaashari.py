def wallCalc_withParallel(wallpar1,wallpar2,f1,f2):
    material_library={"out_Surface_winter":0.03,"woodBevel":0.14,"woodFiber":0.23,"GlassFiber":2.52,"woodStud90":0.63,"gypsum":0.079,"inside_Surface":0.12,"brick":0.12}
    
    wallpar1=["gypsum","woodBevel","GlassFiber","brick","woodFiber"]
    wallpar2=["gypsum","woodBevel","woodStud90","brick","woodFiber"]
    air=["out_Surface_winter","inside_Surface"]
    f1=0.3
    f2=0.7
    
    wallpar1_complete = wallpar1+air
    wallpar2_complete = wallpar2+air
    
    Rtot_betweenstuds=0
    Rtot_atstuds=0
    R_values1=[]
    R_values2=[]
    
    for anylayers in wallpar1_complete:
        R_value=material_library[anylayers]
        R_values1.append(R_value)
        Rtot_atstuds=Rtot_atstuds+R_value
    print "R value for the material at studs is" +str( R_values1)
    print "The total thermal resistance unit calculated at studs is : "+str( Rtot_atstuds)+ " m^2(degC)/W"
    U_at_studs=1/Rtot_atstuds
    print " so  heat transfer coefficent at studs is" +str(U_at_studs)
    print "********************************"
    
    
    for anylayers in wallpar2_complete:
        R_value=material_library[anylayers]
        R_values2.append(R_value)
        Rtot_betweenstuds=Rtot_betweenstuds+R_value
    print "R value for the material at studs is" +str( R_values2)
    print "The total thermal resistance unit calculated between studs is : "+str(Rtot_betweenstuds)+ " m^2(degC)/W"
    U_betweenstuds=1/ Rtot_betweenstuds
    print " so  heat transfer coefficent in between is" +str(U_betweenstuds)
    print "**************************************************"
    
    U_overall=(U_betweenstuds*f1)+(U_at_studs*f2)
    print "total overall heat transfer coefficent is" +str(U_overall)
    
    results=wallCalc_withParallel(wallpar1,wallpar2,0.3,0.7)
    return results



wallpar1=["out_Surface_winter","gypsum","woodBevel","GlassFiber","brick","woodFiber","inside_Surface"]
wallpar2=["out_Surface_winter","gypsum","woodBevel","woodStud90","brick","woodFiber","inside_Surface"]
f1=0.3
f2=0.7
wall_results=wallCalc_withParallel(wallpar1,wallpar2,f1,f2)

#------------------------------------------------------------------------------------------------------------------.

def wallcalc_series (serieslayerlist) :
    
    Material_library = { 'OutsideSurface_Winter' : 0.03 , 'Inside_Surface' : 0.12 , 'Wood_50mm' : 0.44 , 'Wood_Bevel' : 0.14 , 'Wood_Fiberboard' : 0.23 , 'Glass_Fiber' : 2.52 , 'Wood_Stud' : 0.63 , 'Gypsum' : 0.079 ,
    'Cement_Mortar' : 0.018 , 'Common_Brick' : 0.12 , 'Wood_Fiberboard' : 0.23 , 'asphaltshiningroof' : 0.077}
    
    R_series = 0
    
    for anylayer in serieslayerlist :
        if (anylayer == 'Wood_50mm') :                                  
            R_anylayer = Material_library ['Wood_50mm']     
        else :
            R_anylayer = Material_library [ anylayer ] 
        R_series = R_series + R_anylayer
        print R_series
        print "**************************************"
        
    U_series = 1 / R_series 
    print "value of all res: " + str (R_series) 

    print "U:" + str (U_series) 
    
    results = {R_series,U_series}
    return results
    

  
layerlist_door = [ 'OutsideSurface_Winter','Inside_Surface','Wood_50mm']
layerlist_roof = [ 'OutsideSurface_Winter' , 'AsphaltShingleRoofing' ,
'Wood_Fiberboard' ,'Glass_Fiber' , 'Inside_Surface' ]

door = wallcalc_series ( layerlist_door )
roof = wallcalc_series ( layerlist_roof )
