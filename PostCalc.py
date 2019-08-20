# -*- coding: utf-8 -*-


import pandas as pd

def cube(length, width, height):
    # calculate volume, convert to kg
    return int((length/100)*(width/100)*(height/100)*250)+1

parcel = pd.read_csv('./parcel/parcel02.txt', sep=',', index_col= "Zone")


postcodes = pd.read_csv('./parcel/postcodes.txt', sep=',')


pc = int(input("What is the postcode: "))
long = int(input(" Length: "))
wide = int(input(" Width: "))
deep = int(input(" Depth: "))
wt = int(input(" Weight (g): "))
wt = int(wt/1000)+1

for i in range(len(postcodes['low'])):
    if pc >= postcodes['low'][i] and pc <= postcodes[' high'][i]:
        dest = postcodes[' Zone'][i]
        
post_loc = parcel[" SA1"][dest]


calc = cube(long, wide, deep)

if wt >= calc:
    post_calc = 13.85 + (post_loc * wt)
else:
    

    post_calc = 13.85 + (post_loc * calc)

print("Postage to ", pc, "(", dest, ")", "is $", post_calc)