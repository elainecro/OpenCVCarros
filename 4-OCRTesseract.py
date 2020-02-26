from PIL import Image
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#imgTexto = Image.open("imagens/2.png")
#texto = pytesseract.image_to_string(imgTexto)
#print(texto)


#imgOpenCV = cv2.imread("imagens/placa1.png")
#imgResize = cv2.resize(imgOpenCV, (400,200))
#imgGray = cv2.cvtColor(imgResize, cv2.COLOR_RGB2GRAY)
#cv2.imshow("Imagem", imgResize)

#textoPlaca = pytesseract.image_to_string(Image.open("imagens/placa1.png"))
#print(textoPlaca)

#cv2.waitKey(0)

src_path = "imagens/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

    return result


print('Nova tentativa:')
print(get_string(src_path + "carros5.png"))
print('Feito')