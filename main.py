import cv2
import pytesseract

# Указываем путь до установленного дистрибутива Tesseract (для Windows OS only)
# https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
pytesseract.pytesseract.tesseract_cmd = 'Y:\\Codes\\Programming\\Tesseract-OCR\\tesseract.exe'

# Загружаем изображение
img = cv2.imread('imgs\\setpath_02.png')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Будет выведен текст с картинки
config = r'--oem 3 --psm 6'  # Иногда лучше так делать, кода большие символы
text = pytesseract.image_to_string(img, config=config)
print(text)

data = pytesseract.image_to_data(img, config=config)
for i, el in enumerate(data.splitlines()):
    # В первой строке находится названия столбцов
    if i == 0:
        continue
    # Разделяем строку так, чтобы каждое число было отдельно
    el = el.split()
    try:
        # Получаем координаты и толщины найденного текста
        print(el)
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        # Если нашелся какой-то распознанный текст, то рисуем рядом с его рамкой
        if len(el) > 11:
            # Рисуем прямоугольник с вершиной в x, y, шириной и высотой (x+w), (y+h), цветом и толщиной =1
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            # Теперь рисуем распознанный текст прямо на картинке, el[11] - сам текст, (x,y) - координата, шрифт, его размер,
            # ...цвет, толщина
            cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    except IndexError:
        print("Ничего не найдено")

cv2.imshow('Result', img)
cv2.waitKey(0)