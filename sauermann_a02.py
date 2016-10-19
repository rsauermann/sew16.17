import threading
from random import randint
import sys

global textEn
textEn = ''
class Verschluesselung(threading.Thread):
    """
        In dieser Klasse kommt der Text der von jedem Threat verschluesselt werden soll
    """
    text = ''
    doEncrypt = 1
    key = randint(1,9)

    def __init__(self,text,doEncrypt):
        """
            Der Konstruktor der Klasse Verschluesselung,
            dient zur initialisierung der Werte text und doEncrypt
        :param text: ist der Text der Verschluesselt werden soll
        :param doEncrypt: 1 wenn es verschluesselt werden soll 0 wenn entschluesselt
        :return:
        """
        threading.Thread.__init__(self)
        self.text = text
        self.doEncrypt = doEncrypt
        # print (self.doEncrypt)

    def run(self):
        """
            Ist die Funktion in der die eigentliche Ver/Entschluessunlung stattfindent
            Verschluesselung erfolgt ueber den Ascii Code und einen random Key
            der sich erneuert wenn das File neu aufgerufen wird
        :return:
        """
        global textEn
        if self.doEncrypt==1:
            # soll verschluesselt werden
            for c in self.text:
                # false (kommt nicht in d vor)
                textEn+= chr(ord(c) + self.key)
        elif self.doEncrypt==0:
            # soll entschluesselt werden
            for c in self.text:
                textEn+= chr(ord(c) - self.key)
        else:
            print("Eingabe ob Ver-Entschluesselung war ungueltig")

def splitInput(anzahl_threats,text,doEncrypt):
    """
        Teil den Input des User in Brauchbare groessen fuer die Threats ein
        und erstellt diese
    :param anzahl_threats:
    :param text:
    :param doEncrypt:
    :return:
    """
    global textEn
    # gesamtlaenge vom text
    # print l_text
    l_text = round(len(text) /anzahl_threats)
    threads = []
    for i in range(0, anzahl_threats):
        if i < anzahl_threats - 1:
            str = text[int(i * l_text):int((i + 1) * l_text)]
            thread = Verschluesselung(str,doEncrypt)
        else:
            str = text[i * int(l_text):]
            thread = Verschluesselung(str,doEncrypt)
        threads += [thread]
        # Thread gleich starten
        thread.start()
    for x in threads:
        x.join()
    print (textEn)
    textEn=''

def userInput():
    """
        In diser Methode erfolgt die Kommunikation mit dem Benutzer des Programmes
    :return:
    """
    user_doEncrypt = input('Wollen sie entschluesseln (0), verschluesseln(1) oder beenden(2): ')
    try:
        user_doEncrypt=int(user_doEncrypt)
    except ValueError:
        return False
    if user_doEncrypt == 2:
        sys.exit("Programm beendet")
    user_text=input("Bitte den zu bearbeitenden Text angeben: ")
    user_threats = input("Bitte geben sie die Anzahl der Threats an: ")
    try:
        user_threats=int(user_threats)
    except ValueError:
        return False
    if user_threats>len(user_text) or user_threats<0:
        user_threats=len(user_text)
    #user_text=user_text.lower()
    splitInput(user_threats,user_text,user_doEncrypt)

while True:
    userInput()