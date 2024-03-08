import cv2
import mediapipe as mp
import time
#import controlador as cnt
import pyttsx3
from imutils import resize
import pyautogui

cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_width, screen_height = pyautogui.size()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


pTime = 0
cTime = 0

texto = pyttsx3.init()
rate = texto.getProperty('rate')
texto.setProperty('rate', rate-100)

texto = pyttsx3.init()

while True:
    ledLogo = None
    success, img = cap.read()
    img = cv2.flip(img, 1)
    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = img.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(img, (x, y), 3, (0, 255, 0))
            currentMouseX, currentMouseY = pyautogui.position()
            print(currentMouseX, currentMouseY)
            if id == 1:
                screen_x = screen_width * landmark.x
                screen_y = screen_height * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

                if (x >= 20 and x <= 30) and (y >= 80 and y <= 90):
                    print("Jugar...")
                    texto.say("Quiero Jugar")
                    texto.runAndWait()
                    #cnt.led(1)

    img = cv2.resize(img, (1280, 700))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    #print(cx, cy)
                    if (cx >= 40 and cx <= 50) and (cy >= 120 and cy <= 130):
                        print("Jugar...")
                        texto.say("Quiero Jugar")
                        texto.runAndWait()
                        #cnt.led(1)
                    if (cx >= 60 and cx <= 70) and (cy >= 270 and cy <= 280):
                        print("Quiero Comer...")
                        texto.say("Quiero Comer")
                        texto.runAndWait()
                        # cnt.led(1)
                    if (cx >= 50 and cx <= 60) and (cy >= 440 and cy <= 450):
                        print("Dormir...")
                        texto.say("Quiero Domir")
                        texto.runAndWait()
                    if (cx >= 40 and cx <= 50) and (cy >= 580 and cy <= 590):
                        print("Baño...")
                        texto.say("Quiero ir al baño")
                        texto.runAndWait()
                        # cnt.led(1)
                    if (cx >= 1210 and cx <= 1220) and (cy >= 140 and cy <= 150):
                        print("Miedo...")
                        texto.say("Tengo Miedo")
                        texto.runAndWait()
                    if (cx >= 1210 and cx <= 1220) and (cy >= 270 and cy <= 280):
                        print("Frío...")
                        texto.say("Tengo Frío")
                        texto.runAndWait()
                    if (cx >= 1210 and cx <= 1220) and (cy >= 590 and cy <= 600):
                        print("Enojado...")
                        texto.say("Estoy enojado")
                        texto.runAndWait()
                    if (cx >= 250 and cx <= 260) and (cy >= 630 and cy <= 640):
                        print("Dolor...")
                        texto.say("Me duele la cabeza")
                        texto.runAndWait()
                    if (cx >= 410 and cx <= 420) and (cy >= 630 and cy <= 640):
                        print("Dolor...")
                        texto.say("Me duele la panza")
                        texto.runAndWait()
                    if (cx >= 580 and cx <= 590) and (cy >= 640 and cy <= 650):
                        print("Dolor...")
                        texto.say("Tengo nauseas")
                        texto.runAndWait()
                    if (cx >= 740 and cx <= 750) and (cy >= 640 and cy <= 650):
                        print("Dolor...")
                        texto.say("Tengo dolor de piernas")
                        texto.runAndWait()
                    if (cx >= 910 and cx <= 920) and (cy >= 640 and cy <= 650):
                        print("Dolor...")
                        texto.say("Tengo dolor de brazos")
                        texto.runAndWait()
                    if (cx >= 1060 and cx <= 1070) and (cy >= 630 and cy <= 640):
                        print("Dolor...")
                        texto.say("Tengo Fiebre")
                        texto.runAndWait()

                        # cnt.led(1)
                #    if(cx >= 45 and cx <=48) and (cy >=105 and cy <= 150):
                #       print("ON...")
                #       texto.say("Led encendido")
                #       texto.runAndWait()
                        #cnt.led(1)
                #   if (cx >= 50  and cx <= 56) and (cy >= 150 and cy <= 185):
                 #      print("OFF...")
                 #      texto.say("Led apagado")
                 #      texto.runAndWait()
                        #cnt.led(0)
                #   if (cx >= 570 and cx <= 580) and (cy >= 110 and cy <= 120):
                 #      print("Servo ON...")
                  #     texto.say("Servo y rele encendido")
                   #    texto.runAndWait()
                        #cnt.servo(1)
                        #cnt.rele(1)
                #   if (cx >= 580 and cx <= 590) and (cy >= 180 and cy <= 190):
                 #      print("Servo OFF...")
                 #      texto.say("Servo y rele apagado")
                 #      texto.runAndWait()
                        #cnt.servo(0)
                        #cnt.rele(0)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.rectangle(img, (5, 5), (80,690), (0,0,255), 3)

    jugar = cv2.imread('imagenes/jugar.png')
    img[90:154, 10:74] = jugar  # si muevo la imagen debo sumar a la dimension de la misma

    comer = cv2.imread('imagenes/comer.png')
    img[250:314, 10:74] = comer  # si muevo la imagen debo sumar a la dimension de la misma

    dormir = cv2.imread('imagenes/dormir.png')
    img[410:474, 10:74] = dormir  # si muevo la imagen debo sumar a la dimension de la misma

    bano = cv2.imread('imagenes/bano.png')
    img[560:624, 10:74] = bano  # si muevo la imagen debo sumar a la dimension de la misma

    #cv2.putText(img, str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
    cv2.putText(img, "QUIERO", (12, 70), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 255), 2)

    cv2.rectangle(img, (1200, 5), (1275, 690), (0, 0, 255), 3)
    cv2.putText(img, "TENGO", (1205, 70), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 255), 2)

    temor = cv2.imread('imagenes/temor.png')
    img[90:154, 1205:1269] = temor  # si muevo la imagen debo sumar a la dimension de la misma

    frio = cv2.imread('imagenes/frio.png')
    img[250:314, 1205:1269] = frio  # si muevo la imagen debo sumar a la dimension de la misma

    calor = cv2.imread('imagenes/calor.png')
    img[410:474, 1205:1269] = calor  # si muevo la imagen debo sumar a la dimension de la misma

    enojado = cv2.imread('imagenes/enojado.png')
    img[570:634, 1205:1269] = enojado  # si muevo la imagen debo sumar a la dimension de la misma

    cv2.rectangle(img, (90, 600), (1190, 690), (0, 0, 255), 3)
    cv2.putText(img, "ME DUELE", (100, 650), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 0, 255), 2)

    migrana = cv2.imread('imagenes/migrana.png')
    img[615:679, 220:284] = migrana  # si muevo la imagen debo sumar a la dimension de la misma

    estomago = cv2.imread('imagenes/diarrea.png')
    img[615:679, 380:444] = estomago  # si muevo la imagen debo sumar a la dimension de la misma

    vomito = cv2.imread('imagenes/vomito.png')
    img[615:679, 540:604] = vomito  # si muevo la imagen debo sumar a la dimension de la misma

    piernas = cv2.imread('imagenes/piernas.png')
    img[615:679, 700:764] = piernas  # si muevo la imagen debo sumar a la dimension de la misma

    brazo = cv2.imread('imagenes/dolor-brazo.png')
    img[615:679, 860:924] = brazo  # si muevo la imagen debo sumar a la dimension de la misma

    fiebre = cv2.imread('imagenes/fiebre.png')
    img[615:679, 1020:1084] = fiebre  # si muevo la imagen debo sumar a la dimension de la misma

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break

        # release everything
cap.release()
cv2.destroyAllWindows()
