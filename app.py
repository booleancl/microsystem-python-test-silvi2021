import time
import random

# Tú código va aquí
print ("Bienvenido al horóscopo")
user_input = ""

def read_file(app):
    file = open("signs/"+ app,"r",encoding="UTF-8")
    for line in file:
      print(line)



def print_menu():
    print("Selecciona el número correspondiente a tu signo\n")
    print("1 acuario")
    print("2 aries")
    print("3 cancer ")
    print("4 capricornio")
    print("5 geminis")
    print("6 leo")
    print("7 libra")
    print("8 piscis")
    print("9 sagitario")
    print("10 escorpion")
    print("11 tauro")
    print("12 virgo")
    print("13 color de la suerte")
  
while user_input != "exit":
    print_menu()
    user_input = input()


    if user_input == "1":
        read_file("aquarius.txt")
        time.sleep(0.3)
    if user_input =="2":
        read_file("aries.txt")
        time.sleep(0.3)
    if user_input =="3":
        read_file("cancer.txt")
        time.sleep(0.3)
    if user_input =="4":
        read_file("capricornus.txt")
        time.sleep(0.3)
    if user_input =="5":
        read_file("gemini.txt")
        time.sleep(0.3)
    if user_input =="6":
        read_file("leo.txt")
        time.sleep(0.3)
    if user_input =="7":
        read_file("libra.txt")
        time.sleep(0.3)
    if user_input =="8":
        read_file("pisces.txt")
        time.sleep(0.3)       
    if user_input =="9":
        read_file("saggittarius.txt")
        time.sleep(0.3)
    if user_input =="10":
        read_file("scorpio.txt")
        time.sleep(0.3)
    if user_input =="11":
        read_file("taurus.txt")
        time.sleep(0.3)
    if user_input =="12":
        read_file("virgo")
        time.sleep(0.3)
    if user_input =="13":
        print("color de la suerte")
        colors = ["rojo","azul","amarillo","verde","morado","rosado"]

        colors = random.choice(colors) 
        print("tu colors favorito es:",colors)
       
    elif user_input == "exit":
        print("salir")
        exit()
else:
    print("opción incorrecta")
    print("tu color de la suerte es azul")






