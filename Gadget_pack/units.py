
#Model Code to real Units

UnitLength_in_cm     =   3.086 * 10**18
UnitMass_in_g        =   1.989 * 10**33 * 5. *10**6
boxsize = 10
UnitVelocity_in_cm_per_s = (6.67*10**(-8) * UnitMass_in_g/UnitLength_in_cm)**(1/2);
UnitTime_in_s = UnitLength_in_cm / UnitVelocity_in_cm_per_s
UnitEnergy_in_cgs =  UnitMass_in_g * UnitLength_in_cm**2 / UnitTime_in_s**2
UnitDensity_in_cgs = UnitMass_in_g/UnitLength_in_cm**3
UnitColumnDensity_in_cgs = UnitMass_in_g/UnitLength_in_cm**2
M_s = 1.9891 * 10**33 #g
c = 3*10**10 #cm/s
yr_in_s = 31556926