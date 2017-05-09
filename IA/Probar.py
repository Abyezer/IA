import neurolab as nl
import numpy as np

b = np.loadtxt('c17.dat')
net2 = nl.load("red.tmt")
net = nl.load("red2.tmt")
out2 = net2.sim([b])
rr1=np.array([0,0])-out2
rr2=np.array([0,.9])-out2
rr3=np.array([.9,0])-out2
rr4=np.array([.9,.9])-out2
rr1=np.abs(rr1)
rr2=np.abs(rr2)
rr3=np.abs(rr3)
rr4=np.abs(rr4)
rr1=np.sum(rr1)
rr2=np.sum(rr2)
rr3=np.sum(rr3)
rr4=np.sum(rr4)
print rr1,"   ",rr2,"   ",rr3,"   ",rr4
if(rr1<rr2 and rr1<rr3 and rr1<rr4):
    print "Buena calidad. nivel 1"
if(rr2<rr1 and rr2<rr3 and rr2<rr4):
    print "Regular calidad. nivel 2"
if(rr3<rr2 and rr3<rr1 and rr3<rr4):
    print "Regular/mala calidad. nivel 3"
if(rr4<rr2 and rr4<rr3 and rr4<rr1):
    print "Mala calidad. nivel 4"



out = net.sim([b])
r1=np.array([0,0,0])-out
r2=np.array([0,0,.9])-out
r3=np.array([0,.9,0])-out
r4=np.array([0,.9,.9])-out
r5=np.array([.9,0,0])-out
r6=np.array([.9,0,.9])-out
r1=np.abs(r1)
r2=np.abs(r2)
r3=np.abs(r3)
r4=np.abs(r4)
r5=np.abs(r5)
r6=np.abs(r6)
r1=np.sum(r1)
r2=np.sum(r2)
r3=np.sum(r3)
r4=np.sum(r4)
r5=np.sum(r5)
r6=np.sum(r6)
print r1,"   ",r2,"   ",r3,"   ",r4,"   ",r5,"   ",r6
if(r1<=r2 and r1<=r3 and r1<=r4 and r1<=r5 and r1<=r6):
    print "inmaduro nivel: 1. 3-5 meses para el nivel 6 con una temperatura de 3-5C"
if(r2<=r1 and r2<=r3 and r2<=r4 and r2<=r5 and r2<=r6):
    print "inmaduro nivel: 2. a 2 semanas del punto indicado"
if(r3<=r2 and r3<=r1 and r3<=r4 and r3<=r5 and r3<=r6):
    print "maduro, en su punto, nivel 3"
if(r4<=r2 and r4<=r3 and r4<=r1 and r4<=r5 and r4<=r6):
    print "poco exceso madurez nivel: 4. de 1-3 semanas demas de su punto"
if(r5<=r2 and r5<=r3 and r5<=r4 and r5<=r1 and r5<=r6):
    print "exceso madurez nivel: 5. de 3-8 semanas demas de su punto"
if(r6<=r2 and r6<=r3 and r6<=r4 and r6<=r5 and r6<=r1):
    print "mucho exceso madurez nivel: 6. 10-13 semanas excedidas de su punto ideal"
