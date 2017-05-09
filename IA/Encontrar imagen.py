import cv2
import numpy as np
nombre = "z77"
filename = nombre+'.jpg'
iimg = cv2.imread(filename)
img = resized_image = cv2.resize(iimg, (600, 600))
imagen = img
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
naranjas_bajos = np.array([0, 145, 115], dtype=np.uint8)
naranjas_altos = np.array([24,255,255], dtype=np.uint8)
mask = cv2.inRange(hsv, naranjas_bajos, naranjas_altos)
moments = cv2.moments(mask)
area = moments['m00']
print moments['m10']
print area
if(area > 2000000):
#Buscamos el centro x, y del objeto
    x = int(moments['m10']/moments['m00'])
    y = int(moments['m01']/moments['m00'])
    print "x = ", x
    print "y = ", y
cv2.imshow('mask', mask)
cv2.imshow('Camara', imagen)
ret,thresh = cv2.threshold(mask,127,255,0)
contours = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
#print M
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Resultado', cv2.rectangle(img,(x+w/6,y+h/6),(x+w-w/6,y+h-h/6),(0,255,0),1))
img_recortada = img[y+h/3+1:y+h-h/3, x+w/3+1:x+w-w/3] # Crop from x, y, w, h -> 100, 200, 300, 400
cv2.imshow('Recorte', img_recortada)
res = cv2.resize(img_recortada,(15, 15), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Normalizado', res)
matriz_imagen = np.asarray(res,dtype=np.float32)
datos = np.zeros((675))
ubicacion =0
for y in xrange(0, (15)):
    for x in xrange(0, (15)):
        datos[ubicacion]=matriz_imagen[x,y][0]
        datos[ubicacion+1]=matriz_imagen[x,y][1]
        datos[ubicacion+2]=matriz_imagen[x,y][2]
        ubicacion=ubicacion+3
datos = datos/100
np.savetxt(nombre+'nada.dat', datos, fmt='%.4e')
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
