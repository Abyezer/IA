import numpy as np
import neurolab as nl

a1 = np.loadtxt('z11.dat')
a2 = np.loadtxt('z12.dat')
a3 = np.loadtxt('z13.dat')
a4 = np.loadtxt('z21.dat')
a5 = np.loadtxt('z22.dat')
a6 = np.loadtxt('z23.dat')
a7 = np.loadtxt('z24.dat')
a8 = np.loadtxt('z25.dat')
a9 = np.loadtxt('z26.dat')
a10 = np.loadtxt('z27.dat')
a11 = np.loadtxt('z31.dat')
a12 = np.loadtxt('z32.dat')
a13 = np.loadtxt('z33.dat')
a14 = np.loadtxt('z34.dat')
a15 = np.loadtxt('z35.dat')
a16 = np.loadtxt('z36.dat')
a17 = np.loadtxt('z41.dat')
a18 = np.loadtxt('z42.dat')
a19 = np.loadtxt('z43.dat')
a20 = np.loadtxt('z44.dat')
a21 = np.loadtxt('z45.dat')
a22 = np.loadtxt('z46.dat')
a23 = np.loadtxt('z47.dat')
a24 = np.loadtxt('z51.dat')
a25 = np.loadtxt('z52.dat')
a26 = np.loadtxt('z53.dat')
a27 = np.loadtxt('z54.dat')
a28 = np.loadtxt('z55.dat')
a29 = np.loadtxt('z56.dat')
a30 = np.loadtxt('z57.dat')
a31 = np.loadtxt('z71.dat')
a32 = np.loadtxt('z72.dat')
a33 = np.loadtxt('z73.dat')
a34 = np.loadtxt('z74.dat')
a35 = np.loadtxt('z75.dat')
a36 = np.loadtxt('z76.dat')
a37 = np.loadtxt('z77.dat')
input1 =np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37])
input1 = input1*4/10
target1 = np.zeros((len(input1),3))
#for x in xrange(0, 3):
    #target1[x] = [.8,0,0]
for x in xrange(3, 10):
    target1[x] = [0,0,.9]
for x in xrange(10, 17):
    target1[x] = [0,.9,0]
for x in xrange(17, 24):
    target1[x] = [0,.9,.9]
for x in xrange(24, 31):
    target1[x] = [.9,0,0]
for x in xrange(31, 37):
    target1[x] = [.9,0,.9]
b1 = np.loadtxt('c11.dat')
b2 = np.loadtxt('c12.dat')
b3 = np.loadtxt('c13.dat')
b4 = np.loadtxt('c14.dat')
b5 = np.loadtxt('c15.dat')
b6 = np.loadtxt('c16.dat')
b7 = np.loadtxt('c21.dat')
b8 = np.loadtxt('c22.dat')
b9 = np.loadtxt('c23.dat')
b10 = np.loadtxt('c24.dat')
b11 = np.loadtxt('c25.dat')
b12 = np.loadtxt('c26.dat')
b13 = np.loadtxt('c27.dat')
b14 = np.loadtxt('c31.dat')
b15 = np.loadtxt('c32.dat')
b16 = np.loadtxt('c33.dat')
b17 = np.loadtxt('c34.dat')
b18 = np.loadtxt('c35.dat')
b19 = np.loadtxt('c41.dat')
b20 = np.loadtxt('c42.dat')
b21 = np.loadtxt('c43.dat')
b22 = np.loadtxt('c44.dat')
b23 = np.loadtxt('c51.dat')
b24 = np.loadtxt('c52.dat')
b25 = np.loadtxt('c53.dat')
b26 = np.loadtxt('c61.dat')
b27 = np.loadtxt('c62.dat')
b28 = np.loadtxt('c63.dat')
b29 = np.loadtxt('c71.dat')
b30 = np.loadtxt('c72.dat')
b31 = np.loadtxt('c73.dat')
b32 = np.loadtxt('c74.dat')
b33 = np.loadtxt('c75.dat')
b34 = np.loadtxt('c76.dat')
b35 = np.loadtxt('c81.dat')
b36 = np.loadtxt('c82.dat')
b37 = np.loadtxt('c83.dat')
b38 = np.loadtxt('c84.dat')
b39 = np.loadtxt('c85.dat')
b40 = np.loadtxt('c86.dat')
b41 = np.loadtxt('c87.dat')
input2 = np.array([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41])
target2 = np.zeros((len(input2),2))
#for x in xrange(0, 13):
    #target2[x] = [-.8,-.8]
for x in xrange(13, 22):
    target2[x] = [0,.9]
for x in xrange(22, 28):
    target2[x] = [.9,0]
for x in xrange(28, 41):
    target2[x] = [.9,.9]
rango1 = np.zeros((len(input1[0]),2))
a = np.zeros(len(input1))
for x in range(0, len(rango1)):
    a=a-a
    for y in range(0, len(input1)):
        a[y] = input1[y,x]
    #print input1.max(axis=0)
    rango1[x]=[0.004, 0.96]

net = nl.net.newff(rango1, [5, 3])

# Train network
error = net.train(input1, target1, epochs=500, show=2, goal=50.1)
# Simulate network
#net.save("red2.tmt")
out = net.sim([input1[0]])
print error[len(error)-1], "primer error"
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
if(r1<r2 and r1<r3 and r1<r4 and r1<r5 and r1<r6):
    print "inmaduro nivel: 1. 3-5 meses para el nivel 6 con una temperatura de 3-5C"
if(r2<r1 and r2<r3 and r2<r4 and r2<r5 and r2<r6):
    print "inmaduro nivel: 2. a 2 semanas del punto indicado"
if(r3<r2 and r3<r1 and r3<r4 and r3<r5 and r3<r6):
    print "maduro, en su punto, nivel 3"
if(r4<r2 and r4<r3 and r4<r1 and r4<r5 and r4<r6):
    print "poco exceso madurez nivel: 4. de 1-3 semanas demas de su punto"
if(r5<r2 and r5<r3 and r5<r4 and r5<r1 and r5<r6):
    print "exceso madurez nivel: 5. de 3-8 semanas demas de su punto"
if(r6<r2 and r6<r3 and r6<r4 and r6<r5 and r6<r1):
    print "mucho exceso madurez nivel: 6. 10-13 semanas excedidas de su punto ideal"

rango2 = np.zeros((len(input2[0]),2))
b = np.zeros(len(input2))
for x in range(0, len(rango2)):
    b=b-b
    for y in range(0, len(input2)):
        b[y] = input2[y,x]
    #print input1.max(axis=0)
    rango2[x]=[b.min(), b.max()]





net2 = nl.net.newff(rango2, [4, 2])
# Train network
error2 = net2.train(input2, target2, epochs=500, show=2, goal=100.1)
# Simulate network
#net2.save("red.tmt")
#net2 = nl.load("red.tmt")
out2 = net2.sim([input2[0]])
print error[len(error)-1], "segundo error"
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
