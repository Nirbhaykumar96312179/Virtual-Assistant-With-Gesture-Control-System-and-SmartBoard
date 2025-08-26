import threading
import cv2
import numpy as np
import random
import speech_recognition as sr
from handTracker import HandTracker  # Ensure this module is available and correctly implemented

class ColorRect:
    def __init__(self, x, y, w, h, color, text='', alpha=0.5):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = text
        self.alpha = alpha

    def drawRect(self, img, text_color=(255, 255, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=2):
        alpha = self.alpha
        bg_rec = img[self.y:self.y + self.h, self.x:self.x + self.w]
        white_rect = np.ones(bg_rec.shape, dtype=np.uint8)
        white_rect[:] = self.color
        res = cv2.addWeighted(bg_rec, alpha, white_rect, 1 - alpha, 1.0)
        img[self.y:self.y + self.h, self.x:self.x + self.w] = res

        text_size = cv2.getTextSize(self.text, fontFace, fontScale, thickness)[0]
        text_pos = (int(self.x + self.w / 2 - text_size[0] / 2), int(self.y + self.h - 10))
        cv2.putText(img, self.text, text_pos, fontFace, fontScale, text_color, thickness)

    def isOver(self, x, y):
        return self.x < x < self.x + self.w and self.y < y < self.y + self.h

# Initialize the hand detector
detector = HandTracker(detectionCon=1)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Create canvas for drawing
canvas = np.zeros((720, 1280, 3), np.uint8)

# Define previous point for drawing
px, py = 0, 0

# Initialize brush color and size
color = (255, 0, 0)
brushSize = 5
eraserSize = 20

# Create color rectangles for drawing
colorsBtn = ColorRect(200, 0, 100, 100, (120, 255, 0), 'Colors')

colors = [
    ColorRect(300, 0, 100, 100, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))),
    ColorRect(400, 0, 100, 100, (0, 0, 255)),
    ColorRect(500, 0, 100, 100, (255, 0, 0)),
    ColorRect(600, 0, 100, 100, (0, 255, 0)),
    ColorRect(700, 0, 100, 100, (0, 255, 255)),
    ColorRect(800, 0, 100, 100, (0, 0, 0), "Eraser"),
]

clear = ColorRect(900, 0, 100, 100, (100, 100, 100), "Clear")

pens = [
    ColorRect(1100, 50, 100, 100, (50, 50, 50), "5"),
    ColorRect(1100, 150, 100, 100, (50, 50, 50), "10"),
    ColorRect(1100, 250, 100, 100, (50, 50, 50), "15"),
    ColorRect(1100, 350, 100, 100, (50, 50, 50), "20"),
]

penBtn = ColorRect(1100, 0, 100, 50, color, 'Pen')

boardBtn = ColorRect(50, 0, 100, 100, (255, 255, 0), 'Board')

whiteBoard = ColorRect(50, 120, 1020, 580, (255, 255, 255), alpha=0.6)

coolingCounter = 20
hideBoard = True
hideColors = True
hidePenSizes = True
recognized_speech = ""

# Function for speech recognition
def recognize_speech():
    global recognized_speech
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            try:
                recognized_speech = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                recognized_speech = "Could not understand audio"
            except sr.RequestError as e:
                recognized_speech = f"Could not request results from Google Speech Recognition service; {e}"

# Start speech recognition thread
speech_thread = threading.Thread(target=recognize_speech)
speech_thread.daemon = True
speech_thread.start()

while True:
    if coolingCounter:
        coolingCounter -= 1

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)

    detector.findHands(frame)
    positions = detector.getPostion(frame, draw=False)
    upFingers = detector.getUpFingers(frame)

    if upFingers:
        x, y = positions[8][0], positions[8][1]
        if upFingers[1] and not whiteBoard.isOver(x, y):
            px, py = 0, 0

            if not hidePenSizes:
                for pen in pens:
                    if pen.isOver(x, y):
                        brushSize = int(pen.text)
                        pen.alpha = 0
                    else:
                        pen.alpha = 0.5

            if not hideColors:
                for cb in colors:
                    if cb.isOver(x, y):
                        color = cb.color
                        cb.alpha = 0
                    else:
                        cb.alpha = 0.5

                if clear.isOver(x, y):
                    clear.alpha = 0
                    canvas = np.zeros((720, 1280, 3), np.uint8)
                else:
                    clear.alpha = 0.5

            if colorsBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                colorsBtn.alpha = 0
                hideColors = not hideColors
                colorsBtn.text = 'Colors' if hideColors else 'Hide'
            else:
                colorsBtn.alpha = 0.5

            if penBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                penBtn.alpha = 0
                hidePenSizes = not hidePenSizes
                penBtn.text = 'Pen' if hidePenSizes else 'Hide'
            else:
                penBtn.alpha = 0.5

            if boardBtn.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                boardBtn.alpha = 0
                hideBoard = not hideBoard
                boardBtn.text = 'Board' if hideBoard else 'Hide'

            else:
                boardBtn.alpha = 0.5

        elif upFingers[1] and not upFingers[2]:
            if whiteBoard.isOver(x, y) and not hideBoard:
                cv2.circle(frame, positions[8], brushSize, color, -1)
                if px == 0 and py == 0:
                    px, py = positions[8]
                if color == (0, 0, 0):
                    cv2.line(canvas, (px, py), positions[8], color, eraserSize)
                else:
                    cv2.line(canvas, (px, py), positions[8], color, brushSize)
                px, py = positions[8]

        else:
            px, py = 0, 0

    colorsBtn.drawRect(frame)
    cv2.rectangle(frame, (colorsBtn.x, colorsBtn.y), (colorsBtn.x + colorsBtn.w, colorsBtn.y + colorsBtn.h), (255, 255, 255), 2)

    boardBtn.drawRect(frame)
    cv2.rectangle(frame, (boardBtn.x, boardBtn.y), (boardBtn.x + boardBtn.w, boardBtn.y + boardBtn.h), (255, 255, 255), 2)

    if not hideBoard:
        whiteBoard.drawRect(frame)
        canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, img_inv = cv2.threshold(canvas_gray, 20, 255, cv2.THRESH_BINARY_INV)
        img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
        frame = cv2.bitwise_and(frame, img_inv)
        frame = cv2.bitwise_or(frame, canvas)

    if not hideColors:
        for c in colors:
            c.drawRect(frame)
            cv2.rectangle(frame, (c.x, c.y), (c.x + c.w, c.y + c.h), (255, 255, 255), 2)

        clear.drawRect(frame)
        cv2.rectangle(frame, (clear.x, clear.y), (clear.x + clear.w, clear.y + clear.h), (255, 255, 255), 2)

    if not hidePenSizes:
        for pen in pens:
            pen.drawRect(frame)
            cv2.rectangle(frame, (pen.x, pen.y), (pen.x + pen.w, pen.y + pen.h), (255, 255, 255), 2)

    penBtn.drawRect(frame)
    cv2.rectangle(frame, (penBtn.x, penBtn.y), (penBtn.x + penBtn.w, penBtn.y + penBtn.h), (255, 255, 255), 2)

    cv2.putText(frame, recognized_speech, (50, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
