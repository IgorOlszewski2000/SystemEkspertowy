import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import *

#################################
global clickStart
global pytanie1
global pytanie2
pytanie1 = 0
pytanie2 = 0
#################################

def przyciskRobic1(): # SAMA GÓRA DRZEWA
    label1.setText("KTÓRY PRZEDMIOT ZDAŁEŚ LEPIEJ NA MATURZE?")
    print("WYSTARTOWAŁO")
    BPrzycisk1.setEnabled(False)
    BPrzycisk2.setEnabled(True)
    BPrzycisk3.setEnabled(True)
    
def przyciskRobic2(): # DRZEWO NUMER 2 
    label1.setText("CZY NAUKI PRZYRODNICZE SĄ DLA CIEBIE INTERESUJĄCE?")
    BPrzycisk1.setEnabled(False)
    BPrzycisk2.setEnabled(False)
    BPrzycisk3.setEnabled(False)
    BPrzycisk4.setEnabled(True)
    BPrzycisk5.setEnabled(True)
    pytanie1 = 1
    print(pytanie1)

def przyciskRobic3(): # DRZEWO NUMER 1
    label1.setText("CZY INTERESUJESZ SIĘ HISTORIĄ?")
    BPrzycisk1.setEnabled(False)
    BPrzycisk2.setEnabled(False)
    BPrzycisk3.setEnabled(False)
    BPrzycisk4.setEnabled(True)
    BPrzycisk5.setEnabled(True)
    pytanie1 = 2
    print(pytanie1)

def przyciskRobic4():
    BPrzycisk4.hide()
    BPrzycisk5.hide()
    label1.setText("CZY INTERESUJE CIĘ PRACA W LABORATORIUM?")
    print("TAK INTERESUJĘ SIĘ PRZYRODNICZYMI")

def przyciskRobic5():
    BPrzycisk4.hide()
    BPrzycisk5.hide()
    label1.setText("CZY ŚLEDZISZ NOWINKI ZE ŚWIATA FINANSÓW?")
    print("NIE INTERESUJĘ SIĘ PRZYRODNICZYMI")

def przyciskRobic6():
    print("LUDZI")

def przyciskRobic7():
    print("ZWIERZĘTA")

def przyciskRobic8():
    BPrzycisk4.hide()
    BPrzycisk5.hide()
    label1.setText("CZY ŚLEDZISZ NOWINKI ZE ŚWIATA FINANSÓW?")
    print("NIE INTERESUJĘ SIĘ PRZYRODNICZYMI")

def przyciskRobic9():
    BPrzycisk4.hide()
    BPrzycisk5.hide()
    label1.setText("CZY ŚLEDZISZ NOWINKI ZE ŚWIATA FINANSÓW?")
    print("NIE INTERESUJĘ SIĘ PRZYRODNICZYMI")

#################################
def window(): #funkcja glowna
    app=QApplication(sys.argv) #aplikacja
    widget=QWidget() #kontrolki
    
    global BPrzycisk1
    BPrzycisk1 = QPushButton(widget) # przycisk
    BPrzycisk1.setEnabled(True)
    BPrzycisk1.setText("START")
    BPrzycisk1.clicked.connect(przyciskRobic1)
    BPrzycisk1.move(200,100)
    
    global BPrzycisk2
    BPrzycisk2 = QPushButton(widget) # przycisk
    BPrzycisk2.setEnabled(False)
    BPrzycisk2.setText("MATEMATYKA")
    BPrzycisk2.clicked.connect(przyciskRobic2)
    BPrzycisk2.move(200,125)

    global BPrzycisk3
    BPrzycisk3 = QPushButton(widget) # przycisk
    BPrzycisk3.setEnabled(False)
    BPrzycisk3.setText("POLSKI")
    BPrzycisk3.clicked.connect(przyciskRobic3)
    BPrzycisk3.move(200,150)

    global BPrzycisk4
    BPrzycisk4 = QPushButton(widget) # przycisk
    BPrzycisk4.setEnabled(False)
    BPrzycisk4.setText("TAK")
    BPrzycisk4.clicked.connect(przyciskRobic4)
    BPrzycisk4.move(200,175)

    global BPrzycisk5
    BPrzycisk5 = QPushButton(widget) # przycisk
    BPrzycisk5.setEnabled(False)
    BPrzycisk5.setText("NIE")
    BPrzycisk5.clicked.connect(przyciskRobic5)
    BPrzycisk5.move(200,200)

    global BPrzycisk6
    BPrzycisk6 = QPushButton(widget) # przycisk
    BPrzycisk6.setEnabled(False)
    BPrzycisk6.setText("LUDZI")
    BPrzycisk6.clicked.connect(przyciskRobic6)
    BPrzycisk6.move(200,225)

    global BPrzycisk7
    BPrzycisk7 = QPushButton(widget) # przycisk
    BPrzycisk7.setEnabled(False)
    BPrzycisk7.setText("ZWIERZĘTA")
    BPrzycisk7.clicked.connect(przyciskRobic7)
    BPrzycisk7.move(200,250)

    global BPrzycisk8
    BPrzycisk8 = QPushButton(widget) # przycisk
    BPrzycisk8.setEnabled(False)
    BPrzycisk8.setText("TAK")
    BPrzycisk8.clicked.connect(przyciskRobic8)
    BPrzycisk8.move(200,175)

    global BPrzycisk9
    BPrzycisk9 = QPushButton(widget) # przycisk
    BPrzycisk9.setEnabled(False)
    BPrzycisk9.setText("NIE")
    BPrzycisk9.clicked.connect(przyciskRobic9)
    BPrzycisk9.move(200,200)

    global label1
    label1=QLabel(widget)
    global label2
    label2=QLabel(widget)
    global label3
    label3=QLabel(widget)
    
    label1.setText("SYSTEM EKSPERTOWY WSPOMAGAJĄCY WYBÓR STUDIÓW")
    label1.move(120,20)
    #label2.setText("<b>METAFORA - PONIEWAŻ WYBRAŁEŚ KOTA CO LUBI DUŻO JEŚĆ</b>")
    #label2.move(120,50)
    #label3.setText("<img src='kot.jpg' width='200' height='200'>")
    #label3.move(120,70)
    
    widget.setGeometry(50,50,500,500)
    widget.show()
    sys.exit(app.exec_())

if __name__=="__main__": 
    window() #funkcja główna
