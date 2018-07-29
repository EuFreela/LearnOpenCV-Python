

```python
#importação necessária para plotar imagem
from matplotlib import pyplot as plt

#http://pyscience-brasil.wikidot.com/module:numpy
#Esta lib permite trabalhar cm matrizes, justamente, a essencia de uma imagem
import numpy as np 

#https://docs.python.org/3/library/urllib.request.html
#COm esta lib podemos abrir urls em código
import urllib.request

##Lib do opencv
import cv2

#CHAMADA PARA LER IMAGEM REMOTA
remote_img = urllib.request.urlopen("https://s5.postimg.cc/j6d18n5lj/21617464_702679296599345_940433337791009221_n.jpg")
#Transformando em array a imagem obtida da url. A tipagem uint8 tem range de 0-255 - Valores do RGB
arr = np.asarray(bytearray(remote_img.read()), dtype=np.uint8)

#Decodificando imagem. https://docs.opencv.org/3.0-beta/modules/imgcodecs/doc/reading_and_writing_images.html
img = cv2.imdecode(arr,-1)
#Acertando a imagem decodificada para o canal correto: BGR para RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Plotando a imagem
plt.imshow(img)
```




    <matplotlib.image.AxesImage at 0x7f7223bdd128>




![png](output_0_1.png)

