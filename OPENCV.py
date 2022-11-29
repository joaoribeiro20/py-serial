import numpy as np
import cv2
from win10toast import ToastNotifier

n = ToastNotifier()
i = cv2.imread('lula.jpg')

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(i,
            'porra',
            (20, 150),
            font, 1,
            (0, 255, 255),
            2,
            cv2.LINE_4)

            #cv2.LINE_AA)
iPB = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)

#Criação do detector de faces
df = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = df.detectMultiScale(iPB,
 scaleFactor = 1.05, minNeighbors = 7,
 minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE)

notificacao = (len(faces))
print(notificacao)

#Desenha retangulos amarelos na iamgem original (colorida)
for (x, y, w, h) in faces:
 cv2.rectangle(i, (x, y), (x + w, y + h), (255, 0, 0), 7)

#Exibe imagem. Título da janela exibe número de faces
cv2.imshow(str(len(faces))+' face(s) encontrada(s).', i)
if notificacao == 20:
  n.show_toast("NOTIFICAÇÃO", "TEM MAIS DE 4 PESSOAS", duration=15)
cv2.waitKey(0)