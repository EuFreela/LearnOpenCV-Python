import cv2

#CHAMADA PARA LER IMAGEM
img = cv2.imread("img/cri-1.jpg")
#CHAMADA PARA RESIZE DA IMAGEM - NOMEANDO JANELA COM FLAG WINDOWS_NORMAL
cv2.namedWindow("Original_Cri",cv2.WINDOW_NORMAL)
#PLOTANDO IMAGEM
cv2.imshow("Original_Cri",img)
#REDIMENSIONANDO A IMAGEM PLOTADA ONDE PARAMETRO É O NOME DA JANELA SEGUIDO
#DOS VALORES DA RESOLUÇÃO
cv2.resizeWindow("Original_Cri",378,378)

#PROPRIEDADES D IMAGEM CARREGADA
print ("Altura (height): %d pixels" % (img.shape[0]))
print ("Largura (width): %d pixels" % (img.shape[1]))
print ("Canais (channels): %d"      % (img.shape[2]))

cv2.waitKey(0)
cv2.destroyAllWindows()